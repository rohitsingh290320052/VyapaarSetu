# RetailLink Architecture

## Overview

RetailLink is built as a cleanly separated B2B platform with a frontend web application and a Python backend API.

### Frontend
- Next.js 15 App Router
- TypeScript + TailwindCSS
- Reusable UI components
- API client layer with Axios
- Auth hook and typed payloads

### Backend
- FastAPI REST API
- SQLAlchemy with async PostgreSQL
- JWT authentication and role-based access control
- Modular domain packages for users, brands, group orders, payments and logistics
- WebSocket manager for real-time notifications and MOQ progress

### Database
- PostgreSQL relational schema with normalized tables for:
  - users
  - retailers
  - brands
  - products
  - product_variants
  - group_orders
  - order_participants
  - payments
  - transactions
  - shipments
  - notifications
  - retailer_scores
  - referrals
  - campaigns

### Infrastructure
- Docker Compose for local development
- Backend and frontend containers
- PostgreSQL database service

## Core design principles

- API-first, domain-driven structure
- Production-grade layering with services, schemas, and routers
- Clear separation between business logic and transport
- Extensible placeholders for fintech scoring, AI modules, and logistics workflows
