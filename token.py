# Read the token from the token.txt file
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

# Use the token
print(TOKEN)
