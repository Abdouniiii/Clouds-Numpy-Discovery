
def jumpingOnClouds(c, k):
    energy = 100  # we initial energy at 100
    current_cloud = 0
    while True:
        current_cloud = (current_cloud + k) % len(c)  # Calculate the next cloud
        energy -= 1  # we decrease energy by 1 for each jump
        if c[current_cloud] == 1:
            energy -= 2  # we decrease energy by 2 when it's a thunderhead cloud    
        if current_cloud == 0:
            break  # Once we return to cloud 0 the game ends
    return energy
# Sample Input as given
k = 2
c = [0, 0, 1, 0, 0, 1, 1, 0]
result = jumpingOnClouds(c, k)
print(result)



