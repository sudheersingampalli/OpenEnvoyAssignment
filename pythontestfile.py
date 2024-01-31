# This is a Python script
# It demonstrates line comments and blank lines

def greet(name):
    # This function greets the user
    print(f"Hello, {name}!")

'''
adding
three

lines
'''

# Main function
def main():
    # Get user input
    user_name = input("Enter your name: ")

    # Check if the user provided a name
    if user_name:
        greet(user_name)
    else:
        print("You didn't enter a name.")

# Execute the main function
if __name__ == "__main__":
    main()
