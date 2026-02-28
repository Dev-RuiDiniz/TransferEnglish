from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.content import ScenarioTemplate

class ScenarioManager:
    """
    Manages complex conversation scenarios and their prompts.
    """

    @staticmethod
    def get_scenario_prompt(db: Session, scenario_id: str) -> Optional[str]:
        """
        Retrieves the system prompt modifier for a specific scenario.
        """
        query = select(ScenarioTemplate).where(ScenarioTemplate.id == scenario_id)
        scenario = db.execute(query).scalar_one_or_none()
        
        if not scenario:
            return None
            
        config = scenario.config
        prompt = (
            f"ACT AS: {config.get('persona', 'an interlocutor')}. "
            f"TONE: {config.get('tone', 'conversational')}. "
            f"CURRENT SCENARIO: {scenario.title}. "
            f"OBJECTIVES: {', '.join(config.get('objectives', []))}. "
            "Follow the scenario strictly but naturally."
        )
        return prompt

    @staticmethod
    def list_scenarios(db: Session, level: Optional[str] = None):
        query = select(ScenarioTemplate)
        if level:
            query = query.where(ScenarioTemplate.level == level)
        return db.execute(query).scalars().all()

scenario_manager = ScenarioManager()
