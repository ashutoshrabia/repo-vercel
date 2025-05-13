# api/inference.py
import json
from flask import Request
from app.query import query_rag_handler  # we’ll wrap your query logic

def handler(request: Request):
    """
    Expects JSON:
      { "question": "...", "top_k": 3 }
    Returns JSON:
      { "response": "...", "sources": [...], "web_citations": [...] }
    """
    try:
        body = request.get_json()
        result = query_rag_handler(body["question"], body.get("top_k", 3))
        return {"statusCode": 200, "body": json.dumps(result)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
