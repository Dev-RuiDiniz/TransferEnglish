import stripe
import os
from typing import Optional
from app.core.config import settings

class PaymentService:
    """
    Stripe Integration Service for Checkout and Subscription management.
    """
    def __init__(self):
        stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
        self.webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    def create_checkout_session(self, tenant_id: str, email: str, plan_price_id: str):
        """
        Create a Stripe Checkout session for a tenant.
        """
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': plan_price_id,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url=f"{settings.DOMAIN}/billing?success=true",
                cancel_url=f"{settings.DOMAIN}/billing?canceled=true",
                customer_email=email,
                metadata={
                    "tenant_id": tenant_id
                }
            )
            return session.url
        except Exception as e:
            print(f"Stripe Error: {e}")
            return None

    def handle_webhook(self, payload: bytes, sig_header: str):
        """
        Validate and process Stripe webhooks.
        """
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, self.webhook_secret
            )
            return event
        except Exception as e:
            print(f"Webhook Validation Error: {e}")
            return None

payment_service = PaymentService()
