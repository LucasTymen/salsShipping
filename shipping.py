logo = """
#        ######   #   #### ####  ## #
#   #    #####    #   #### ###  ### #   #
#   #### ####     #   #### ##  #### #   ####
#        ###  #   #   #### ######## #
#####    ##       #   #### ######## #####
#   #    #   ##   #   ##   ######## #   #
#           ###   #        ######## #
######## ######## ######## ######## ########

"""

# weight definition
weight = 1

# ground shipping definition
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else :
  cost_ground = weight * 4.75 + 20

# Premium Charge definition
premium_ground = 125.00

# drone shipping definition
if weight <= 2.0 :
  drone_cost_ground = weight * 4.5
elif weight <= 6.0 :
  drone_cost_ground = weight * 9.0
elif weight <= 10.0 :
  drone_cost_ground = weight * 12.0
else :
  drone_cost_ground = weight * 14.25

print(logo)
print("Cost Ground : ", cost_ground)
print("Ground Shipping Premium $ ", cost_ground + premium_ground)
print("========================================")
print("Cost DRONE  : ", drone_cost_ground)
print("DRONE Shipping Premium $ ", drone_cost_ground + premium_ground)
