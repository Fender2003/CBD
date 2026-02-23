"""add indexes for group_match_requests lookup

Revision ID: 20260222_0002
Revises: 20260222_0001
Create Date: 2026-02-22 00:10:00.000000
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "20260222_0002"
down_revision: Union[str, None] = "20260222_0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "ix_group_match_requests_from_group_id",
        "group_match_requests",
        ["from_group_id"],
        unique=False,
    )
    op.create_index(
        "ix_group_match_requests_to_group_id",
        "group_match_requests",
        ["to_group_id"],
        unique=False,
    )
    op.create_index(
        "ix_group_match_requests_status",
        "group_match_requests",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_group_match_requests_status", table_name="group_match_requests")
    op.drop_index("ix_group_match_requests_to_group_id", table_name="group_match_requests")
    op.drop_index("ix_group_match_requests_from_group_id", table_name="group_match_requests")
