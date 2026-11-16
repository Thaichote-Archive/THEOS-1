# สร้าง geojson/manifest.json จากไฟล์ .geojson ในโฟลเดอร์ geojson ที่ขึ้นต้นด้วย TH1
# วิธีใช้: วางไฟล์นี้ไว้ข้าง index.html แล้วรัน  python make_manifest.py
import json, pathlib
PREFIX = "TH1"
d = pathlib.Path(__file__).parent / "geojson"
names = sorted(p.name for p in d.glob("*.geojson") if p.name.upper().startswith(PREFIX.upper()))
(d / "manifest.json").write_text(json.dumps(names, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(names), "ไฟล์ ->", d / "manifest.json")
