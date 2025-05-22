# Problem summary: calculate the total distance between two lists of numbers
# Solution idea: sort the lists and calculate the distance between each pair of elements in the same index.
list_1 = []
list_2 = []


with open('input_1.txt', 'r') as f:
    for line in f:
        a, b = map(int, line.split())
        list_1.append(a)
        list_2.append(b)

### Q1 #####

list_1.sort()
list_2.sort()
distances = [abs(list_1[i] - list_2[i]) for i in range(len(list_1))]
total_distance = sum(distances)
print(f'Q1: The total distance between the lists is: {total_distance}')

##### Q2 #####
# Problem summary: calculate the similarity score between two lists of numbers.
# Solution idea:
# option 1: naive O(n^2) - pass with double for-loop and count everything naively (Not Implemented)
# option 2: count repetitions of numbers separately in each list, multiply (repititions in list_1 * repettions in list_2 * the value) - O(n* dictionary operations) = O(n) on average 

reps_1 = {x:0 for x in set(list_1 + list_2)} 
reps_2 = {x:0 for x in set(list_1 + list_2)} 

def count_repetitions(lst,reps):
    for x in lst:
        reps[x] += 1
    return reps

reps_1 = count_repetitions(list_1,reps_1)
reps_2 = count_repetitions(list_2, reps_2)

similarity_score = 0
for x in reps_1.keys():
    similarity_score += reps_1[x]*reps_2[x]*x

print(f'Q2: similarity_score between the lists is: {similarity_score}') 


