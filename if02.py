def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    d=a
    if d>b:
        d=b
    if d>c:
        d=c
    return d
print(main(1,4,2))
print(main(-5,-3,-1))