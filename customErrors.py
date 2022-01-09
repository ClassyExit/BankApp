# Custom Error Classes


class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""

    # Deposit request is < 0
    def Err_01(self):
        print("Request must be greater than 0!")


class ValueTooBigError(Exception):
    """Raised when the input value is too big"""

    # Withdrawl exceeds balance
    def Err_01(self):
        print("Your request exceeds your available balance!")
