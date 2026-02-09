"""Add email and phone number to passengers

Revision ID: a34f9e2d1c77
Revises: 7b6a1c8d4e9f
Create Date: 2026-02-09 13:45:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = "a34f9e2d1c77"
down_revision: Union[str, Sequence[str], None] = "7b6a1c8d4e9f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("passengers", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "email",
                sqlmodel.sql.sqltypes.AutoString(),
                nullable=False,
                server_default="",
            )
        )
        batch_op.add_column(
            sa.Column(
                "phone_number",
                sqlmodel.sql.sqltypes.AutoString(),
                nullable=False,
                server_default="",
            )
        )


def downgrade() -> None:
    with op.batch_alter_table("passengers", schema=None) as batch_op:
        batch_op.drop_column("phone_number")
        batch_op.drop_column("email")
