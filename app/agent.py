from app.memory import Memory
from app.planner import Planner
from app.rag import retrieve_context

class SalesAgent:
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()

    def handle_query(self, query):
        plan = self.planner.create_plan(query)
        context = retrieve_context(query)
        self.memory.add(query)
        return f'Plan: {plan} | Context: {context}'
