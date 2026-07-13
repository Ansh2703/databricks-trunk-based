"""
Pytest configuration file for databricks-gitflow tests.

This file contains fixtures and configuration for pytest tests.
"""

import pytest


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests (fast, no external dependencies)"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests (slower, may use Databricks)"
    )


@pytest.fixture
def sample_customer_data():
    """Fixture providing sample customer data for testing."""
    return [
        {"customer_id": 1, "name": "John Doe", "email": "john@example.com", "state": "CA"},
        {"customer_id": 2, "name": "Jane Smith", "email": "jane@example.com", "state": "NY"},
        {"customer_id": 3, "name": "Bob Johnson", "email": "bob@example.com", "state": "TX"},
    ]


@pytest.fixture
def expected_schema():
    """Fixture defining expected table schemas."""
    return {
        "bronze": ["customer_id", "name", "email", "state", "ingestion_timestamp"],
        "silver": ["customer_id", "name", "email", "state", "processed_timestamp"],
        "gold": ["state", "customer_count"],
    }
