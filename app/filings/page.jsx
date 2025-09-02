import React from 'react'

export default async function FilingsPage() {
  // Server component: fetch from our API route
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE || ''}/api/filings`, { cache: 'no-store' })
  const data = await res.json().catch(() => ({ data: [] }))

  return (
    <main style={{padding: 24}}>
      <h1>Filings</h1>
      <ul>
        {(data.data || []).map(f => (
          <li key={f.id}>
            <strong>{f.symbol}</strong> — {f.headline}
          </li>
        ))}
      </ul>
    </main>
  )
}
