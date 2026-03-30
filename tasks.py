# tasks.py
from agents import ReportGeneratorAgent, ReportSummarizerAgent

class ReportWorkflow:
    """Orchestrates report generation and summarization"""
    def __init__(self):
        self.generator = ReportGeneratorAgent()
        self.summarizer = ReportSummarizerAgent()

    def run_workflow(self, topic: str):
        # Generate detailed report
        report = self.generator.generate_report(topic)
        print("\n=== Detailed Report ===\n", report)

        # Summarize report
        summary = self.summarizer.summarize_report(report)
        print("\n=== Summarized Report ===\n", summary)

        return report, summary
