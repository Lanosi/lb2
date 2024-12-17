class Main:
    def __init__(self, hours_work, cost_hour):
        self.hours_work = hours_work
        self.cost_hour = cost_hour

    def __str__(self):
        return (f"Количество часов работы: {self.hours_work}\n"
                f"Тариф оплаты за час: {self.cost_hour}")

    def Total_cost_of_work(self, hours_work, cost_hour):
        finally_cost = hours_work * cost_hour
        print(finally_cost)

Total_cost = Main(24, 100)
print(Total_cost)
Total_cost.Total_cost_of_work(24,100)
