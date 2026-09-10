// Stress test: deliberately pushes well past expected normal traffic to
// find where the system starts to degrade or fail. Unlike load.js, the
// goal here isn't a clean pass — rising latency or error rates at the
// higher stages are the useful signal, not a surprise.
import { sleep } from 'k6';
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';
import { textSummary } from 'https://jslib.k6.io/k6-summary/0.0.2/index.js';
import { BASE_URL, CREDENTIALS } from '../lib/config.js';
import { authenticate } from '../lib/auth.js';
import { runBookingFlow } from '../lib/booking-flow.js';

export const options = {
  scenarios: {
    booking_flow: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '30s', target: 20 },
        { duration: '1m', target: 20 },
        { duration: '30s', target: 60 },
        { duration: '1m', target: 60 },
        { duration: '30s', target: 120 },
        { duration: '2m', target: 120 },
        { duration: '1m', target: 0 },
      ],
    },
  },
  thresholds: {
    // Looser than load.js on purpose — we expect degradation at the top
    // stages. These thresholds catch a *total* meltdown, not fine-tuning.
    http_req_failed: ['rate<0.20'],
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
    'reports/stress-report.html': htmlReport(data),
    stdout: textSummary(data, { indent: ' ', enableColors: true }),
  };
}
