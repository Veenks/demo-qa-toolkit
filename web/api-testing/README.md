# Web — API Testing

API test suite for [Restful-booker](https://restful-booker.herokuapp.com/) — the same target used in `web/performance` — covering authentication, full CRUD on bookings, negative cases, and several **documented quirks in the API's real behavior**. Built with Postman, runnable via the GUI or automated with Newman.

## Structure

```
web/api-testing/
├── postman/
│   ├── veenks-restful-booker.postman_collection.json   → the test suite itself
│   └── restful-booker.postman_environment.json           → base URL, credentials, and runtime variables
├── package.json                                              → Newman + HTML reporter
└── reports/                                                     → generated HTML report (gitignored)
```

## Coverage

| Folder | What it covers |
|---|---|
| Auth | Valid login (saves token for later requests), invalid credentials |
| Booking - Read | List all, filter by name, get by id (including not-found) |
| Booking - Create | Valid creation, plus two known data-integrity quirks (below) |
| Booking - Update | Valid update with token, rejected without token, rejected with `Authorization` header, partial update (PATCH) |
| Booking - Delete | Valid delete, confirming the booking is gone, deleting a non-existent booking |

## Known quirks in this API (documented, not treated as script bugs)

This API is intentionally imperfect — it's built as a practice target with real inconsistencies. The suite documents these rather than silently working around them, the same way `web/manual/bug-reports` documents real Sauce Demo bugs:

- **Invalid credentials return `200`, not `401`** — the response body has a `reason` field instead of a `token`, so callers have to check for the token's absence rather than relying on the status code
- **Decimal `totalprice` loses precision** on save (e.g. `150.75` isn't stored as sent)
- **Invalid date formats are silently accepted and corrupted** instead of being rejected with a validation error
- **Authentication only works via a `Cookie` header** — sending the token as a standard `Authorization` header is rejected with `403`
- **A successful `DELETE` returns `201 Created`**, not `200 OK` or `204 No Content` as would be conventional
- **Deleting a non-existent booking returns `405 Method Not Allowed`** instead of `404 Not Found`

## Running via Postman (GUI)

1. Import both files from `postman/` into Postman (collection + environment)
2. Select the "Restful-booker" environment (top-right dropdown)
3. Run requests individually, or use the Collection Runner to run the whole suite in order

## Running via Newman (CLI / CI)

```bash
npm install
npm test
```

This runs the full collection headlessly and generates an HTML report at `reports/api-report.html`.

## CI

Runs automatically via `.github/workflows/newman.yml` on every push or PR touching this folder.
