# Agent Skills Directory
Skills = reusable runtime capabilities (Python packages/functions) called via agent tools.

## Defined Skills (Contracts only – impl in Day 3+)

1. **skill_download_youtube**
   - Input: {"video_url": str, "format": "mp4 | audio"}
   - Output: {"local_path": str, "duration_sec": int, "success": bool}
   - Purpose: Fetch source video for repurposing/transcription.

2. **skill_transcribe_audio**
   - Input: {"audio_path": str, "language": "en | auto"}
   - Output: {"transcript": str, "segments": [{"start": float, "end": float, "text": str}]}
   - Purpose: Convert downloaded audio to structured text for analysis.

3. **skill_analyze_engagement**
   - Input: {"post_id": str, "platform": "twitter"}
   - Output: {"likes": int, "replies": int, "sentiment_score": float, "key_comments": [str]}
   - Purpose: Post-publish analytics to feed back into memory/planner.

Each skill will be a Python module with strict Pydantic I/O models + error handling.