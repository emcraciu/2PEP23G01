## Quiz

https://www.classmarker.com/

## Homework

Create a context manager that will time how long it took to execute the context code block and display a graph with
execution time when the context ends.

- Since the same instance can be used in multiple contexts make sure that the graph will show data for each time the
  object was used in a context. Se see usage example below
- You will need to store the graph in the context object in order to be able to update graph information on each run
- Inorder to use the same instance and store the graph information the context object is created before we use the
  "with" statement

example

```python

class MyMyContextManager:
    def __enter__(self):
    # your code
    def __exit__(self, exc_type, exc_val, exc_tb):
    # your code

obj = MyMyContextManager()
with obj as value1:
    sleep(1)
with obj as value2:
    sleep(2)
with obj as value3:
    sleep(3)

# Now graph will contain 3 values based on how long each context needed to execute. Notice that you will not even be
# the value1-3 objects inside the context. You can even choose to wite the conetext as 
with obj:
# code
```