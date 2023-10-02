def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    x2=n//10%10
    x3=n//100%10
    x4=n//1000%10
    x5=n//10000
    a=x1
    if x2>a:
        a=x2
        d=2
    if x3>a:
        a=x3
        d=3
    if x4>a:
        a=x4
        d=4
    if x5>a:
        a=x5
        d=5
    return d
print(main(76514))
print(main(54694))