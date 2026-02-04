# tests/test_skills_interface.py
import pytest
from pydantic import BaseModel, ValidationError

# Expected interface from skills/README.md
class DownloadInput(BaseModel):
    video_url: str
    format: str  # "mp4" | "audio"

class DownloadOutput(BaseModel):
    local_path: str
    duration_sec: int
    success: bool

def mock_skill_download_youtube(input_data: dict):
    # Placeholder — no real skill yet → wrong shape → fails
    return {"path": "/tmp/video.mp4"}  # missing keys, wrong types

def test_download_youtube_input_output_contract():
    input_dict = {"video_url": "https://youtube.com/watch?v=abc123", "format": "mp4"}
    
    try:
        input_model = DownloadInput(**input_dict)
    except ValidationError as e:
        pytest.fail(f"Input validation failed unexpectedly: {e}")
    
    output_dict = mock_skill_download_youtube(input_dict)
    
    try:
        output_model = DownloadOutput(**output_dict)
    except ValidationError as e:
        pytest.fail(f"Skill output does NOT match contract: {str(e)}")
    
    assert output_model.success is True, "Skill reported failure"
    assert output_model.local_path.endswith(".mp4"), "Wrong file extension"