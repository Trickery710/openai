# Read the token from the token.txt file
with open(".key", "r") as f:
    TOKEN = f.read().strip()

# Use the token
print(TOKEN)
