from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, TenantMixin
import uuid
from datetime import datetime

class Subscription(Base, TimestampMixin, TenantMixin):
    """
    Manages subscription status for a tenant.
    Plans: individual, business_starter, business_pro
    """
    __tablename__ = "subscriptions"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    stripe_customer_id: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=True)
    stripe_subscription_id: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=True)
    
    plan_name: Mapped[str] = mapped_column(String(50), default="free")
    status: Mapped[str] = mapped_column(String(50), default="inactive") # active, trialing, canceled, past_due
    
    current_period_end: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    cancel_at_period_end: Mapped[bool] = mapped_column(Boolean, default=False)
