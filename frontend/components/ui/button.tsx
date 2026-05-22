import React from 'react';
import clsx from 'clsx';

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'secondary';
}

const variantClasses: Record<string, string> = {
  default: 'bg-brand-500 text-white hover:bg-brand-600',
  secondary: 'border border-white/10 bg-slate-800 text-slate-100 hover:bg-slate-700',
};

export function Button({ className, variant = 'default', ...props }: ButtonProps) {
  return (
    <button
      className={clsx(
        'inline-flex items-center justify-center rounded-2xl px-5 py-3 text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-400 disabled:opacity-50 disabled:pointer-events-none',
        variantClasses[variant],
        className,
      )}
      {...props}
    />
  );
}
