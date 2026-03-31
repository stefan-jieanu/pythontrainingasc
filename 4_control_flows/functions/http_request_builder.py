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

def build_request(url: str, *path_segments: str, **query_params: str | int | bool) -> str:
  segments = '/' + '/'.join(path_segments) if path_segments else ''

  query_items_list = [f"{key}={str(value)}" for key, value in query_params.items()]
  query = '?' + '&'.join(query_items_list) if query_params else ''

  return f"{url.rstrip('/')}{segments}{query}"

print(
  build_request(
    "https://api.example.com",
    "users",
    "123",
    active=True,
    location="US",
    format="json"
  )
)

print(
  build_request(
    "https://api.example.com/",
    active=True,
    format="json"
  )
)

print(
  build_request(
    "https://api.example.com/",
    "users",
    "123",
  )
)

print(
  build_request(
    "https://api.example.com"
  )
)

#build_request() - throws missing 1 required positional argument: 'url'