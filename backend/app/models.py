# backend/app/models.py
from . import db
from datetime import datetime

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(20), nullable=False)
    market_area_id = db.Column(db.Integer, db.ForeignKey('market_areas.id'), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    size_sq_meters = db.Column(db.Numeric, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    transactions = db.relationship('Transaction', backref='property', lazy=True)
    insights = db.relationship('PropertyInsight', backref='property', lazy=True)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    transactions = db.relationship('Transaction', backref='user', lazy=True)
    preferences = db.relationship('UserPreference', backref='user', lazy=True)


class MarketArea(db.Model):
    __tablename__ = 'market_areas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    average_price = db.Column(db.Numeric, nullable=True)
    growth_rate = db.Column(db.Numeric, nullable=True)
    rental_yield = db.Column(db.Numeric, nullable=True)
    population_density = db.Column(db.Numeric, nullable=True)
    crime_rate = db.Column(db.Numeric, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    properties = db.relationship('Property', backref='market_area', lazy=True)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # e.g., Buy, Rent
    price = db.Column(db.Numeric, nullable=False)
    transaction_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PropertyInsight(db.Model):
    __tablename__ = 'property_insights'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    insight_type = db.Column(db.String(50), nullable=False)  # e.g., Price trend, Investment score
    value = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserPreference(db.Model):
    __tablename__ = 'user_preferences'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    search_criteria = db.Column(db.JSON, nullable=False)  # e.g., { "city": "Sydney", "min_price": 500000 }
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)