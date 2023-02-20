# n = 10

# for row in range(n):
# 	for col in range (n):
# 		if row+col < n:
# 			print('', end=" ")
# 		else:
# 			print("#", end = ' ')
# 	print('#')


###2 WAYS OF WRITING LOOPS AND RUNNING PROGRAMS -- one by using mains and functions and another by just writing code.

def ricky(n):
	for row in range(n):
		print((''*(n + row))+
		('#'*row) + '##')

if __name__ == '__main__':
	ricky(10)