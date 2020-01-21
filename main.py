import json
from calendar import monthrange

INDEXOF2020=838
with open('./382000000A-000077-002') as json_file:
    date_records = json.load(json_file)['result']['records']

def main():
    price = 0
    while True:
        text = input("輸入單程票價: ")
        try:
            price = int(text)

            for x in range(2,13):
                workdays = get_workdays(2020,x)
                print(f"{x}月份工作日：{workdays}天，乘車{workdays*2}次")
                if workdays*2 >= 11 and workdays*2 <= 20: #10%
                    print("符合9折優惠")
                    print(which_cheaper(price, workdays, 0.9))
                    # print(f"{workdays*2}次 * {price}元 * 90% = {workdays*2*price*0.9}")
                elif workdays*2 >= 21 and workdays*2 <= 30: #15%
                    print("符合85折優惠")
                    print(which_cheaper(price, workdays, 0.85))
                    # print(f"{workdays*2}次 * {price}元 * 85% = {workdays*2*price*0.85}")
                elif workdays*2 >= 31 and workdays*2 <= 40: #20%
                    print("符合8折優惠")
                    print(which_cheaper(price, workdays, 0.8))
                    # print(f"{workdays*2}次 * {price}元 * 80% = {workdays*2*price*0.8}")
                elif workdays*2 >= 41 and workdays*2 <= 50: #25%
                    print("符合75折優惠")
                    print(which_cheaper(price, workdays, 0.75))
                    # print(f"{workdays*2}次 * {price}元 * 75% = {workdays*2*price*0.75}")
                elif workdays*2 > 51: #30%
                    print("符合7折優惠")
                    print(which_cheaper(price, workdays, 0.7))
                    # print(f"{workdays*2}次 * {price}元 * 70% = {workdays*2*price*0.7}")
                else: #0%
                    print(which_cheaper(price, workdays, 1))
                    # print(f"{workdays*2}次 * {price}元 = {workdays*2*price}")
            break
        except ValueError:    
            print("請輸入數字")

        
def get_workdays(year, month, ):
    current_month_records = []
    for x in range(INDEXOF2020,len(date_records)-1):
        record = date_records[x]
        if f"{year}/{month}/" in record['date']:
            current_month_records.append(record)
    return monthrange(year, month)[1]-len(current_month_records)

def which_cheaper(price, workdays, discount):
    if workdays*2*price*discount >= 1280:
        return f"---------- 買 1280 ----------"
    else:
        return f"----------  儲值{workdays*2*price}元，回饋{int(workdays*2*price*(1-discount))} = {workdays*2*price*discount} ----------"


if __name__ == "__main__":
    main()