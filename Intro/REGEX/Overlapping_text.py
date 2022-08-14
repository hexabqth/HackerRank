'''
HTML
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.

Example (based on the original Python documentation):

Code

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag
    def handle_endtag(self, tag):
        print "Found an end tag   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")
Output

Found a start tag  : html
Found a start tag  : head
Found a start tag  : title
Found an end tag   : title
Found an end tag   : head
Found a start tag  : body
Found a start tag  : h1
Found an end tag   : h1
Found an empty tag : br
Found an end tag   : body
Found an end tag   : html


.handle_starttag(tag, attrs)

This method is called to handle the start tag of an element. (For example: <div class='marks'>)
The tag argument is the name of the tag converted to lowercase.
The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.


.handle_endtag(tag)

This method is called to handle the end tag of an element. (For example: </div>)
The tag argument is the name of the tag converted to lowercase.


.handle_startendtag(tag,attrs)

This method is called to handle the empty tag of an element. (For example: <br />)
The tag argument is the name of the tag converted to lowercase.
The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.


'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())

lst=[input() for i in range(n)]
s=''.join(lst)
exp=r'(?<=<)(?:.*?)(?=>)'
r=re.compile(exp)
exp2=r'(?<=[/])\w+'
tags=r.findall(s)
r2=re.compile(exp2)
for tag in tags:
    if r2.findall(tag):
        print('Found a end tag  :'+tag)
    else:
        print('Found a start tag  :'+tag)
