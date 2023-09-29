#Darren Chen
# 9/26/23

# Project 1 CPSC 335

schedule = [[1], [2]]
# schedule = [['12:00':'13:00'],['14:00':'15:00']]

# read file
# assuming there is only two people per meeting

import re

def main():
  with open('input.txt') as f:
    lines = f.readlines()

  i = 0
  while i < len(lines):
    busy_schedule1 = re.findall(r"'(\d+:\d+)':'(\d+:\d+)'", lines[i])
    busy_schedule1 = [ [start, end] for start, end in busy_schedule1]
    i += 1

    working_period1 = lines[i].strip()[1:-1].split(',')
    i += 1

    busy_schedule2 = re.findall(r"'(\d+:\d+)':'(\d+:\d+)'", lines[i])
    busy_schedule2 = [ [start, end] for start, end in busy_schedule2]
    i += 1

    working_period2 = lines[i].strip()[1:-1].split(',')
    i += 1

    duration = int(lines[i])
    i += 1

    # Do something with the extracted info

    print(busy_schedule1)
    print(working_period1)
    print(busy_schedule2)
    print(working_period2)
    print(duration)




def Solution(Busy_schedule: list[int], Working_period: list[int], duration: int):
  availability = []

  Busy_schedule2 = [[5], [7]]

  #get minimum working time
  start_time = max(Busy_schedule[0], Busy_schedule2[0])
  end_time = min(Busy_schedule[len(Busy_schedule) - 1], Busy_schedule2[len(Busy_schedule2) - 1])

  #get the baseline schedule
  baseschedule = [start_time, end_time]

  print(baseschedule)

  #get the busy times
  busy_times = Busy_schedule + Busy_schedule2

  #trim the busy times off the baseline schedule
  for i in busy_times:
    for interval in busy_times:
      if interval > start_time and interval < end_time:
        s, e = busy_times.remove(interval)
        availability.append([s, i.s])
        availability.append([e, i.e])
      #set the interval now to e since we have to trim off the first part
      if interval < start_time:
        interval.s = i.e
      #reverse it
      if interval > end_time:
        interval.e = i.s

  return availability

main()
# Solution(schedule, ['9:00','19:00'], 30)
