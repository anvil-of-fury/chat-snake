import pytest
from unittest.mock import patch

from chatbot import find_best_match, get_fallback_response, data

def test_find_best_match_exact_match():
    question = "What does the eligibility verification agent (EVA) do?"
    expected_answer = "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    result = find_best_match(question)
    assert result == expected_answer

def test_find_best_match_no_match():
    question = "What is the weather today?"
    result = find_best_match(question)
    assert result is None

def test_find_best_match_empty_string():
    result = find_best_match("")
    assert result is None

def test_threshold_boundary():
    with patch('chatbot.fuzz.ratio') as mock_ratio:
        mock_ratio.return_value = 49
        result = find_best_match("test question")
        assert result is None
        
        mock_ratio.return_value = 50
        result = find_best_match("test question")
        assert result is not None

def test_get_fallback_response():
    result = get_fallback_response()
    expected_text = "I'm here to help with questions about Thoughtful AI's automation agents!"
    assert expected_text in result
    assert "EVA" in result
    assert "CAM" in result
    assert "PHIL" in result