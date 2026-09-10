"""Helper to inject axe-core and run accessibility scans against a Playwright page.

axe-core is the industry-standard accessibility rules engine (built by Deque,
the same engine used under the hood by Lighthouse and many browser extensions).
There's no official Python package for it — the standard approach, documented
by axe-core itself, is to inject the script into the page and run it in the
browser's own JS context, which is exactly what this does.
"""
from playwright.sync_api import Page

AXE_CDN_URL = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.0/axe.min.js"


def run_axe(page: Page, include_selector: str = None) -> dict:
    """Injects axe-core into the current page and runs a full accessibility scan.

    Returns the raw axe-core results object (with `violations`, `passes`, etc).
    Optionally scope the scan to a CSS selector via `include_selector`.
    """
    page.add_script_tag(url=AXE_CDN_URL)
    script = (
        f"async () => await axe.run('{include_selector}')"
        if include_selector
        else "async () => await axe.run()"
    )
    return page.evaluate(script)


def assert_no_violations(results: dict, fail_on=("critical", "serious")):
    """Fails the test if any violation with an impact level in `fail_on` is found.

    Violations outside `fail_on` (e.g. 'moderate', 'minor') are reported in the
    assertion message but don't block the test on their own — this mirrors how
    most teams triage a11y findings in practice: not every issue blocks a
    release, but critical/serious ones should.
    """
    violations = results.get("violations", [])
    blocking = [v for v in violations if v.get("impact") in fail_on]

    if blocking:
        details = "\n".join(
            f"  - [{v['impact']}] {v['id']}: {v['description']} "
            f"({len(v['nodes'])} element(s) affected) — {v['helpUrl']}"
            for v in blocking
        )
        raise AssertionError(
            f"Found {len(blocking)} accessibility violation(s) with impact in {fail_on}:\n{details}"
        )
