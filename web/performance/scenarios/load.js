// Load test: simulates expected normal-to-peak traffic with a gradual
// ramp up, a sustained plateau, and a ramp down. This is the main
// "does it hold up under realistic load" scenario.
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
        { duration: '30s', target: 10 },  // ramp up
        { duration: '2m', target: 10 },   // hold — sustained normal load
        { duration: '30s', target: 20 },  // ramp to peak
        { duration: '2m', target: 20 },   // hold — sustained peak load
        { duration: '30s', target: 0 },   // ramp down
      ],
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<800'],
    http_req_failed: ['rate<0.01'],
    'http_req_duration{endpoint:auth}': ['p(95)<500'],
    'http_req_duration{endpoint:create_booking}': ['p(95)<800'],
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
    'reports/load-report.html': htmlReport(data),
    stdout: textSummary(data, { indent: ' ', enableColors: true }),
  };
}
