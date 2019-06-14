total_number_of_blocks = int(input("Enter the number of blocks: "))
blocks_in_current_row = 0
height = 0
i = 0

	
while i < total_number_of_blocks:
    blocks_in_current_row += 1
    if blocks_in_current_row == height + 1:
        height += 1
        print('{:^120}'.format("|BLOCK|" * blocks_in_current_row))
        blocks_in_current_row = 0
    i+=1

print('\n')
print("The height of the pyramid:", height)
print('\n')
print("Remaining Blocks:")    
print("|BLOCK|" * blocks_in_current_row)