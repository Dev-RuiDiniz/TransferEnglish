import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.analytics import FluencySession
from app.models.user import User

class EnterpriseReportService:
    """
    Generates enterprise-level reports for Tenant Admins.
    Aggregates data across all organization members.
    """

    @staticmethod
    def get_tenant_metrics(db: Session, tenant_id: str):
        """
        Aggregates session data for a specific tenant using Pandas.
        """
        # Fetch all session data for the tenant
        query = (
            select(FluencySession, User.full_name)
            .join(User, FluencySession.user_id == User.id)
            .where(FluencySession.tenant_id == tenant_id)
        )
        
        results = db.execute(query).all()
        
        if not results:
            return None
            
        data = []
        for session, full_name in results:
            data.append({
                "User": full_name,
                "IFP": session.ifp_score,
                "Accuracy": session.accuracy_avg,
                "Latency": session.response_latency_avg,
                "Words": session.total_words,
                "Duration": session.duration_seconds
            })
            
        df = pd.DataFrame(data)
        
        # Summary statistics
        summary = {
            "avg_ifp": df["IFP"].mean(),
            "avg_accuracy": df["Accuracy"].mean(),
            "total_words": df["Words"].sum(),
            "user_ranking": df.groupby("User")["IFP"].mean().sort_values(ascending=False).to_dict()
        }
        
        return summary

    @staticmethod
    def generate_pdf_report(summary: dict, tenant_name: str) -> BytesIO:
        """
        Generates a PDF summary report using ReportLab.
        """
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, f"Fluency Performance Report: {tenant_name}")
        
        p.setFont("Helvetica", 12)
        p.drawString(100, 720, f"Average IFP Score: {summary['avg_ifp']:.2f}")
        p.drawString(100, 700, f"Average Accuracy: {summary['avg_accuracy']:.2f}%")
        p.drawString(100, 680, f"Total Vocabulary Practiced: {summary['total_words']} words")
        
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, 640, "Top Performers (Avg IFP):")
        
        y = 620
        p.setFont("Helvetica", 11)
        for user, score in list(summary["user_ranking"].items())[:5]:
            p.drawString(120, y, f"- {user}: {score:.2f}")
            y -= 20
            
        p.showPage()
        p.save()
        
        buffer.seek(0)
        return buffer

report_service = EnterpriseReportService()
