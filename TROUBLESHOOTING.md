# Troubleshooting Guide

## Issues Fixed

### 1. WebDriver Installation Error
**Problem**: `OSError: [WinError 193] %1 is not a valid Win32 application`

**Solution**:
- Cleared webdriver-manager cache
- Reinstalled webdriver-manager with version 4.0.2
- Switched default browser from Chrome to Firefox (more stable on Windows)

**File**: `fix_drivers.py` - Automated troubleshooting script

### 2. Unicode/Encoding Issues on Windows
**Problem**: `UnicodeEncodeError: 'charmap' codec can't encode character`

**Solution**:
- Replaced emoji characters with ASCII symbols `[+]`, `[!]`, `[x]`, `[*]`
- This is compatible with Windows Console encoding

**Files Updated**:
- `main.py`
- `fix_drivers.py`

## Current Status

✓ **Working**: Firefox driver with Udemy access
✓ **Tested**:
  - App launches correctly
  - Connects to Udemy.com
  - Detects login status
  - Interactive menu functional
  - Non-headless mode (visible browser)

## If You Still Have Issues

### Option 1: Run the Fix Script
```bash
python fix_drivers.py
```
This will:
- Clear the cache
- Reinstall webdriver-manager
- Test all browsers
- Tell you which one works

### Option 2: Use a Specific Browser
```bash
# Firefox (recommended for Windows)
python main.py
# (Press Enter to select firefox, or type firefox)

# Edge (Windows native)
python main.py
# (Type edge)
```

### Option 3: Manual Install
```bash
# Clear cache manually
rm -r %USERPROFILE%\.wdm

# Reinstall cleanly
pip install --upgrade --force-reinstall webdriver-manager selenium

# Run app
python main.py
```

## Browser Compatibility

| Browser | Status | Notes |
|---------|--------|-------|
| Firefox | ✓ Working | Recommended for Windows |
| Edge | ? Untested | Windows native browser |
| Chrome | ? Untested | May need additional setup |

## Next: Finding the Login Button

The login button has been updated with the correct Udemy locator:
```python
SIGN_IN_BUTTON = (By.XPATH, "//a[@data-purpose='header-login']")
```

The app can now:
1. Click the login button
2. Enter email/password
3. Submit the login form

Ready to test login? Run: `python main.py`
