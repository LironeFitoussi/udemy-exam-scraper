// =============================================================
// Udemy Exam Scraper - Paste into browser DevTools Console
// Paste this from ANY state: results page, mode selection,
// or already inside a question. It handles all cases.
// =============================================================

(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const results = [];

  // Wait for selector to appear (resolves with element)
  function waitFor(selector, timeout = 20000) {
    return new Promise((resolve, reject) => {
      const el = document.querySelector(selector);
      if (el) return resolve(el);
      const observer = new MutationObserver(() => {
        const el = document.querySelector(selector);
        if (el) { observer.disconnect(); resolve(el); }
      });
      observer.observe(document.body, { childList: true, subtree: true });
      setTimeout(() => { observer.disconnect(); reject(new Error(`Timeout waiting for: ${selector}`)); }, timeout);
    });
  }

  function safeText(el) {
    try { return el?.innerText?.trim() || ''; } catch { return ''; }
  }

  /** Convert innerHTML to text, preserving image URLs as ![image](url) markers */
  function htmlToTextWithImages(el) {
    if (!el) return null;
    let html = el.innerHTML;
    if (!html) return el.innerText?.trim() || null;
    // Replace <img> tags with markdown-style image references
    html = html.replace(/<img[^>]+src=["']([^"']+)["'][^>]*>/gi, '\n![image]($1)\n');
    // Replace <br> with newlines
    html = html.replace(/<br\s*\/?>/gi, '\n');
    // Replace block-level closing tags with newlines
    html = html.replace(/<\/(?:p|div|li|h[1-6])>/gi, '\n');
    // Strip all remaining HTML tags
    html = html.replace(/<[^>]+>/g, '');
    // Decode common HTML entities
    html = html.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, ' ');
    // Collapse excessive blank lines
    html = html.replace(/\n{3,}/g, '\n\n');
    return html.trim() || null;
  }

  // ---- Step 1: Handle pre-exam screens ----
  const retakeOrBegin =
    document.querySelector('button[data-purpose="start-quiz"]') ||
    [...document.querySelectorAll('button')].find(b => b.innerText?.trim() === 'Retake test');

  if (retakeOrBegin) {
    console.log('[*] Clicking Retake/Begin test...');
    retakeOrBegin.click();
    await sleep(1500);
  }

  // ---- Step 2: Handle mode selection screen ----
  const modeCards = document.querySelectorAll('[class*="mode-card--mode-card--"]');
  if (modeCards.length > 0) {
    console.log('[*] Mode selection screen - clicking Practice mode...');
    const practiceCard = [...modeCards].find(el => el.innerText?.includes('Practice mode'));
    if (practiceCard) {
      practiceCard.click();
      console.log('[+] Clicked Practice mode');
      await sleep(2000);
    }
  }

  // ---- Step 3: Wait for first question ----
  console.log('[*] Waiting for first question to load...');
  try {
    await waitFor('#question-prompt', 20000);
    await waitFor('input[name="answer"]', 20000);
    await sleep(200);
  } catch (e) {
    console.error('[x] Could not find question:', e.message);
    return;
  }

  // ---- Scraping helpers ----
  function getQuestionText() {
    const el = document.querySelector('#question-prompt [data-purpose*="rich-text-viewer"]') ||
               document.querySelector('#question-prompt');
    return htmlToTextWithImages(el);
  }

  function getOptions() {
    const inputs = [...document.querySelectorAll('input[name="answer"]')];
    return inputs.map(inp => {
      const label = document.querySelector(`label[for="${inp.id}"]`);
      // Try the answer-body div first, fall back to any rich-text-viewer
      const textEl = label?.querySelector('[class*="answer-body"]') ||
                     label?.querySelector('[data-purpose*="rich-text-viewer"]');
      return { index: parseInt(inp.dataset.index), text: htmlToTextWithImages(textEl) || safeText(textEl) };
    }).filter(opt => opt.text);
  }

  function getQuestionType() {
    const first = document.querySelector('input[name="answer"]');
    return first?.type === 'checkbox' ? 'multi_select' : 'single_select';
  }

  async function selectRandomAnswers() {
    const inputs = [...document.querySelectorAll('input[name="answer"]')];
    if (!inputs.length) return [];
    const isMulti = inputs[0].type === 'checkbox';
    let chosen;
    if (isMulti) {
      const k = Math.max(2, Math.floor(Math.random() * (inputs.length - 1)) + 1);
      chosen = [...inputs].sort(() => Math.random() - 0.5).slice(0, k);
      // Click checkboxes one at a time with a small delay so React registers each click
      for (const inp of chosen) {
        document.querySelector(`label[for="${inp.id}"]`)?.click();
        await sleep(80);
      }
    } else {
      chosen = [inputs[Math.floor(Math.random() * inputs.length)]];
      document.querySelector(`label[for="${chosen[0].id}"]`)?.click();
    }
    return chosen.map(i => parseInt(i.dataset.index));
  }

  async function submitAnswer() {
    // Wait up to 2s for the button to be enabled (React enables it after selection registers)
    const deadline = Date.now() + 2000;
    while (Date.now() < deadline) {
      const btn = document.querySelector('button[data-purpose="submit-answer"], button[data-purpose="check-answer"]');
      if (btn && !btn.disabled) { btn.click(); return; }
      await sleep(50);
    }
    // Fallback: click even if still disabled
    const btn = document.querySelector('button[data-purpose="submit-answer"], button[data-purpose="check-answer"]');
    if (btn) btn.click();
  }

  function getCorrectAnswers(options) {
    const correctPanes = [...document.querySelectorAll('[data-purpose="answer"]')].filter(p =>
      p.className.includes('answer-result-pane--answer-correct--')
    );

    return correctPanes.map(pane => {
      const textEl = pane.querySelector('[class*="answer-body"]') ||
                     pane.querySelector('[data-purpose*="rich-text-viewer"]');
      const correctText = htmlToTextWithImages(textEl) || safeText(textEl);
      if (!correctText) return null;

      // Exact match
      let match = options.find(opt => opt.text === correctText);
      // Substring match fallback (compare first 30 chars of plain text, ignoring image markers)
      if (!match) {
        const plainCorrect = correctText.replace(/!\[image\]\([^)]+\)/g, '').trim();
        match = options.find(opt => {
          const plainOpt = opt.text.replace(/!\[image\]\([^)]+\)/g, '').trim();
          return plainOpt.length >= 20 && plainCorrect.includes(plainOpt.slice(0, 30));
        });
      }
      return match ? match.index : null;
    }).filter(idx => idx !== null);
  }

  function getExplanation() {
    return htmlToTextWithImages(document.querySelector('#overall-explanation'));
  }

  function downloadJSON(data, filename) {
    const a = Object.assign(document.createElement('a'), {
      href: URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })),
      download: filename
    });
    a.click();
  }

  // ---- Main scraping loop ----
  const EXPECTED_QUESTIONS = 65;
  let questionNum = 0;

  while (true) {
    questionNum++;

    if (questionNum > EXPECTED_QUESTIONS) {
      console.log(`\n[+] Reached ${EXPECTED_QUESTIONS} questions - done.`);
      downloadJSON(results, 'exam_results_final.json');
      break;
    }

    // (question + inputs are already loaded - transition poll below ensures this)

    const questionText = getQuestionText();
    if (!questionText) { console.log('[!] Empty question text - stopping'); break; }

    const options = getOptions();
    console.log(`[~] Q${questionNum}: got ${options.length} options`);
    if (!options.length) { console.log('[!] No answer options found - stopping'); break; }

    const questionType = getQuestionType();
    console.log(`[~] Q${questionNum}: type=${questionType}, selecting answers...`);
    const selected = await selectRandomAnswers();
    await submitAnswer();

    console.log(`[*] Q${questionNum} (${questionType}) selected: [${selected}] — ${questionText.slice(0, 50)}...`);

    // Wait for result pane to appear
    try {
      await waitFor('[class*="question-result--question-result"]', 8000);
    } catch (e) {
      console.log(`[!] Q${questionNum}: result pane did not appear - ${e.message}`);
      break;
    }

    const correctAnswers = getCorrectAnswers(options);
    const explanation = getExplanation();
    console.log(`[~] Q${questionNum}: correct=[${correctAnswers.join(', ')}], explanation=${explanation ? 'yes' : 'no'}`);

    results.push({ question: questionText, question_type: questionType, options, correct_answers: correctAnswers, explanation });
    console.log(`[+] Q${questionNum} correct: [${correctAnswers.join(', ')}]`);

    // Advance to next question
    const nextBtn =
      document.querySelector('button[data-purpose="go-to-next-question"]') ||
      [...document.querySelectorAll('button')].find(b => b.innerText?.trim() === 'Next question');
    if (!nextBtn) {
      console.log('\n[+] No Next button - exam complete!');
      downloadJSON(results, 'exam_results_final.json');
      break;
    }

    // Snapshot state before navigating
    const currentHighlight = document.querySelector('[data-purpose="question-navigation-item"][class*="highlight"]');
    const currentHighlightTitle = currentHighlight?.querySelector('[class*="question-navigation-item--title"]')?.innerText?.trim() || '';
    const currentQuestionText = questionText;

    // Wait for Next button to be enabled (Udemy enables it async after result renders)
    const btnDeadline = Date.now() + 3000;
    while (Date.now() < btnDeadline && nextBtn.disabled) await sleep(50);

    nextBtn.click();

    // Step 1: wait for sidebar highlight OR question text to change
    const t1 = Date.now() + 8000;
    while (Date.now() < t1) {
      await sleep(50);
      const newHighlight = document.querySelector('[data-purpose="question-navigation-item"][class*="highlight"]');
      const newTitle = newHighlight?.querySelector('[class*="question-navigation-item--title"]')?.innerText?.trim() || '';
      if (newTitle && newTitle !== currentHighlightTitle) break;
      const newQ = safeText(document.querySelector('#question-prompt'));
      if (newQ && newQ !== currentQuestionText) break;
    }

    // Step 2: wait for inputs, or detect results/summary screen
    const deadline = Date.now() + 8000;
    let loaded = false;
    while (Date.now() < deadline) {
      await sleep(50);
      if (document.querySelectorAll('input[name="answer"]').length > 0) { loaded = true; break; }
      if (document.querySelector('[class*="practice-test-result"]') ||
          document.querySelector('[data-purpose="exam-score"]') ||
          !document.querySelector('#question-prompt')) {
        console.log('\n[+] Results screen detected - exam complete!');
        downloadJSON(results, 'exam_results_final.json');
        return;
      }
    }
    if (!loaded) {
      console.log(`[!] Q${questionNum}: inputs did not appear - downloading ${results.length} results`);
      downloadJSON(results, 'exam_results_final.json');
      break;
    }
  }

  console.log(`\n[+] Done! ${results.length} questions scraped.`);
})();
