#!/usr/bin/env python3
"""Inventory all downloaded parts, extract native subtitles, then run local ASR.
Run: uv run --python 3.12 --with mlx-whisper python scripts/prepare_bilibili.py
"""
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'.cache/bilibili-transcripts'; out.mkdir(exist_ok=True)
parts=[]
for item in json.loads((ROOT/'sources/catalog.json').read_text()):
    if item['platform']!='bilibili': continue
    for n,media in enumerate(sorted((ROOT/'.cache/bilibili-download'/item['id']).rglob('*.mp4')),1):
        meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type','-of','json',str(media)]))
        key=f"{item['id']}-P{n:02}"
        parts.append({'id':key,'source_id':item['source_id'],'media':str(media.relative_to(ROOT)), 'duration':float(meta['format']['duration']), 'native_subtitles':any(s['codec_type']=='subtitle' for s in meta['streams'])})
        if parts[-1]['native_subtitles']:
            subprocess.run(['ffmpeg','-v','error','-i',str(media),'-map','0:s:0','-y',str(out/(key+'.srt'))],check=True)
(ROOT/'.cache/bilibili-parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2))
import mlx_whisper
# Short parts first so long courses do not delay all other materials.
for part in sorted(parts,key=lambda p:p['duration']):
    target=out/(part['id']+'.json')
    if target.exists() or (out/(part['id']+'.srt')).exists(): continue
    print('START',part['id'],round(part['duration']),flush=True)
    try:
        result=mlx_whisper.transcribe(str(ROOT/part['media']),path_or_hf_repo='mlx-community/whisper-medium-mlx')
        target.write_text(json.dumps({'id':part['id'],'source_id':part['source_id'],'model':'mlx-community/whisper-medium-mlx','language':result['language'],'segments':result['segments'],'human_checked':False},ensure_ascii=False,indent=2))
        print('DONE',part['id'],flush=True)
    except Exception as exc: print('FAILED',part['id'],type(exc).__name__,str(exc),flush=True)
