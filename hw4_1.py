def total_salary(path):
    employees = None
    try:
        with open(path, encoding='utf-8') as file:
            employees = file.read().split('\n')
        employees = {employee.split(",")[0] : int(employee.split(",")[1]) for employee in employees}
        sum_salary = sum(employees.values())
        return (sum_salary, sum_salary / len(employees) if len(employees) > 0 else 1)
    except FileNotFoundError:
        return None
    except ValueError:
        return None
    except IndexError:
        return None