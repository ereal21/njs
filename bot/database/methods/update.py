import datetime

from bot.database.models import (
    User,
    ItemValues,
    Goods,
    Categories,
    PromoCode,
    StockNotification,
    ResellerPrice,
)
from bot.database import Database


def set_role(telegram_id: str, role: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(
        values={User.role_id: role})
    Database().session.commit()


def update_balance(telegram_id: int | str, summ: int) -> None:
    old_balance = User.balance
    new_balance = old_balance + summ
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(
        values={User.balance: new_balance})
    Database().session.commit()


def update_user_language(telegram_id: int, language: str) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(
        values={User.language: language})
    Database().session.commit()


def update_lottery_tickets(telegram_id: int, delta: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(
        values={User.lottery_tickets: User.lottery_tickets + delta}, synchronize_session=False)
    Database().session.commit()


def reset_lottery_tickets() -> None:
    Database().session.query(User).update({User.lottery_tickets: 0})
    Database().session.commit()


def buy_item_for_balance(telegram_id: str, summ: int) -> int:
    old_balance = User.balance
    new_balance = old_balance - summ
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(
        values={User.balance: new_balance})
    Database().session.commit()
    return Database().session.query(User.balance).filter(User.telegram_id == telegram_id).one()[0]


def update_item(item_name: str, new_name: str, new_description: str, new_price: int,
                new_category_name: str, new_delivery_description: str | None) -> None:
    Database().session.query(ItemValues).filter(ItemValues.item_name == item_name).update(
        values={ItemValues.item_name: new_name}
    )
    Database().session.query(Goods).filter(Goods.name == item_name).update(
        values={Goods.name: new_name,
                Goods.description: new_description,
                Goods.price: new_price,
                Goods.category_name: new_category_name,
                Goods.delivery_description: new_delivery_description}
    )
    Database().session.commit()


def update_category(category_name: str, new_name: str) -> None:
    Database().session.query(Goods).filter(Goods.category_name == category_name).update(
        values={Goods.category_name: new_name})
    Database().session.query(Categories).filter(Categories.name == category_name).update(
        values={Categories.name: new_name})
    Database().session.commit()


def update_promocode(code: str, discount: int | None = None, expires_at: str | None = None) -> None:
    """Update promo code discount or expiry date."""
    values = {}
    if discount is not None:
        values[PromoCode.discount] = discount
    if expires_at is not None or expires_at is None:
        values[PromoCode.expires_at] = expires_at
    if not values:
        return
    Database().session.query(PromoCode).filter(PromoCode.code == code).update(values=values)
    Database().session.commit()


def set_reseller_price(reseller_id: int, item_name: str, price: int) -> None:
    session = Database().session
    entry = session.query(ResellerPrice).filter_by(
        reseller_id=reseller_id, item_name=item_name
    ).first()
    if entry:
        entry.price = price
    else:
        session.add(ResellerPrice(reseller_id=reseller_id, item_name=item_name, price=price))
    session.commit()


def clear_stock_notifications(item_name: str) -> None:
    Database().session.query(StockNotification).filter(
        StockNotification.item_name == item_name
    ).delete(synchronize_session=False)
    Database().session.commit()


def process_purchase_streak(telegram_id: int) -> None:
    """Update streak data after a successful purchase."""
    session = Database().session
    user = session.query(User).filter(User.telegram_id == telegram_id).one()
    today = datetime.date.today()

    if user.streak_discount:
        user.streak_discount = False
        user.purchase_streak = 0

    if user.last_purchase_date:
        last_date = datetime.date.fromisoformat(user.last_purchase_date)
        diff = (today - last_date).days
        if diff == 1:
            user.purchase_streak += 1
        elif diff > 1:
            user.purchase_streak = 1
    else:
        user.purchase_streak = 1

    user.last_purchase_date = today.isoformat()

    if user.purchase_streak >= 3:
        user.purchase_streak = 0
        user.streak_discount = True

    session.commit()
