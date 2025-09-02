import React from 'react'
import Link from 'next/link'

export default function Home() {
  return (
    <main style={{padding: 24, fontFamily: 'Inter, Arial'}}>
      <h1>Disclosr (live-first)</h1>
      <p>Minimal Next.js + Supabase scaffold.</p>
      <p><Link href="/filings">View filings</Link></p>
    </main>
  )
}
