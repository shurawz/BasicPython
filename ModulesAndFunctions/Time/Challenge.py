import time

clk1 = time.time()
print("Information on first clock is: {} " .format(clk1))

clk2 = time.perf_counter()
print("Information on second clock is: {}".format(clk2))

clk3 = time.monotonic()
print("Information on third clock is: {}".format(clk3))

time.sleep(2.4) #It makes the next instruction to be printed on the screen after the given argument like '2.4' seconds.

clk4 = time.process_time()
print("Information on forth clock is: {}".format(clk4))

print(end='\n')
print("=" * 130)
print(end='\n')


# He solved:

# import time

print("time.time() is {}.".format(time.get_clock_info('time')))
print("time.perf_counter() is {}.".format(time.get_clock_info('perf_counter')))
print("time.monotonic() is {}.".format(time.get_clock_info('monotonic')))
print("time.process_time() is {}.".format(time.get_clock_info('process_time')))