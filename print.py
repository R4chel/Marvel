'''
Created September 30, 2015

@Author Rachel Ehrlich
'''
from py2neo import Graph, Relationship

def write_node_list_for_gephi(graph):
    fout = open('bin/character_list_gephi.csv', 'w')
    fout.write("ID\r\n")
    for node in graph.find("Character"):
        node_str = "{0}\r\n".format(node["name"])
        fout.write(node_str)
    fout.close()

def write_node_degree_list_for_gephi(graph):
    fout = open('bin/character_list_degree_gephi.csv', 'w')
    fout.write("ID;Issues\r\n")
    record_list = graph.cypher.execute("MATCH (char:Character)-[:IS_IN]->(c) RETURN char, count(*) as issues")
    for rec in record_list.records:
        node_str = "{0};{1}\r\n".format(rec["char"]["name"],rec["issues"])
        fout.write(node_str)
    fout.close()

def write_knows_edge_list_for_gephi(graph):
    fout = open('bin/knows_edge_list_gephi.csv', 'w')
    fout.write("Source;Target;Weight\r\n")
    for rel in graph.match(rel_type="KNOWS"):
        edge_str = "{0};{1};{2}\r\n".format(rel.nodes[0]["name"], rel.nodes[1]["name"], rel["common_issues"])
        fout.write(edge_str)
    fout.close()

graph = Graph()
write_node_list_for_gephi(graph)
write_node_degree_list_for_gephi(graph)
