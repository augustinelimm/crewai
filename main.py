import os
from crewai import Crew
from langchain_openai import ChatOpenAI
from decouple import config
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()

class SkincareCrew:
    def __init__(self, skin_type, concerns, budget, existing_products=""):
        self.skin_type = skin_type
        self.concerns = concerns
        self.budget = budget
        self.existing_products = existing_products

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        korean_researcher = agents.korean_skincare_researcher()
        product_researcher = agents.product_researcher()
        skincare_expert = agents.skincare_expert()

        routine_framework = tasks.gather_korean_routine_framework(
            korean_researcher,
            self.skin_type,
            self.concerns,
            self.budget
        )

        product_research = tasks.research_olive_young_award_products(
            product_researcher,
            self.skin_type,
            self.concerns,
            self.budget,
            "2024"
        )

        personalized_routine = tasks.create_personalized_routine(
            skincare_expert,
            self.skin_type,
            self.concerns,
            self.budget,
            self.existing_products
        )

        crew = Crew(
            agents=[korean_researcher, product_researcher, skincare_expert],
            tasks=[routine_framework, product_research, personalized_routine],
            verbose=True,
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Korean Skincare Routine Planner Crew")
    print('---------------------------------------------------')
    skin_type = input("What is your skin type? (e.g., oily, dry, combination, sensitive): ")
    concerns = input("What are your main skin concerns? (e.g., acne, aging, dullness, pores): ")
    budget = input("What is your budget tier? (e.g., drugstore, mid-range, luxury): ")
    existing_products = input("What products are you currently using? (optional): ")
    
    skincare_crew = SkincareCrew(skin_type, concerns, budget, existing_products)
    result = skincare_crew.run()
    
    print("\n\n###############")
    print("## Here is Your Personalized Korean Skincare Routine")
    print("###############")
    print(result)