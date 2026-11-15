from ultralytics import YOLO

model = YOLO("yolo26n-seg.pt")
result = model("bus.jpg", save = True, retina_masks = True, verbose = False)[0]

for box, masks in zip(result.boxes, result.masks.data):
    x1, y1, x2, y2 = box.xyxy[0].tolist()
    box_area = (x2 - x1) * (y2 - y1)
    mask_area = float(masks.sum())
    name, ratio = result.names[int(box.cls)],mask_area/box_area
    print(name)
    print(ratio)
    print(mask_area)