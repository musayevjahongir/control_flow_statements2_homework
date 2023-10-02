def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    d=a
    if a<b:
        d=b
    if a==b:
        d=0
    return d 
print(main(3,7))
print(main(5,5))