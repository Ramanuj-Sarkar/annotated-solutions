def mix(s1, s2):
    def make_dict(s):
        s_dict = {}
        for x in s:
            if ord('a') <= ord(x) <= ord('z'):
                if x not in s_dict:
                    s_dict[x] = 0
                s_dict[x] += 1
        return {k:v for k,v in s_dict.items() if v > 1}
    
    raw_list = []
    d1, d2 = make_dict(s1), make_dict(s2)
    outorder = ['1','2','=']
    
    for letter in d1:
        if letter not in d2 or d1[letter] > d2[letter]:
            raw_list.append(('1',letter,d1[letter]))
        elif d1[letter] < d2[letter]:
            raw_list.append(('2',letter,d2[letter]))
        else:
            raw_list.append(('=',letter,d1[letter]))

    for letter in d2:
        if letter not in d1:
            raw_list.append(('2',letter,d2[letter]))

    return '/'.join(['{}:{}'.format(x[0],x[1]*x[2]) for x in sorted(raw_list,
                                                            key=(lambda x: (x[2] * -1, outorder.index(x[0]) ,x[1])))])
