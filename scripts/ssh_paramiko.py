import paramiko

# Define the SSH parameters
hostname = '192.168.1.1'  # IP address or hostname of the remote device
username = 'username'    # SSH username
password = 'password'    # SSH password
command = 'pwd'  # Command to run on the remote device

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote device
    client.connect(hostname, username=username, password=password)

    # Run the command on the remote device
    stdin, stdout, stderr = client.exec_command(command)

    # Retrieve the output of the command
    output = stdout.read().decode()

    # Print the output
    print("Command output:")
    print(output)

except paramiko.AuthenticationException as e:
    print("Authentication failed:", e)

except paramiko.SSHException as e:
    print("Failed to establish SSH connection:", e)

except Exception as e:
    print("Error:", e)

finally:
    # Close the SSH connection
    client.close()
