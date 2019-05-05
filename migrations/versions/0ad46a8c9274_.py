"""empty message

Revision ID: 0ad46a8c9274
Revises: 46981e93a367
Create Date: 2019-05-01 21:06:43.390513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ad46a8c9274'
down_revision = '46981e93a367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poll_name', sa.String(length=64), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_poll_category'), 'poll', ['category'], unique=False)
    op.create_index(op.f('ix_poll_poll_name'), 'poll', ['poll_name'], unique=True)
    op.create_table('option',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poll_id', sa.Integer(), nullable=True),
    sa.Column('option', sa.String(length=50), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['poll_id'], ['poll.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_option_option'), 'option', ['option'], unique=False)
    op.add_column('user', sa.Column('preference', sa.String(length=300), nullable=True))
    op.create_index(op.f('ix_user_preference'), 'user', ['preference'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_preference'), table_name='user')
    op.drop_column('user', 'preference')
    op.drop_index(op.f('ix_option_option'), table_name='option')
    op.drop_table('option')
    op.drop_index(op.f('ix_poll_poll_name'), table_name='poll')
    op.drop_index(op.f('ix_poll_category'), table_name='poll')
    op.drop_table('poll')
    # ### end Alembic commands ###