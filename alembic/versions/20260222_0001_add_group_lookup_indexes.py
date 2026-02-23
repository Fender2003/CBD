"""add indexes for group ownership and lobby/request lookups

Revision ID: 20260222_0001
Revises:
Create Date: 2026-02-22 00:00:00.000000
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "20260222_0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.execute("CREATE INDEX IF NOT EXISTS ix_groups_leader_id ON groups (leader_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_group_cards_group_id ON group_cards (group_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_group_cards_is_in_lobby ON group_cards (is_in_lobby)")

    op.execute("CREATE INDEX IF NOT EXISTS ix_group_match_requests_from_group_id ON group_match_requests (from_group_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_group_match_requests_to_group_id ON group_match_requests (to_group_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_group_match_requests_status ON group_match_requests (status)")



def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_group_match_requests_status")
    op.execute("DROP INDEX IF EXISTS ix_group_match_requests_to_group_id")
    op.execute("DROP INDEX IF EXISTS ix_group_match_requests_from_group_id")

    op.execute("DROP INDEX IF EXISTS ix_group_cards_is_in_lobby")
    op.execute("DROP INDEX IF EXISTS ix_group_cards_group_id")
    op.execute("DROP INDEX IF EXISTS ix_groups_leader_id")
