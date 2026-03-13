from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001_initial_schema'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "pgcrypto";')
    op.create_table(
        'users',
        sa.Column('id', sa.UUID, primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('role', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    op.create_table(
        'tournaments',
        sa.Column('id', sa.UUID, primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=False),
        sa.Column('participant_limit', sa.Integer, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    op.create_table(
        'matches',
        sa.Column('id', sa.UUID, primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('tournament_id', sa.UUID, nullable=False),
        sa.Column('player1_id', sa.UUID, nullable=False),
        sa.Column('player2_id', sa.UUID, nullable=False),
        sa.Column('scheduled_time', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('player1_score', sa.Integer),
        sa.Column('player2_score', sa.Integer),
        sa.Column('status', sa.String(length=50), nullable=False, server_default='scheduled'),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    op.create_foreign_key('fk_matches_tournament', 'matches', 'tournaments', ['tournament_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_matches_player1', 'matches', 'users', ['player1_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_matches_player2', 'matches', 'users', ['player2_id'], ['id'], ondelete='CASCADE')
    op.create_index('idx_tournaments_name', 'tournaments', ['name'])
    op.create_index('idx_matches_tournament_id', 'matches', ['tournament_id'])
    op.create_index('idx_matches_scheduled_time', 'matches', ['scheduled_time'])

def downgrade() -> None:
    op.drop_index('idx_matches_scheduled_time', table_name='matches')
    op.drop_index('idx_matches_tournament_id', table_name='matches')
    op.drop_index('idx_tournaments_name', table_name='tournaments')
    op.drop_constraint('fk_matches_player2', 'matches', type_='foreignkey')
    op.drop_constraint('fk_matches_player1', 'matches', type_='foreignkey')
    op.drop_constraint('fk_matches_tournament', 'matches', type_='foreignkey')
    op.drop_table('matches')
    op.drop_table('tournaments')
    op.drop_table('users')