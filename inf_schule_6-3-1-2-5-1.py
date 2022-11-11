user_in = str(input("Bitte geben sie die zu reversierende Geheimnachricht ein!\n"))
input_list = user_in.split()
input_list.reverse()
rev_list = [x[::-1] for x in input_list][::-1]
out = ' '.join(rev_list)
print(out)