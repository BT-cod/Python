# BREAK
for i in range(11):
    print("6 X",i, "=", i*6)
    if(i == 7):
        break

# CONTINUE
for i in range(11):
    if(i == 7):
        continue
    print("6 X",i, "=", i*6)