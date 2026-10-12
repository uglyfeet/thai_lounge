# Functional Requirements — The Thai Lounge

## 1. Introduction

This document describes the functions the Thai Lounge website must provide for customers and the business owner.

## 2. Customer Requirements

- **FR1:** Customers can view a list of massage treatments.
- **FR2:** Each treatment displays its name, description, duration and price.
- **FR3:** Customers can register, log in and log out securely.
- **FR4:** Customers can select a treatment, appointment date and available time.
- **FR5:** The system validates booking details and prevents conflicting appointments.
- **FR6:** Customers can view their bookings.
- **FR7:** Customers can cancel a booking, subject to the business cancellation policy.
- **FR8:** Customers can pay online using Stripe.
- **FR9:** Customers receive clear booking and payment confirmation messages.

## 3. Business Owner Requirements

- **FR10:** The owner can securely access the administration area.
- **FR11:** The owner can create, view, update and delete treatments.
- **FR12:** The owner can manage appointment availability and bookings.
- **FR13:** The owner can view booking and payment statuses.

## 4. General Website Requirements

- **FR14:** The website provides navigation between its main pages.
- **FR15:** Forms validate required fields and display helpful error messages.
- **FR16:** The website displays correctly on desktop, tablet and mobile screens.
- **FR17:** The website provides a clear way for customers to contact the business.

## 5. Payment Requirements

- **FR18:** Stripe handles payment processing without the website storing customers' card details.
- **FR19:** The system records payment status and associates it with the relevant booking.
- **FR20:** The system handles unsuccessful or cancelled payments appropriately.

## 6. Acceptance Criteria

The requirements will be considered met when the relevant features have been implemented and tested successfully. Tests will cover valid and invalid form submissions, appointment conflicts, access permissions, booking management and Stripe test payments.