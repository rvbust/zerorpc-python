import zerorpc
import time

sg_service = "tcp://localhost:4242"

c = zerorpc.Client()
c.connect(sg_service)
st = time.time()
arr = c.send_array(1920, 1080)
print(time.time() - st)
print(arr)

