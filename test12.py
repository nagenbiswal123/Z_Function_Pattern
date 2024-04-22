#Below a and b are the Global variables 
#Always write a variable name in proper syntax/proper name, otherwise Interviewer will think you don't have the real Experience.
#Ruleno1: Always declare a variable in small case
#If you variable name in 2 part like it below, EC2_Instance_Name
# and also we are clalled snake casing , Ec2_Instance_Name
#In Camle casing format to write a varibale name is, Ec2InstanceName
#Make a variable as discriptive Format, like in a Good format/In full name instead of writing fn, n.


#Some Good format of writing the Variable name

# Define configuration variables for a web server
"""
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

# Update configuration values
port = 443
is_https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}") """

a=9
b=3

def addition():
    c=23 #Local scope Variable
    print(a + b + c)

def sub():
    print(a - b)

addition()
sub()

