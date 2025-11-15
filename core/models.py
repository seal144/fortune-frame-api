import enum
import uuid

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from core import database as db


class CurrencyTypeEnum(enum.Enum):
    FIAT = "FIAT"
    CRYPTO = "CRYPTO"
    METAL = "METAL"


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)

    def __repr__(self):
        return f"User: {self.id}"


class CurrencyType(db.Model):
    __tablename__ = "currency_type"

    id = Column(Integer, primary_key=True)
    name = Column(Enum(CurrencyTypeEnum), nullable=False, unique=True)

    def __repr__(self):
        return f"CurrencyType: {self.name}"


class Currency(db.Model):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    code = Column(String(5), nullable=False)
    multiplier = Column(Float)
    currency_type = Column(Integer, ForeignKey("currency_type.id"), nullable=False)
    parent = Column(Integer, ForeignKey("currency.id"))

    currency_type_rel = db.relationship("CurrencyType", backref="currencies")

    def __repr__(self):
        return f"currency: {self.name}"


class Asset(db.Model):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    order = Column(Integer)
    currency = Column(Integer, ForeignKey("currency.id"), nullable=False)
    note = Column(String(200))

    currency_rel = db.relationship("Currency", backref="assets")

    @property
    def currency_code(self):
        return self.currency_rel.code

    @property
    def currency_name(self):
        return self.currency_rel.name

    def __repr__(self):
        return f"asset: {self.value} {self.currency_rel.name if self.currency_rel else 'Unknown'}"


class ExchangeRate(db.Model):
    __tablename__ = "exchange_rate"

    id = Column(Integer, primary_key=True)
    mid = Column(Float, nullable=False)
    currency = Column(Integer, ForeignKey("currency.id"), nullable=False)
    date = Column(Date, nullable=False)

    currency_rel = db.relationship("Currency", backref="exchange_rates")

    def __repr__(self):
        return f"exchange_rate: {self.mid} {self.currency_rel.name if self.currency_rel else 'Unknown'} {self.date}"
