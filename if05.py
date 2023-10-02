def main(n):
    """
    Find the largest digit of the five-digit number.
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
    if x3>a:
        a=x3
    if x4>a:
        a=x4
    if x5>a:
        a=x5
    return a
print(main(23546))
print(main(17921))