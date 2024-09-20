import re

def add_strings(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    num1 = num1.zfill(len(num2))
    result, carry = "", 0
    
    for i in range(len(num2) - 1, -1, -1):
        total = int(num1[i]) + int(num2[i]) + carry
        result = str(total % 10) + result
        carry = total // 10
    
    if carry:
        result = str(carry) + result
    return result

def subtract_strings(num1, num2):
    result, carry = "", 0
    num1 = num1.zfill(len(num2))
    
    for i in range(len(num2) - 1, -1, -1):
        sub = int(num1[i]) - int(num2[i]) - carry
        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0
        result = str(sub) + result
        
    return result

def remove_leading_zeros(s):
    return re.sub(r"^0+(?!$)", "", s)

def karatsuba_multiply(X, Y):
    max_len = max(len(X), len(Y))
    X = X.zfill(max_len)
    Y = Y.zfill(max_len)
    half_len = max_len // 2
    result = "0"

    while max_len > 0:
        if max_len < 10:
            return str(int(X) * int(Y))

        Xl = X[:-half_len]
        Xr = X[-half_len:]
        Yl = Y[:-half_len]
        Yr = Y[-half_len:]

        P = str(int(Xl) * int(Yl))
        Q = str(int(Xr) * int(Yr))
        R = str(int(add_strings(Xl, Xr)) * int(add_strings(Yl, Yr)))

        result = add_strings(add_strings(P + '0' * (2 * (max_len - half_len)), subtract_strings(R, add_strings(P, Q)) + '0' * (max_len - half_len)), Q)
        
        break

    return result

if __name__ == "__main__":
    A = "14568862"
    B = "6533624"
    
    print("Результат умножения {} и {}: {}".format(A, B, karatsuba_multiply(A, B)))