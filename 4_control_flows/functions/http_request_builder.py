# Create a function that builds a fake HTTP request configuration.
# def build_request(url, *path_segments, **query_params)

# Requirements
# url
#  - Base URL.
# *path_segments
#  - Additional path elements.
# **query_params
# - Query string parameters.

# Example 1
# build_request("https://api.example.com", "products")

# Output:
# https://api.example.com/products

# Example 2
# build_request(
#     "https://api.example.com",
#     "users",
#     "123",
#     active=True,
#     format="json"
# )

# Expected output:
# https://api.example.com/users/123?active=True&format=json