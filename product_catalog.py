from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

def user_preference():
    response = ""
    while response != "N":
        print("Input a preference:")
        preference = input()
        products.append(preference)
        # Add the customer preference to the list

        response = input("Do you want to add another preference? (Y/N): ").upper()
customer_preferences = [user_preference]

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_set = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = [set(product["tags"]) for product in products]



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags: set, customer_tags:set):
    return len(product_tags & customer_tags)
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    customer_set = set(customer_preferences)   # eliminate duplicates
    recommendations = []

    for product in products:
        product_tags = set(product.get("tags", []))  # safely get tags as a set
        matches = count_matches(product_tags, customer_set)
        recommendations.append((product.get("name", "<unnamed>"), matches))

    # Sort by best matches (highest first)
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

    '''
        Args:
            products (list): A list of product dictionaries.
            customer_tags (set): A set of tags associated with the customer.
        Returns:
            list: A list of products containing product names and their match counts.
        '''
    pass

# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(products, customer_set)

print(recommendations)


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#For this code, there was a lot of operations that were used in order to keep it working. For intersections, when the lists were changed to sets, duplicates had to
#be elminitated. Without turning the lists into the sets, there would be definite confusion and the number of duplicates or wrong preferences would be prevalent. 
#With loops the code had to go around again and again in order to get the results of what the user was asking for. By having a high number of 
#products with a lot of different tags, the loops were forced on repeat for a number of times. There was also input and output operations with
#needing to upload the data from an outside source (github) to another coding system (VS Code). Assignment operations were a huge part of this
#code as well. In order for certain functions to be created or to work they must be assigned into another function.
# 2. How might this code change if you had 1000+ products? If this code incldued 1,000+ products things would look and operate a little different.
#The paramaters for tags in the lists would change as there would be more tags to pick from. The system would have to loop through more products
#eliminating more duplicates in the converted sets. 
