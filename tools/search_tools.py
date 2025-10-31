from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
import json
import os

class SearchToolInput(BaseModel):
    query: str = Field(..., description="The search query")

class SearchTools(BaseTool):
    name: str = "Search the Internet"
    description: str = "Useful for searching the internet for current information"
    args_schema: type[BaseModel] = SearchToolInput

    def _run(self, query: str) -> str:
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ.get('SERPER_API_KEY', ''),
            'content-type': 'application/json'
        }
        
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            return response.text
        except Exception as e:
            return f"Search error: {e}"

    @staticmethod
    def search_internet(query: str) -> str:
        tool = SearchTools()
        return tool._run(query)