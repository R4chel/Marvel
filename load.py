'''
Created September 28, 2015

@author Rachel Ehrlich
'''
# import urllib2
from py2neo import cypher, Graph

def read_character_issues(db):
    # data = urllib2.urlopen('http://exposedata.com/marvel/data/source.csv')
    data = open('bin/character_issue.csv', 'r')
    for line in data:
        print line

db = Graph()
read_character_issues(db)

