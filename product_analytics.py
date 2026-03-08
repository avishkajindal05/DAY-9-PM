from collections import namedtuple

# 1️⃣ Named Tuple
Product = namedtuple("Product", ["id", "name", "category", "price"])


# 2️⃣ Product Catalog (15 products, 4 categories)

catalog = [
    Product(1, "Laptop", "Electronics", 75000),
    Product(2, "Smartphone", "Electronics", 50000),
    Product(3, "Headphones", "Electronics", 3000),
    Product(4, "Smartwatch", "Electronics", 12000),

    Product(5, "T-Shirt", "Clothing", 800),
    Product(6, "Jeans", "Clothing", 2000),
    Product(7, "Jacket", "Clothing", 4500),
    Product(8, "Sneakers", "Clothing", 3500),

    Product(9, "Python Crash Course", "Books", 1200),
    Product(10, "Clean Code", "Books", 1500),
    Product(11, "Atomic Habits", "Books", 900),

    Product(12, "Coffee Maker", "Home", 2500),
    Product(13, "Air Fryer", "Home", 7000),
    Product(14, "Desk Lamp", "Home", 1200),
    Product(15, "Office Chair", "Home", 9000)
]


# Quick references
p = {product.id: product for product in catalog}


# 3️⃣ Customer Cart Sets

customer_1_cart = {p[1], p[5], p[9], p[12]}
customer_2_cart = {p[1], p[2], p[9], p[13]}
customer_3_cart = {p[1], p[3], p[10], p[12]}
customer_4_cart = {p[1], p[6], p[11], p[14]}
customer_5_cart = {p[1], p[7], p[9], p[15]}

all_carts = [
    customer_1_cart,
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart
]


# 4️⃣ Shopping Behaviour Analysis

# (a) Bestsellers -> products in ALL carts
bestsellers = set.intersection(*all_carts)

# (b) Catalog Reach -> products in ANY cart
catalog_reach = set.union(*all_carts)

# (c) Exclusive Purchases (customer 1 only)

other_carts_union = set.union(
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart
)

exclusive_customer1 = customer_1_cart - other_carts_union


# 5️⃣ Product Recommendation

def recommend_products(customer_cart, all_carts):

    other_products = set.union(*all_carts)

    recommendations = other_products - customer_cart

    return recommendations


# 6️⃣ Category Summary

def category_summary():

    categories = {product.category for product in catalog}

    summary = {
        category: {p.name for p in catalog if p.category == category}
        for category in categories
    }

    return summary


# -------- Example Output --------

if __name__ == "__main__":

    print("Bestsellers:")
    print({p.name for p in bestsellers})

    print("\nCatalog Reach:")
    print({p.name for p in catalog_reach})

    print("\nExclusive purchases (Customer 1):")
    print({p.name for p in exclusive_customer1})

    print("\nRecommendations for Customer 1:")
    recs = recommend_products(customer_1_cart, all_carts)
    print({p.name for p in recs})

    print("\nCategory Summary:")
    print(category_summary())