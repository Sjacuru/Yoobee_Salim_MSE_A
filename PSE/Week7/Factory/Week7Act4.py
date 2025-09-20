#Week 7 - Activity 4: Singeleton and  Factory design pattern (due date 25 Sep 2025 )

#Develop a code to show the usage of both design patterns in your coding for; Design
# a payment processing system that supports multiple payment methods (e.g., Creditcard,
# PayPal, Bank Transfer, CryptoPayment, GooglePay).

# 1 - Use the Factory Design Pattern to create different payment method objects dynamically.
# 2 - Ensure the payment gateway (the main entry point for processing payments) is implemented
# as a Singleton, so only one instance of the gateway exists in the system.

#Explain your design choices and share your GitHub with code implementation.

from abc import ABC, abstractmethod

# 1) Abstract Product
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Execute the payment."""
        pass

# 2) Concrete Products
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"PayPal payment ${amount}"

class StripePayment(PaymentMethod):
    def process_payment(self, amount) -> str:
        return f"Stripe payment ${amount}"

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount) -> str:
        return f"Credit Card payment ${amount}"

# 3) Factory
class PaymentFactory:
    _registry = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "credit_card": CreditCardPayment, 
    }

    @classmethod
    def create_payment_method(cls, method_type: str) -> PaymentMethod:
        payment_cls = cls._registry.get(method_type.lower())
        if payment_cls is None:
            raise ValueError(f"Unknown method type: {method_type!r}. "
                             f"Available: {list(cls._registry.keys())}")
        return payment_cls()


class PaymentGateway:
    _instance = None

    def __new__(cls):
        """It creates one instance of the PaymentGateway."""
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process_payment(self, amount: float, method_type: str) -> str:
        """Process any payment."""
        # Use  Factory to get the correct payment method object
        payment_method = PaymentFactory.create_payment_method(method_type)
        # Delegate the processing to the specific payment method
        result = payment_method.process_payment(amount)
        return result
    
# 4) Client code (examples)
def main():
    factory = PaymentFactory()

    paypal = factory.create_payment_method("paypal")
    print(paypal.process_payment(200.0))  

    stripe = factory.create_payment_method("stripe")
    print(stripe.process_payment(100.0))  

    credit_card = factory.create_payment_method("credit_card")
    print(credit_card.process_payment(300.0))  

    gateway = PaymentGateway()

    test_amount = 200.9

    test_method = ["paypal", "stripe", "credit_card"]

    for method in test_method:
        result = gateway.process_payment(test_amount, method)
        print("result is ",result)
    
                
if __name__ == "__main__":
    main()
