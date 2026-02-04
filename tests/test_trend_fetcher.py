# tests/test_trend_fetcher.py
import pytest
import jsonschema
from jsonschema import validate, ValidationError

# Mocked expected schema from specs/technical.md (simplified trend alert structure)
TREND_SCHEMA = {
    "type": "object",
    "properties": {
        "trend_id": {"type": "string"},
        "topic": {"type": "string"},
        "relevance_score": {"type": "number"},
        "sources": {"type": "array", "items": {"type": "string"}},
        "timestamp": {"type": "string", "format": "date-time"}
    },
    "required": ["trend_id", "topic", "relevance_score", "timestamp"],
    "additionalProperties": False
}

def mock_fetch_trend_data():
    # This is a placeholder — real impl doesn't exist yet → test MUST fail
    # Intentionally bad/missing data to force failure
    return {
        "topic": "summer fashion Ethiopia",  # missing trend_id, relevance_score, etc.
        "sources": ["newsapi", "twitter"]
    }

def test_trend_data_matches_contract():
    data = mock_fetch_trend_data()
    try:
        validate(instance=data, schema=TREND_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Trend data does not match contract: {e.message}")

    # Additional business assertions (should also fail currently)
    assert "relevance_score" in data, "Missing relevance_score"
    assert data["relevance_score"] > 0.75, "Relevance below threshold"