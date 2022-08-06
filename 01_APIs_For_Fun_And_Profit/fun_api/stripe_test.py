import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

charges = stripe.Charge.list(limit=3)

print(charges)