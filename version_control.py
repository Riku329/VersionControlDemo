# Version 1
print("Hello, World")

# Version 2
name = input("Enter Your Name:")
print(f"Hello,{name}!")

# Version 3
while True:
    name = input("Enter your name (or 'exit' to quit):")
    if name.lower() =='exit':
        break
    print(f"Hello, {name}!")  