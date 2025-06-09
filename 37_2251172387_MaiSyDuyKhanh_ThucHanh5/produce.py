import stomp

conn = stomp.Connection([('172.20.10.12', 61613)])
conn.connect('admin', 'admin', wait=True)

queue = 'Thuc Hanh 7'
messsage= 'Hello my friend'

conn.send(destination=f'/queue/{queue}', body=f'{messsage}')
print("Message sent.")

conn.disconnect()
