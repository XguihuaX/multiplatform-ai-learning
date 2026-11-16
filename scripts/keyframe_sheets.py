#!/usr/bin/env python3
"""Create timestamped overview frames; inspect originals when text is small."""
import json, subprocess
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
for item in json.loads((ROOT/'sources/catalog.json').read_text()):
    video = ROOT/'.cache/video-retry'/f"{item['source_id']}.mp4"
    dest = ROOT/'.cache/frames'/item['id']
    if not video.exists() or (dest/'sheet.jpg').exists(): continue
    dest.mkdir(parents=True, exist_ok=True)
    try:
        d = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(video)]))
        count = 6 if d < 180 else 12
        sheet = Image.new('RGB',(1440,820*((count+2)//3)), 'white')
        index=[]
        for i in range(count):
            t = d*(i+.4)/count
            p = dest/f'frame_{i+1:02d}.jpg'
            subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(t),'-i',str(video),'-frames:v','1','-vf','scale=960:-1','-y',str(p)],check=True)
            im=Image.open(p); im.thumbnail((480,780))
            x,y=(i%3)*480,(i//3)*820
            sheet.paste(im,(x+(480-im.width)//2,y+30))
            ImageDraw.Draw(sheet).text((x+8,y+8),f"{item['id']} | {t:.1f}s / {d:.1f}s",fill='black')
            index.append({'time_seconds':t,'path':p.name})
        sheet.save(dest/'sheet.jpg',quality=88)
        (dest/'index.json').write_text(json.dumps(index,indent=2))
        print('DONE',item['id'],d,flush=True)
    except Exception as e: print('FAILED',item['id'],str(e),flush=True)
