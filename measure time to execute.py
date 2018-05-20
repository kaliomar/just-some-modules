

import time
start_time = time.time()

for i in range(0, 1000000):
   print (i)

print("--- %s seconds ---" % (time.time() - start_time))
