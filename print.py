'''
Created September 30, 2015

@Author Rachel Ehrlich
'''
from py2neo import Graph, Relationship

def write_knows_edge_list_for_gephi(graph):
    fout = open('bin/knows_edge_list_gephi.csv', 'w')
    for rel in graph.match(rel_type="KNOWS"):
        edge_str = "{0};{1};{2}\r\n".format(rel.nodes[0]["name"], rel.nodes[1]["name"], rel["common_issues"])
        fout.write(edge_str)
    fout.close()

graph = Graph()
write_knows_edge_list_for_gephi(graph)
