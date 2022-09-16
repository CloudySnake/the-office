import uuid

JOB_TITLES = ["SALES_REP", "REGIONAL_MANAGER", "MANAGER", "HR", "ACCOUNTING"]


class Employee:
    """
    Employee class for maintaining employee information.
    """
    def __init__(self, name: str, job_title: str):
        self.name = name
        self.job_title = job_title
        self.employee_id = uuid.uuid4()

    def update_contact_info(self, name: str) -> str:
        """
        Update the employee's contact info.
        Args:
            name (str): The employee's new name.

        Returns:
            str: The employee's previous name
        """
        past_name = self.name
        self.name = name
        return past_name

    def promote_employee(self, job_title: str) -> None:
        """
        Promote an employee to a new job title.
        Args:
            job_title (str): The employee's new job title.

        Returns:
            None
        """
        if job_title not in JOB_TITLES:
            raise ValueError(
                f"Invalid job title {job_title}, expected one of {JOB_TITLES}"
            )
        self.job_title = job_title
