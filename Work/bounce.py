# bounce.py
#
# Exercise 1.5
# sears.py

rubber_ball_height = 100 # (meters)
total_bounce = 10 # total bounce
bounce = 1  # inital bounce
ground_bounce = .60 # 3/5 of the height
total = (rubber_ball_height * ground_bounce) 

while bounce < total_bounce:
    print(bounce, (round(total, 4)))
    bounce = bounce + 1
    total = total * ground_bounce