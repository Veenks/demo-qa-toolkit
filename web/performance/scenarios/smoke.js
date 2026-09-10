// Smoke test: minimal load (2 VUs, 30s), just to confirm the flow works
// end-to-end and the pipeline itself isn't broken. Run this before load/stress.
import { sleep } from 'k6';
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';
import { textSummary } from 'https://jslib.k6.io/k6-summary/0.0.2/index.js';
import { BASE_URL, CREDENTIALS } from '../lib/config.js';
import { authenticate } from '../lib/auth.js';
import { runBookingFlow } from '../lib/booking-flow.js';

export const options = {
  vus: 2,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<1000'],
    http_req_failed: ['rate<0.01'],
  },
};

export function setup() {
  return { token: authenticate(BASE_URL, CREDENTIALS.username, CREDENTIALS.password) };
}

export default function (data) {
  runBookingFlow(data.token);
  sleep(1);
}

export function handleSummary(data) {
  return {
    'smoke-report.html': htmlReport(data),
    stdout: textSummary(data, { indent: ' ', enableColors: true }),
  };
}