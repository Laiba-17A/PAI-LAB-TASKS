
class Account:
    def __init__(self):
        # Private members
        self.__acc_no = None
        self.__acc_bal = None
        self.__sec_code = None

    def set_accdetails(self,acc_no,acc_bal,sec_code):
        self.__acc_no=acc_no
        self.__acc_bal=acc_bal
        self.__sec_code=sec_code

    def print_accdetails(self):
        print("Account Number:",self.__acc_no)
        print("Account Balance:",self.__acc_bal)
        print("Security Code:",self.__sec_code)



acc=Account()
acc.set_accdetails(123456789,50000,"AB5673")
acc.print_accdetails()

