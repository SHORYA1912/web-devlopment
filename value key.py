
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "country": "USA"
}

key = input("Enter the key to search: ")

if key in data:
    print(f"The value for '{key}' is: {data[key]}")
else:
    print("Key not found.")