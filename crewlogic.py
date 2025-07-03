import os
from crewai import Agent, Task, Crew, LLM
#from langchain_ollama import ChatOllama
from langchain_community.chat_models import ChatOllama
from crewai.cli.constants import ENV_VARS
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM


def run_crew(llm, topic: str):
    planner = Agent(
    role=" story planner",
    goal="to create a story plan on the given topic: {topic}.",
    backstory="you are a working under a person who wants you to plan the plots of the story.",
    allow_delegation=False,
    verbose=True,
     llm = llm
    ) 
    
    writer = Agent(
        role="story writer",
        goal="to write a story plan according to the plan. The topic is {topic}",
        backstory="you are a childrens' story writer. You will write the story according to the plan.",
        allow_delegation=False,
        verbose=True,
        llm = llm
    ) 
    
    narrator = Agent(
         role="story narrator",
        goal="to narrate the story exactly",
        backstory="you are very good at telling stories in an engaging manner. You will take the story and narrate it",
        allow_delegation=False,
        verbose=True,
        llm = llm
        
    )
    
    plan = Task(
        description=("Write a plan on the topic. The plots should be engaging and thrilling."),
        expected_output="a summary of the happenings in the story and then a final list of the plots",
        agent=planner
        
    )
    story = Task(
        description=("Write a story according to the plan. The story should be engaging and thrilling."),
        expected_output="a short story, and a moral lesson in the end",
        agent=writer
        
    )
    narration = Task(
        description=("Narrate the story as if narrating to children. Narrate to them in a thrilling and engaging way"),
        expected_output="narration like, He said '....' then He did this, that. Then the narrator's opinion ",
        agent=narrator
        
    )
    crew = Crew(
        agents = [planner, writer, narrator],
        tasks = [plan, story, narration],
        verbose =1
    )
    result = crew.kickoff(inputs = {"topic": f"{topic}"})
    return result
   