a = int(input("birinchi tomon: "))
b = int(input("ikkinchi tomon: "))
c = int(input("uchunchi tomon: "))

if a == b == c:
    print("teng tomonli")
elif a == b or b == c or a == c:
    print("teng yonli")
else:
    print("turli yonli")