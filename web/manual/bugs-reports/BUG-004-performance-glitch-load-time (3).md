# BUG-004 — Significant load delay for performance_glitch_user

**Status:** Open
**Severity:** Low
**Priority:** Low
**Related test case:** LOGIN-01 (executed against `performance_glitch_user`)

## Environment
- App: saucedemo.com
- User: `performance_glitch_user`
- Browser: Chrome (latest)

## Preconditions
None.

## Steps to Reproduce
1. Log in with `performance_glitch_user` / `secret_sauce`
2. Observe the time it takes to reach the product listing page

## Expected Result
Login completes and the product page loads within a normal timeframe (comparable to `standard_user`, roughly 1-2 seconds).

## Actual Result
Login/page load takes noticeably longer (several seconds) compared to `standard_user`, under identical network conditions.

## Impact
Not severity-critical on its own for a demo account, but flagged here because unexplained load delays are worth a dedicated performance investigation — see `web/performance/` for a more rigorous load-testing approach to this class of issue.

## Evidence
_Screenshot/timing placeholder — attach network timing (DevTools) here._
