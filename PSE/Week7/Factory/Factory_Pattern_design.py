#In the original code, add or remove a payment method mneans 
#the need to open the code and add or remove a class in Checkout  
#that is tied to those implementations. In this code version checkout 
#abstracts any received processor, without dependending on classes.  


from abc import ABC, abstractmethod

class PaymentProcessor (ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """process the payment and return a result string (or object)"""



class PayPalPayment (PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via PayPal"

class StripePayment (PaymentProcessor):
    def process_payment(self, amount) -> str:
        return f"Processing ${amount:.2f} via Stripe"
    
class CreditCardPayment (PaymentProcessor):
    def process_payment(self, amount) -> str:
        return f"Processing ${amount:.2f} via Credit Card"
    
#Client code - tightly coupled and repetitive
"""def checkout (payment_method, amount):
    if payment_method == "paypal":
        processor = PayPalPayment() #Direct instantiation

    elif payment_method == "stripe":
        processor = StripePayment() #Direct instantiation

    elif payment_method == "credit_card":
        processor = CreditCardPayment() #Direct instantiation
    
    else:
        raise ValueError ("Unknown payment method") 

    return processor.process_payment(amount)"""

#Use Payment processor
def checkout(processor: PaymentProcessor, amount: float) -> str:
    return processor.process_payment(amount)

def get_payment_processor(method: str) -> PaymentProcessor:
    mapping = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "credit_card": CreditCardPayment,
    }
    try:
        return mapping[method.lower()]()
    except KeyError:
        raise ValueError(f"Unknown payment method: {method}")

def checkout_with_method(method: str, amount: float) -> str:
    processor = get_payment_processor(method)
    return checkout(processor, amount)


print(checkout_with_method("paypal", 20))