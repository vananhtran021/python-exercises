import random
def dice_roll():
    roll=random.randint(1,6)
    return roll
while True:
    roll=dice_roll()
    print(roll)
    if roll==6:
        break
#roll=dice_roll()
#while roll!=6:
 #   roll=dice_roll()
  #  print(roll)