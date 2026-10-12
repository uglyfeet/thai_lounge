# Deployment

## Purpose

This document describes how to run The Thai Lounge website locally and deploy it to a live hosting service.

## Local Setup

1. Install Python and Git.
2. Clone the GitHub repository to the local computer.
3. Create and activate a Python virtual environment.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Configure environment variables for sensitive settings, including Django's secret key and Stripe credentials.
6. Run database migrations using `python manage.py migrate`.
7. Start the development server using `python manage.py runserver`.
8. Open the local website in a browser and test the main features.

## Cloud Deployment

The website will be deployed to a suitable hosting service, with the final provider confirmed during implementation.

Deployment will include:

- Configuring environment variables securely.
- Installing dependencies from `requirements.txt`.
- Configuring the production database.
- Running database migrations.
- Configuring static files and production settings.
- Disabling Django debug mode.
- Configuring the allowed host names and secure settings.
- Configuring Stripe test credentials for testing payments.

## Deployment Testing

After deployment, the live website will be tested to confirm that pages load, accounts work, bookings can be managed and Stripe test payments behave as expected.

The deployed website will be checked against the local version to identify any differences.

## Security

Secret keys, database credentials and Stripe credentials must not be committed to GitHub. Production settings must be configured separately from local development settings.