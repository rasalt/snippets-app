##!/usr/bin/python
import logging

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
  """
  Store a snippet with an associated name
  Returns the name and snippet
  """
  logging.error("FIXME: Unimplemented - put({!r},{!r})".format(name, snippet))
                                                                                    
  
def get(name):
  """ Retrieves the snippet with a given name.
  If there is no such snippet...
  Returns the snippet.  
  """  
  logging.error("FIXME: Unimplemented - get({!r})".format(name))
  return ""
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
  
if __name__ == '__main__':  
  main()