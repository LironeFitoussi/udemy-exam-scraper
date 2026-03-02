"""
Generate an HTML preview from scraped exam JSON data.
Usage: python generate_html.py [input.json] [output.html]
"""
import json
import re
import sys
import html as html_mod
from pathlib import Path


def render_text(text):
    """Convert plain text to HTML, rendering ![image](url) markers and links."""
    if not text:
        return ""

    # Split text into chunks: URLs/image-markers vs plain text.
    # Process each chunk differently to avoid escaping URLs.
    IMG_MD = r'!\[image\]\(https?://[^)]+\)'
    IMG_URL = r'https?://[^\s"<>]+\.(?:png|jpg|jpeg|gif|webp|svg)(?:\?[^\s"<>]*)?'
    LINK_URL = r'https?://[^\s"<>]+'
    token_re = re.compile(f'({IMG_MD}|{IMG_URL}|{LINK_URL})')

    parts = token_re.split(text)
    out = []
    for part in parts:
        if re.fullmatch(IMG_MD, part):
            url = re.search(r'\((https?://[^)]+)\)', part).group(1)
            out.append(f'<img src="{url}" alt="diagram" loading="lazy">')
        elif re.fullmatch(IMG_URL, part):
            out.append(f'<img src="{part}" alt="diagram" loading="lazy">')
        elif re.fullmatch(LINK_URL, part):
            safe = html_mod.escape(part)
            out.append(f'<a href="{safe}" target="_blank" rel="noopener">{safe}</a>')
        else:
            escaped = html_mod.escape(part)
            out.append(escaped.replace("\n", "<br>\n"))
    return "".join(out)


def generate_html(data):
    single = sum(1 for q in data if q["question_type"] == "single_select")
    multi = len(data) - single

    cards = []
    for i, q in enumerate(data):
        is_multi = q["question_type"] == "multi_select"
        type_label = f"Select Multiple ({len(q['correct_answers'])})" if is_multi else "Single Answer"
        type_class = "type-multi" if is_multi else "type-single"
        letters = "ABCDEFGHIJ"

        opts_html = ""
        for oi, opt in enumerate(q["options"]):
            is_correct = oi in q.get("correct_answers", []) or opt.get("index", oi) in q.get("correct_answers", [])
            correct_cls = " correct" if is_correct else ""
            letter_cls = "letter-correct" if is_correct else ""
            opts_html += f'''<li class="option{correct_cls}">
                <span class="letter {letter_cls}">{letters[oi]}</span>
                <span class="opt-text">{render_text(opt["text"])}</span>
            </li>\n'''

        explanation_html = render_text(q.get("explanation", ""))

        cards.append(f'''
    <div class="card" id="q{i+1}">
        <div class="q-header">
            <span class="q-num">Q{i+1}</span>
            <span class="{type_class}">{type_label}</span>
        </div>
        <div class="q-text">{render_text(q["question"])}</div>
        <ul class="opts">{opts_html}</ul>
        <button class="toggle" onclick="toggleExpl(this)">Show Explanation</button>
        <div class="expl">{explanation_html}</div>
    </div>''')

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exam Preview — {len(data)} Questions</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f0f2f5; color: #1a1a2e; line-height: 1.6; padding: 20px; }}
.header {{ text-align: center; padding: 28px 20px; background: linear-gradient(135deg, #667eea, #764ba2); color: #fff; border-radius: 12px; margin: 0 auto 20px; max-width: 900px; }}
.header h1 {{ font-size: 1.7rem; margin-bottom: 6px; }}
.header .stats {{ font-size: .95rem; opacity: .9; }}
.toolbar {{ max-width: 900px; margin: 0 auto 18px; display: flex; gap: 10px; flex-wrap: wrap; }}
.toolbar input {{ flex: 1; min-width: 180px; padding: 10px 14px; border: 2px solid #ddd; border-radius: 8px; font-size: .95rem; outline: none; }}
.toolbar input:focus {{ border-color: #667eea; }}
.toolbar select, .toolbar button {{ padding: 10px 16px; border: 2px solid #ddd; border-radius: 8px; font-size: .95rem; background: #fff; cursor: pointer; }}
.toolbar button {{ border: none; background: #667eea; color: #fff; }}
.toolbar button:hover {{ background: #5a6fd6; }}
.toolbar button.on {{ background: #e74c3c; }}
.card {{ background: #fff; border-radius: 12px; padding: 26px; margin: 0 auto 18px; max-width: 900px; box-shadow: 0 2px 8px rgba(0,0,0,.08); }}
.q-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }}
.q-num {{ background: #667eea; color: #fff; padding: 4px 14px; border-radius: 20px; font-weight: 600; font-size: .85rem; }}
.type-single {{ padding: 4px 12px; border-radius: 20px; font-size: .8rem; font-weight: 500; background: #e8f5e9; color: #2e7d32; }}
.type-multi {{ padding: 4px 12px; border-radius: 20px; font-size: .8rem; font-weight: 500; background: #fff3e0; color: #e65100; }}
.q-text {{ font-size: 1.05rem; margin-bottom: 18px; line-height: 1.7; }}
.opts {{ list-style: none; }}
.option {{ padding: 12px 16px; margin-bottom: 8px; border-radius: 8px; border: 2px solid #e8e8e8; display: flex; align-items: flex-start; gap: 12px; }}
.option.correct {{ border-color: #4caf50; background: #e8f5e9; }}
.letter {{ width: 28px; height: 28px; border-radius: 50%; background: #f0f0f0; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: .85rem; flex-shrink: 0; }}
.letter-correct {{ background: #4caf50; color: #fff; }}
.opt-text {{ flex: 1; }}
img {{ max-width: 100%; border-radius: 8px; margin: 10px 0; display: block; border: 1px solid #eee; }}
.toggle {{ margin-top: 12px; padding: 8px 18px; border: 2px solid #667eea; background: transparent; color: #667eea; border-radius: 8px; cursor: pointer; font-size: .9rem; font-weight: 500; }}
.toggle:hover {{ background: #667eea; color: #fff; }}
.expl {{ display: none; margin-top: 16px; padding: 18px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea; font-size: .93rem; line-height: 1.7; }}
.expl.show {{ display: block; }}
.expl a {{ color: #667eea; text-decoration: none; }}
.expl a:hover {{ text-decoration: underline; }}
.hidden {{ display: none !important; }}
.nav {{ position: fixed; bottom: 20px; right: 20px; display: flex; gap: 8px; }}
.nav button {{ width: 44px; height: 44px; border-radius: 50%; border: none; background: #667eea; color: #fff; font-size: 1.2rem; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,.2); }}
.nav button:hover {{ background: #5a6fd6; }}
@media (max-width: 600px) {{ body {{ padding: 10px; }} .card {{ padding: 16px; }} .toolbar {{ flex-direction: column; }} }}
</style>
</head>
<body>
<div class="header">
    <h1>AWS Exam Questions Preview</h1>
    <div class="stats">{len(data)} questions &middot; {single} single &middot; {multi} multi-select</div>
</div>
<div class="toolbar">
    <input id="search" type="text" placeholder="Search questions...">
    <select id="typeFilter">
        <option value="all">All Types</option>
        <option value="single">Single Select</option>
        <option value="multi">Multi Select</option>
    </select>
    <button id="toggleAll">Show All Answers</button>
    <button id="toggleCorrect">Hide Correct</button>
</div>
{"".join(cards)}
<div class="nav">
    <button onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="Scroll to top">&uarr;</button>
</div>
<script>
function toggleExpl(btn) {{
    const expl = btn.nextElementSibling;
    expl.classList.toggle('show');
    btn.textContent = expl.classList.contains('show') ? 'Hide Explanation' : 'Show Explanation';
}}

let allShown = false;
document.getElementById('toggleAll').addEventListener('click', function() {{
    allShown = !allShown;
    this.textContent = allShown ? 'Hide All Answers' : 'Show All Answers';
    this.classList.toggle('on', allShown);
    document.querySelectorAll('.expl').forEach(e => e.classList.toggle('show', allShown));
    document.querySelectorAll('.toggle').forEach(b => b.textContent = allShown ? 'Hide Explanation' : 'Show Explanation');
    if (!allShown) {{
        document.querySelectorAll('.option.correct').forEach(o => {{ /* keep visible */ }});
    }}
}});

let correctHidden = false;
document.getElementById('toggleCorrect').addEventListener('click', function() {{
    correctHidden = !correctHidden;
    this.textContent = correctHidden ? 'Show Correct' : 'Hide Correct';
    this.classList.toggle('on', correctHidden);
    document.querySelectorAll('.option').forEach(o => {{
        if (correctHidden) {{
            o.classList.remove('correct');
            o.querySelector('.letter')?.classList.remove('letter-correct');
        }} else {{
            if (o.dataset.correct === '1') {{
                o.classList.add('correct');
                o.querySelector('.letter')?.classList.add('letter-correct');
            }}
        }}
    }});
}});

// Mark correct options with data attribute for toggle
document.querySelectorAll('.option.correct').forEach(o => o.dataset.correct = '1');

function filterCards() {{
    const q = document.getElementById('search').value.toLowerCase();
    const t = document.getElementById('typeFilter').value;
    document.querySelectorAll('.card').forEach(c => {{
        const matchType = t === 'all' || (t === 'single' && c.querySelector('.type-single')) || (t === 'multi' && c.querySelector('.type-multi'));
        const matchText = !q || c.textContent.toLowerCase().includes(q);
        c.classList.toggle('hidden', !(matchType && matchText));
    }});
}}
document.getElementById('search').addEventListener('input', filterCards);
document.getElementById('typeFilter').addEventListener('change', filterCards);
</script>
</body>
</html>'''


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "exam_results_final.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace(".json", ".html")
    if output_file == input_file:
        output_file = "exam_preview.html"

    path = Path(input_file)
    if not path.exists():
        print(f"[!] File not found: {input_file}")
        sys.exit(1)

    data = json.loads(path.read_text(encoding="utf-8"))
    html_content = generate_html(data)
    Path(output_file).write_text(html_content, encoding="utf-8")
    print(f"[+] Generated {output_file} with {len(data)} questions")


if __name__ == "__main__":
    main()
