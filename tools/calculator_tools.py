from simpleeval import simple_eval
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class CalculatorToolInput(BaseModel):
    expression: str = Field(..., description="The mathematical expression to calculate")

class CalculatorTools(BaseTool):
    name: str = "Calculator"
    description: str = "Useful for performing calculations and budget planning"
    args_schema: type[BaseModel] = CalculatorToolInput

    def _run(self, expression: str) -> str:
        try:
            result = simple_eval(expression)
            return f"Calculation result: {result}"
        except Exception as e:
            return f"Error calculating: {e}"

    @staticmethod
    def calculate_budget(expression: str) -> str:
        tool = CalculatorTools()
        return tool._run(expression)