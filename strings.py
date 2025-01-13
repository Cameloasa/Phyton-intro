
msg = "Welcome to Phyton 101:Strings"
print(msg)
#1 Welcome Ring To Tyler
# print title - concatenate/capitalize
msg1 =msg[18]+ " " + msg[:8] +  msg[24:28]+ msg[7:10] + " " + msg[8] + msg[13] + msg[2] + msg[1] + msg[24]
print(msg1.title())
#reverse
print(msg1[:: -1])
#find
print(msg.find("h"))
print(msg.find("Phyton"))
#replace
msg_replace =msg.replace("Phyton", "Java")
print(msg_replace)
#membership
# check if 'Phyton' is in message
print('Phyton' in msg)
print('Java' not in msg)
#string formatting
name = "tylor"
color = "RED"
msg3 = '[' + name.capitalize() + '] loves the color '  + color.lower() + '!'
print(msg3)
formatted_message = f"[{name.capitalize()}] loves the color {color.lower()}!"
print(formatted_message)

