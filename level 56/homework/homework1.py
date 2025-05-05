def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)