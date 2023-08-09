## def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# value = input("값 : ")
# n = int(input("값 : "))

# print_n_times(value, n)

## def print_n_time(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print(" ")
# print_n_time(10, "안녕", "하세요", "잘자")

def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕")