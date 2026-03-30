# main.py
from tasks import ReportWorkflow

if __name__ == "__main__":
    topic = input("Enter the topic for the report: ")
    workflow = ReportWorkflow()
    workflow.run_workflow(topic)
