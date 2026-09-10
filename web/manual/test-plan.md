# Test Plan — Sauce Demo E-commerce Flow

## 1. Objective

Validate the core purchase flow of the Sauce Demo application — login, product browsing, cart management, and checkout — to confirm the application behaves as expected across standard use cases and to identify defects.

## 2. Scope

### In scope
- Login (valid and invalid credentials, all seeded user types)
- Product listing and sorting
- Add/remove items from cart
- Checkout flow (information, overview, confirmation)

### Out of scope
- Payment gateway integration (Sauce Demo simulates checkout without real payment processing)
- Backend/database validation (no access to the application's backend)
- Load/performance testing (covered separately in `web/performance/`)

## 3. Test Approach

- Exploratory testing first, to understand actual behavior before writing formal cases
- Structured test case execution second, covering both happy paths and negative/edge cases
- Every defect found is logged as a bug report with clear repro steps, expected vs. actual result, and severity/priority

## 4. Test Environment

| Item | Detail |
|---|---|
| Application | [saucedemo.com](https://www.saucedemo.com/) |
| Browser(s) | Chrome (latest), Firefox (latest) |
| Test accounts | `standard_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user` (password: `secret_sauce`) |
| Test data | Seeded product catalog (no data setup required) |

## 5. Entry Criteria

- Application is reachable and login page loads correctly
- Test accounts are valid and active

## 6. Exit Criteria

- All test cases in `test-cases.md` have been executed
- All identified defects are logged with severity/priority assigned
- No open blocker-severity defects remain undocumented

## 7. Roles

| Role | Responsibility |
|---|---|
| QA | Test case design, execution, defect reporting |

## 8. Risks

| Risk | Mitigation |
|---|---|
| Seeded bugs may change if the demo app is updated | Re-validate test cases periodically; note the date of last execution in each bug report |
