##!/usr/bin/python
import logging
import psycopg2


logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
connection = psycopg2.connect("dbname='snippets' user='action' host='localhost'")
logging.debug("Database connection establised")

def put(name, snippet):
  """
  Store a snippet with an associated name
  Returns the name and snippet
  """
  logging.info("Storing snippet - put({!r},{!r})".format(name, snippet))
  cursor = connection.cursor()
  command = "Insert into snippets values (%s, %s)"
  cursor.execute(command, (name, snippet))

  logging.debug("Snipper stored successfully")
  return name, snippet
                                                                                    
  
def get(name):
  """ Retrieves the snippet with a given name.
  If there is no such snippet...
  Returns the snippet.  
  """  
  tup = ()
  logging.info("Retrieving the snippet- get({!r})".format(name))
  cursor = connection.cursor()
  command = "select keyword,message from snippets where keyword='{}'".format(name)
  print "Command is {}".format(command)
  cursor.execute(command)
  tup = cursor.fetchone()
  print "tup is {}".format(tup)
  #connection.commit()
  logging.debug("Retrieved the snippet")
  return tup[1]
import argparse
import sys 
def main():
  """Main function"""
  logging.info("Construction of parser")
  parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text ")
  #Adding subparser
  subparsers = parser.add_subparsers(dest="command", help="Available Commands")
  
  #Subparser for the put command
  logging.debug("Constructing put subparser")
  put_parser = subparsers.add_parser("put", help="Store a snippet")
  put_parser.add_argument("name", help="Name of snippet")
  put_parser.add_argument("snippet", help="Snippet text")
  
  logging.debug("Constructing get subparser")
  get_parser = subparsers.add_parser("get", help="Store a snippet")
  get_parser.add_argument("name", help="Name of snippet")
  
  
  
  arguments = parser.parse_args(sys.argv[1:])
  print "Arguments is {}".format(arguments)
                                 
  arguments  = vars(arguments)
  print "Arguments are now {}".format(arguments)
  command = arguments.pop("command")
  
  if command == "put":
    name, snippet = put(**arguments)
    print("Store {!r} and {!r}".format(snippet, name))
  elif command =="get":
    snippet = get(**arguments)
    print("Retrieved snippet {!r}".format(snippet))
    
      
if __name__ == '__main__':  
  main()