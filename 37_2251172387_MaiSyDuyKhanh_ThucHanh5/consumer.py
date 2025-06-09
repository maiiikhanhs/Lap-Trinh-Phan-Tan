import time
import stomp

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print('Received:', frame.body)

conn = stomp.Connection([('172.20.10.12', 61613)])
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True)

queue = 'th5'

conn.subscribe(destination=f'/topic/{queue}', id=2, ack='auto')

print("Waiting for messages...")

while True:
    time.sleep(1)