# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time()
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.
import time
time_info = time.get_clock_info("time")
perf_counter_info = time.get_clock_info("perf_counter")
monotonic_info = time.get_clock_info("monotonic")
process_time_info = time.get_clock_info("process_time")

print()
print(time_info)
print(perf_counter_info)
print(monotonic_info)
print(process_time_info)