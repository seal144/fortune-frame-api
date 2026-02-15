"""populate_currency_type

Revision ID: 804b1894c195
Revises: 0dc7d109b2d1
Create Date: 2026-02-15 14:22:10.787850

"""

import sqlalchemy as sa
from alembic import op

from core.models import CurrencyTypeEnum

# revision identifiers, used by Alembic.
revision = "804b1894c195"
down_revision = "0dc7d109b2d1"
branch_labels = None
depends_on = None


def upgrade():
    currency_type_table = sa.table(
        "currency_type",
        sa.column("id", sa.Integer),
        sa.column("name", sa.Enum(CurrencyTypeEnum)),
    )

    op.bulk_insert(
        currency_type_table,
        [
            {"name": CurrencyTypeEnum.FIAT},
            {"name": CurrencyTypeEnum.CRYPTO},
            {"name": CurrencyTypeEnum.METAL},
        ],
    )


def downgrade():
    op.execute("DELETE FROM currency_type WHERE name IN ('FIAT', 'CRYPTO', 'METAL')")
