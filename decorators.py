# a function that takes a function as a parameter and modifies it and outputs another function

def announce(f):
  def wrapper():
    print('About to run the function...')
    f()
    print('Done with the function.')
  return wrapper

# add the announce decorater to the function
@announce
def hello():
  print('Hello, world!')

hello()