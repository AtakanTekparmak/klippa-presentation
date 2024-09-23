import pytest
from tools.ddg_search import web_search, SearchResult

def test_web_search_valid_query():
    query = "Python programming"
    results = web_search(query)
    assert len(results) > 0
    assert all(isinstance(result, SearchResult) for result in results)
    assert all(result.title and result.href and result.body for result in results)
    
def test_web_search_max_results():
    query = "Python programming"
    max_results = 3
    results = web_search(query, max_results=max_results)
    assert len(results) <= max_results
