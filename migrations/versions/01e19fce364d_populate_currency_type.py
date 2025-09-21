"""populate currency_type

Revision ID: 01e19fce364d
Revises: 395ac0c52cef
Create Date: 2025-09-21 15:13:40.363277

"""

import sqlalchemy as sa
from alembic import op

from core.models import CurrencyTypeEnum

# revision identifiers, used by Alembic.
revision = "01e19fce364d"
down_revision = "395ac0c52cef"
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
