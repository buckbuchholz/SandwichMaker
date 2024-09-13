class SandwichMachine:
    def __init__(self, machine_resources):
        """Initialize machine resources."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True if the order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = large_dollars * 1.0 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Returns True when payment is accepted, or False if money is insufficient."""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Exact amount. No change required.")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")


def main():
    resources = {
        "bread": 12,
        "ham": 18,
        "cheese": 24
    }

    recipes = {
        "small": {
            "ingredients": {
                "bread": 2,
                "ham": 4,
                "cheese": 4
            },
            "cost": 1.75,
        },
        "medium": {
            "ingredients": {
                "bread": 4,
                "ham": 6,
                "cheese": 8
            },
            "cost": 3.25,
        },
        "large": {
            "ingredients": {
                "bread": 6,
                "ham": 8,
                "cheese": 12
            },
            "cost": 5.50,
        }
    }

    machine = SandwichMachine(resources)

    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")
        elif choice in recipes:
            if machine.check_resources(recipes[choice]["ingredients"]):
                coins = machine.process_coins()
                if machine.transaction_result(coins, recipes[choice]["cost"]):
                    machine.make_sandwich(choice, recipes[choice]["ingredients"])
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
