def add_employee_to_company(companies, company_name, employee_id):
    if company_name not in companies:
        companies[company_name] = set()
    companies[company_name].add(employee_id)


def print_companies(companies):
    for company_name, employees in companies.items():
        print(company_name)
        for employee_id in employees:
            print(f"-- {employee_id}")


def main():
    companies = {}
    while True:
        input_data = input()
        if input_data == "End":
            break
        company_name, employee_id = input_data.split(" -> ")
        add_employee_to_company(companies, company_name, employee_id)

    print_companies(companies)


if __name__ == "__main__":
    main()