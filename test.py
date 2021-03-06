
top = 6
right = 6
corners = ((1,1), (1,top), (right, 1), (right, top))
print(corners)
corner_list = []
state = (4,5)
xy1 = state
euclidian_sum = 0
#Iterate through corners
for i in range(0,len(corners)):
    # Get length to each corner
    xy2 = corners[i]
    print(f"performing {xy1} - {xy2}")
    euclidian_sum += ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5
    print(euclidian_sum)
print(f"Total is: {euclidian_sum/4}")
'''
if (corners.index((right,8))):
    out = corners.index((right,8))
else: 
    out = False

x=5
while True:
    try:
        corners.index((right,x))
        print("Doing something")
        break
    except ValueError:
        print("Doing Nothing")
        break
print("We out")
'''