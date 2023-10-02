def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    d=a
    if b>d:
        d=b
    if c>d:
        d=c
    return d
print(main(1,4,2))
print(main(-5,-4,-2))