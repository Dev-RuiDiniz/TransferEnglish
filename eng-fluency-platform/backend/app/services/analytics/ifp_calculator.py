import numpy as np
from typing import List, Dict

class IFPCalculator:
    """
    IFP (Índice de Fluência sob Pressão) Algorithm.
    Calculates a score based on phonetic accuracy, response latency, and hesitation.
    """
    
    @staticmethod
    def calculate_session_score(
        accuracies: List[float], 
        latencies: List[float], 
        hesitations: List[int]
    ) -> float:
        """
        Calculates the IFP for a session.
        - Higher accuracy = higher IFP
        - Higher latency = lower IFP (Pressure factor)
        - Higher count of hesitations = lower IFP
        """
        if not accuracies:
            return 0.0
            
        avg_accuracy = np.mean(accuracies)
        avg_latency = np.mean(latencies)
        total_hesitations = sum(hesitations)

        # Normalization factors (empirical values for early stage)
        # Latency Penalty: -5 points per second over benchmark (1.5s)
        latency_penalty = max(0, (avg_latency - 1.5) * 5)
        
        # Hesitation Penalty: -2 points per hesitation
        hesitation_penalty = total_hesitations * 2
        
        # IFP Base (0-100)
        # We start with accuracy and apply pressure-related penalties
        ifp = avg_accuracy - latency_penalty - hesitation_penalty
        
        return float(np.clip(ifp, 0, 100))

    @staticmethod
    def get_fluency_rating(ifp_score: float) -> str:
        if ifp_score >= 90: return "Native-like"
        if ifp_score >= 75: return "Fluent"
        if ifp_score >= 60: return "Functional"
        if ifp_score >= 40: return "Developing"
        return "Initial"

ifp_calculator = IFPCalculator()
