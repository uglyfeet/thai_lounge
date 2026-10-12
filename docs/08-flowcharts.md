# Flowcharts

## Purpose

Flowcharts will describe the main processes used by The Thai Lounge website before implementation.

## 1. Customer Registration and Login

1. Customer opens the registration or login page.
2. Customer enters their details.
3. The system validates the information.
4. If the information is invalid, an error message is displayed.
5. If registration is successful, an account is created.
6. If login details are correct, the customer is logged in.

## 2. Booking an Appointment

1. Customer logs in and selects a treatment.
2. Customer chooses an appointment date.
3. The system displays available appointment times.
4. Customer selects a time.
5. The system checks that the appointment is valid and available.
6. If the time is unavailable, the customer selects another time.
7. If the time is available, the system creates a booking.
8. The customer continues to payment through Stripe.
9. The system records the payment result and updates the booking status as appropriate.
10. The customer receives confirmation or an error message.

## 3. Stripe Payment

1. Customer proceeds to Stripe Checkout.
2. Stripe processes the payment.
3. The system checks the payment result.
4. If payment succeeds, the payment status is updated.
5. If payment fails or is cancelled, the system handles the result and informs the customer.

## 4. Owner Management

1. Owner logs in to the administration area.
2. Owner selects treatments, availability or bookings.
3. Owner makes the required changes.
4. The system validates and saves the changes.
5. The owner receives confirmation or an error message.

## Design Status

These flowcharts describe the intended processes. They will be checked and refined during implementation and testing.