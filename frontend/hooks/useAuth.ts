import { useState, useEffect } from 'react';
import api, { setAuthToken } from '@/lib/api';
import type { AuthTokens, UserProfile } from '@/lib/types';

const STORAGE_KEY = 'retailink_tokens';

export function useAuth() {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [tokens, setTokens] = useState<AuthTokens | null>(null);

  useEffect(() => {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    if (stored) {
      const parsed = JSON.parse(stored) as AuthTokens;
      setTokens(parsed);
      setAuthToken(parsed.access_token);
    }
  }, []);

  const login = async (email: string, password: string) => {
    const response = await api.post<AuthTokens>('/auth/token', { username: email, password });
    setTokens(response.data);
    setAuthToken(response.data.access_token);
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(response.data));
    return response.data;
  };

  const logout = () => {
    setTokens(null);
    setUser(null);
    setAuthToken(null);
    window.localStorage.removeItem(STORAGE_KEY);
  };

  return { user, tokens, login, logout };
}
