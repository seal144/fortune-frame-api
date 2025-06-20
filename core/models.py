import enum

from sqlalchemy import DateTime, Enum, Float, Integer, String

from core import database as db


class CurrencyTypeEnum(enum.Enum):
    FIAT = "fiat"
    CRYPTO = "crypto"
    METAL = "metal"


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(Integer, primary_key=True)

    def __repr__(self):
        return f"User: {self.id}"


class currency_type(db.Model):
    __tablename__ = "currency_type"

    id = db.Column(Integer, primary_key=True)
    name = db.Column(Enum(CurrencyTypeEnum), nullable=False)

    def __repr__(self):
        return f"CurrencyType: {self.name}"


class currency(db.Model):
    __tablename__ = "currency"

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(200), nullable=False)
    code = db.Column(String(5), nullable=False)
    multiplier = db.Column(Float, nullable=False)
    currency_type = db.Column(
        Integer, db.ForeignKey("currency_type.id"), nullable=False
    )
    parent = db.Column(Integer, db.ForeignKey("currency.id"))

    def __repr__(self):
        return f"currency: {self.name}"


class asset(db.Model):
    __tablename__ = "asset"

    id = db.Column(Integer, primary_key=True)
    value = db.Column(Float, nullable=False)
    created_at = db.Column(DateTime, nullable=False)
    updated_at = db.Column(DateTime)
    order = db.Column(Integer)
    currency = db.Column(Integer, db.ForeignKey("currency.id"), nullable=False)
    user = db.Column(Integer, db.ForeignKey("users.id"), nullable=False)
    note = db.Column(String(200))

    currency_rel = db.relationship("currency", backref="assets")

    def __repr__(self):
        return f"asset: {self.value} {self.currency_rel.name if self.currency_rel else 'Unknown'}"
