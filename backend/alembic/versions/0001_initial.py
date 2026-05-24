"""Initial database schema.

Revision ID: 0001_initial
Revises: None
Create Date: 2026-05-23 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('phone', sa.String(), nullable=True, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('role', sa.String(), nullable=False, server_default='retailer'),
        sa.Column('is_active', sa.Boolean(), nullable=True, server_default=sa.text('true')),
        sa.Column('is_verified', sa.Boolean(), nullable=True, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_phone'), 'users', ['phone'], unique=False)

    op.create_table(
        'retailers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True, unique=True),
        sa.Column('shop_name', sa.String(), nullable=False),
        sa.Column('gst_number', sa.String(), nullable=True),
        sa.Column('pincode', sa.String(), nullable=False),
        sa.Column('latitude', sa.String(), nullable=True),
        sa.Column('longitude', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('shop_photo_url', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_index(op.f('ix_retailers_pincode'), 'retailers', ['pincode'], unique=False)

    op.create_table(
        'brands',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True, unique=True),
        sa.Column('company_name', sa.String(), nullable=False),
        sa.Column('gst_number', sa.String(), nullable=True),
        sa.Column('website', sa.String(), nullable=True),
        sa.Column('moq_default', sa.Integer(), nullable=False, server_default='50'),
        sa.Column('catalog_metadata', sa.JSON(), nullable=True),
        sa.Column('approved', sa.Boolean(), nullable=True, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('brand_id', sa.Integer(), sa.ForeignKey('brands.id', ondelete='CASCADE'), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('sku', sa.String(), nullable=True, unique=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    op.create_index(op.f('ix_products_category'), 'products', ['category'], unique=False)

    op.create_table(
        'product_variants',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.id', ondelete='CASCADE'), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('unit', sa.String(), nullable=False),
        sa.Column('price', sa.Numeric(12, 2), nullable=False),
        sa.Column('moq', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('stock_estimate', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'campaigns',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('brand_id', sa.Integer(), sa.ForeignKey('brands.id', ondelete='CASCADE'), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True, server_default=sa.text('true')),
        sa.Column('configuration', sa.JSON(), nullable=True),
        sa.Column('performance', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'group_orders',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('brand_id', sa.Integer(), sa.ForeignKey('brands.id', ondelete='SET NULL'), nullable=True),
        sa.Column('product_variant_id', sa.Integer(), sa.ForeignKey('product_variants.id', ondelete='SET NULL'), nullable=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('pincode', sa.String(), nullable=False),
        sa.Column('geo_radius_meters', sa.Integer(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('moq_target', sa.Integer(), nullable=False),
        sa.Column('current_quantity', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('pricing_tiers', sa.JSON(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default='open'),
        sa.Column('expires_at', sa.DateTime(), nullable=True),
        sa.Column('metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_index(op.f('ix_group_orders_pincode'), 'group_orders', ['pincode'], unique=False)

    op.create_table(
        'order_participants',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('group_order_id', sa.Integer(), sa.ForeignKey('group_orders.id', ondelete='CASCADE'), nullable=True),
        sa.Column('retailer_id', sa.Integer(), sa.ForeignKey('retailers.id', ondelete='CASCADE'), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('committed_price', sa.Numeric(12, 2), nullable=False),
        sa.Column('joined_at', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default='confirmed'),
    )

    op.create_table(
        'payments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('order_participant_id', sa.Integer(), sa.ForeignKey('order_participants.id', ondelete='SET NULL'), nullable=True),
        sa.Column('retailer_id', sa.Integer(), sa.ForeignKey('retailers.id', ondelete='SET NULL'), nullable=True),
        sa.Column('amount', sa.Numeric(12, 2), nullable=False),
        sa.Column('currency', sa.String(), nullable=False, server_default='INR'),
        sa.Column('provider', sa.String(), nullable=False, server_default='razorpay'),
        sa.Column('provider_payload', sa.JSON(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default='pending'),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('payment_id', sa.Integer(), sa.ForeignKey('payments.id', ondelete='SET NULL'), nullable=True),
        sa.Column('retailer_id', sa.Integer(), sa.ForeignKey('retailers.id', ondelete='SET NULL'), nullable=True),
        sa.Column('amount', sa.Numeric(12, 2), nullable=False),
        sa.Column('currency', sa.String(), nullable=False, server_default='INR'),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False, server_default='completed'),
        sa.Column('metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'shipments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('group_order_id', sa.Integer(), sa.ForeignKey('group_orders.id', ondelete='SET NULL'), nullable=True),
        sa.Column('carrier', sa.String(), nullable=True),
        sa.Column('tracking_id', sa.String(), nullable=True),
        sa.Column('status', sa.String(), nullable=False, server_default='pending'),
        sa.Column('route_cluster', sa.JSON(), nullable=True),
        sa.Column('eta', sa.DateTime(), nullable=True),
        sa.Column('metadata', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'notifications',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('body', sa.String(), nullable=False),
        sa.Column('channel', sa.String(), nullable=False, server_default='app'),
        sa.Column('payload', sa.JSON(), nullable=True),
        sa.Column('read', sa.Boolean(), nullable=True, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'referrals',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('retailer_id', sa.Integer(), sa.ForeignKey('retailers.id', ondelete='CASCADE'), nullable=True),
        sa.Column('referred_phone', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False, server_default='pending'),
        sa.Column('reward_earned', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table(
        'retailer_scores',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('retailer_id', sa.Integer(), sa.ForeignKey('retailers.id', ondelete='CASCADE'), nullable=True),
        sa.Column('score', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('rank', sa.String(), nullable=True),
        sa.Column('inputs', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('retailer_scores')
    op.drop_table('referrals')
    op.drop_table('notifications')
    op.drop_table('shipments')
    op.drop_table('transactions')
    op.drop_table('payments')
    op.drop_table('order_participants')
    op.drop_table('group_orders')
    op.drop_table('campaigns')
    op.drop_table('product_variants')
    op.drop_table('products')
    op.drop_table('brands')
    op.drop_table('retailers')
    op.drop_table('users')
