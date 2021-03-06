"""empty message

Revision ID: 7da1074205f1
Revises: 
Create Date: 2019-04-11 22:01:06.457577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7da1074205f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('tag', sa.String(length=80), nullable=True),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todo_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=80), nullable=True),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('tid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tid'], ['todo.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_item')
    op.drop_table('todo')
    op.drop_table('user')
    # ### end Alembic commands ###
