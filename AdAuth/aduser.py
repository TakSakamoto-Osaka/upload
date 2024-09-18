class AdUser:
    def __init__(
        self,
        name: str,
        display_name: str,
        company: str,
        employee_number: str,
        department: str,
        mail: str,
        employee_type: str,
        telephone_number: str,
        phonetic_name: str,
        member_of: list[str],
    ):
        self.name = name
        self.display_name = display_name
        self.company = company
        self.employee_number = employee_number
        self.department = department

        self.mail = mail
        self.employee_type = employee_type
        self.telephone_number = telephone_number
        self.phonetic_name = phonetic_name
        self.member_of = member_of

    def __str__(self):
        return (
            f"name: {self.name}\n"
            + f"display_name: {self.display_name}\n"
            + f"comnapy: {self.company}\n"
            + f"employee_number: {self.employee_number}\n"
            + f"department: {self.department}\n"
            + f"mail: {self.mail}\n"
            + f"employee_type: {self.employee_type}\n"
            + f"telephone_number: {self.telephone_number}\n"
            + f"phonetic_name: {self.phonetic_name}\n"
            + f"member_of: {self.member_of}"
        )
