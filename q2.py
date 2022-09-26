

def salesman_info(sales_per_week):
    salesman_count = len(sales_per_week)
    total_monthly_sales = [4*x for x in sales_per_week]
    commissions = [0.05*x if x > 5000 else 0 for x in total_monthly_sales]
    remarks = []

    for sale in total_monthly_sales:
        if sale >= 80000:
            remarks.append("Excellent")
        elif sale < 80000 and sale >= 60000:
            remarks.append("Good")
        elif sale < 60000 and sale >= 40000:
            remarks.append("Average")
        else:
            remarks.append("Work Hard")

    print(f"Total Monthly Sales : {total_monthly_sales}")
    print(f"Commission : {commissions}")
    print(f"Remarks : {remarks}")


salesman_info([5000, 1000, 50700])
