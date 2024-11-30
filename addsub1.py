import socket

# Create a socket object
s = socket.socket()

# Connect to the server
s.connect(("ad.samsclass.info", 10204))

# Loop to solve 5 challenges
for _ in range(5):
    # Receive the server's challenge
    challenge = s.recv(1024).decode().strip()
    print(f"Challenge: {challenge}")

    if "Add these numbers:" in challenge:
        # Extract numbers for addition
        numbers = challenge.split("Add these numbers:")[1]
    elif "Subtract these numbers:" in challenge:
        # Extract numbers for subtraction
        numbers = challenge.split("Subtract these numbers:")[1]
    else:
        print("Unknown challenge format!")
        break

    # Clean the extracted numbers string to remove non-numeric text
    numbers = numbers.strip()  # Remove leading/trailing spaces
    numbers = numbers.split("Answer:")[0].strip()  # Remove trailing "Answer:"

    # Debug: Print the cleaned numbers string
    print(f"Cleaned numbers string: '{numbers}'")

    try:
        # Parse the numbers into integers
        num1, num2 = map(int, numbers.split())
    except ValueError:
        print(f"Failed to parse numbers from: '{numbers}'")
        break

    # Perform the required operation
    if "Add these numbers:" in challenge:
        result = num1 + num2
    elif "Subtract these numbers:" in challenge:
        result = num1 - num2

    # Print the result and send it back to the server
    print(f"Answer: {result}")
    s.send(f"{result}\n".encode())

    # Receive and print the server's feedback
    response = s.recv(1024).decode().strip()
    print(response)

# After completing all challenges, check for the flag message
flag_response = s.recv(1024).decode().strip()
print(f"Flag response: {flag_response}")

# Close the connection
s.close()

