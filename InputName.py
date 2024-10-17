name = str(input("Enter your name: "))

# remove whitespace from str
name = name.strip()

# capitalize => Auto capitalize a single word
# name = name.capitalize()

# Auto capitalize the first letter of each word
name = name.title()

# name = str(input("Enter your name: ")).strip().title()

print(f"My name is {name}")
