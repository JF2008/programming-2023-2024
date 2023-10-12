# Loop practice
# 10/10/2023
# Jonathan Feng

groceries = ["hot wheels", "lego", "ice cream", "video games"]

for item in groceries:
    print(f"* {item}")
    print("  ---")


stars = ["*", "**", "***", "****", "*****"]

for row in stars:
    print(row)

#Happy new year exercise bot

import time

for i in range(10):
    print(10 - i)
    time.sleep(1)
print("happy new year!")