"""populate_currency

Revision ID: dc794b4ad723
Revises: 804b1894c195
Create Date: 2026-02-15 14:25:25.474986

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "dc794b4ad723"
down_revision = "804b1894c195"
branch_labels = None
depends_on = None


def upgrade():
    currency_table = sa.table(
        "currency",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String),
        sa.column("code", sa.String),
        sa.column("currency_type_id", sa.Integer),
    )

    op.bulk_insert(
        currency_table,
        [
            {"name": "Australian Dollar", "code": "AUD", "currency_type_id": 1},
            {"name": "Brazilian Real", "code": "BRL", "currency_type_id": 1},
            {"name": "Bulgarian Lev", "code": "BGN", "currency_type_id": 1},
            {"name": "British Pound Sterling", "code": "GBP", "currency_type_id": 1},
            {"name": "Canadian Dollar", "code": "CAD", "currency_type_id": 1},
            {"name": "Chilean Peso", "code": "CLP", "currency_type_id": 1},
            {"name": "Chinese Yuan Renminbi", "code": "CNY", "currency_type_id": 1},
            {"name": "Czech Koruna", "code": "CZK", "currency_type_id": 1},
            {"name": "Danish Krone", "code": "DKK", "currency_type_id": 1},
            {"name": "Euro", "code": "EUR", "currency_type_id": 1},
            {"name": "Hong Kong Dollar", "code": "HKD", "currency_type_id": 1},
            {"name": "Hungarian Forint", "code": "HUF", "currency_type_id": 1},
            {"name": "Indonesian Rupiah", "code": "IDR", "currency_type_id": 1},
            {"name": "Israeli New Shekel", "code": "ILS", "currency_type_id": 1},
            {"name": "Icelandic Króna", "code": "ISK", "currency_type_id": 1},
            {"name": "Indian Rupee", "code": "INR", "currency_type_id": 1},
            {"name": "Japanese Yen", "code": "JPY", "currency_type_id": 1},
            {"name": "South Korean Won", "code": "KRW", "currency_type_id": 1},
            {"name": "Malaysian Ringgit", "code": "MYR", "currency_type_id": 1},
            {"name": "Mexican Peso", "code": "MXN", "currency_type_id": 1},
            {"name": "Norwegian Krone", "code": "NOK", "currency_type_id": 1},
            {"name": "New Zealand Dollar", "code": "NZD", "currency_type_id": 1},
            {"name": "Philippine Peso", "code": "PHP", "currency_type_id": 1},
            {"name": "Romanian Leu", "code": "RON", "currency_type_id": 1},
            {"name": "Polish Złoty", "code": "PLN", "currency_type_id": 1},
            {"name": "Singapore Dollar", "code": "SGD", "currency_type_id": 1},
            {"name": "Swedish Krona", "code": "SEK", "currency_type_id": 1},
            {"name": "Swiss Franc", "code": "CHF", "currency_type_id": 1},
            {"name": "Thai Baht", "code": "THB", "currency_type_id": 1},
            {"name": "Turkish Lira", "code": "TRY", "currency_type_id": 1},
            {"name": "Ukrainian Hryvnia", "code": "UAH", "currency_type_id": 1},
            {"name": "United States Dollar", "code": "USD", "currency_type_id": 1},
            {"name": "South African Rand", "code": "ZAR", "currency_type_id": 1},
        ],
    )


def downgrade():
    currency_table = sa.table(
        "currency",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String),
        sa.column("code", sa.String),
        sa.column("currency_type_id", sa.Integer),
    )

    op.execute(currency_table.delete().where(currency_table.c.currency_type_id == 1))
