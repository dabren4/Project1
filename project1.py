#Darren Chen
# 9/26/23

# Project 1 CPSC 335

def Solution(Busy_schedule: list[int], Working_period: list[int], duration: int):
  availability = []

  Busy_schedule2 = []

  #get minimum working time
  start_time = max(Busy_schedule[0], Busy_schedule2[0])
  end_time = min(Busy_schedule[Busy_schedule.length()-1], Busy_schedule2[Busy_schedule2.length()-1])

  #get the baseline schedule
  baseschedule = [start_time, end_time]

# Solution([['12:00':'13:00'],['14:00':'15:00']], ['9:00','19:00'], 30)
