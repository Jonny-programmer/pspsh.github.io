"""краткое описание мутации

Revision ID: c18fc3ec2950
Revises: 7aff259a10d5
Create Date: 2023-03-12 16:26:15.563986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c18fc3ec2950'
down_revision = '7aff259a10d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('photo_source', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teachers_id'), 'teachers', ['id'], unique=False)
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year_grad', sa.Date(), nullable=False),
    sa.Column('photo_source', sa.String(), nullable=True),
    sa.Column('monitor_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['monitor_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grades_id'), 'grades', ['id'], unique=False)
    op.create_table('hws',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['grade_id'], ['grades.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hws_id'), 'hws', ['id'], unique=False)
    op.create_table('pupils',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('photo_source', sa.String(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['grade_id'], ['grades.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pupils_id'), 'pupils', ['id'], unique=False)
    op.drop_index('ix_items_description', table_name='items')
    op.drop_index('ix_items_id', table_name='items')
    op.drop_index('ix_items_title', table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('owner_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_items_title', 'items', ['title'], unique=False)
    op.create_index('ix_items_id', 'items', ['id'], unique=False)
    op.create_index('ix_items_description', 'items', ['description'], unique=False)
    op.drop_index(op.f('ix_pupils_id'), table_name='pupils')
    op.drop_table('pupils')
    op.drop_index(op.f('ix_hws_id'), table_name='hws')
    op.drop_table('hws')
    op.drop_index(op.f('ix_grades_id'), table_name='grades')
    op.drop_table('grades')
    op.drop_index(op.f('ix_teachers_id'), table_name='teachers')
    op.drop_table('teachers')
    # ### end Alembic commands ###
