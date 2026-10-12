# Testing Strategy

## Purpose

Testing will check that The Thai Lounge website works correctly, protects customer information and meets the project requirements.

## 1. Manual Testing

Manual tests will check that:

- Customers can register, log in and log out.
- Treatments display the correct names, descriptions, durations and prices.
- Customers can select available appointment dates and times.
- Invalid booking details are rejected.
- Conflicting appointments cannot be booked.
- Customers can view and manage their own bookings.
- Stripe test payments update the payment status correctly.
- Failed or cancelled payments are handled appropriately.
- Owners can manage treatments, availability and bookings.
- Forms display useful validation messages.
- Pages work on desktop and mobile screen sizes.

## 2. Automated Testing

Django automated tests will be written for important functionality, including:

- Model validation and relationships.
- Booking form validation.
- Prevention of conflicting appointments.
- Customer authentication and access permissions.
- Treatment and booking views.
- Payment status handling where practical.

## 3. Security Testing

Testing will check that:

- Customers cannot access another customer's bookings.
- Restricted management pages require appropriate permissions.
- Sensitive settings are not committed to GitHub.
- Card details are handled by Stripe rather than stored by the website.

## 4. Browser and Responsive Testing

The website will be tested in a desktop browser and at smaller screen sizes to check navigation, forms, layout and readability.

## 5. Defect Recording and Retesting

Problems found during testing will be corrected and tested again. Important changes will be committed to GitHub regularly.

## Completion Criteria

Testing is complete when the mandatory project requirements have been checked, significant defects have been corrected, and the deployed website has been tested where applicable.