import stripe
from django.conf import settings


class StripePayments:
    def __init__(self, api_key):
        self.api_key = settings.STRIPE_API_KEY


    def create_session(self, obj, user):
        stripe.api_key = self.api_key
        print(obj.title)
        create_product = stripe.Product.create(
            name=obj.title,
        )


        price = stripe.Price.create(
            unit_amount=int(obj.price) * 91,
            currency='rub',
            product=create_product['id'],
        )

        session = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[
                {
                    "price": price.id,
                    "quantity": 1
                }
            ],
            mode="payment",
            client_reference_id=user.id
        )
        return session

    @staticmethod
    def retrieve_session(session_id):

        stripe.api_key = settings.STRIPE_API_KEY
        get_session = stripe.checkout.Session.retrieve(session_id)
        return get_session.get('payment_status')