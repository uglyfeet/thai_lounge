# Database Design

## Purpose

The database will store treatment details, customer accounts, bookings and payment records for The Thai Lounge website.

Django's built-in user model will manage customer accounts and login details.

## Database Tables

### 1. User

Uses Django's built-in user model.

Stores customer account information, including username, email address and securely hashed password.

### 2. Treatment

Stores the treatments offered by the business.

Fields:
- `name` — treatment name
- `description` — treatment details
- `duration` — treatment length in minutes
- `price` — treatment price
- `active` — whether the treatment is currently available to book

### 3. Booking

Stores customer appointments.

Fields:
- `customer` — links to the customer account
- `treatment` — links to the selected treatment
- `date` — appointment date
- `start_time` — appointment start time
- `end_time` — calculated appointment end time
- `status` — booking status, such as pending, confirmed or cancelled
- `created_at` — date and time the booking was created

The system will validate appointment times and prevent conflicting bookings.

### 4. Payment

Stores payment information associated with a booking.

Fields:
- `booking` — links to the relevant booking
- `amount` — payment amount
- `stripe_session_id` — identifies the Stripe checkout session
- `stripe_payment_id` — identifies the Stripe payment when available
- `status` — payment status
- `created_at` — date and time the payment record was created

Stripe will process payments. The website will not store customers' card details.

## Relationships

- One customer can have multiple bookings.
- One treatment can be associated with multiple bookings.
- Each booking belongs to one customer and one treatment.
- A booking can have associated payment information.

## Data Integrity and Security

Django models and validation will help ensure that required information is supplied and booking conflicts are prevented. Customer accounts will be protected by Django authentication, and customers will only be able to access their own bookings.

Stripe secret keys and other sensitive settings will be stored outside the source code.

## Design Status

This is the proposed database design. It will be checked against the assessment requirements and refined during implementation if necessary.