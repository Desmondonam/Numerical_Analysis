# successive over-relaxation (SOR)

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda u1, u2, u3, u4, u5, u6: (u2 - 0.5*u6 + 2.5)/3
f2 = lambda u1, u2, u3, u4, u5, u6: ( u1 + u3 - 0.5*u5 + 1.5)/3
f3 = lambda u1, u2, u3, u4, u5, u6: (u2 + u4 + 1)/3
f4 = lambda u1, u2, u3, u4, u5, u6: (u3 + 0.5*u5 + 1)/3
f5 = lambda u1, u2, u3, u4, u5, u6: (u4 - 0.5*u2 +u6 + 1.5)/3
f6 = lambda u1, u2, u3, u4, u5, u6: (u5 - 0.5*u1 + 2.5)/3

# Initial setup
u1_0 = 0
u2_0 = 0
u3_0 = 0
u4_0 = 0
u5_0 = 0
u6_0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Reading relaxation factor
w = float(input("Enter relaxation factor: "))

# Implementation of successive over-relaxation
print('\n Count\t u1\t u2\t u3\t u4\t u5\t u6\t\n')

condition = True

while condition:
    u1_1 = (1-w) * u1_0 + w * f1(u1_0,u2_0,u3_0,u4_0,u5_0,u6_0)
    u2_1 = (1-w) * u2_0 + w * f2(u1_1,u2_0,u3_0,u4_0,u5_0,u6_0)
    u3_1 = (1-w) * u3_0 + w * f3(u1_1,u2_1,u3_0,u4_0,u5_0,u6_0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, u1_1,u2_1,u3_1))
    e1 = abs(u1_0-u1_0);
    e2 = abs(u2_0-u2_1);
    e3 = abs(u3_0-u3_1);
    
    count += 1
    u1_0 = u1_1
    u2_0 = u2_1
    u3_0 = u3_1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x = %0.3f, y = %0.3f and z = %0.3f\n'% (u1_1,u2_1,u3_1))