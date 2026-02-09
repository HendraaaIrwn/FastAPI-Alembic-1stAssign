"""Create trains and passengers tables

Revision ID: 7b6a1c8d4e9f
Revises: 421f28077c10
Create Date: 2026-02-09 13:20:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = "7b6a1c8d4e9f"
down_revision: Union[str, Sequence[str], None] = "421f28077c10"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "trains",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("train_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("origin", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("destination", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("departure_time", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("arrival_time", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "passengers",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("passenger_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("seat_number", sa.Integer(), nullable=False),
        sa.Column("train_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["train_id"], ["trains.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("passengers")
    op.drop_table("trains")
