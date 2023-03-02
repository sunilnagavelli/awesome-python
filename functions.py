"""
FUNCTIONS
"""

RATE_DOLLAR_PER_HOUR = 60
TOTAL_HOURS = 176

def monthly_pay():
    """
    FUNC 01
    """
    print(f"Monthly Payout for {TOTAL_HOURS}: ${RATE_DOLLAR_PER_HOUR * TOTAL_HOURS} ")

monthly_pay()

def monthly_pay_dyna(hours):
    """
    FUNC 02
    """
    print(f"Monthly Payout for {hours}: ${RATE_DOLLAR_PER_HOUR * hours} ")

monthly_pay_dyna(160)


def monthly_pay_with_days(days):
    """
    FUNC 03
    """
    hours = days * 8
    print(f"Monthly Payout for {hours} hours i.e {days} days: ${RATE_DOLLAR_PER_HOUR * hours} ")

monthly_pay_with_days(30)

monthly_pay_with_days(22)

