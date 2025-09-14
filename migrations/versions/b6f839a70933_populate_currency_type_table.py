"""populate currency_type table

Revision ID: b6f839a70933
Revises: 08b6910a7c9c
Create Date: 2025-09-14 10:58:45.752606

"""

import sqlalchemy as sa
from alembic import op

from core.models import CurrencyTypeEnum

# revision identifiers, used by Alembic.
revision = "b6f839a70933"
down_revision = "08b6910a7c9c"
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
