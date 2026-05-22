export interface UserProfile {
  id: number;
  email: string;
  phone?: string;
  role: string;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface GroupOrder {
  id: number;
  title: string;
  description?: string;
  pincode: string;
  category?: string;
  moq_target: number;
  current_quantity: number;
  status: string;
  pricing_tiers?: Array<Record<string, unknown>>;
  created_at: string;
}
