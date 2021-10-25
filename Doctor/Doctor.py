from vidstream import *
import tkinter as tk
import socket
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def start_listening():
	t1 = threading.Thread(target=server.start_server)
	t2 = threading.Thread(target=receiver.start_server)
	t1.start()
	t2.start()

def start_camera_stream():
	camera_client= CameraClient(text_target_ip.get(1.0, 'end-1c'),7777)
	t3 = threading.Thread(target=camera_client.start_stream)
	t3.start()

def start_screen_sharing():
	screen_client= ScreenShareClient(text_target_ip.get(2.0, 'end-1c'),7777)
	t4 = threading.Thread(target=screen_client.start_stream)
	t4.start()

def start_audio_stream():
	audio_sender= AudioSender(text_target_ip.get(1.0, 'end-1c'),6666)
	t5 = threading.Thread(target=audio_sender.start_stream)
	t5.start()

#GUI
window = tk.Tk()
window.title("Doctor - Caller")
window.geometry("300x200")

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip =tk.Text(window, height=1)
text_target_ip.pack()

listen_btn = tk.Button(window, text="Start Listening", width=50, command=start_listening)
listen_btn.pack(anchor=tk.CENTER, expand=True)

camera_btn = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
camera_btn.pack(anchor=tk.CENTER, expand=True)

screen_btn = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
screen_btn.pack(anchor=tk.CENTER, expand=True)

audio_btn = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
audio_btn.pack(anchor=tk.CENTER, expand=True)

window.mainloop()