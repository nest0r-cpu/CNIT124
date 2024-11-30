import socket

# Create a socket object
s = socket.socket()

# Connect to the server at the specified address and port
s.connect(("ad.samsclass.info", 10203))

# Receive the server's initial message (including the number)
response = s.recv(1024).decode()
print(f"Server said: {response}")

# Extract the number from the server's message
# Assuming the number is after "Your number is " in the response
number_start = response.find("Your number is ") + len("Your number is ")
number_str = response[number_start:].strip()  # Extract the number as a string
number = int(number_str)  # Convert the number to an integer

# Add one to the number
reply = number + 1
print(f"Number: {number}, Sending: {reply}")

# Send the incremented number back to the server
s.send(f"{reply}\n".encode())

# Receive the server's response (likely the flag) and print it
flag = s.recv(1024).decode()
print(f"Server response: {flag}")

# Close the connection
s.close()

