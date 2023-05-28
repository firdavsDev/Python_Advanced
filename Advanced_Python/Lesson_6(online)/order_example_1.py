'''
About project: This is a simple example of how to use dataclasses & encapsulation  in Python.
'''


from dataclasses import dataclass, field
from enum import Enum


class PaymentStatus(Enum):
    """Bu to'lov holati"""
    CANCELLED = "cancelled"
    PENDING = "pending"
    PAID = "paid"


class PaymentStatusError(Exception):
    """Custom exception for when the payment status is invalid."""
    pass


@dataclass
class LineItem:
    """Bu buyurtma savatchamiz"""
    name: str # item nomi
    price: int # item narxi
    quantity: int # item soni

    @property
    def total_price(self) -> int:
        """Bu buyurtma savatchamizdagi barcha itemlar narxini hisoblaydi"""
        return self.price * self.quantity


@dataclass
class Order:
    """Buyurtma"""
    items: list[LineItem] = field(default_factory=list) # savatchamiz
    _payment_status: PaymentStatus = PaymentStatus.PENDING # protect variable is PENDING

    def add_item(self, item: LineItem):
        """Bu buyurtma savatchamizga item qo'shadi"""
        self.items.append(item)

    def set_payment_status(self, status: PaymentStatus) -> None:
        """Bu buyurtma holatini o'zgartiradi"""
        if self._payment_status == PaymentStatus.PAID: # agar buyurtma to'langan holatda bo'lsa
            raise PaymentStatusError(
                "You can't change the status of an already paid order."
            )
        self._payment_status = status

    @property
    def total_price(self) -> int:
        """Bu buyurtma savatchamizdagi barcha itemlar narxini hisoblaydi"""
        return sum(item.total_price for item in self.items) #sum() bu buyurtma savatchamizdagi barcha itemlar narxini hisoblaydi

if __name__ == "__main__":

    order = Order()
    order.add_item(LineItem("Apple", 10, 2)) # itemlarni savatchaga saqladik
    order.add_item(LineItem("Banana", 20, 3)) # itemlarni savatchaga saqladik
    order.add_item(LineItem("Orange", 30, 4)) # itemlarni savatchaga saqladik
    order.total_price = 200 # buyurtma narxi 200
    # print(order.total_price) # 200 # savol
    # To'lov holatini o'zgartirish
    order.set_payment_status(PaymentStatus.PAID) # buyurtmani to'langan holatga o'tkazdik
    print(order._payment_status) # paid
    # To'lov holatini o'zgartirish
    order.set_payment_status(PaymentStatus.CANCELLED) # buyurtmani bekor qilish
    print(order._payment_status) # cancelled (xatolik yuz berdi)

# Xulosalar

# _payment_status bu bizning private variable uni o'zgartirish mumkin emas va Ammo uni o'zgartirish uchun bizga set_payment_status() methodidan foydalanishimiz kerak buldi
# Pythonda private variable yaratish uchun _ ni ishlatishimiz kerak




