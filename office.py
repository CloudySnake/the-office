from collections import defaultdict
from typing import Set

from employee import Employee


class TheOffice:
    """A class to manage office sales & employees
    """

    def __init__(self, regional_manager: str, employees: Set[Employee], location: str):
        self.regional_manager = regional_manager
        self.employees = employees
        self.location = location
        self.sales = defaultdict(int)

    def __str__(self) -> str:
        return f"Welcome to The Office! The boss here is {self.regional_manager}."

    def record_sale(self, employee: Employee) -> None:
        """Record a sale for an employee.

        Args:
            employee (Employee): The employee who made the sale.

        Returns:
            None
        """
        self.sales[employee] += 1

    def get_employee_sales(self, employee: Employee) -> int:
        """Return the number of sales an employee has made.

        Args:
            employee (Employee): The employee whose sales numbers we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        return self.sales[employee]

    def _fire_employee(self, employee: Employee) -> None:
        """Fire an employee.

        Args:
            employee (Employee): The employee to fire.

        Returns:
            None
        """
        self.employees.remove(employee)
