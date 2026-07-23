# f"{value:flag}"

number1: int = 342
number2: float = -3415.5243
number3: float = 3.1414

# floating point precision      :.(number)f
print(f"{number1:.2f}")
print(f"{number2:.2f}")
print(f"{number3:.2f}")


# allocating space      :(number)
print(f"{number1:7}")
print(f"{number2:7}")
print(f"{number3:7}")


# allocate and zero pad that many spaces     :0(number)
print(f"{number1:07}")
print(f"{number2:07}")
print(f"{number3:07}")


# use plus sign to indicate positive value     :+
print("use plus sign to indicate positive value     :+")
print(f"{number1:+}")
print(f"{number2:+}")
print(f"{number3:+}")
