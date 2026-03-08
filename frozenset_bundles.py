"""
=====================================================
FROZENSET STUDY NOTES
=====================================================

What is a frozenset?

A frozenset is an immutable version of a set in Python.
Once created, elements cannot be added, removed, or changed.

Example:
    s = frozenset({1,2,3})

Properties:
- Unordered
- No duplicates
- Immutable
- Hashable (can be used as dictionary keys)

-----------------------------------------------------

Difference: set vs frozenset

| Feature | set | frozenset |
|-------|------|-----------|
| Mutable | Yes | No |
| Add/Remove | Allowed | Not allowed |
| Hashable | No | Yes |
| Dictionary Key | Cannot use | Can use |

Example:

    s = {1,2,3}
    s.add(4)

    fs = frozenset({1,2,3})
    # fs.add(4)  -> ERROR


-----------------------------------------------------

When to use frozenset in real systems?

1. Dictionary keys for combinations
   Example: bundle discounts

2. Graph algorithms
   Represent immutable node sets

3. Caching systems
   Frozen data structures ensure consistency

4. Security-sensitive systems
   Prevent modification of important collections

Example real use:
    frozenset({'Electronics','Books'}) → bundle deal
"""
from collections import namedtuple
import timeit


# Product structure
Product = namedtuple("Product", ["id", "name", "category", "price"])


# Sample products
catalog = [
    Product(1,"Laptop","Electronics",75000),
    Product(2,"Phone","Electronics",50000),
    Product(3,"Headphones","Electronics",3000),

    Product(4,"Clean Code","Books",1500),
    Product(5,"Python Crash Course","Books",1200),

    Product(6,"Tshirt","Clothing",800),
    Product(7,"Jeans","Clothing",2000),

    Product(8,"Coffee Maker","Home",3000),
]


# --------------------------------------------------
# 2️⃣ Bundle Discount System
# --------------------------------------------------

bundle_discounts = {

    frozenset({'Electronics','Books'}): 10,
    frozenset({'Electronics','Clothing'}): 8,
    frozenset({'Home','Electronics'}): 12,
    frozenset({'Books','Clothing'}): 5

}


# --------------------------------------------------
# 3️⃣ Bundle Checker Function
# --------------------------------------------------

def check_bundle_discount(cart):

    """
    cart → set of Product objects

    Steps:
    1. Extract categories from cart
    2. Convert to set
    3. Check if bundle exists
    """

    cart_categories = {product.category for product in cart}

    for bundle, discount in bundle_discounts.items():

        if bundle.issubset(cart_categories):
            return discount

    return 0


# Example cart
cart = {
    catalog[0],   # Laptop
    catalog[3],   # Clean Code
}


discount = check_bundle_discount(cart)


# --------------------------------------------------
# 4️⃣ Performance Benchmark
# --------------------------------------------------

"""
Benchmark: set vs frozenset creation speed
Running 100000 iterations using timeit

Observation:
- set creation is slightly faster
- frozenset creation takes slightly more time
  due to immutability and hashing

However frozenset allows:
- safe dictionary keys
- immutable combinations
"""

set_time = timeit.timeit(
    "set(['Electronics','Books'])",
    number=100000
)

frozenset_time = timeit.timeit(
    "frozenset(['Electronics','Books'])",
    number=100000
)


print("Set creation time:", set_time)
print("Frozenset creation time:", frozenset_time)


# --------------------------------------------------
# Demo
# --------------------------------------------------

if __name__ == "__main__":

    print("Cart Categories:", {p.category for p in cart})

    discount = check_bundle_discount(cart)

    print("Applicable Discount:", discount,"%")