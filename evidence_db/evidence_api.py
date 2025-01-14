import os
import json

from flask import Flask, make_response, redirect, url_for
from flask import request, jsonify, render_template

from evidence_retrieval import EvidenceRetrieval

evid_retrieval = EvidenceRetrieval(test_dataset_type = "mmcovar")

os.environ["FLASK_RUN_HOST"] = "0.0.0.0"

app = Flask(__name__)

'''

'''
@app.route('/search', methods = ["GET"])
def search():
    query = request.args.get('query')
    evidences = evid_retrieval.search_evidence(query = query)
    return {
        "query": query,
        "evidences": evidences
    }


@app.route('/search_with_claim', methods = ["GET"])
def search_with_claim():
    query = request.args.get('query')
    claim = request.args.get("claim")
    context = ""
    
    if request.args.get("context") is not None:
        context = request.args.get("context")
    
    evidences = evid_retrieval.search_evidence(
        query = query,
        claim = claim,
        context = context
    )
    return {
        "query": query,
        "claim": claim,
        "context": context,
        "evidences": evidences
    }

@app.route('/search_by_source', methods = ["GET"])
def search_by_source():
    query = request.args.get('query')
    sources = json.loads(request.args.get('sources'))
    
    
    evidences = evid_retrieval.search_evidence_by_sources(query = query, sources = sources)
    return {
        "query": query,
        "sources": sources,
        "evidences": evidences
    }


@app.route('/search_by_source_with_claim', methods = ["GET"])
def search_by_source_with_claim():
    query = request.args.get('query')
    sources = json.loads(request.args.get('sources'))
    
    claim = request.args.get("claim")
    context = ""
    
    if request.args.get("context") is not None:
        context = request.args.get("context")
    
    evidences = evid_retrieval.search_evidence_by_sources(
        query = query,
        sources = sources,
        claim = claim,
        context = context
    )
    return {
        "query": query,
        "sources": sources,
        "claim": claim,
        "context": context,
        "evidences": evidences
    }

if __name__ == "__main__":
	app.run()