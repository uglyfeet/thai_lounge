# Non-Functional Requirements — The Thai Lounge

## 1. Usability

- **NFR1:** The website must be easy to navigate and suitable for users with different levels of technical ability.
- **NFR2:** Forms must provide clear instructions and helpful error messages.
- **NFR3:** The layout must adapt to desktop, tablet and mobile screens.

## 2. Performance

- **NFR4:** Pages should load within a reasonable time under normal usage.
- **NFR5:** Images should be optimised to avoid unnecessarily slow page loading.

## 3. Security

- **NFR6:** Customer passwords must be handled securely using Django authentication.
- **NFR7:** Customers must only be able to access and manage their own bookings.
- **NFR8:** Sensitive configuration, including secret keys and Stripe credentials, must not be committed to GitHub.
- **NFR9:** Debug mode must be disabled in the deployed application.
- **NFR10:** Online payments must be processed through Stripe without storing card details in the application database.

## 4. Reliability

- **NFR11:** The system must validate booking information and prevent conflicting appointments.
- **NFR12:** Booking and payment statuses must be recorded accurately.
- **NFR13:** The website should provide clear feedback when an operation fails.

## 5. Maintainability

- **NFR14:** The project must use Django apps to organise related functionality.
- **NFR15:** Code should be readable, consistently formatted and documented where appropriate.
- **NFR16:** Dependencies must be recorded in `requirements.txt`.

## 6. Accessibility

- **NFR17:** Forms must have associated labels and accessible validation messages.
- **NFR18:** Text must be readable, with sufficient contrast between text and background.
- **NFR19:** Interactive elements must be usable with a keyboard where practical.

## 7. Assessment and Deployment

- **NFR20:** The source code must be maintained in a GitHub repository with regular commits.
- **NFR21:** The README must link to the project documentation.
- **NFR22:** The deployed website must use appropriate production settings and protect sensitive information.