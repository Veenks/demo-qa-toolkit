# Web — Automation

End-to-end test automation framework for [Sauce Demo](https://www.saucedemo.com/), built with **Playwright + Python**, following the Page Object Model (POM) — split further into **Map / Actions / Asserts** partials per page — and running automatically in CI.

## Why this structure

- **Playwright**: auto-waiting and reliable selectors, without the flakiness typical of older tools
- **Python + pytest**: readable syntax, fixtures for setup, marker-based test selection (`smoke` vs `regression`)
- **Map / Actions / Asserts split**: Python has no native "partial classes" like C#, so each page is split into three small mixin classes — one per concern — combined into a single class via multiple inheritance in that page's `__init__.py`:
  - `map.py` — locators only (where things are)
  - `actions.py` — verbs only (what a user can do)
  - `asserts.py` — verifications only (what can be checked)

  This keeps each file focused and small, and makes it obvious where to add new code: a new locator goes in `map.py`, a new interaction in `actions.py`, a new check in `asserts.py`.

## Structure

```
web/automation/
├── pages/
│   ├── login/
│   │   ├── map.py
│   │   ├── actions.py
│   │   ├── asserts.py
│   │   └── __init__.py       → combines the three into LoginPage
│   ├── inventory/            (same structure)
│   ├── cart/                 (same structure)
│   └── checkout/             (same structure — covers all 3 checkout steps)
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py                → shared fixtures (page objects, pre-authenticated session)
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Usage example

From the outside, each page behaves like a single class — callers don't need to know it's split into three files:

```python
from pages.login import LoginPage

login_page = LoginPage(page)
login_page.goto()
login_page.login("standard_user", "secret_sauce")
```

## Coverage

| Area | Cases covered (see `../manual/test-cases.md`) |
|---|---|
| Login | LOGIN-01 to LOGIN-04 |
| Cart | CART-01 to CART-04 |
| Checkout | CHK-01 to CHK-04 |

Tests are tagged `@pytest.mark.smoke` (core happy path) or `@pytest.mark.regression` (broader coverage).

## Running locally

```bash
# Recommended: use a virtual environment scoped to this project
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
playwright install

pytest              # run everything
pytest -m smoke     # smoke tests only
pytest --headed     # run with a visible browser
```

## CI

Every push or PR touching this folder triggers the workflow defined at the repo root (`.github/workflows/playwright.yml` — GitHub Actions only reads workflows from `.github/workflows/` at the top level, not from subfolders).
