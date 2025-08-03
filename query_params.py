"""Query parameters are key-value pairs appended to the end of a URL, following a question mark (?). They are a fundamental way to pass optional data to an endpoint, commonly used for filtering, sorting, and pagination."""

from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

# A simple in-memory db
show_items_db = []


@app.get("/items/")
async def read_items(
    category : Optional[str] = None, # Optional query param with default value
    search: str = Query(..., min_length=3, max_length=50, description="Search query string"),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10,ge=1, le=100, description="Number of items to return"),
    tags: Optional[List[str]] = Query(None, description="Filter by tags")

):
    """
    Retrieve items with filtering, pagination, and search.
    - To pass multiple tags: /items/?search=...&tags=tag1&tags=tag2
    """
    results = show_items_db
    if category:
        results = [item for item in results if item.get("category") == category]

    return {"results" : results[skip: skip + limit], "search_query": search, "tags" : tags}


# In a real app, would use the 'search' and 'tags' params to filter the database query\




