#!/usr/bin/env python3
"""Apple Silicon local medium ASR. Run via uv --with mlx-whisper."""
import json, time
from pathlib import Path
import mlx_whisper

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / '.cache/transcripts'
out.mkdir(parents=True, exist_ok=True)
for item in json.loads((ROOT / 'sources/catalog.json').read_text()):
    media = ROOT / '.cache/video-retry' / (item['source_id'] + '.mp4')
    target = out / (item['id'] + '.json')
    if not media.exists() or target.exists():
        continue
    print('START', item['id'], flush=True)
    started = time.monotonic()
    result = mlx_whisper.transcribe(str(media), path_or_hf_repo='mlx-community/whisper-medium-mlx')
    target.write_text(json.dumps({'id':item['id'], 'source_id':item['source_id'],
        'model':'mlx-community/whisper-medium-mlx', 'language':result['language'],
        'segments':result['segments'], 'human_checked':False}, ensure_ascii=False, indent=2))
    print('DONE', item['id'], round(time.monotonic()-started,1), flush=True)
