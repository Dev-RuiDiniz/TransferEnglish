from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.models.knowledge import ConceptMastery
from app.models.linguistics import Cognate

class PathGenerator:
    """
    Generates personalized learning paths based on user performance.
    Prioritizes low-mastery concepts (weak points).
    """

    @staticmethod
    def get_next_mission(db: Session, user_id: str) -> Dict[str, str]:
        """
        Suggests the next pedagogical mission (e.g., practice specific phonemes).
        """
        # Find concepts with lowest mastery
        query = select(ConceptMastery).where(
            ConceptMastery.user_id == user_id,
            ConceptMastery.is_mastered == False
        ).order_by(ConceptMastery.mastery_score.asc())
        
        gaps = db.execute(query).scalars().all()
        
        if not gaps:
            return {
                "title": "Natural Conversation",
                "description": "You are doing great! Let's just talk naturally.",
                "target_focus": "General Fluency"
            }
            
        # Prioritize the most critical gap
        main_gap = gaps[0]
        
        return {
            "title": f"Mastering '{main_gap.concept_name}'",
            "description": f"You've encountered some challenges with {main_gap.concept_name}. Let's focus on this.",
            "target_focus": main_gap.concept_name,
            "concept_type": main_gap.concept_type
        }

path_generator = PathGenerator()
