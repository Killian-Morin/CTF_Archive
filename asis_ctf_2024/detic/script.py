import subprocess
import threading

# Attempt at opening the nc connection and getting the point necessary for the solving but it writes to the file after finishing the script

def read_from_server(process):
    """Function to read from the server continuously."""
    while True:
        line = process.stdout.readline()
        if line == '':
            break  # Connection closed
        print(f"{line.strip()}")
        if line.find('P1') != -1 or line.find('P2') != -1 or line.find('P3') != -1:
            file.write(line)

def interactive_nc(host, port):
    try:
        # Launch the `nc` process
        process = subprocess.Popen(
            ['nc', host, str(port)],
            stdin=subprocess.PIPE,  # Pipe for sending input
            stdout=subprocess.PIPE, # Pipe for receiving output
            stderr=subprocess.PIPE, # Pipe for receiving error messages
            text=True               # Handle as text
        )

        # Start a thread to read from the server continuously
        reader_thread = threading.Thread(target=read_from_server, args=(process,))
        reader_thread.daemon = True
        reader_thread.start()

        # Keep the connection open and allow user to send input
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                break  # Exit the loop and close the connection
            process.stdin.write(user_input + '\n')
            process.stdin.flush()

        # Close the process after user exits
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.wait()

    except Exception as e:
        print(f"An error occurred: {e}")

file = open('./coordinates.txt', 'a')

# Call the function with example host and port
interactive_nc('65.109.192.143', 13770)
