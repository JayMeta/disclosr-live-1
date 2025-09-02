Disclosr - Live-first rebuild

This folder is a clean, live-first scaffold for Disclosr using Next.js + Supabase.

What's included:
- Minimal Next.js app (frontend + serverless API routes)
- `scripts/migrate_to_supabase.py` migration helper (SQLite -> Postgres)
- `requirements.txt` for Python scripts
- GitHub Actions workflow `migrate.yml` to run migration in CI

Next steps:
- Set Supabase project and get SUPABASE_URL and service role key
- Add repo secrets: SUPABASE_URL, SUPABASE_SERVICE_KEY, DATABASE_URL
- Push to GitHub and connect to Vercel (or deploy manually)

Local dev:
- Frontend: `npm install` then `npm run dev`
- Migration (local test): `python scripts/migrate_to_supabase.py --sqlite ../disclosr_backend/disclosr.db --pg "$DATABASE_URL"`
