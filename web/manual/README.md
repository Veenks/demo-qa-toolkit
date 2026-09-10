# Web — Manual Testing

Manual QA artifacts for a web application: a test plan, structured test cases, and bug reports — following the same process we'd use on a real client engagement.

## Target under test

[Sauce Demo](https://www.saucedemo.com/) — a public e-commerce demo app used for QA practice, intentionally seeded with bugs. We use it here so every artifact in this folder is fully reproducible: anyone can log in and verify the same results.

## Contents

| File | What it is |
|---|---|
| [`test-plan.md`](./test-plan.md) | Scope, approach, environment, entry/exit criteria for this test cycle |
| [`test-cases.md`](./test-cases.md) | Structured test cases covering login, cart, and checkout |
| [`bug-reports/`](./bug-reports) | Real bugs found while executing the test cases, documented with repro steps |

## How to reproduce

1. Go to [saucedemo.com](https://www.saucedemo.com/)
2. Log in with one of the standard test accounts (`standard_user`, `problem_user`, `performance_glitch_user`, etc.) — password for all is `secret_sauce`
3. Follow the steps in [`test-cases.md`](./test-cases.md)
