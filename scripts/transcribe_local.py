#!/usr/bin/env python3
"""Local ASR; cached transcripts are provisional evidence, not finished notes.

Run: uv run --python 3.12 --with faster-whisper python scripts/transcribe_local.py
"""
import json
from pathlib import Path
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[1]
media = ROOT / '.cache/video-retry'
out = ROOT / '.cache/transcripts'
out.mkdir(parents=True, exist_ok=True)
model = WhisperModel('medium', device='cpu', compute_type='int8', cpu_threads=8)
catalog = json.loads((ROOT / 'sources/catalog.json').read_text())
for item in catalog:
    video = media / (item['source_id'] + '.mp4')
    target = out / (item['id'] + '.json')
    if not video.exists() or target.exists():
        continue
    print('START', item['id'], item['title'], flush=True)
    try:
        segments, info = model.transcribe(str(video), beam_size=3, vad_filter=True)
        rows = [{'start': s.start, 'end': s.end, 'text': s.text} for s in segments]
        target.write_text(json.dumps({'id': item['id'], 'source_id': item['source_id'],
            'model':'faster-whisper medium int8', 'language':info.language,
            'segments':rows, 'human_checked':False}, ensure_ascii=False, indent=2))
        print('DONE', item['id'], len(rows), flush=True)
    except Exception as exc:
        print('FAILED', item['id'], type(exc).__name__, str(exc), flush=True)
