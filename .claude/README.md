# Claude Configuration for Udemy Exam Scraper

This directory contains all Claude-related configurations for the Udemy Exam Scraper project, enabling specialized agents, custom commands, and automation hooks.

## 📁 Directory Structure

```
.claude/
├── CLAUDE.md                    # Main project context and conventions
├── config.json                  # Configuration file
├── README.md                    # This file
├── agents/                      # Specialized sub-agents
│   ├── test-runner.md          # Run tests with coverage
│   ├── scraper-analyzer.md     # Validate scraped data
│   ├── code-explorer.md        # Explore codebase
│   └── feature-builder.md      # Implement new features
├── commands/                    # Custom slash commands
│   ├── run.md                  # Execute scraper
│   ├── test.md                 # Run pytest
│   ├── add-page.md             # Create page objects
│   ├── validate.md             # Validate data
│   ├── lint.md                 # Code quality checks
│   ├── debug.md                # Debug mode
│   └── export-exams.md         # Export data
└── hooks/                       # Automation hooks
    ├── pre-edit-security.md    # Security warnings before edits
    ├── post-test-report.md     # Test result summaries
    ├── pre-commit-checks.md    # Validation before commits
    └── data-validation-hook.md # Auto-validate scraped data
```

## 🚀 Quick Start

### Read First
Start with **[CLAUDE.md](CLAUDE.md)** - it contains:
- Project overview and goals
- Development workflow
- Code organization conventions
- Environment setup
- Debugging tips
- Security best practices

### Available Commands
Use these slash commands in Claude Code:

| Command | Purpose |
|---------|---------|
| `/run` | Execute the scraper |
| `/test` | Run pytest suite |
| `/add-page [name]` | Create new page object |
| `/validate` | Check scraped data quality |
| `/lint` | Run code style checks |
| `/debug` | Run with verbose logging |
| `/export-exams` | Export data to JSON/CSV/Excel |

### Specialized Agents
Claude will automatically use these when appropriate:

- **test-runner**: Handles `/test` and related test commands
- **scraper-analyzer**: Validates and analyzes scraped data
- **code-explorer**: Answers questions about codebase structure
- **feature-builder**: Helps implement new features

## 📖 Documentation

Each file in this directory has a specific purpose:

### CLAUDE.md
**Read this first!** Contains:
- Project description and goals
- How to run the scraper
- Page Object Model conventions
- Data format and validation
- Environment setup
- Debugging and troubleshooting

### config.json
Machine-readable configuration:
- Project metadata
- Enabled agents and commands
- Hook triggers
- Dependencies

### Agents (agents/ directory)
Specialized sub-agents for different tasks:
- **test-runner.md**: Test execution and coverage
- **scraper-analyzer.md**: Data validation and analysis
- **code-explorer.md**: Codebase exploration
- **feature-builder.md**: Feature implementation

### Commands (commands/ directory)
Custom slash commands documented:
- **run.md**: Execution options and modes
- **test.md**: Testing framework integration
- **add-page.md**: Page object scaffolding
- **validate.md**: Data quality checks
- **lint.md**: Code style and security
- **debug.md**: Debugging with logging/screenshots
- **export-exams.md**: Data export formats

### Hooks (hooks/ directory)
Automation that runs automatically:
- **pre-edit-security.md**: Prevents credentials in code
- **post-test-report.md**: Summarizes test results
- **pre-commit-checks.md**: Validates before commits
- **data-validation-hook.md**: Ensures data quality

## 💡 Usage Examples

### Running the Scraper
```
User: "Start scraping from a Udemy course"
Claude: "I'll use /run to start the scraper with interactive prompts"
```

### Testing Your Changes
```
User: "Run the tests"
Claude: "I'll use the test-runner agent to execute pytest"
```

### Adding a New Page Object
```
User: "Create a page object for the exam results page"
Claude: "I'll use /add-page ExamResultsPage to scaffold it"
```

### Validating Data Quality
```
User: "Check if the scraped data is valid"
Claude: "I'll use /validate to run comprehensive data checks"
```

## 🔒 Security Features

These hooks automatically protect your code:

1. **pre-edit-security**: Warns before committing credentials
2. **pre-commit-checks**: Validates code before commits
3. **data-validation-hook**: Ensures data integrity

Never commit secrets! Use environment variables instead.

## 🎯 Key Conventions

### Page Objects
- File name: `snake_case` (e.g., `exam_page.py`)
- Class name: `PascalCase` (e.g., `ExamPage`)
- Locators: `UPPER_SNAKE_CASE` (e.g., `SUBMIT_BUTTON`)
- Methods: `lower_snake_case` (e.g., `click_submit()`)

### Code Style
- Python PEP 8 compliance
- Use black formatter
- Run `/lint` before committing
- Include docstrings for complex methods

### Testing
- Test files in `tests/` directory
- File naming: `test_*.py`
- Use pytest framework
- Run `/test` before commits

## 📊 Data Format

Scraped exam data follows this JSON structure:
```json
{
  "course_id": "123456",
  "course_name": "Python Programming",
  "exams": [
    {
      "exam_id": "exam_1",
      "title": "Midterm Exam",
      "questions": [
        {
          "id": "q1",
          "text": "What is Python?",
          "answers": ["A) Language", "B) Snake", "C) Framework"],
          "correct_answer": "A) Language"
        }
      ]
    }
  ]
}
```

Use `/validate` to ensure data conforms to this schema.

## 🛠️ Getting Help

### Read Documentation
1. **[CLAUDE.md](CLAUDE.md)** - Project-specific conventions
2. **Command files** in `commands/` - How each command works
3. **Agent files** in `agents/` - When agents are used
4. **Hook files** in `hooks/` - Automation details

### Ask Claude
```
User: "How do I create a new page object?"
Claude: "I'll help! First let me check /add-page documentation"

User: "What's the correct data format?"
Claude: "Let me review the CLAUDE.md for the data schema"
```

### Run Diagnostics
```
/run --debug        # Run scraper with verbose logging
/test --cov         # Run tests with coverage report
/validate --strict  # Strict data validation
/lint --strict      # Strict code quality checks
```

## 📝 Notes

- This .claude folder was generated as a complete setup
- All configurations follow project conventions
- Hooks run automatically to catch issues early
- Agents are used transparently when helpful
- Commands provide shortcuts for common tasks

## 🔄 Maintenance

Keep this folder updated:
- Update CLAUDE.md when conventions change
- Add new commands as features are added
- Update agents when new capabilities needed
- Review hooks periodically for relevance

Questions? Check CLAUDE.md first, then ask Claude!
