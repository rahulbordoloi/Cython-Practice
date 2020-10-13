# Cython-Practice

## Prerequisite

1. `pip install cython`
2. The system must have MingW/G++ (any versions) installed.

## Build File

```
python3 setup.py build_ext --inplace
```

## Testing Both the Cython and Python Files

```
python3 testing.py
```

## Compare Cython code with Python [Implementation]

```
cython -a Depreciated\example_cy.pyx
```

Note : It generates a HTML File.