class PayPalPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class StripePayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"
    
class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
#Client code - tightly coupled and repetitive
def checkout (payment_method, amount):
    if payment_method == "paypal":
        processor = PayPalPayment() #Direct instantiation

    elif payment_method == "stripe":
        processor = StripePayment() #Direct instantiation

    elif payment_method == "credit_card":
        processor = CreditCardPayment() #Direct instantiation
    
    else:
        raise ValueError ("Unknown payment method") 

    return processor.process_payment(amount)