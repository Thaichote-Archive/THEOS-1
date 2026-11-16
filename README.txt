วิธีนำขึ้นเว็บ (GitHub Pages)
1. อัปโหลด index.html และโฟลเดอร์ geojson ทั้งโฟลเดอร์ไปที่ root ของ repo
2. เปิดผ่าน URL ของ GitHub Pages (ไม่ใช่ดับเบิลคลิกไฟล์ เพราะ file:// โหลด geojson ไม่ได้)
3. หน้าเว็บจะแสดงทุกไฟล์ใน geojson/manifest.json ที่ชื่อไฟล์ขึ้นต้นด้วย TH1 (ไม่สนตัวพิมพ์เล็ก/ใหญ่)
4. เพิ่มไฟล์ใหม่: วาง TH1_xxx.geojson ในโฟลเดอร์ geojson แล้วรัน  python make_manifest.py  (สร้าง manifest.json ให้อัตโนมัติ) จากนั้นอัปโหลดขึ้น repo
   หรือแก้ manifest.json เองโดยเพิ่ม {"file":"TH1_xxx.geojson","v":1} (แก้ไฟล์เดิมให้เพิ่มเลข v)
