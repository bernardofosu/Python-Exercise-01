bills = [22, 295, 176, 37, 105, 10, 1100, 86, 52]

tips: list = []
totals: list = []

def calc_tip(bills):
    for bill in bills:
        # print(bill)
        if (bill > 50 and bill < 300):
            tip = bill * 0.15
            tips.append(tip)
            totals.append(tip + bill)
        elif (bill >= 300):
            tip = bill * 0.20
            tips.append(tip)
            totals.append(tip + bill)
        else:
            tip = 0
            tips.append(tip)
            totals.append(tip + bill)

calc_tip(bills)
print("Tips: ", tips)
print("Ini Bills: ", bills)
print("Totals Bills: ", totals)
print(calc_tip(bills))

def sum_num(bills):
    sum1 = 0
    for i in bills:
        sum1 +=i
    return sum1 / len(bills)
print(sum_num(bills))

def sum_num(tips):
    sum1 = 0
    for i in tips:
        sum1 +=i
    return sum1 / len(tips)

print(sum_num(tips))