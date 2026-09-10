# BUG-001 — All product images are identical for problem_user

**Status:** Open
**Severity:** Medium
**Priority:** Medium
**Related test case:** PROD-01

## Environment
- App: saucedemo.com
- User: `problem_user`
- Browser: Chrome (latest)

## Preconditions
Logged in as `problem_user`.

## Steps to Reproduce
1. Log in with `problem_user` / `secret_sauce`
2. Observe the product listing page

## Expected Result
Each of the 6 products displays its own distinct image.

## Actual Result
All 6 products display the same image (a dog), regardless of the actual product.

## Impact
Users cannot visually distinguish between products before adding them to the cart, which directly affects purchase decisions.

## Evidence
_Screenshot placeholder — attach product grid screenshot here._
