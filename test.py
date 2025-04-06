import ArmstrongNumber as arm
print("Armstrong number list 1 to 100000")
for i in range(1,100000):
    if arm.isArmstrong(i):
        print(i)
