# .Claude Configuration Index

## 📊 Quick Stats
- **Total Files**: 20
- **Total Documentation**: 1,728 lines
- **Configuration Size**: 96 KB
- **Status**: ✅ Production Ready

---

## 📖 Main Documents

| File | Purpose | Lines |
|------|---------|-------|
| [**CLAUDE.md**](CLAUDE.md) | 📘 Project guide - READ THIS FIRST | 180+ |
| [**README.md**](README.md) | Overview and navigation | 200+ |
| [**SETUP_SUMMARY.md**](SETUP_SUMMARY.md) | What was created and how to use it | 250+ |
| [**INDEX.md**](INDEX.md) | This file - quick reference | - |
| [**config.json**](config.json) | Machine-readable configuration | JSON |

---

## 🤖 Agents (4 total)

Located in [`agents/`](agents/) directory

| Agent | Purpose | When to Use |
|-------|---------|------------|
| [**test-runner.md**](agents/test-runner.md) | Run pytest with coverage | User: "Run the tests" |
| [**scraper-analyzer.md**](agents/scraper-analyzer.md) | Validate scraped data | `/validate` command |
| [**code-explorer.md**](agents/code-explorer.md) | Explore codebase | "Where is X?" questions |
| [**feature-builder.md**](agents/feature-builder.md) | Implement features | "Add new page object" |

---

## 🎮 Commands (7 total)

Located in [`commands/`](commands/) directory

| Command | File | Purpose |
|---------|------|---------|
| `/run` | [run.md](commands/run.md) | Execute scraper (interactive/headless) |
| `/test` | [test.md](commands/test.md) | Run pytest (with options) |
| `/add-page [Name]` | [add-page.md](commands/add-page.md) | Create page object scaffold |
| `/validate` | [validate.md](commands/validate.md) | Check data quality |
| `/lint` | [lint.md](commands/lint.md) | Code style and security checks |
| `/debug` | [debug.md](commands/debug.md) | Run with verbose logging |
| `/export-exams` | [export-exams.md](commands/export-exams.md) | Export to JSON/CSV/Excel/PDF |

---

## 🔧 Hooks (4 total)

Located in [`hooks/`](hooks/) directory

| Hook | File | Triggers | Purpose |
|------|------|----------|---------|
| pre-edit-security | [pre-edit-security.md](hooks/pre-edit-security.md) | Before edits | Detect hardcoded secrets |
| post-test-report | [post-test-report.md](hooks/post-test-report.md) | After tests | Show test summaries |
| pre-commit-checks | [pre-commit-checks.md](hooks/pre-commit-checks.md) | Before commits | Validate code |
| data-validation-hook | [data-validation-hook.md](hooks/data-validation-hook.md) | Data changes | Ensure data integrity |

---

## 🚀 Getting Started

### 1. Read CLAUDE.md First ⭐
```bash
cat .claude/CLAUDE.md
```
Contains project overview, workflows, conventions, and setup.

### 2. Try Commands
```bash
/run              # Execute scraper
/test             # Run tests
/add-page Page    # Create page object
/validate         # Check data quality
/lint             # Code style checks
/debug            # Debug mode
/export-exams     # Export data
```

### 3. Use Agents (Automatic)
Claude uses agents automatically:
- "Run tests" → **test-runner** agent
- "Check data" → **scraper-analyzer** agent
- "Where is X?" → **code-explorer** agent
- "Add feature" → **feature-builder** agent

### 4. Review Conventions
Read CLAUDE.md section on:
- Page Object Model pattern
- Code organization
- Testing approach
- Data format
- Security practices

---

## 📋 File Organization

```
.claude/
├── 📖 Documentation
│   ├── CLAUDE.md              Main project guide
│   ├── README.md              Configuration overview
│   ├── SETUP_SUMMARY.md       What was created
│   ├── INDEX.md               This file
│   └── config.json            Configuration
│
├── 🤖 agents/                 4 specialized agents
│   ├── test-runner.md
│   ├── scraper-analyzer.md
│   ├── code-explorer.md
│   └── feature-builder.md
│
├── 🎮 commands/               7 custom commands
│   ├── run.md
│   ├── test.md
│   ├── add-page.md
│   ├── validate.md
│   ├── lint.md
│   ├── debug.md
│   └── export-exams.md
│
└── 🔧 hooks/                  4 automation hooks
    ├── pre-edit-security.md
    ├── post-test-report.md
    ├── pre-commit-checks.md
    └── data-validation-hook.md
```

---

## 💡 Quick Reference

### Common Tasks

| Task | Command | What Happens |
|------|---------|--------------|
| Run scraper | `/run` | Interactive browser automation |
| Run scraper (silent) | `/run-headless` | No UI, for automation |
| Run tests | `/test` | Pytest with summary |
| Create page object | `/add-page Name` | Scaffold new page class |
| Check data | `/validate` | Data quality report |
| Check code style | `/lint` | Code quality checks |
| Debug issue | `/debug --pause` | Verbose logging + pause on error |
| Export data | `/export-exams` | JSON/CSV/Excel/PDF options |

### Key Conventions

```python
# Page Object Pattern
class PageNamePage(BasePage):
    LOCATOR_NAME = (By.ID, "selector")

    def method_name(self):
        self.click(self.LOCATOR_NAME)

# Test Pattern
class TestPageNamePage:
    def test_something(self, driver):
        page = PageNamePage(driver)
        # assertions...
```

### Data Format
```json
{
  "course_id": "id",
  "course_name": "name",
  "exams": [{
    "exam_id": "id",
    "title": "title",
    "questions": [{
      "id": "id",
      "text": "text",
      "answers": [],
      "correct_answer": "answer"
    }]
  }]
}
```

---

## 🎓 Learn More

### For Understanding Structure
- **CLAUDE.md** - Project overview and conventions
- **README.md** - How .claude folder works

### For Using Commands
- **command files** in `commands/` - Syntax, options, examples

### For Using Agents
- **agent files** in `agents/` - Capabilities and use cases

### For Understanding Automation
- **hook files** in `hooks/` - What runs and when

### For Configuration
- **config.json** - All settings in machine-readable format

---

## ❓ Questions?

### "How do I...?"
→ Check **[CLAUDE.md](CLAUDE.md)** first

### "What does [command] do?"
→ See `commands/[command].md`

### "When is [agent] used?"
→ See `agents/[agent].md`

### "How do I [task]?"
→ Search relevant file or ask Claude!

---

## 📊 Statistics

| Category | Count | Status |
|----------|-------|--------|
| Agents | 4 | ✅ All active |
| Commands | 7 | ✅ All active |
| Hooks | 4 | ✅ All active |
| Documentation Files | 20 | ✅ Complete |
| Total Lines | 1,728+ | ✅ Comprehensive |
| Configuration | 1 | ✅ Ready |

---

## 🎯 Next Steps

1. ✅ **Setup Complete** - Configuration is ready
2. **Read [CLAUDE.md](CLAUDE.md)** - Understand project
3. **Try `/run`** - Execute the scraper
4. **Try `/test`** - Run test suite
5. **Create page objects** - Use `/add-page`
6. **Validate data** - Use `/validate`

---

## 📝 Version Info

- **Version**: 1.0
- **Created**: 2026-03-01
- **Status**: ✅ Production Ready
- **Last Updated**: 2026-03-01

---

**Start with [CLAUDE.md](CLAUDE.md) →**
