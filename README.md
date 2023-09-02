# Deep dive into Loops

## What do we get when we iterate?
- String - characters (strings of length 1)
- List - elements of the list
- Tuple - elements of the tuple
- Dictionary - the keys
- dict.items() - a tuple of each key-value
- File - the lines of the file

## Range

### What do we get from range in each iteration

```
for one_item in range(3):
    print(f"{one_item}: Hooray!")
```

When we use range(n), we get each of the numbers from 0 until and not including n.

This means, a total of n numbers

### Calling Range with 2 elements
We can call range with 2 elements -- starting point and ending + 1

```
for one_number in range(10, 15):
    print(one_number)
```

### Callling Range with 3 elements

We can call range with 3 elements ie. start, stop+1, step_size

```
for one_number in range(20, 30, 2):
    print(one_number)
```

### Counting Backwards

```
for one_number in range(30, 20, -1):
    print(one_number)
```

NOTE: Make sure that the first argument is bigger than the second one

## Enumerate

```
for one_item in enumerate(s):
    print(one_item)
```