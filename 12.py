from ultralytics import YOLO

model = YOLO("yolo26n-pose.pt")
result = model("bus.jpg", save = True, verbose = False)[0]

for xy, conf in zip(result.keypoints.xy, result.keypoints.conf):
    visible = xy[conf > 0.5]
    width = float(visible[:, 0].max() - visible[:, 0].min())
    height = float(visible[:, 1].max() - visible[:, 1].min())

    posture = "unknown" if len(visible) < 6 else "lying" if width > height else "upright"

    print(posture)