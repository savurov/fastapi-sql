"""add foreign key for messages

Revision ID: fab19e759cab
Revises: 3464366c9d6d
Create Date: 2023-11-20 23:13:00.372954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fab19e759cab'
down_revision: Union[str, None] = '3464366c9d6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_messages_users', 'users', ['author'], ['id'])

def downgrade():
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_constraint('fk_messages_users', type_='foreignkey')
