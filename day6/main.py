"""
n = 16
1 16
2 8
4 4

n = 28
a b
1 28
2 14
4 7
6
28
a*b = n
a <= b
a^2 <= axb = n
1 <= a <= sqrt(n)
"""
##
n = 28

t = 1

for i in range(2, int(n ** .5) + 1):
	if n % i == 0:
		t += i
		if i * i != n:
			t += n // i

print(t)

##
import sys

a, b, c = map(int, sys.stdin.readline().split())

sys.stdout.write(str(a + b + c) + "\n")

##
import sys

sys.set_int_max_str_digits(2147483647)
n = int(sys.stdin.readline())

t = 1

for i in range(2, n + 1):
	t *= i
sys.stdout.write(str(t))

##
"""
a = 1
b = 10

3 9
3

a = 1
b = 4
3
1


a = 4
b = 20
6 18
5
1 b=20
3 6 9 12 15 18 - 6
1 a-1=3
3 - 1

1 -> 20 6
20 // 3 = 6

1 -> 3
3 // 3 = 1
"""
import sys

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(str(b // 3 - (a - 1) // 3))

##
"""
a = 1
b = 11
2 4 6 8 10 - 30
2 10
5
start = a + a%2
end = b - b%2
2 4 6
2 6
3
n = (end - start)//2 + 1
n * (2*start + (n-1)*2)//2
5 * (2*2 + (5-1)*2)//2 = 30
"""
import sys

a, b = map(int, sys.stdin.readline().split())
start = a + a % 2
end = b - b % 2
n = (end - start) // 2 + 1
tong = n * (2 * start + (n - 1) * 2) // 2
sys.stdout.write(str(tong))

##
"""
n = 5
1 2 3 4 5
3
9

n = 10
5 25
"""
