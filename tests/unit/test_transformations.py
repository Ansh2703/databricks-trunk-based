"""
Unit tests for transformation logic.

These tests validate individual transformation functions without requiring Databricks.
"""

import pytest


@pytest.mark.unit
def test_customer_data_structure(sample_customer_data):
    """Test that sample customer data has the expected structure."""
    assert len(sample_customer_data) == 3
    assert all("customer_id" in customer for customer in sample_customer_data)
    assert all("name" in customer for customer in sample_customer_data)
    assert all("email" in customer for customer in sample_customer_data)
    assert all("state" in customer for customer in sample_customer_data)


@pytest.mark.unit
def test_bronze_schema_expectations(expected_schema):
    """Test bronze layer schema definition."""
    bronze_schema = expected_schema["bronze"]
    assert "customer_id" in bronze_schema
    assert "name" in bronze_schema
    assert "email" in bronze_schema
    assert "state" in bronze_schema
    assert "ingestion_timestamp" in bronze_schema


@pytest.mark.unit
def test_silver_schema_expectations(expected_schema):
    """Test silver layer schema definition."""
    silver_schema = expected_schema["silver"]
    assert "customer_id" in silver_schema
    assert "name" in silver_schema
    assert "email" in silver_schema
    assert "state" in silver_schema
    assert "processed_timestamp" in silver_schema


@pytest.mark.unit
def test_gold_schema_expectations(expected_schema):
    """Test gold layer schema definition."""
    gold_schema = expected_schema["gold"]
    assert "state" in gold_schema
    assert "customer_count" in gold_schema
    assert len(gold_schema) == 2  # Only state and customer_count


@pytest.mark.unit
def test_email_validation():
    """Test email format validation logic."""
    valid_emails = ["user@example.com", "test.user@domain.co.uk"]
    invalid_emails = ["invalid", "no@domain", "@example.com"]
    
    # Simple email validation (this is a placeholder for real validation logic)
    def is_valid_email(email):
        return "@" in email and "." in email.split("@")[1]
    
    for email in valid_emails:
        assert is_valid_email(email), f"Expected {email} to be valid"
    
    for email in invalid_emails:
        assert not is_valid_email(email), f"Expected {email} to be invalid"


@pytest.mark.unit
def test_state_aggregation_logic(sample_customer_data):
    """Test the aggregation logic for counting customers by state."""
    # Simulate the gold layer aggregation
    state_counts = {}
    for customer in sample_customer_data:
        state = customer["state"]
        state_counts[state] = state_counts.get(state, 0) + 1
    
    # Validate aggregation results
    assert state_counts["CA"] == 1
    assert state_counts["NY"] == 1
    assert state_counts["TX"] == 1
    assert len(state_counts) == 3
