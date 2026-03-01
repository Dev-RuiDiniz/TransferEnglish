from sqlalchemy.orm import Session
from sqlalchemy import delete
from app.models.user import User
from app.models.analytics import FluencySession
from app.models.knowledge import ConceptMastery
from app.models.gamification import UserAchievement

class GDPRService:
    """
    Handles Right to be Forgotten (Exclusão de Dados) as per LGPD/GDPR.
    """

    @staticmethod
    def purge_user_data(db: Session, user_id: str) -> bool:
        """
        Permanently deletes all data associated with a user across all modules.
        """
        try:
            # 1. Delete progress and analytics
            db.execute(delete(FluencySession).where(FluencySession.user_id == user_id))
            db.execute(delete(ConceptMastery).where(ConceptMastery.user_id == user_id))
            db.execute(delete(UserAchievement).where(UserAchievement.user_id == user_id))
            
            # 2. Delete the user itself
            db.execute(delete(User).where(User.id == user_id))
            
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Purge Error: {e}")
            return False

gdpr_service = GDPRService()
