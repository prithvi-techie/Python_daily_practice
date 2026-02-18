#seperate each diit from the numebr and print it on the new line
a = 256
while a>0:    # let a=256 ->  256>0 (next line)
    print(a%10)   #256%10 -> 6 -> print(6)
    a = a//10    # 256//10 -> 25.6 -> 25 -> 25>0 (first line) loop start again
                 # // = floor division, neglect decimal and give only int
