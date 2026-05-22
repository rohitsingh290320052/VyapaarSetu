# VyapaarSetu — Direct Retail Infrastructure

> Empowering small retailers to buy directly from brands through hyperlocal group commerce.

![Next.js](https://img.shields.io/badge/Next.js-15-black)
![TypeScript](https://img.shields.io/badge/TypeScript-Ready-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Overview

VyapaarSetu is a Direct-to-Retailer (D2R) hyperlocal commerce platform that enables small retailers and kirana stores to collectively place bulk orders directly from manufacturers and FMCG brands.

The platform solves:
- High MOQ (Minimum Order Quantity) barriers
- Distributor-heavy pricing chains
- Fragmented retail procurement
- Lack of financial access for small retailers

By pooling demand from multiple nearby retailers, VyapaarSetu unlocks factory pricing and improves margins for small businesses.

---

# 💡 Core Idea

Instead of:

```text
Manufacturer → Distributor → Wholesaler → Retailer
```

VyapaarSetu enables:

```text
Manufacturer → VyapaarSetu Network → Retailers
```

Retailers in the same locality join a shared group order.

Once the MOQ is reached:
- The manufacturer fulfills directly
- Retailers get ex-factory pricing
- Logistics are consolidated
- Everyone saves money

---

# ✨ Key Features

## 🛒 MOQ Pooling Engine
- Hyperlocal group buying
- Live MOQ progress tracking
- Real-time order participation
- Dynamic pricing tiers
- Countdown-based order windows

---

## 📍 Geo-Based Retail Network
- Pincode/geo-radius clustering
- Nearby retailer activity feed
- Shared logistics routes
- Hyperlocal delivery optimization

---

## 💳 Embedded Fintech
- BNPL-ready architecture
- Retailer reliability scoring
- Transaction-based trust engine
- Payment history analytics

---

## 📈 Retail Intelligence
- Demand heatmaps
- Seasonal trend prediction
- AI-ready recommendation system
- Smart reorder suggestions

---

## 📱 Mobile-First Experience
- Fully responsive UI
- PWA-ready architecture
- WhatsApp-first growth loops
- Push notifications

---

# 🏗️ Tech Stack

## Frontend
- Next.js 15
- React
- TypeScript
- TailwindCSS
- Shadcn UI
- TanStack Query

## Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- WebSockets

## Infrastructure
- Docker
- Docker Compose
- Vercel
- Railway / Render

## Integrations
- Razorpay
- Firebase Cloud Messaging
- Mapbox
- WhatsApp APIs

---

# 🧠 System Architecture

```text
                 ┌──────────────────┐
                 │  Retailers App   │
                 └────────┬─────────┘
                          │
                          ▼
                ┌──────────────────┐
                │  VyapaarSetu     │
                │------------------│
                │ MOQ Engine       │
                │ Payments         │
                │ Realtime Orders  │
                │ Retail Scoring   │
                │ Logistics Layer  │
                └────────┬─────────┘
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│ Manufacturers   │           │ Logistics Layer │
└─────────────────┘           └─────────────────┘
```

---

# 🔥 Core Workflow

## 1. Brand Creates Campaign
A manufacturer launches a group-buy campaign with:
- MOQ target
- Product catalog
- Pricing tiers
- Delivery zones

---

## 2. Retailers Join Orders
Nearby retailers:
- Discover active orders
- Select quantity
- Join pooled orders
- Invite nearby shops

---

## 3. MOQ Gets Fulfilled
Once the combined quantity reaches MOQ:
- Payments are processed
- Orders are locked
- Logistics workflow begins

---

## 4. Consolidated Delivery
Retailers receive:
- Shared delivery routing
- Shipment tracking
- Invoices
- Delivery notifications

---

# 📊 Platform Roles

## 👨‍💼 Retailers
- Join group orders
- Track savings
- Access better pricing
- Build credit profile

## 🏭 Brands
- Launch campaigns
- Reach retailers directly
- Access market analytics
- Forecast demand

## 🛡️ Admins
- Monitor transactions
- Manage disputes
- Approve retailers/brands
- Track platform analytics

---

# 🧬 Future Roadmap

- AI procurement assistant
- Predictive demand engine
- Retailer credit marketplace
- Inventory financing
- Retail POS integration
- Voice-based ordering
- WhatsApp-native ordering
- Retailer-to-retailer inventory exchange

---

# 📂 Project Structure

```bash
vyapaarsetu/
│
├── apps/
│   ├── web/
│   ├── admin/
│   └── mobile/
│
├── backend/
│   ├── auth/
│   ├── orders/
│   ├── payments/
│   ├── logistics/
│   ├── analytics/
│   └── ai/
│
├── database/
│
├── docker/
│
├── docs/
│
└── shared/
```

---

# ⚙️ Local Setup

## Clone Repository

```bash
git clone https://github.com/your-username/vyapaarsetu.git
cd vyapaarsetu
```

---

## Install Frontend

```bash
cd apps/web
npm install
npm run dev
```

---

## Install Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Run Docker

```bash
docker-compose up --build
```

---

# 🔐 Environment Variables

```env
DATABASE_URL=
JWT_SECRET=
RAZORPAY_KEY_ID=
RAZORPAY_SECRET=
MAPBOX_API_KEY=
FIREBASE_SERVER_KEY=
```

---

# 📸 Screens Planned

- Retailer Home Feed
- MOQ Progress Dashboard
- Group Order Detail
- Brand Analytics Dashboard
- Admin Control Panel
- Shipment Tracking
- Retailer Savings Analytics

---

# 🎯 Vision

VyapaarSetu aims to become:

> “The operating system powering small retail commerce.”

Not just a marketplace —
but a complete commerce + fintech + logistics infrastructure layer for millions of small retailers.

---

# 🤝 Contributing

Contributions, ideas, and feature suggestions are welcome.

```bash
fork → build → improve → pull request
```

---

# 🌍 Built For The Future Of Retail

**VyapaarSetu — Buy Better Together.**
