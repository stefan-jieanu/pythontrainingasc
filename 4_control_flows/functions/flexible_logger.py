# You are implementing a logging utility that can accept an arbitrary
# number of messages and optional configuration parameters.

# def log_messages(*messages, **options):
# Requirements
# *messages
# Accepts any number of log messages.
# Each message should be printed on a new line.

# **options
# Optional configuration for the logger.

# Supported options:

# Option	Default	Description
# level	    "INFO"	Log level
# prefix	""	    Custom prefix
# uppercase	False	Convert messages to uppercase

# Example 1:
# log_messages("Server started", "Listening on port 8000")

# Output:
# [INFO] Server started
# [INFO] Listening on port 8000

# Example 2:
# log_messages(
#     "disk almost full",
#     "cleanup recommended",
#     level="warning",
#     uppercase=True
# )

# Output:
# [warning] DISK ALMOST FULL
# [warning] CLEANUP RECOMMENDED

# Example 3:
# log_messages(
#     "User login",
#     "Session started",
#     prefix="AUTH"
# )

# Output:
# AUTH [INFO] User login
# AUTH [INFO] Session started