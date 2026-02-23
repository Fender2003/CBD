"""add challenge-team lookup indexes on group_cards

Revision ID: 20260222_0003
Revises: 20260222_0002
Create Date: 2026-02-22 00:20:00.000000
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "20260222_0003"
down_revision: Union[str, None] = "20260222_0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("ix_group_cards_rated", "group_cards", ["rated"], unique=False)
    op.create_index("ix_group_cards_player_count", "group_cards", ["player_count"], unique=False)
    op.create_index("ix_group_cards_booking_date", "group_cards", ["booking_date"], unique=False)
    op.create_index("ix_group_cards_start_time", "group_cards", ["start_time"], unique=False)
    op.create_index("ix_group_cards_end_time", "group_cards", ["end_time"], unique=False)
    op.create_index(
        "ix_group_cards_challenge_lobby",
        "group_cards",
        ["is_in_lobby", "rated", "player_count", "booking_date", "start_time", "end_time"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_group_cards_challenge_lobby", table_name="group_cards")
    op.drop_index("ix_group_cards_end_time", table_name="group_cards")
    op.drop_index("ix_group_cards_start_time", table_name="group_cards")
    op.drop_index("ix_group_cards_booking_date", table_name="group_cards")
    op.drop_index("ix_group_cards_player_count", table_name="group_cards")
    op.drop_index("ix_group_cards_rated", table_name="group_cards")
