# BUG-003 — Cart button state does not update correctly for problem_user

**Status:** Open
**Severity:** Medium
**Priority:** Medium
**Related test case:** CART-01, CART-02

## Environment
- App: saucedemo.com
- User: `problem_user`
- Browser: Chrome (latest)

## Preconditions
Logged in as `problem_user`, on the product listing page.

## Steps to Reproduce
1. Log in with `problem_user` / `secret_sauce`
2. Click "Add to cart" on any product
3. Observe the button state
4. Click the button again to remove the item

## Expected Result
After adding, the button changes from "Add to cart" to "Remove". After removing, it reverts back to "Add to cart", and the cart badge count updates accordingly in both steps.

## Actual Result
The button state and/or cart badge count does not update consistently — in some cases the badge count does not reflect the actual number of items in the cart.

## Impact
Users may be uncertain whether an item was actually added or removed, which can lead to checkout errors (wrong items/quantities).

## Evidence
_Screenshot placeholder — attach cart badge + button state screenshots here._
