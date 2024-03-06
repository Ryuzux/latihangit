def kaprekarNumbers(p, q):
    kaprekar_list = []

    while p <= q:
        str_kap = list(str(p * p))
        length = len(str_kap)
        
        if length > 0:
            bagian1 = int(''.join(str_kap[:length//2])) if length > 1 else 0
            bagian2 = int(''.join(str_kap[length//2:])) if length > 1 else int(str_kap[0])

            if bagian1 + bagian2 == p:
                kaprekar_list.append(p)

        p += 1
    if kaprekar_list:
        hasil_string = ' '.join(map(str, kaprekar_list))
        print(hasil_string)
    else:
        print("INVALID RANGE")

print(kaprekarNumbers(1, 100))
