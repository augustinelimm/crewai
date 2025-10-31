from crewai import Agent, Crew
from textwrap import dedent
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # or other models

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of experience making travel itineraries"""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed per-day plan include budget, packing suggestions, and safety tips"""),
            tools=[
                SearchTools(),
                CalculatorTools()
            ],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert in analysing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices, and traveller interests"""),
            tools = [SearchTools()],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgable local tour guide with extensive information about the city, it's attractions and customs"""),
            goal=dedent(f"""Provide the BEST insights about selected city"""),
            tools=[SearchTools()],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
