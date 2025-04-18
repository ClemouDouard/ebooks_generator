from crew import StructureCrew

def run_1(topic: str):
    inputs = {
        'topic': topic
    }
    return StructureCrew().crew().kickoff(inputs=inputs)