from pypresence import Presence
import time

client_id = "1083389751186440202"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

# Make sure you are using the same name that you used when uploading the image
RPC.update(state="Touching grass", details="It's so cool!", large_image="touching")

while 1:
    time.sleep(15)
