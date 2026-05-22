import { ArrowRight } from 'lucide-react';
import { Button } from '@/components/ui/button';

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto flex min-h-screen max-w-6xl flex-col justify-center px-6 py-16">
        <div className="rounded-[32px] border border-white/10 bg-slate-900/80 p-10 shadow-glow backdrop-blur-xl">
          <div className="space-y-8">
            <div className="space-y-4">
              <p className="text-sm uppercase tracking-[0.4em] text-brand-300">RetailLink</p>
              <h1 className="text-5xl font-semibold tracking-tight text-white">
                Direct-to-retailer group buying, scaled for modern kirana networks.
              </h1>
              <p className="max-w-2xl text-lg text-slate-300">
                Enable retailers to join pooled MOQ orders nearby, unlock brand pricing, and capture embedded fintech risk profiles.
              </p>
            </div>
            <div className="flex flex-wrap gap-4">
              <Button>Explore retailer app</Button>
              <Button variant="secondary">Brand dashboard</Button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
