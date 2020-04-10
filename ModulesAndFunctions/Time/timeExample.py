######First time on time

# import time
#
# print(time.gmtime(0))
# print(time.localtime())
#
# print(time.time())


######Second time

# import time
#
# feat_time = time.localtime()
#
# print("Year: ", feat_time.tm_year)
# print("Month: ", feat_time.tm_mon)
# print("Day: ", feat_time.tm_mday)
    # 'tm_yday' means total days from jan 1 and 'tm_mday' means total days from the current month

######Third time and hard one

import time
from time import time as my_timer
import random

input("Please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input("Please enter to end")

end_time = my_timer()

print("Started at: " + time.strftime("%X", time.localtime(start_time)))
print("Ended at: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time is {0} seconds.".format(end_time - start_time))