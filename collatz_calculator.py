c0 = int(input("Please give me a number greater than zero:  "))
count = 0
print(c0)

while c0 != 1:
    count += 1
    if c0 % 2 == 0:
        c0 = c0 / 2
        print("Divided by 2:   ",int(c0))
    else:    
        c0 = 3 * c0 +1 
        print("Times 3 plus 1: ", int(c0))
        
print("We made it! ",int(c0))
print("# of Steps:  ", count)