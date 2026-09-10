# Web — Performance Testing

Load, smoke, and stress testing for [Restful-booker](https://restful-booker.herokuapp.com/) — a public booking API with authentication and full CRUD — built with **k6**.

## Why Restful-booker (not Sauce Demo)

k6 operates at the HTTP/API level, not the browser level — it sends real requests and measures response times, throughput, and error rates directly against a backend. Sauce Demo (used in `web/manual` and `web/automation`) is a static frontend with no real backend to load-test, so we switched targets here to one that actually has an API worth stressing.

## Structure

```
web/performance/
├── lib/
│   ├── config.js          → base URL and credentials (one place to change target)
│   ├── auth.js             → shared authentication helper
│   └── booking-flow.js       → the actual user flow (list, create, get, update, delete)
├── scenarios/
│   ├── smoke.js               → sanity check: does the script/API work at all? (2 VUs, 30s)
│   ├── load.js                  → realistic traffic simulation (ramps to 20 VUs, sustained)
│   └── stress.js                  → pushes past normal capacity to find the breaking point (up to 120 VUs)
└── reports/                          → generated HTML reports (gitignored, created on run)
```

`scenarios/` files only define *load shape* (VUs, stages, thresholds) — the actual request logic lives once in `lib/booking-flow.js` and is shared by all three, so there's a single place to update if the API changes.

## Why three separate scenarios

| | Smoke | Load | Stress |
|---|---|---|---|
| Goal | Confirm the script and API work at all | Confirm the API holds up under expected traffic | Find where it starts to degrade or break |
| Load | Minimal (2 VUs, 30s) | Realistic (ramps to 20 VUs, sustained) | Aggressive (ramps to 120 VUs) |
| Run order | Always first | After smoke passes | After load passes, when you want to know the ceiling |
| A failure means | The script is broken, or the API is down | The API can't handle expected traffic | Expected at some point — the useful signal is *where* |

Always run `smoke.js` first. If it fails, the problem is the script or the API's availability — you haven't tested performance yet. If smoke passes but `load.js` fails, that's a real capacity issue.

## Running locally

Requires [k6](https://k6.io/docs/get-started/installation/) installed (not a Python/npm package — it's a standalone binary).

```bash
# 1. Always start here
k6 run scenarios/smoke.js

# 2. Then the realistic load scenario
k6 run scenarios/load.js

# 3. Only if you want to find the breaking point
k6 run scenarios/stress.js
```

Each run prints a summary to the terminal and generates an HTML report under `reports/` (e.g. `reports/load-report.html`) — open it in a browser for a visual breakdown of response times, request rates, and thresholds.

> Note: the HTML/text report renderers are pulled from a public CDN at runtime (`k6-reporter`, `jslib.k6.io`), so running these scripts requires internet access on the machine executing them.

## Reading the results

- **`http_req_duration`** — how long requests take (we check the 95th percentile, i.e. "95% of requests were faster than this")
- **`http_req_failed`** — the error rate; a rising error rate under load is the clearest signal of a system struggling
- Results are also tagged per endpoint (`endpoint: auth`, `create_booking`, etc.), so the report can show which specific step is the bottleneck, not just an overall average
