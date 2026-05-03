class UPI:
    def pay(self,**kwargs):
        return f"paid ₹{kwargs['amount']} using UPI {kwargs['upi_id']}"
class card:
    def pay(self,**kwargs):
        return f"paid ₹{kwargs['amount']} using Card {kwargs['card_no']}"
class wallet:
    def pay(self,**kwargs):
        return f"paid ₹{kwargs['amount']} using Wallet {kwargs['wallet_id']}"

payments=[UPI(),card(),wallet()]
print(payments[0].pay(amount=500, upi_id="akash@oksbi"))
print(payments[1].pay(amount=1000, card_no="1234XXXX"))
print(payments[2].pay(amount=200, wallet_id="PAYTM123"))
