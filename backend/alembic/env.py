import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context


# ensure backend package (which contains `app`) is importable
here = os.path.abspath(os.path.dirname(__file__))
backend_path = os.path.abspath(os.path.join(here, '..'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app.db.base import Base  # noqa: E402


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def _get_sqlalchemy_url() -> str:
    """Return a SQLAlchemy URL from `DATABASE_URL` or a sqlite fallback.

    Alembic may run in environments without the asyncpg driver available
    (e.g. Windows without MSVC). We prefer a sync URL for Alembic, so
    strip the `+asyncpg` suffix when present.
    """
    url = os.getenv('DATABASE_URL')
    if not url:
        # fallback to a local sqlite URL for offline dev
        return 'sqlite:///./dev.db'
    # Alembic (offline) expects a sync URL; strip known async drivers
    for suffix in ('+asyncpg', '+aiosqlite'):
        if suffix in url:
            return url.replace(suffix, '')
    return url


# Ensure the SQLAlchemy URL is set from the environment if provided
sqlalchemy_url = _get_sqlalchemy_url()
config.set_main_option('sqlalchemy.url', sqlalchemy_url)


# Provide the metadata for 'autogenerate' support
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = _get_sqlalchemy_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
