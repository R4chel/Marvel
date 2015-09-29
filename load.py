'''
Created September 28, 2015

@author Rachel Ehrlich
'''
# import urllib2
from py2neo import cypher, Graph, Relationship
import re

def parse_line(graph, line):
    pattern = re.compile('"(.*)","((.*)\s(\d+))"')
    matches = pattern.match(line)
    if matches is None:
        return
    character = matches.groups()[0]
    issue_name = matches.groups()[1]
    comic = matches.groups()[2]
    issue = matches.groups()[3]
    character_node = graph.merge_one("Character", "name", character)
    issue_node = graph.merge_one("Issue", "name", issue_name)
    issue_node.properties["comic"] = comic
    issue_node.properties["number"] = issue
    relationship = Relationship(character_node, "IS_IN", issue_node)
    graph.create_unique(relationship)

def read_character_issues(graph):
    # data = urllib2.urlopen('http://exposedata.com/marvel/data/source.csv')
    data = open('bin/character_issue.csv', 'r')
    for line in data:
        parse_line(graph, line)

def add_constraints(graph):
    labels = ["Character", "Issue"]
    for label in labels:
        try:
            graph.schema.create_uniqueness_constraint(label,"name")
        except:
            pass

graph = Graph()
add_constraints(graph)
read_character_issues(graph)

