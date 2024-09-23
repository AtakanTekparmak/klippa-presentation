from duckduckgo_search import DDGS
from pydantic import BaseModel

# Declare constants
MAX_RESULTS = 5         

class SearchResult(BaseModel):
    """
    A search result from DuckDuckGo Search (DDGS).
    """
    title: str
    href: str
    body: str

def web_search(
        query: str,
        max_results: int = MAX_RESULTS
    ) -> list[SearchResult]:
    """
    Search the web using DuckDuckGo Search (DDGS) and return the results.
    """
    results_list = DDGS().text(
        keywords=query,
        max_results=max_results 
    )
    return [SearchResult(**result) for result in results_list]