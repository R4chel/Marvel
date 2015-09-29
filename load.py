'''
Created September 28, 2015

@author Rachel Ehrlich
'''
# import urllib2
from py2neo import cypher, Graph
import re

def parse_line(line):
    pattern = re.compile('"(.*)","(.*)\s(\d+)"')
    matches = pattern.match(line)
    if matches is None:
        return
    character = matches.groups()[0]
    comic = matches.groups()[1]
    issue = matches.groups()[2]
    print character + " appears in " + comic + " #" + str(issue)

def read_character_issues(db):
    # data = urllib2.urlopen('http://exposedata.com/marvel/data/source.csv')
    data = open('bin/character_issue.csv', 'r')
    for line in data:
        parse_line(line)

db = Graph()
read_character_issues(db)

