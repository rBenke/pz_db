from connector import Neo4jConnection
from ogb.nodeproppred import NodePropPredDataset
from tqdm import tqdm

#TODO: Try this, if it wont work (bacause of lack of disc space)  then generate an artificial graph instead.

def main():
    dataset = NodePropPredDataset("ogbn-products", root="/data")[0][0]
    conn = Neo4jConnection()
    edges = dataset["edge_index"]
    num_nodes = dataset["num_nodes"]
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    
    edges = list(zip(edges[0,:].tolist(), edges[1,:].tolist()))
    for edge_lst in tqdm(partition(edges, 1000)):
        conn.run_query(f"UNWIND $props as map MATCH (n1:Node),(n2:Node) WHERE n1.id=map[0] and n2.id=map[1] CREATE (n1)-[r:REL]->(n2)", {"props": edge_lst})
        


if __name__=="__main__":
    main()
