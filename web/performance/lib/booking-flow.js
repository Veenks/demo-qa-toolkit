// The core user flow, shared by smoke/load/stress scenarios so we're not
// duplicating request logic three times — only the load shape (VUs/stages)
// differs between scenario files.
import http from 'k6/http';
import { check, group } from 'k6';
import { BASE_URL } from './config.js';

export function runBookingFlow(token) {
  let bookingId;

  group('List bookings', function () {
    const res = http.get(`${BASE_URL}/booking?firstname=Sally&lastname=Brown`, {
      tags: { endpoint: 'list_bookings' },
    });
    check(res, { 'list bookings: status 200': (r) => r.status === 200 });
  });

  group('Create booking', function () {
    const payload = JSON.stringify({
      firstname: 'John',
      lastname: 'Doe',
      totalprice: 150,
      depositpaid: true,
      bookingdates: { checkin: '2026-01-01', checkout: '2026-01-05' },
      additionalneeds: 'Breakfast',
    });
    const res = http.post(`${BASE_URL}/booking`, payload, {
      headers: { 'Content-Type': 'application/json' },
      tags: { endpoint: 'create_booking' },
    });
    const ok = check(res, {
      'create booking: status 200': (r) => r.status === 200,
      'create booking: returns bookingid': (r) => r.json('bookingid') !== undefined,
    });
    if (ok) bookingId = res.json('bookingid');
  });

  // Downstream steps depend on a valid booking — bail out cleanly if creation failed,
  // instead of throwing confusing errors on every following request.
  if (!bookingId) return;

  group('Get booking by id', function () {
    const res = http.get(`${BASE_URL}/booking/${bookingId}`, {
      tags: { endpoint: 'get_booking' },
    });
    check(res, { 'get booking: status 200': (r) => r.status === 200 });
  });

  group('Update booking', function () {
    const payload = JSON.stringify({
      firstname: 'John',
      lastname: 'Doe',
      totalprice: 200,
      depositpaid: false,
      bookingdates: { checkin: '2026-01-02', checkout: '2026-01-06' },
      additionalneeds: 'Lunch',
    });
    const res = http.put(`${BASE_URL}/booking/${bookingId}`, payload, {
      headers: { 'Content-Type': 'application/json', Cookie: `token=${token}` },
      tags: { endpoint: 'update_booking' },
    });
    check(res, { 'update booking: status 200': (r) => r.status === 200 });
  });

  group('Delete booking', function () {
    const res = http.del(`${BASE_URL}/booking/${bookingId}`, null, {
      headers: { Cookie: `token=${token}` },
      tags: { endpoint: 'delete_booking' },
    });
    check(res, {
      'delete booking: status 200 or 201': (r) => r.status === 200 || r.status === 201,
    });
  });
}
