import datetime
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, Text, Boolean, VARCHAR
from bot.database.main import Database
from sqlalchemy.orm import relationship


class Permission:
    USE = 1
    BROADCAST = 2
    SETTINGS_MANAGE = 4
    USERS_MANAGE = 8
    SHOP_MANAGE = 16
    ADMINS_MANAGE = 32
    OWN = 64
    ASSIGN_PHOTOS = 128


class Role(Database.BASE):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    default = Column(Boolean, default=False, index=True)
    permissions = Column(Integer)
    users = relationship('User', backref='role', lazy='dynamic')

    def __init__(self, name: str, permissions=None, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0
        self.name = name
        self.permissions = permissions

    @staticmethod
    def insert_roles():
        roles = {
            'USER': [Permission.USE],
            'ADMIN': [Permission.USE, Permission.BROADCAST,
                      Permission.SETTINGS_MANAGE, Permission.USERS_MANAGE,
                      Permission.SHOP_MANAGE, Permission.ASSIGN_PHOTOS],
            'OWNER': [Permission.USE, Permission.BROADCAST,
                      Permission.SETTINGS_MANAGE, Permission.USERS_MANAGE,
                      Permission.SHOP_MANAGE, Permission.ADMINS_MANAGE,
                      Permission.OWN, Permission.ASSIGN_PHOTOS],
            'ASSISTANT': [Permission.USE, Permission.ASSIGN_PHOTOS],
        }
        default_role = 'USER'
        for r in roles:
            role = Database().session.query(Role).filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            Database().session.add(role)
        Database().session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name


class User(Database.BASE):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, nullable=False, unique=True, primary_key=True)
    username = Column(String(64), nullable=True)
    role_id = Column(Integer, ForeignKey('roles.id'), default=1)
    balance = Column(BigInteger, nullable=False, default=0)
    lottery_tickets = Column(Integer, nullable=False, default=0)
    purchase_streak = Column(Integer, nullable=False, default=0)
    last_purchase_date = Column(VARCHAR, nullable=True)
    streak_discount = Column(Boolean, nullable=False, default=False)
    language = Column(String(5), nullable=True)
    referral_id = Column(BigInteger, nullable=True)
    registration_date = Column(VARCHAR, nullable=False)
    user_operations = relationship("Operations", back_populates="user_telegram_id")
    user_unfinished_operations = relationship("UnfinishedOperations", back_populates="user_telegram_id")
    user_goods = relationship("BoughtGoods", back_populates="user_telegram_id")

    def __init__(self, telegram_id: int, registration_date: datetime.datetime, balance: int = 0,
                 referral_id=None, role_id: int = 1, language: str | None = None,
                 username: str | None = None, purchase_streak: int = 0,
                 last_purchase_date: str | None = None, streak_discount: bool = False):
        self.telegram_id = telegram_id
        self.username = username
        self.role_id = role_id
        self.balance = balance
        self.referral_id = referral_id
        self.registration_date = registration_date
        self.language = language
        self.purchase_streak = purchase_streak
        self.last_purchase_date = last_purchase_date
        self.streak_discount = streak_discount


class Categories(Database.BASE):
    __tablename__ = 'categories'
    name = Column(String(100), primary_key=True, unique=True, nullable=False)
    parent_name = Column(String(100), nullable=True)
    allow_discounts = Column(Boolean, nullable=False, default=True)
    allow_referral_rewards = Column(Boolean, nullable=False, default=True)
    item = relationship("Goods", back_populates="category")

    def __init__(
        self,
        name: str,
        parent_name: str | None = None,
        allow_discounts: bool = True,
        allow_referral_rewards: bool = True,
    ):
        self.name = name
        self.parent_name = parent_name
        self.allow_discounts = allow_discounts
        self.allow_referral_rewards = allow_referral_rewards


class Goods(Database.BASE):
    __tablename__ = 'goods'
    name = Column(String(100), nullable=False, unique=True, primary_key=True)
    price = Column(BigInteger, nullable=False)
    description = Column(Text, nullable=False)
    delivery_description = Column(Text, nullable=True)
    category_name = Column(String(100), ForeignKey('categories.name'), nullable=False)
    category = relationship("Categories", back_populates="item")
    values = relationship("ItemValues", back_populates="item")

    def __init__(self, name: str, price: int, description: str, category_name: str,
                 delivery_description: str | None = None):
        self.name = name
        self.price = price
        self.description = description
        self.delivery_description = delivery_description
        self.category_name = category_name


class ItemValues(Database.BASE):
    __tablename__ = 'item_values'
    id = Column(Integer, nullable=False, primary_key=True)
    item_name = Column(String(100), ForeignKey('goods.name'), nullable=False)
    value = Column(Text, nullable=True)
    is_infinity = Column(Boolean, nullable=False)
    item = relationship("Goods", back_populates="values")

    def __init__(self, name: str, value: str, is_infinity: bool):
        self.item_name = name
        self.value = value
        self.is_infinity = is_infinity


class BoughtGoods(Database.BASE):
    __tablename__ = 'bought_goods'
    id = Column(Integer, nullable=False, primary_key=True)
    item_name = Column(String(100), nullable=False)
    value = Column(Text, nullable=False)
    price = Column(BigInteger, nullable=False)
    buyer_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=False)
    bought_datetime = Column(VARCHAR, nullable=False)
    unique_id = Column(BigInteger, nullable=False, unique=True)
    user_telegram_id = relationship("User", back_populates="user_goods")

    def __init__(self, name: str, value: str, price: int, bought_datetime: str, unique_id,
                 buyer_id: int = 0):
        self.item_name = name
        self.value = value
        self.price = price
        self.buyer_id = buyer_id
        self.bought_datetime = bought_datetime
        self.unique_id = unique_id


class Operations(Database.BASE):
    __tablename__ = 'operations'
    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=False)
    operation_value = Column(BigInteger, nullable=False)
    operation_time = Column(VARCHAR, nullable=False)
    user_telegram_id = relationship("User", back_populates="user_operations")

    def __init__(self, user_id: int, operation_value: int, operation_time: str):
        self.user_id = user_id
        self.operation_value = operation_value
        self.operation_time = operation_time


class UnfinishedOperations(Database.BASE):
    __tablename__ = 'unfinished_operations'
    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=False)
    operation_value = Column(BigInteger, nullable=False)
    operation_id = Column(String(500), nullable=False)
    message_id = Column(BigInteger, nullable=True)
    user_telegram_id = relationship("User", back_populates="user_unfinished_operations")

    def __init__(self, user_id: int, operation_value: int, operation_id: str, message_id: int | None = None):
        self.user_id = user_id
        self.operation_value = operation_value
        self.operation_id = operation_id
        self.message_id = message_id


class Achievement(Database.BASE):
    __tablename__ = 'achievements'
    code = Column(String(50), primary_key=True, unique=True)

    def __init__(self, code: str):
        self.code = code


class UserAchievement(Database.BASE):
    __tablename__ = 'user_achievements'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=False)
    achievement_code = Column(String(50), ForeignKey('achievements.code'), nullable=False)
    achieved_at = Column(VARCHAR, nullable=False)

    def __init__(self, user_id: int, achievement_code: str, achieved_at: str):
        self.user_id = user_id
        self.achievement_code = achievement_code
        self.achieved_at = achieved_at


class PromoCode(Database.BASE):
    __tablename__ = 'promo_codes'
    code = Column(String(50), primary_key=True, unique=True)
    discount = Column(Integer, nullable=False)
    expires_at = Column(VARCHAR, nullable=True)
    active = Column(Boolean, default=True)

    def __init__(self, code: str, discount: int, expires_at: str | None = None, active: bool = True):
        self.code = code
        self.discount = discount
        self.expires_at = expires_at
        self.active = active


class Reseller(Database.BASE):
    __tablename__ = 'resellers'
    user_id = Column(BigInteger, ForeignKey('users.telegram_id'), primary_key=True, unique=True)

    def __init__(self, user_id: int):
        self.user_id = user_id


class ResellerPrice(Database.BASE):
    __tablename__ = 'reseller_prices'
    id = Column(Integer, primary_key=True)
    reseller_id = Column(BigInteger, ForeignKey('resellers.user_id'), nullable=False)
    item_name = Column(String(100), ForeignKey('goods.name'), nullable=False)
    price = Column(BigInteger, nullable=False)

    def __init__(self, reseller_id: int, item_name: str, price: int):
        self.reseller_id = reseller_id
        self.item_name = item_name
        self.price = price


class StockNotification(Database.BASE):
    __tablename__ = 'stock_notifications'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=False)
    item_name = Column(String(100), ForeignKey('goods.name'), nullable=False)

    def __init__(self, user_id: int, item_name: str):
        self.user_id = user_id
        self.item_name = item_name


def register_models():
    Database.BASE.metadata.create_all(Database().engine)
    Role.insert_roles()
