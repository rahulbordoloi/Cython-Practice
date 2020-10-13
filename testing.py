# Importing Modules
import timeit

# Importing Variables
cy, py = [], []
loops = 100

# Loop to Measure Time
for i in range(loops):
    cy.append(timeit.timeit('example_cy.test(5)', setup = 'import example_cy', number = 1000))
    py.append(timeit.timeit('example_py.test(5)', setup = 'import example_py', number = 1000))

# Finding out the Average of Each Category
cy_mean = sum(cy) / loops
py_mean = sum(py) / loops

# Printing the Results
print("Cython is {}x faster [over {} loops]".format(py_mean/cy_mean, loops))
    
