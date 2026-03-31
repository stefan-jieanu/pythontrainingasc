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

def build_request(url, *path_segments, **query_params):
    result = url.rstrip("/")
    if path_segments:
        result += "/" + "/".join(path_segments)
    if query_params:
        pairs = [f"{key}={value}" for key, value in query_params.items()]
        result += "?" + "&".join(pairs)
    return result

print(build_request("https://api.example.com", "products"))
print(build_request(
    "https://api.example.com",
    "users",
    "123",
    active=True,
    format="json"
))