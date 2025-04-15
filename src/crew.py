from crewai import Crew, Agent, Process, Task, LLM
from crewai.project import CrewBase, agent, task, crew

from config import MODEL, API_KEY

model = LLM(
    model=MODEL,
    api_key=API_KEY
)

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
            goal='Create the structure of the book, with the ideas for the different chapters and ideas for images',
            backstory='You are someone who loves to organize and structure things. You are very good at making a well made structure for a book for every kind of topic.',
            memory=False,
            llm=model,
        )
    
    @task
    def structure_task(self) -> Task:
        return Task(
            description='Create the structure of the book about the topic: {topic}',
            agent=self.structure_agent(),
            expected_output='''
            A markdown structure of the book about the topic: {topic} like this plain example:
            # Title
            ## Chapter 1
            ### Section 1.1
            - Text idea 1
            - Text idea 2
            ...
            - Image idea 1 (the prompt that you would give to an image generator to generate the image)
            - Image idea 2 (the prompt that you would give to an image generator to generate the image)
            ...
            ### Section 1.2
            - Text idea 1
            - Text idea 2
            ...
            - Image idea 1 (the prompt that you would give to an image generator to generate the image)
            - Image idea 2 (the prompt that you would give to an image generator to generate the image)
            ...
            ## Chapter 2
            ### Section 2.1
            - Text idea 1
            - Text idea 2
            ...
            - Image idea 1 (the prompt that you would give to an image generator to generate the image)
            - Image idea 2 (the prompt that you would give to an image generator to generate the image)
            ...
            ### Section 2.2
            - Text idea 1
            - Text idea 2
            ...
            - Image idea 1 (the prompt that you would give to an image generator to generate the image)
            - Image idea 2 (the prompt that you would give to an image generator to generate the image)
            ...
            ...
            # Conclusion
            ''',
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )