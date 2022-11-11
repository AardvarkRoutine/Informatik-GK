user_in = str(input("Geben sie die zu encodierende Nachricht ein!\n"))
K = 8
chnk_len = len(user_in) // K
res = []
for idx in range(0, len(user_in), chnk_len):
    res.append(user_in[idx : idx + chnk_len])
res.reverse()
final = [x[::-1] for x in res][::-1]
print(' '.join(final))