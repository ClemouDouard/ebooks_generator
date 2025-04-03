from crewai import Crew, Agent, Process, Task
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff

from config import LLM

@CrewBase
class StructureCrew:
    """
    This crew is responsible for creating :
        - The structure of the book
        - Ideas for the different chapters
        - Ideas for images
    """

    @agent
    def structure_agent(self) -> Agent:
        return Agent(
            role='Structurator',
            goal='Create the structure of the book',
            backstory='You are someone who loves to organize and structure things. You are very good at making a well made structure for a book for every kind of topic.',
            memory=False,
            llm=LLM,
        )