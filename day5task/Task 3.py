#  Task 3: Keyword Config System (**kwargs)
# Create:
# def system_config(**settings):
# Print all key-value pairs
# 👉 Example:
# mode: debug
# version: 1.0
def system_config(**settings):
    for key, value in settings.items():
        print(key + ":", value)

system_config(mode="debug", version="1.0")