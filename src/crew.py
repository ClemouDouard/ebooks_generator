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
    
    @agent
    def chapter_agent(self) -> Agent:
        return Agent(
            role='Chapter Creator',
            goal='Create ideas for the different chapters',
            backstory='You are someone who loves to write and create ideas for chapters. You are very good at making a well made ideas for chapters for a book for every kind of topic.',
            memory=False,
            llm=LLM,
        )
    
    @agent
    def image_agent(self) -> Agent:
        return Agent(
            role='Image Creator',
            goal='Create ideas for images',
            backstory='You are someone who loves to create images. You are very good at making a well made ideas for images for a book for every kind of topic.',
            memory=False,
            llm=LLM,
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
            ### Section 1.2
            ## Chapter 2
            ### Section 2.1
            ### Section 2.2
            ''',
        )
    
    @task
    def chapter_task(self) -> Task:
        return Task(
            description='Create ideas for the different chapters of the book about the topic: {topic}',
            agent=self.chapter_agent(),
            expected_output='''
            The structure of the book with the different ideas in it like this plain example:
            # Title
            ## Chapter 1
            ### Section 1.1
            - Idea 1
            - Idea 2
            ### Section 1.2
            - Idea 1
            - Idea 2
            ## Chapter 2
            ### Section 2.1
            - Idea 1
            - Idea 2
            ### Section 2.2
            - Idea 1
            - Idea 2
            ''',
        )
    
    @task
    def image_task(self) -> Task:
        return Task(
            description='Create ideas for images for the book about the topic: {topic}',
            agent=self.image_agent(),
            expected_output='''
            The structure of the book with the different ideas found earlier and ideas for images in it like this plain example:
            # Title
            ## Chapter 1
            ### Section 1.1
            - Idea 1
            - Idea 2
            - Image Idea 1
            - Image Idea 2
            ### Section 1.2
            - Idea 1
            - Idea 2
            - Image Idea 1
            - Image Idea 2
            ## Chapter 2
            ### Section 2.1
            - Idea 1
            - Idea 2
            - Image Idea 1
            - Image Idea 2
            ### Section 2.2
            - Idea 1
            - Idea 2
            - Image Idea 1
            - Image Idea 2
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