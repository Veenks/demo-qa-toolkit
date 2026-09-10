// Shared authentication helper — every scenario calls this once in setup().
import http from 'k6/http';
import { check } from 'k6';

export function authenticate(baseUrl, username, password) {
  const res = http.post(
    `${baseUrl}/auth`,
    JSON.stringify({ username, password }),
    { headers: { 'Content-Type': 'application/json' }, tags: { endpoint: 'auth' } }
  );

  check(res, { 'auth: status 200': (r) => r.status === 200 });
  return res.json('token');
}
