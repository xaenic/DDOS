import socket
import requests
import time


def send_raw_packets():
    target_ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    num_packets = int(input("Enter the number of packets to send: "))

    message = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((target_ip, port))
        for i in range(num_packets):
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f"Packet {i+1} sent to {target_ip}:{port} at {timestamp}")
            sock.sendall(message)
    except Exception as e:
        print(f"Error sending packets: {e}")

    sock.close()


def send_http_requests():
    target_url = input("Enter the target URL: ")
    target_url = f"https://{target_url.replace('https://','')}"
    pages = input("Enter pages to request e.g /about,/services): ").split(',')
    pages.append('')
    num_requests = int(input("Enter the number of requests to send: "))

    headers = {'User-Agent': 'My Test User-Agent'}

    for i in range(num_requests):
        try:

            for e in pages:
                response = requests.get(f"{target_url}/{e}", headers=headers)
                if response.status_code == 200:
                    print(
                        f"Request {i+1} to {target_url}/{e} sent successful-status-code: {response.status_code} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
                else:
                    print(
                        f"Request {i+1} failed with status code {response.status_code}")
        except Exception as e:
            print(f"Error sending request {i+1}: {e}")

        time.sleep(0.1)


def main():
    print("Welcome to the Stress Testing Application")
    print("Choose an option:")
    print("1. Send raw packets")
    print("2. Send HTTP requests")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        send_raw_packets()
    elif choice == '2':
        send_http_requests()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
