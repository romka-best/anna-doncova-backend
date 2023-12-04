from typing import Optional, Dict

from app.firebase import db
from app.models import Subscription, SubscriptionType, SubscriptionPeriod, SubscriptionStatus, Currency


async def get_subscription(subscription_id: str) -> Optional[Subscription]:
    subscription_ref = db.collection("subscriptions").document(str(subscription_id))
    subscription = await subscription_ref.get()

    if subscription.exists:
        return Subscription(**subscription.to_dict())


async def get_subscription_by_user_id(user_id: str) -> Optional[Subscription]:
    subscription_stream = db.collection("subscriptions").where("user_id", "==", user_id).limit(1).stream()
    async for doc in subscription_stream:
        return Subscription(**doc.to_dict())
    return None


async def create_subscription_object(user_id: str,
                                     type: SubscriptionType,
                                     period: SubscriptionPeriod,
                                     status: SubscriptionStatus,
                                     currency: Currency,
                                     amount: float) -> Subscription:
    subscription_ref = db.collection('subscriptions').document()
    return Subscription(
        id=subscription_ref.id,
        user_id=user_id,
        type=type,
        period=period,
        status=status,
        currency=currency,
        amount=amount
    )


async def write_subscription(user_id: str,
                             type: SubscriptionType,
                             period: SubscriptionPeriod,
                             status: SubscriptionStatus,
                             currency: Currency,
                             amount: float) -> Subscription:
    subscription = await create_subscription_object(user_id, type, period, status, currency, amount)
    await db.collection('subscriptions').document(subscription.id).set(subscription.to_dict())

    return subscription


async def update_subscription(subscription_id: str, data: Dict):
    subscription_ref = db.collection('subscriptions').document(subscription_id)
    await subscription_ref.update(data)


async def update_subscription_in_transaction(transaction, subscription_id: str, data: Dict):
    transaction.update(db.collection('subscriptions').document(subscription_id), data)