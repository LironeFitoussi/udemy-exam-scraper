# Udemy Exam Scraper - Setup & Getting Started

## What's Been Built

### Core Components Created:
1. **UdemyPage** (`pages/udemy_page.py`) - Main page object for Udemy interactions
   - Navigate to Udemy home
   - Check login status
   - Search for courses
   - Navigate to My Courses
   - Get page title and URL

2. **LoginPage** (`pages/login_page.py`) - Login page object
   - Enter email and password
   - Click login button
   - Complete login workflow
   - Get error messages
   - Check if login form is visible

3. **Enhanced DriverFactory** (`utils/driver_factory.py`)
   - Uses `webdriver-manager` for automatic driver management
   - **Non-headless mode for development** (browsers open visibly)
   - Supports Chrome, Firefox, and Edge
   - No manual driver setup needed

4. **Main Application** (`main.py`)
   - Interactive menu-driven interface
   - Browser selection
   - Login workflow
   - Navigate to courses
   - Search functionality
   - Page information display

### Updated Dependencies:
- `selenium==4.21.0`
- `webdriver-manager==4.0.1` - Auto-manages WebDrivers
- `python-dotenv==1.0.0` - For environment variables

## How to Run

### First Time Setup:
```bash
# Install dependencies
pip install -r requirements.txt
```

### Run the Application:
```bash
# Option 1: Direct Python
python main.py

# Option 2: Using npm
npm start
```

### What Happens:
1. Browser opens **visibly** (non-headless)
2. Udemy.com loads
3. App checks if you're logged in
4. If not logged in, prompts for login
5. Interactive menu appears with options

## Browser Features During Development:
✓ **Visible browser window** - see everything happening
✓ **Auto WebDriver management** - no manual driver downloads
✓ **Interactive debugging** - pause and inspect page
✓ **Full page interaction** - all Udemy features accessible

## Next Steps:
1. Run the app and test Udemy navigation
2. Create ExamPage object for exam interaction
3. Build course listing scraper
4. Implement exam question extraction
5. Add data export functionality

## Project Structure:
```
├── pages/
│   ├── base_page.py       # Base class with common methods
│   ├── udemy_page.py      # Udemy main page interactions ✓ NEW
│   └── login_page.py      # Login workflow ✓ NEW
├── utils/
│   ├── driver_factory.py  # WebDriver management ✓ UPDATED
│   └── __init__.py
├── main.py                # Entry point ✓ UPDATED
├── requirements.txt       # Dependencies ✓ UPDATED
└── .claude/               # Claude configuration
```

## Important Notes:
- Credentials are **NOT stored** - you enter them when needed
- Add a `config/credentials.json` if you want to store credentials (it's gitignored)
- Non-headless mode allows you to see and interact with the browser
- All locators can be updated as Udemy's HTML changes
