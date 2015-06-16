"""empty message

Revision ID: 4236b7b9bf0f
Revises: 30_add_audit_events
Create Date: 2015-06-10 08:04:00.175499

"""

# revision identifiers, used by Alembic.
revision = '50_remove_updated_details'
down_revision = '50_add_audit_events'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('archived_services', 'updated_reason')
    op.drop_column('archived_services', 'updated_by')
    op.drop_column('draft_services', 'updated_reason')
    op.drop_column('draft_services', 'updated_by')
    op.drop_column('services', 'updated_reason')
    op.drop_column('services', 'updated_by')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('services', sa.Column('updated_by', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('services', sa.Column('updated_reason', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('draft_services', sa.Column('updated_by', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('draft_services', sa.Column('updated_reason', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('archived_services', sa.Column('updated_by', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('archived_services', sa.Column('updated_reason', sa.VARCHAR(), autoincrement=False, nullable=False))
    ### end Alembic commands ###
