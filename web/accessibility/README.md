# Web — Accessibility Testing

Automated accessibility (a11y) scans of [Sauce Demo](https://www.saucedemo.com/) — the same target used in `web/manual` and `web/automation` — built with **axe-core** injected into Playwright pages.

## Why axe-core, and why inject it instead of a Python package

axe-core is the industry-standard accessibility rules engine (built by Deque; it's what powers Lighthouse's a11y audit and many browser extensions under the hood). It's a JavaScript library, and there's no official first-party Python port — the standard, documented approach is to inject the script into the page under test and run it in the browser's own JS context. That's exactly what [`lib/axe_helper.py`](./lib/axe_helper.py) does: it adds the axe-core script via Playwright, then evaluates `axe.run()` inside the page and returns the results back to Python.

## Structure

```
web/accessibility/
├── lib/
│   └── axe_helper.py    → injects axe-core, runs the scan, and turns results into a pass/fail assertion
├── tests/
│   ├── test_login_page_a11y.py
│   ├── test_inventory_page_a11y.py
│   └── test_cart_and_checkout_a11y.py
├── requirements.txt
└── pytest.ini
```

## How violations are triaged

axe-core reports violations with an `impact` level: `critical`, `serious`, `moderate`, or `minor`. This suite fails a test only on `critical` or `serious` findings — `moderate`/`minor` issues are still visible in the failure message if a test does fail for another reason, but don't block the suite on their own. This mirrors how most teams actually triage accessibility findings: not everything blocks a release, but the high-impact issues should.

## Running locally

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
playwright install

pytest
```

An HTML report (`report.html`) is generated after each run. Each failure includes the specific axe-core rule that failed, how many elements were affected, and a link to Deque's documentation for that rule.

## CI

Runs automatically via `.github/workflows/accessibility.yml` on every push or PR touching this folder.
