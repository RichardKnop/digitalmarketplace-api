"""Add framework and framework status fields

Revision ID: 60_add_framework_status
Revises: 50_remove_updated_details
Create Date: 2015-06-16 09:18:05.389816

"""

# revision identifiers, used by Alembic.
revision = '60_add_framework_status'
down_revision = '50_remove_updated_details'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # add framework field
    framework_enum = sa.Enum('gcloud', name='framework_enum')
    framework_enum.create(op.get_bind())
    framework_column = sa.Column('framework', framework_enum,
                                 nullable=False, index=True, server_default='gcloud')
    op.add_column('frameworks', framework_column)
    # remove framework default
    op.alter_column('frameworks', 'framework', server_default=None)

    # add status column
    status_enum = sa.Enum(
        'pending', 'open', 'clarification', 'questions_ended',
        'award', 'live', 'expired',
        name='framework_status_enum')
    status_enum.create(op.get_bind())
    status_column = sa.Column('status', status_enum,
                              nullable=False, index=True, server_default='pending')
    op.add_column('frameworks', status_column)
    op.execute("UPDATE frameworks SET status = 'expired' WHERE expired = TRUE;")
    op.execute("UPDATE frameworks SET status = 'live' WHERE expired = FALSE;")


def downgrade():
    op.drop_column('frameworks', 'framework')
    op.drop_column('frameworks', 'status')
