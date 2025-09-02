Next steps to go live

1. Create a Supabase project and note the following:
   - SUPABASE_URL (example: https://xyz.supabase.co)
   - SUPABASE_SERVICE_KEY (service role key)
   - DATABASE_URL (Postgres connection string)
2. In GitHub repo secrets, add: SUPABASE_URL, SUPABASE_SERVICE_KEY, DATABASE_URL
3. In Vercel project env, add: NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, SUPABASE_SERVICE_KEY
4. Push this folder to a new GitHub repo and connect to Vercel.
5. Run the `migrate` GitHub Action from the Actions UI to copy local `disclosr_backend/disclosr.db` into Supabase. (The workflow assumes the original backend repo is checked out at `../disclosr_backend` relative to this folder on the runner; if not, change the path to where `disclosr.db` will be placed in the workspace.)
