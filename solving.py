# X= int(input())
# if (1<=X<=31):
#     if(X==25):
#         print("CHRISTMAS")
#     else:
#        print("ORDINARY")

# def max_sum_of_two_distinct_numbers(test_cases):
#     results = []
#     for case in test_cases:
#         n, arr = case
#         # Use set to get distinct integers
#         distinct_nums = list(set(arr))
#         # Sort in descending order
#         distinct_nums.sort(reverse=True)
#         # Sum the two largest distinct numbers
#         max_sum = distinct_nums[0] + distinct_nums[1]
#         results.append(max_sum)
#     return results

# T = int(input())
# test_cases = []
#
# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     test_cases.append((N, A))
#
# results = max_sum_of_two_distinct_numbers(test_cases)
# for res in results:
#     print(res)

# n = int(input())
# if (n%2!=0):
#     print("Weird")
# elif (n%2==0 and n>=2 and n<=5):
#     print("Not Weird")
# elif (n%2==0 and n>=6 and n<=20):
#     print("Weird")
# elif (n%2==0 and n>20):
#     print("Not Weird")

# a = int(input())
# b = int(input())
# solveMeFirst = a+b
# print(solveMeFirst)

# n = int(input())
# for i in range(1,n+1):
#     print(i,end='')

# def is_leap(year):
#     if (year % 400 == 0):
#         return True
#     elif (year % 100 == 0):
#         return False
#     elif (year % 4 == 0):
#         return True
#     else:
#         return False

# def max_mangoes(X,Y,Z):
#     if(Y>=Z):
#         return 0
#     return (Z-Y)//X

# T = int(input())
# for i in range(T):
#  N = int(input())
#  if (N%3==0):
#     print("YES")
#  else:
#     print("NO")

n = int(input())         # Way Too Long Words
for i in range(n):
    word = input()
    if (len(word)>10):
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)

w = int(input())
if (w>2 and w%2==0):    #Watermelon
 print("YES")
else:
 print("NO")

























