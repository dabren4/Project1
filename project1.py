#Darren Chen
# 9/26/23

# Project 1 CPSC 335

# read file
# assuming there is only two people per meeting

import re

with open('input.txt') as f:
  lines = f.readlines()

i = 0
test_cases = []

while i < len(lines):
  busy_schedule1 = re.findall(r"'(\d+:\d+)':'(\d+:\d+)'", lines[i])
  busy_schedule1 = [[start, end] for start, end in busy_schedule1]

  # Parse as list instead of string
  working_period1 = lines[i+1].strip()[2:-2].split("','")

  busy_schedule2 = re.findall(r"'(\d+:\d+)':'(\d+:\d+)'", lines[i+2])
  busy_schedule2 = [[start, end] for start, end in busy_schedule2]

  working_period2 = lines[i+3].strip()[2:-2].split("','")

  duration = int(lines[i+4])

  test_cases.append((busy_schedule1, working_period1,
                    busy_schedule2, working_period2,
                    duration))

  i += 5

# convert the list string into minutes to calc duration later
def convert_time(time_str):
  hours, minutes = time_str.split(':')
  return int(hours) * 60 + int(minutes)



def Solution(Busy_schedule, Working_period, Busy_schedule2, Working_period2, duration):
  availability = []

  #get minimum working time
  start_time = max(Working_period[0], Working_period2[0])
  end_time = min(Working_period[len(Working_period) - 1], Working_period2[len(Working_period2) - 1])

  #get the baseline schedule
  baseschedule = [start_time, end_time]

  #get the busy times
  busy_times = Busy_schedule + Busy_schedule2

  current_time = start_time

  for interval in busy_times:

    # Find availability before this busy time
    if interval[0] > current_time:
      start = convert_time(current_time)
      end = convert_time(interval[0])

      if (end - start) >= duration:
        availability.append([current_time, interval[0]])

    # Update current time
    current_time = interval[1]

  # Add any remaining availability
  if current_time < end_time:
     availability.append([current_time, end_time])

  return availability

# goes thru all the test cases
for case in test_cases:
  busy_schedule1, working_period1, busy_schedule2, working_period2, duration = case

  result = Solution(busy_schedule1, working_period1, busy_schedule2, working_period2, duration)
  print("result is ", result)
