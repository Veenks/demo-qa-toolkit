# BUG-002 — "Price (low to high)" sort does not reorder products for problem_user

**Status:** Open
**Severity:** High
**Priority:** High
**Related test case:** PROD-02

## Environment
- App: saucedemo.com
- User: `problem_user`
- Browser: Chrome (latest)

## Preconditions
Logged in as `problem_user`, on the product listing page.

## Steps to Reproduce
1. Log in with `problem_user` / `secret_sauce`
2. Open the sort dropdown
3. Select "Price (low to high)"
4. Observe the resulting product order

## Expected Result
Products reorder in ascending order by price.

## Actual Result
The product order does not change, or changes incorrectly — items are not sorted by ascending price.

## Impact
Users relying on sort to find the cheapest option get an incorrect list, which can lead to a poor purchase decision or lost trust in the store.

## Evidence
_Screenshot placeholder — attach before/after sort screenshots here._
