from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
from app.services.auth.data_deletion import gdpr_service

router = APIRouter()

@router.delete("/me/purge", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_data(
    db: Session = Depends(deps.get_db_with_tenant),
    current_user: User = Depends(deps.get_current_user)
):
    """
    LGPD: Permanent deletion of all user data (Right to be Forgotten).
    """
    success = gdpr_service.purge_user_data(db, current_user.id)
    if not success:
        raise HTTPException(
            status_code=500,
            detail="Error during data deletion. Please contact support."
        )
    return

@router.get("/compliance-check")
def get_privacy_info():
    """
    Public info about data treatment.
    """
    return {
        "is_lgpd_compliant": True,
        "is_gdpr_compliant": True,
        "audio_encryption": "AES-256",
        "data_retention": "365 days or until request"
    }
