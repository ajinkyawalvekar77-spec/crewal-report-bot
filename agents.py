# agents.py
import os
from dotenv import load_dotenv
import httpx
from tools import TextCleaner
from crewai import Agent
from pydantic import PrivateAttr

# Load API keys
load_dotenv()
GROK_API_KEY = os.getenv("GROK_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GROK_ENDPOINT = "https://api.grok.ai/v1/generate"

class ReportGeneratorAgent(Agent):
    """Generates detailed report using Grok AI"""
    _cleaner: TextCleaner = PrivateAttr()

    def __init__(self):
        super().__init__(
            role="Report Generator",
            goal="Generate a detailed report from a topic",
            backstory="I am an AI agent specialized in creating detailed reports",
            llm=None,
            disable_native=True
        )
        self._cleaner = TextCleaner()

    def generate_report(self, topic: str) -> str:
        prompt = f"Write a detailed report on the topic: {topic}. Include structured paragraphs, explanations, and relevant facts."
        headers = {"Authorization": f"Bearer {GROK_API_KEY}"}
        payload = {"prompt": prompt, "max_tokens": 1000}

        try:
            with httpx.Client(timeout=30) as client:
                response = client.post(GROK_ENDPOINT, json=payload, headers=headers, verify=True)
                response.raise_for_status()
                report = response.json().get("text", "")
        except Exception as e:
            report = f"Error: Could not fetch report from Grok AI. {str(e)}"
        return self._cleaner.clean_text(report)

class ReportSummarizerAgent(Agent):
    """Summarizes report into <=300 words using Grok AI"""
    _cleaner: TextCleaner = PrivateAttr()

    def __init__(self):
        super().__init__(
            role="Report Summarizer",
            goal="Summarize a detailed report into a short paragraph",
            backstory="I am an AI agent specialized in condensing long reports",
            llm=None,
            disable_native=True
        )
        self._cleaner = TextCleaner()

    def summarize_report(self, report: str) -> str:
        prompt = f"Summarize the following report in a clear paragraph of no more than 300 words:\n{report}"
        headers = {"Authorization": f"Bearer {GROK_API_KEY}"}
        payload = {"prompt": prompt, "max_tokens": 300}

        try:
            with httpx.Client(timeout=30) as client:
                response = client.post(GROK_ENDPOINT, json=payload, headers=headers, verify=True)
                response.raise_for_status()
                summary = response.json().get("text", "")
        except Exception as e:
            summary = f"Error: Could not fetch summary from Grok AI. {str(e)}"
        return self._cleaner.clean_text(summary)
