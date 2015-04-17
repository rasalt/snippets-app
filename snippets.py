##!/usr/bin/python
import logging
import psycopg2


logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
connection = psycopg2.connect("dbname='snippets' user='action' host='localhost'")
logging.debug("Database connection establised")

def put(name, snippet, hide):
  """
  Store a snippet with an associated name
  Returns the name and snippet
  """
  logging.info("Storing snippet - put({!r},{!r})".format(name, snippet))
  cursor = connection.cursor()
  print "Hide is {}".format(hide)
  with connection, connection.cursor() as cursor:
    try:
      command = "Insert into snippets values (%s, %s, %s)"  
      cursor.execute(command, (name, snippet, hide))
    except psycopg2.IntegrityError:
      print "Updating "
      connection.rollback() # without this it won't work.
      command = "update snippets set message=%s, hidden=%s where keyword=%s"
      cursor.execute(command, (snippet,hide,name))
          
  logging.debug("Snippet stored successfully")
  return name, snippet
                                                                                    
  
def get(name):
  """ Retrieves the snippet with a given name.
  If there is no such snippet...
  Returns the snippet.  
  """  
  tup = ()
  logging.info("Retrieving the snippet- get({!r})".format(name))
  with connection, connection.cursor() as cursor:
    cursor.execute("select message from snippets where keyword=%s", (name,))
    tup = cursor.fetchone()
  if not tup:
    snip = ""
    err = True
  else:
    print "tup is {}".format(tup)
    logging.debug("Retrieved the snippet")
    snip = tup[0]
    err = False
  
  return snip, err

def catalog(show):
  """ Retrieves the catalog of the get function
  """  
  logging.info("Retrieving the Catalog 5nippet- catalog")
  with connection, connection.cursor() as cursor:
    cursor.execute("select * from snippets where hidden=%s OR hidden=False order by keyword", (show,)) 
    catalog_rows = cursor.fetchall()
  
  for row in catalog_rows:
    print "row {}".format(row)
    
def grep(string):
  """ Retrieves the right row wit the grep string 
  """  
  logging.info("Retrieving the message with the right grep string")
  with connection, connection.cursor() as cursor:
    cursor.execute("select * from snippets where message like %s", (string+'%',))
    rows = cursor.fetchall()
  if rows:
    for row in rows:
      print "row is {}".format(row)
  else:
    print "No message was found with your grep string"
      

import argparse
import sys 
def main():
  """Main function"""
  logging.info("Construction of parser")
  parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text ")
  #Adding subparserc
  subparsers = parser.add_subparsers(dest="command", help="Available Commands")
  
  #Subparser for the put command
  logging.debug("Constructing put subparser")
  put_parser = subparsers.add_parser("put", help="Store a snippet")
  put_parser.add_argument("name", help="Name of snippet")
  put_parser.add_argument("snippet", help="Snippet text")
  put_parser.add_argument("--hide", help="Whether to hide this snippert from search", action="store_true")
  
  logging.debug("Constructing get subparser")
  get_parser = subparsers.add_parser("get", help="Store a snippet")
  get_parser.add_argument("name", help="Name of snippet")
  
  
  catalog_parser = subparsers.add_parser("catalog", help="Getting a catalog")
  catalog_parser.add_argument("--show", help="Show all or not from the snippets table whether hidden or not", action="store_true")
  
  grep_parser = subparsers.add_parser("grep", help="Search for a string ")
  grep_parser.add_argument("string",help="Grep string to search")
  
  arguments = parser.parse_args(sys.argv[1:])
  print "Arguments is {}".format(arguments)
                                 
  arguments  = vars(arguments)
  print "Arguments are now {}".format(arguments)
  command = arguments.pop("command")
  
  if command == "put":
    name, snippet = put(**arguments)
    print("Store {!r} and {!r}".format(snippet, name))
  elif command =="get":
    snippet, error = get(**arguments)
    if error == True:
      print "Snippet is non existent do ask for what exists"
    else:
      print("Retrieved snippet {!r}".format(snippet))
  elif command == "catalog":
    catalog(**arguments)
  elif command == "grep":
    grep(**arguments)
    
    
    
      
if __name__ == '__main__':  
  main()