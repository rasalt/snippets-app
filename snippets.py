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

#if __name__ == '__main__':
#  put(name, snippet)