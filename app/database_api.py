from typing import Union

from fastapi import FastAPI

from py2neo import Graph
from neo4j.connector import Neo4jConnection

database_app = FastAPI()

#TODO: write fastapi server that search the database for all incoming edges to given user

def get_edges_to(client_id):
    conn = Neo4jConnection()
    results = conn.run_query(f" MATCH (n1:Node)-[]->(n2:Node) WHERE n2.id={client_id} RETURN n1.id, n2.id")
    results = [(x["n1.id"],x["n2.id"]) for x in results]
    return results
