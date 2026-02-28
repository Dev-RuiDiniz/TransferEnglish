from typing import Any
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
from app.services.billing.stripe_service import payment_service
from app.models.billing import Subscription

router = APIRouter()

@router.post("/checkout-session")
def create_billing_session(
    plan_id: str,
    db: Session = Depends(deps.get_db_with_tenant),
    current_admin: User = Depends(deps.get_current_admin)
) -> Any:
    """
    Generate a Stripe Checkout URL for the tenant admin.
    """
    # Map friendly names to actual Stripe price IDs (In prod, these are in config)
    price_map = {
        "individual": "price_123_individual",
        "starter": "price_456_starter",
        "pro": "price_789_pro"
    }
    
    price_id = price_map.get(plan_id)
    if not price_id:
        raise HTTPException(status_code=400, detail="Invalid plan selected")
        
    checkout_url = payment_service.create_checkout_session(
        tenant_id=current_admin.tenant_id,
        email=current_admin.email,
        plan_price_id=price_id
    )
    
    if not checkout_url:
        raise HTTPException(status_code=500, detail="Stripe session creation failed")
        
    return {"url": checkout_url}

@router.get("/status")
def get_subscription_status(
    db: Session = Depends(deps.get_db_with_tenant),
    current_admin: User = Depends(deps.get_current_admin)
) -> Any:
    """
    Check current subscription status for the tenant.
    """
    sub = db.query(Subscription).filter(Subscription.tenant_id == current_admin.tenant_id).first()
    if not sub:
        return {"status": "inactive", "plan": "free"}
    
    return {
        "status": sub.status,
        "plan": sub.plan_name,
        "expires_at": sub.current_period_end
    }
