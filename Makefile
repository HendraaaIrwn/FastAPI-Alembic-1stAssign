
dev:
	uv run uvicorn main:app --reload

# Target `alembic_init` untuk membuat struktur folder/konfigurasi Alembic pertama kali.
alembic_init:
	uv run alembic init alembic

# Target `alembic_revision` untuk membuat file migration baru dari perubahan model.
alembic_revision:
	uv run alembic revision --autogenerate -m "Init SQLModel Migrations"

# Target `alembic_migrate` untuk menerapkan seluruh migration hingga revision terbaru.
alembic_migrate:
	uv run alembic upgrade head
