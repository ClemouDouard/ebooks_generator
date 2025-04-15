from crew import EbookCrew

def run_1(topic: str):
    inputs = {
        'topic': topic
    }
    EbookCrew().crew().kickoff(inputs=inputs)