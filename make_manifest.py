# สร้าง geojson/manifest.json อัตโนมัติ จากไฟล์ที่ชื่อขึ้นต้น TH1 ในโฟลเดอร์ geojson
# วิธีใช้: วางไฟล์นี้ข้าง ๆ โฟลเดอร์ geojson แล้วรัน  python make_manifest.py
import json, os
PFX = "TH1"
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "geojson")
fs = sorted(f for f in os.listdir(d) if f.upper().startswith(PFX) and f.lower().endswith((".geojson", ".json")) and f != "manifest.json")
out = [{"file": f, "v": int(os.path.getmtime(os.path.join(d, f)))} for f in fs]
json.dump(out, open(os.path.join(d, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False)
print(len(out), "ไฟล์:", *fs, sep="\n  ")
