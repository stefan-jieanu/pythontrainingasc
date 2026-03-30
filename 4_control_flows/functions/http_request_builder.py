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

import re


def build_request(url, *path_segments, **query_params):
    # Verify if first argument is valid secure URL
    pattern = "^https?:\\/\\/([0-9A-Za-z-]+\\.)+[A-Za-z]{2,}$"
    if not re.match(pattern, url): raise TypeError("No secure URL provided")

    full_url = [url]

    for segment in path_segments:
        full_url.append(f"/{segment}")
    
    if len(query_params):
        last_key = list(query_params.keys())[-1]

        full_url.append("?")
        for key, value in query_params.items():
            formatted_path = f"{key}={value}"
            if key != last_key: formatted_path += "&"

            full_url.append(formatted_path)

    print("".join(full_url))


# Example 1
build_request("https://api.example.com", "products")

# Example 2
build_request(
    "https://api.example.com",
    "users",
    "123",
    active=True,
    format="json"
)