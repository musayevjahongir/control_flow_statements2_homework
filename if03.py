def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    d=a
    if a>b and b>c:
        d=b
    if a>c and c>b:
        d=c
    return d
print(main(3,7,1))
print(main(5,5,-1))