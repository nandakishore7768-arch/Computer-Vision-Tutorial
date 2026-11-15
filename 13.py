from ultralytics import YOLO

model = YOLO("yolo26n-obb.pt")
result = model("https://ultralytics.com/images/boats.jpg", save = True, verbose = False)[0]

oob = result.obb

rotated_area = oob.xywhr[:, 2]* oob.xywhr[:, 3]
x1, y1, x2, y2 = oob.xyxy.T
upright_area = (x1 - x2) * (y1 - y2)

print(f"{len(oob)} objects, classes: {sorted({result.names[int(c)] for c in oob.cls})}")
cx, cy, w, h, angle = oob.xywhr[0].tolist()
print(f"first box: center=({cx:.0f}, {cy:.0f}) size={w:.0f}x{h:.0f} angle={angle:.2f} rad")
ratio = float((upright_area / rotated_area).median())
print(f"an axis-aligned box would be {ratio:.1f}x larger (median)")