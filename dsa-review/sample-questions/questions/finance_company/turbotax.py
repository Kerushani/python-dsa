"""
Prompt:
Design an object-oriented system to support a simplified online tax filing application. The system should allow users to:

Create an account and manage their tax profiles.

Add different types of income (e.g., employment, investments).

Add deductions (e.g., education, medical expenses).

Automatically calculate estimated taxes owed or refund.

Export or submit their return.

Follow-up Requirements:

How would you handle different income types using inheritance or composition?

How would you separate the calculation logic from the data models?

How would you structure the system to support future addition of new income or deduction types?

How would you support saving draft returns or submitting final versions?
"""

"""
Notes:
"""
import enum
from typing import List, Tuple, Dict

"""
Total_Income:
    Variables: total_income
    method:
        calculate_total_income
"""
class TotalIncome():
    def __init__(self, income_sources: List[Dict]):
        self.income_sources=income_sources
        self.total_income = 0
    def get_total_income(self) -> float:
        return self.total_income 
    def caclulate_total_income(self) -> float:
        for income_source in self.income_sources:
            self.total_income += income_source["amount"]
            return self.get_total_income()
    

"""
Total_Deductions:
    Variables: total_deduction
    Methods: 
        calculate_total_deduction
----
"""
class TotalDeductions():
    def __init__(self, deduction_sources:List[Dict]):
        self.total_deductions = 0
        self.deduction_sources = deduction_sources
    def get_total_deductions(self) -> float:
        return self.total_deductions
    def caclulate_total_deductions(self) -> float:
        for deduction_source in self.deduction_sources:
            self.total_deductions += deduction_source["amount"]
            return self.get_total_deductions()
"""
TaxCalculation():
    variable: total_tax_return
    method:
        calculate_tax_return()
"""
class TaxCalculation():
    def __init__(self):
        self.total_tax_return =0
    def get_tax_return(self) -> float:
        return self.total_tax_return
    def calculate_taxable_income(self, total_income: float, total_deduction: float) -> float:
        self.total_tax_return = total_income - total_deduction
        return self.total_tax_return
        

"""
Account():
    varibles: name, email, tax_profile
    method:
        display_tax_return()
"""
class Account():
    def __init__(self, name: str, email: str):
        self.name = name
        self.email =email
        self.tax_return_amount = 0
    def get_tax_return_amount(self) -> float:
        return self.tax_return_amount
    def display_tax_return(self, tax_calculation) -> float:
        self.tax_return_amount = tax_calculation
        return self.tax_return_amount


user_data = {
    "user_id": "U123",
    "name": "Kerushani Sivaneswaran",
    "email": "keru@example.com",
    "tax_profile": {
        "profile_id": "TP2024",
        "filing_year": 2024,
        "income_sources": [
            {
                "income_id": "I001",
                "type": "employment",
                "amount": 72000.0,
                "details": {
                    "employer_name": "ABC Corp",
                    "position": "Software Engineer",
                    "monthly_salary": 6000
                }
            },
            {
                "income_id": "I002",
                "type": "investment",
                "amount": 1200.0,
                "details": {
                    "source": "Stocks",
                    "broker": "Wealthsimple",
                    "gains": 1200
                }
            }
        ],
        "deductions": [
            {
                "deduction_id": "D001",
                "category": "education",
                "description": "Tuition fees",
                "amount": 3000.0
            },
            {
                "deduction_id": "D002",
                "category": "donation",
                "description": "Red Cross donation",
                "amount": 500.0
            }
        ],
        "status": "draft",
        "total_income": 73200.0,
        "total_deductions": 3500.0,
        "tax_owed": 9500.0
    }
}

tax_return = {
    "return_id": "TRX2024",
    "user_id": "U123",
    "tax_profile": user_data["tax_profile"],
    "submitted_date": "2025-04-20",
    "refund_amount": 0.0,
    "tax_owed": 9500.0
}

class Demo():
    def run(self):
        account = Account(user_data["name"], user_data["email"])
        tax_calculation = TaxCalculation()
        total_income_obj = TotalIncome(user_data["tax_profile"]["income_sources"])
        total_deductions_obj = TotalDeductions(user_data["tax_profile"]["deductions"])
        total_deductions = total_deductions_obj.caclulate_total_deductions()
        total_income = total_income_obj.caclulate_total_income()
        tax_calculated = tax_calculation.calculate_taxable_income(total_income, total_deductions)

        print(account.display_tax_return(tax_calculated))

demo = Demo()
demo.run()