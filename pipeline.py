from agents import build_reader_agent , build_search_agent , writer_chain , critic_chain
from rich import print

def run_research_pipeline(topic : str) -> dict :
    state = {}

    # search agent working
    print("\n"+" ="*50)
    print("step1 - search agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [
            [("user", f"Search for recent and reliable information on {topic}")]
        ]
    })
    state["search_results"] = search_result['messages'][-1].content

    print("\n search result \n", state["search_results"])

    