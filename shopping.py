def calc_price(weight):
  ground = 20
  drone = 0
  premium_ground = 125
  if weight > 10:
    ground += 4.75 * weight
    drone += 14.25 * weight
  elif (weight > 6):
    ground += 4 * weight
    drone += 12 * weight
  elif (weight > 2):
    ground += 3 * weight
    drone += 9 * weight
  else:
    ground += 1.5 * weight
    drone += 4.5 * weight
  if (ground < drone) and (ground < premium_ground):
    return "Ground: $" + str(ground)
  if (premium_ground < drone) and (premium_ground < ground):
    return "premium_ground: $" + str(premium_ground)
  if (drone < ground) and (drone < premium_ground):
    return "drone: $" + str(drone)

print(calc_price(4.8))
print(calc_price(41.5))


