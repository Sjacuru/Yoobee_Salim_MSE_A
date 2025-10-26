from abc import ABC, abstractmethod

# 1. Abstract Product (Payment Method)
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Execute the payment. Must be implemented by all concrete payment methods."""
        pass

# 2. Concrete Products (Various Payment Methods)
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount} via Credit Card."

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount} via PayPal."

class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount} via Bank Transfer."

class CryptoPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount} via Crypto."

class GooglePayPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount} via Google Pay."

# 3. Factory (Creates Payment Method Objects)
class PaymentFactory:
    # Registry of available payment methods
    _registry = {
        "credit_card": CreditCardPayment,
        "paypal": PayPalPayment,
        "bank_transfer": BankTransferPayment,
        "crypto": CryptoPayment,
        "google_pay": GooglePayPayment,
    }

    @classmethod
    def create_payment_method(cls, method_type: str) -> PaymentMethod:
        """Factory method to create a payment method instance dynamically."""
        payment_class = cls._registry.get(method_type.lower())
        if not payment_class:
            raise ValueError(f"Unknown payment method: {method_type}. Available: {list(cls._registry.keys())}")
        return payment_class()

# 4. Singleton (The Main Payment Gateway)
class PaymentGateway:
    _instance = None

    def __new__(cls):
        """Ensures only one instance of the PaymentGateway is created."""
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
            # Any initialization can be done here
        return cls._instance

    def process_payment(self, amount: float, method_type: str) -> str:
        """The main entry point to process any payment."""
        # Use the Factory to get the correct payment method object
        payment_method = PaymentFactory.create_payment_method(method_type)
        # Delegate the processing to the specific payment method
        result = payment_method.process_payment(amount)
        return result

# 5. Client Code & Testing
def main():
    # Test the Singleton behavior
    gateway1 = PaymentGateway()
    gateway2 = PaymentGateway()
    
    print(f"Are gateways the same instance? {gateway1 is gateway2}")  # Should print: True

    # Test processing payments with different methods
    test_amount = 100.50
    methods_to_test = ["credit_card", "paypal", "bank_transfer", "crypto", "google_pay"]

    for method in methods_to_test:
        try:
            result = gateway1.process_payment(test_amount, method)
            print(f"SUCCESS: {result}")
        except ValueError as e:
            print(f"ERROR with '{method}': {e}")

    # Test error handling for an unknown method
    try:
        gateway1.process_payment(test_amount, "unknown_method")
    except ValueError as e:
        print(f"EXPECTED ERROR: {e}")

if __name__ == "__main__":
    main()