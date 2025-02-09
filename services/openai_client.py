from typing import Dict, List, Optional
import openai
import asyncio
from datetime import datetime

class OpenAIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    async def analyze_code(self, code: str) -> Dict:
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a code analysis expert."},
                    {"role": "user", "content": f"Analyze this code and provide suggestions:\n{code}"}
                ]
            )
            return {
                "analysis": response.choices[0].message.content,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            raise Exception(f"Failed to analyze code: {str(e)}")

    async def generate_documentation(self, code: str) -> Dict:
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Generate comprehensive documentation."},
                    {"role": "user", "content": f"Create documentation for:\n{code}"}
                ]
            )
            return {
                "documentation": response.choices[0].message.content,
                "format": "markdown",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            raise Exception(f"Failed to generate documentation: {str(e)}")