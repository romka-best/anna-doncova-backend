import re
from datetime import datetime, timezone

from app.models.common import Currency


class PackageType:
    GPT3 = "GPT3"
    GPT4 = "GPT4"
    CHAT = "CHAT"
    DALLE3 = "DALLE3"
    FACE_SWAP = "FACE_SWAP"
    ACCESS_TO_CATALOG = "ACCESS_TO_CATALOG"
    VOICE_MESSAGES = "VOICE_MESSAGES"
    FAST_MESSAGES = "FAST_MESSAGES"


class PackageStatus:
    SUCCESS = 'SUCCESS'
    WAITING = 'WAITING'
    ERROR = 'ERROR'


class Package:
    id: str
    user_id: str
    status: PackageStatus
    type: PackageType
    currency: Currency
    amount: float
    quantity: int
    provider_payment_charge_id: str
    created_at: datetime
    edited_at: datetime

    def __init__(self,
                 id: str,
                 user_id: str,
                 type: PackageType,
                 status: PackageStatus,
                 currency: Currency,
                 amount: float,
                 quantity: int,
                 provider_payment_charge_id="",
                 created_at=None,
                 edited_at=None):
        self.id = id
        self.user_id = user_id
        self.type = type
        self.status = status
        self.currency = currency
        self.amount = amount
        self.quantity = quantity
        self.provider_payment_charge_id = provider_payment_charge_id

        current_time = datetime.now(timezone.utc)
        self.created_at = created_at if created_at is not None else current_time
        self.edited_at = edited_at if edited_at is not None else current_time

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'type': self.type,
            'status': self.status,
            'currency': self.currency,
            'amount': self.amount,
            'quantity': self.quantity,
            'provider_payment_charge_id': self.provider_payment_charge_id,
            'created_at': self.created_at,
            'edited_at': self.edited_at
        }

    @staticmethod
    def get_prices(currency: Currency):
        prices = {
            PackageType.GPT3: '',
            PackageType.GPT4: '',
            PackageType.CHAT: '',
            PackageType.DALLE3: '',
            PackageType.FACE_SWAP: '',
            PackageType.ACCESS_TO_CATALOG: '',
            PackageType.VOICE_MESSAGES: '',
            PackageType.FAST_MESSAGES: '',
        }

        if currency == Currency.RUB:
            prices[PackageType.GPT3] = '1₽'
            prices[PackageType.GPT4] = '10₽'
            prices[PackageType.CHAT] = '100₽'
            prices[PackageType.DALLE3] = '10₽'
            prices[PackageType.FACE_SWAP] = '15₽'
            prices[PackageType.ACCESS_TO_CATALOG] = '1 000₽'
            prices[PackageType.VOICE_MESSAGES] = '2 500₽'
            prices[PackageType.FAST_MESSAGES] = '2 000₽'
        elif currency == Currency.EUR:
            prices[PackageType.GPT3] = '0.01€'
            prices[PackageType.GPT4] = '0.1€'
            prices[PackageType.CHAT] = '1€'
            prices[PackageType.DALLE3] = '0.1€'
            prices[PackageType.FACE_SWAP] = '0.15€'
            prices[PackageType.ACCESS_TO_CATALOG] = '10€'
            prices[PackageType.VOICE_MESSAGES] = '25€'
            prices[PackageType.FAST_MESSAGES] = '20€'
        else:
            prices[PackageType.GPT3] = '$0.01'
            prices[PackageType.GPT4] = '$0.1'
            prices[PackageType.CHAT] = '$1'
            prices[PackageType.DALLE3] = '$0.1'
            prices[PackageType.FACE_SWAP] = '$0.15'
            prices[PackageType.ACCESS_TO_CATALOG] = '$10'
            prices[PackageType.VOICE_MESSAGES] = '$25'
            prices[PackageType.FAST_MESSAGES] = '$20'

        return prices

    @staticmethod
    def get_price(currency: Currency, package_type: PackageType, quantity: int):
        prices = Package.get_prices(currency)
        price_raw = prices[package_type]
        price_clear = re.sub(r'[^\d.]', '', price_raw)
        price = float(price_clear) if '.' in price_clear else int(price_clear)

        return int(quantity * price)