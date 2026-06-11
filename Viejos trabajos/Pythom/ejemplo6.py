variable_1=1
variable_2=2

auxiliary=variable_1
variable_1=variable_2
variable_2=auxiliary

variable_1=1
variable_2=2



for i in range(length//2):
    my_list[i],my_list[length-i-1]=my_list[length-i-1],my_list[i]
print(my_list)