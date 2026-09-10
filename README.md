# demo-qa-toolkit

End-to-end QA toolkit by [Veenks](https://github.com/veenks) — organized by what you're testing (web, mobile, desktop, database, AI), and inside each, by testing strategy (manual, automation, API, performance, and more). Built to show how we actually work, not just to list tools.

## Why organized this way

We structure this repo the way a client thinks about their own problem first — "I need to test my mobile app" — not the way QA disciplines are usually filed. Inside each target, you'll find the relevant strategies for that context; not every strategy applies to every target, and we don't force symmetry where it doesn't make sense.

## Structure

```
demo-qa-toolkit/
├── web/
│   ├── manual/              → test plans, test case design, bug reports
│   ├── automation/          → E2E framework, Page Object Model, CI pipeline (Playwright)
│   ├── api-testing/         → schema validation, negative cases, request chaining (Postman/Newman)
│   ├── performance/         → load and stress testing, result reports (k6)
│   ├── contract-testing/    → consumer-driven contract tests between services (Pact) — coming soon
│   └── accessibility/       → a11y checks against WCAG (axe-core) — coming soon
├── mobile/                  → coming soon
│   ├── manual/
│   └── automation/          → Appium
├── desktop/                 → coming soon
│   └── automation/
├── database/                → coming soon
│   └── data-testing/        → data integrity checks, migration validation
└── ai/                      → coming soon
    ├── agent-testing/       → validating tool-call sequences, error handling, scope
    └── llm-evals/           → evals and semantic scoring for non-deterministic outputs
```

## What's live vs. what's coming

| Status | Area |
|---|---|
| ✅ Live | `web/manual`, `web/automation`, `web/api-testing`, `web/performance` |
| 🔜 Coming soon | `web/contract-testing`, `web/accessibility`, `mobile/*`, `desktop/*`, `database/*`, `ai/*` |

We're adding new areas incrementally rather than shipping everything half-built — each folder only goes live once it has real, working content.

## Where to start, depending on what you're evaluating

- **Web automation skills** → [`web/automation/`](./web/automation)
- **API testing depth** → [`web/api-testing/`](./web/api-testing)
- **Performance testing approach** → [`web/performance/`](./web/performance)
- **How we document and communicate QA work** → [`web/manual/`](./web/manual)

Each folder has its own README with setup instructions and details on what it demonstrates.

## About Veenks

Veenks is a software consulting studio helping teams build, ship, and maintain reliable software. Quality engineering — the focus of this repo — is one of our core service lines.

[LinkedIn](#) · [Contact](mailto:torresjavier83@gmail.com)
