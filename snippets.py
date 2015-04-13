#!/usr/bin/python
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
  arguments = parser.parse_args(sys.argv[1:])
  print "Arguments is {}".format(arguments)
if __name__ == '__main__':  
  main()