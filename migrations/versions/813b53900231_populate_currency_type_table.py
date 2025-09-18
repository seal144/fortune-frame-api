"""populate_currency_type_table

Revision ID: 813b53900231
Revises: 6517c69348a8
Create Date: 2025-09-18 09:09:07.260484

"""

import sqlalchemy as sa
from alembic import op

from core.models import CurrencyTypeEnum

# revision identifiers, used by Alembic.
revision = "813b53900231"
down_revision = "6517c69348a8"
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
