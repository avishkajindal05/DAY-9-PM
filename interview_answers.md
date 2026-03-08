Q1: Conceptual - Tuple Immutability Trap
Can we run t[0][0] = 99?
YES, it works!
Python
Copy
t = ([1, 2], [3, 4])
t[0][0] = 99
print(t)  # Output: ([99, 2], [3, 4])
Why it works:
Tuples are immutable in the sense that you cannot reassign tuple elements: t[0] = [99, 2] would fail with TypeError
However, the tuple contains references to mutable objects (lists)
The lists themselves are mutable, so modifying the contents of the referenced list is allowed
We're not changing which object t[0] points to—we're modifying the object it points to
What this reveals:
Python's "immutability" is shallow—it only applies to the container's immediate structure
A tuple guarantees its element references won't change, but makes no guarantees about the objects those references point to
This is a common source of bugs when using mutable objects (lists, dicts, sets) inside tuples
Q2: Coding - Duplicate Detection
Python
Copy
def find_duplicates(lst):
    """
    Returns set of elements appearing more than once.
    Uses set operations only - O(n) time complexity.
    """
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return duplicates
Alternative one-liner using set operations:
Python
Copy
def find_duplicates(lst):
    return set(lst) - set(dict.fromkeys(lst))  # Or use collections.Counter logic manually
Actually, cleaner O(n) approach:
Python
Copy
def find_duplicates(lst):
    seen = set()
    return {x for x in lst if x in seen or seen.add(x)}
Complexity: O(n) time, O(n) space
Q3: Debug Problem - Unique to Each List
Why it fails:
The buggy code only returns elements in a but not in b ([1, 2]). It misses elements unique to b ([4, 5]).
The fix:
Python
Copy
def unique_to_each(a, b):
    """
    Returns elements that appear in exactly one of the two lists.
    (Symmetric difference: in a OR b, but not both)
    """
    set_a = set(a)
    set_b = set(b)
    result = set_a ^ set_b  # Symmetric difference operator
    return list(result)
Explanation:
set_a - set_b gives elements only in a (asymmetric difference)
set_a ^ set_b (symmetric difference △) gives elements in exactly one set
Equivalent to: (set_a | set_b) - (set_a & set_b) or (set_a - set_b) | (set_b - set_a)