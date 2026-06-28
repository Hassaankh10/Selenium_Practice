# Selenium Practice

Python scripts for learning and practicing web automation with Selenium WebDriver.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver (matching your Chrome version)

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install selenium webdriver-manager
```

## Scripts

| File | Description |
|------|-------------|
| `script.py` | Basic browser navigation |
| `modscript.py` | ChromeDriver setup via `webdriver-manager` |
| `login.py` | Login form automation |
| `loginjellyfin.py` | Login automation for a self-hosted media server |
| `checkbox.py` | Checkbox interaction with explicit waits |
| `mousehover.py` | Mouse hover using ActionChains |
| `nopcustomer.py` | Admin panel automation on a demo e-commerce site |
| `alnafilinks.py` | Extracting footer links from a webpage |
| `wikipedia.py` | Search and dropdown selection on Wikipedia |
| `selenium_screenshot.py` | Capturing screenshots |
| `xpath_axes_test.py` | XPath axes (parent, child, sibling, ancestor, etc.) |

> **Note:** Scripts that require credentials use placeholder values (`YOUR_USERNAME`, `YOUR_PASSWORD`). Replace these before running.

## Practice Tasks

Step-by-step exercises in [`Practice Tasks/`](Practice%20Tasks/) — `prac_task1.py` through `prac_task10.py`.

## Screenshots

Automation screenshots are saved to the [`Screenshot/`](Screenshot/) folder.
