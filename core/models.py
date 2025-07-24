import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from core import database as db


class CurrencyTypeEnum(enum.Enum):
    FIAT = "fiat"
    CRYPTO = "crypto"
    METAL = "metal"


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)

    def __repr__(self):
        return f"User: {self.id}"


class CurrencyType(db.Model):
    __tablename__ = "currency_type"

    id = Column(Integer, primary_key=True)
    name = Column(Enum(CurrencyTypeEnum), nullable=False)

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

    def __repr__(self):
        return f"currency: {self.name}"


class Asset(db.Model):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)
    order = Column(Integer)
    currency = Column(Integer, ForeignKey("currency.id"), nullable=False)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    note = Column(String(200))

    currency_rel = db.relationship("Currency", backref="assets")

    def __repr__(self):
        return f"asset: {self.value} {self.currency_rel.name if self.currency_rel else 'Unknown'}"
