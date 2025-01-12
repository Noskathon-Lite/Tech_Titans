{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6b92f2ea-d2c6-46fe-b3aa-a7aed503e953",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ultralytics import YOLO"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "8127ffa7-c8f5-4e95-9d1c-4d9cbcb4e9a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = YOLO(\"yolo11n-cls.pt\")  # load a pretrained model (recommended for training)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "e87cc746-40c3-4a17-b42f-94fdd9d3838d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "New https://pypi.org/project/ultralytics/8.3.59 available 😃 Update with 'pip install -U ultralytics'\n",
      "Ultralytics 8.3.58 🚀 Python-3.12.3 torch-2.5.1+cu124 CPU (AMD Ryzen 7 5800H with Radeon Graphics)\n",
      "\u001b[34m\u001b[1mengine/trainer: \u001b[0mtask=classify, mode=train, model=yolo11n-cls.pt, data=/home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset, epochs=20, time=None, patience=100, batch=16, imgsz=64, save=True, save_period=-1, cache=False, device=None, workers=8, project=None, name=train2, exist_ok=False, pretrained=True, optimizer=auto, verbose=True, seed=0, deterministic=True, single_cls=False, rect=False, cos_lr=False, close_mosaic=10, resume=False, amp=True, fraction=1.0, profile=False, freeze=None, multi_scale=False, overlap_mask=True, mask_ratio=4, dropout=0.0, val=True, split=val, save_json=False, save_hybrid=False, conf=None, iou=0.7, max_det=300, half=False, dnn=False, plots=True, source=None, vid_stride=1, stream_buffer=False, visualize=False, augment=False, agnostic_nms=False, classes=None, retina_masks=False, embed=None, show=False, save_frames=False, save_txt=False, save_conf=False, save_crop=False, show_labels=True, show_conf=True, show_boxes=True, line_width=None, format=torchscript, keras=False, optimize=False, int8=False, dynamic=False, simplify=True, opset=None, workspace=None, nms=False, lr0=0.01, lrf=0.01, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=7.5, cls=0.5, dfl=1.5, pose=12.0, kobj=1.0, nbs=64, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, bgr=0.0, mosaic=1.0, mixup=0.0, copy_paste=0.0, copy_paste_mode=flip, auto_augment=randaugment, erasing=0.4, crop_fraction=1.0, cfg=None, tracker=botsort.yaml, save_dir=runs/classify/train2\n",
      "\u001b[34m\u001b[1mtrain:\u001b[0m /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/train... found 5812 images in 2 classes ✅ \n",
      "\u001b[34m\u001b[1mval:\u001b[0m /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/validation... found 1201 images in 2 classes ✅ \n",
      "\u001b[34m\u001b[1mtest:\u001b[0m None...\n",
      "Overriding model.yaml nc=80 with nc=2\n",
      "\n",
      "                   from  n    params  module                                       arguments                     \n",
      "  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 \n",
      "  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                \n",
      "  2                  -1  1      6640  ultralytics.nn.modules.block.C3k2            [32, 64, 1, False, 0.25]      \n",
      "  3                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                \n",
      "  4                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]     \n",
      "  5                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              \n",
      "  6                  -1  1     87040  ultralytics.nn.modules.block.C3k2            [128, 128, 1, True]           \n",
      "  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              \n",
      "  8                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]           \n",
      "  9                  -1  1    249728  ultralytics.nn.modules.block.C2PSA           [256, 256, 1]                 \n",
      " 10                  -1  1    332802  ultralytics.nn.modules.head.Classify         [256, 2]                      \n",
      "YOLO11n-cls summary: 151 layers, 1,533,666 parameters, 1,533,666 gradients, 3.3 GFLOPs\n",
      "Transferred 234/236 items from pretrained weights\n",
      "\u001b[34m\u001b[1mTensorBoard: \u001b[0mStart with 'tensorboard --logdir runs/classify/train2', view at http://localhost:6006/\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[34m\u001b[1mtrain: \u001b[0mScanning /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/tra\u001b[0m"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[34m\u001b[1mtrain: \u001b[0mWARNING ⚠️ /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/train/non_biodegradable/00000006 - Copy.jpg: corrupt JPEG restored and saved\n",
      "\u001b[34m\u001b[1mtrain: \u001b[0mWARNING ⚠️ /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/train/non_biodegradable/00000006.jpg: corrupt JPEG restored and saved\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[34m\u001b[1mval: \u001b[0mScanning /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/valid\u001b[0m"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[34m\u001b[1mval: \u001b[0mWARNING ⚠️ /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/validation/non_biodegradable/00000261.jpg: corrupt JPEG restored and saved\n",
      "\u001b[34m\u001b[1moptimizer:\u001b[0m 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... \n",
      "\u001b[34m\u001b[1moptimizer:\u001b[0m AdamW(lr=0.000714, momentum=0.9) with parameter groups 39 weight(decay=0.0), 40 weight(decay=0.0005), 40 bias(decay=0.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[34m\u001b[1mTensorBoard: \u001b[0mmodel graph visualization added ✅\n",
      "Image sizes 64 train, 64 val\n",
      "Using 0 dataloader workers\n",
      "Logging results to \u001b[1mruns/classify/train2\u001b[0m\n",
      "Starting training for 20 epochs...\n",
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       1/20         0G     0.4899          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.863          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       2/20         0G     0.3195          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.858          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       3/20         0G     0.3091          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.824          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       4/20         0G     0.3198          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.864          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       5/20         0G     0.2931          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.886          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       6/20         0G     0.2768          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all       0.86          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       7/20         0G     0.2545          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.845          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       8/20         0G     0.2255          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.866          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "       9/20         0G     0.2184          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.898          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      10/20         0G     0.1869          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.893          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      11/20         0G     0.1979          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.887          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      12/20         0G     0.1833          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all       0.88          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      13/20         0G     0.1819          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.886          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      14/20         0G     0.1651          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.882          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      15/20         0G     0.1571          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.876          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      16/20         0G     0.1492          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.888          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      17/20         0G     0.1457          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.898          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      18/20         0G     0.1334          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.898          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      19/20         0G     0.1256          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all        0.9          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Epoch    GPU_mem       loss  Instances       Size\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "      20/20         0G     0.1179          4         64: 100%|██████████| 364/36\n",
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all      0.892          1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "20 epochs completed in 0.121 hours.\n",
      "Optimizer stripped from runs/classify/train2/weights/last.pt, 3.2MB\n",
      "Optimizer stripped from runs/classify/train2/weights/best.pt, 3.2MB\n",
      "\n",
      "Validating runs/classify/train2/weights/best.pt...\n",
      "Ultralytics 8.3.58 🚀 Python-3.12.3 torch-2.5.1+cu124 CPU (AMD Ryzen 7 5800H with Radeon Graphics)\n",
      "YOLO11n-cls summary (fused): 112 layers, 1,528,586 parameters, 0 gradients, 3.2 GFLOPs\n",
      "\u001b[34m\u001b[1mtrain:\u001b[0m /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/train... found 5812 images in 2 classes ✅ \n",
      "\u001b[34m\u001b[1mval:\u001b[0m /home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset/validation... found 1201 images in 2 classes ✅ \n",
      "\u001b[34m\u001b[1mtest:\u001b[0m None...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "               classes   top1_acc   top5_acc: 100%|██████████| 38/38 [00:01<00:0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   all        0.9          1\n",
      "Speed: 0.0ms preprocess, 0.3ms inference, 0.0ms loss, 0.0ms postprocess per image\n",
      "Results saved to \u001b[1mruns/classify/train2\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "results = model.train(data=\"/home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset\", epochs=20, imgsz=64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "12c0056f-89cd-4846-827a-fc5ec9662528",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_12191/490167918.py:20: UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.\n",
      "  plt.legend()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x797a61eca9c0>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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NmzAypUr0bx5c7Ro0aJK7fH19UXPnj2xYcMGrF+/Hq6urhg4cGCpY+4vGff09ERMTAwKCgoqPfegQYOwf/9+bNu2rcxzmZmZKCoqKvXYTz/9VOreHTp0CAcPHjR/nqujT58+0Ov1Ze75Rx99BJlMZj7nnTt3yry2VatWAPDA/hGZcGSGnEZUVBQ6deqEzZs3A0CZYOapp57C22+/jTFjxqBTp044ffo01qxZgwYNGlT7Wq1atcLQoUPx6aefIisrC506dcLOnTuRlJRU5tinnnoK33zzDXx8fNC0aVPs378fO3bsKLMicatWraBQKLBw4UJkZWVBpVLhiSeeQFBQUJlzTpgwAZ9//jlGjx6No0ePon79+vj+++/x119/YcmSJWXyGGqqqu/ZyJEjsXr1akybNg2HDh3CI488gtzcXOzYsQOTJk3CgAED8Pjjj2PEiBH4+OOPkZiYiF69esFgMODPP//E448/bi6rHz9+PN577z2MHz8ebdu2xR9//IGEhIQqt9nb2xuPPvooFi1aBJ1Oh7p162L79u24dOlSmWPfffddbN++HV27dsWECRPQpEkTpKamYuPGjdi7d685edXUx48//hi7du3CwoULq/U+Dh48GC+88AI+/fRT9OzZs9R5AaBp06Z47LHH0KZNG/j5+eHIkSP4/vvvSy01UJ7p06fj559/xlNPPYXRo0ejTZs2yM3NxenTp/H999/j8uXLpUbQYmJi0KVLF7z00ksoKCjAkiVL4O/vj3/961/V6g8A9OvXD48//jjefPNNXL58GS1btsT27duxefNmTJ061ZxP9vbbb+OPP/5A3759ERkZibS0NHz66aeoV6+eeV0gogcSqYqKSBTLli0TAAjt27cv81x+fr7w2muvCaGhoYJarRY6d+4s7N+/v0zZc1VKswVBEPLy8oQpU6YI/v7+goeHh9CvXz/h6tWrZUqI7969K4wZM0YICAgQPD09hZ49ewp///23EBkZWaa098svvxQaNGggKBSKUmXa97dREATh1q1b5vO6uroKzZs3L1PSbOrL+++/X+b9uL+d5anqeyYIxnLoN998U4iKihKUSqUQEhIiPPfcc0JycrL5mKKiIuH9998XYmNjBVdXVyEwMFDo3bu3cPTo0VLnGTdunODj4yN4eXkJgwYNEtLS0ioszS6v5PfatWvC008/Lfj6+go+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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "results_path = \"./runs/classify/train2/results.csv\"\n",
    "results = pd.read_csv(results_path)\n",
    "plt.figure()\n",
    "plt.plot(results['epoch'],results['train/loss'],label = 'train loss')\n",
    "plt.plot(results['epoch'],results['val/loss'],label = 'val loss',c='red')\n",
    "plt.grid()\n",
    "plt.title(\"Loss vs ephos\")\n",
    "plt.ylabel(\"loss\")\n",
    "plt.xlabel(\"ephos\")\n",
    "plt.legend()\n",
    "\n",
    "plt.figure()\n",
    "plt.plot(results['epoch'],results['metrics/accuracy_top1']*100)\n",
    "plt.grid()\n",
    "plt.title(\"Validation accuracy vs ephos\")\n",
    "plt.ylabel(\"loss\")\n",
    "plt.xlabel(\"ephos\")\n",
    "plt.legend()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b04f3377-7447-4c45-94e6-9bc40360187e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "0: 64x64 biodegradable 0.96, non_biodegradable 0.04, 3.0ms\n",
      "Speed: 3.7ms preprocess, 3.0ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.6ms\n",
      "Speed: 2.2ms preprocess, 4.6ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.94, non_biodegradable 0.06, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.94, non_biodegradable 0.06, 4.4ms\n",
      "Speed: 1.8ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.87, non_biodegradable 0.13, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.59, non_biodegradable 0.41, 4.5ms\n",
      "Speed: 1.8ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.84, non_biodegradable 0.16, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.84, non_biodegradable 0.16, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.97, non_biodegradable 0.03, 4.3ms\n",
      "Speed: 1.6ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.92, non_biodegradable 0.08, 4.4ms\n",
      "Speed: 1.7ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.82, biodegradable 0.18, 4.5ms\n",
      "Speed: 1.8ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.72, biodegradable 0.28, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.66, biodegradable 0.34, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.58, biodegradable 0.42, 4.7ms\n",
      "Speed: 1.8ms preprocess, 4.7ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.56, non_biodegradable 0.44, 4.5ms\n",
      "Speed: 1.8ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.68, biodegradable 0.32, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.72, biodegradable 0.28, 4.2ms\n",
      "Speed: 2.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.71, biodegradable 0.29, 4.4ms\n",
      "Speed: 1.7ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.4ms\n",
      "Speed: 1.7ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.98, non_biodegradable 0.02, 4.7ms\n",
      "Speed: 1.7ms preprocess, 4.7ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.62, biodegradable 0.38, 4.5ms\n",
      "Speed: 2.0ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.67, biodegradable 0.33, 4.2ms\n",
      "Speed: 1.7ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.83, biodegradable 0.17, 6.1ms\n",
      "Speed: 2.2ms preprocess, 6.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.99, biodegradable 0.01, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.96, biodegradable 0.04, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.96, biodegradable 0.04, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.95, biodegradable 0.05, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.96, biodegradable 0.04, 4.3ms\n",
      "Speed: 1.7ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.94, non_biodegradable 0.06, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.97, biodegradable 0.03, 4.4ms\n",
      "Speed: 1.9ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.96, biodegradable 0.04, 4.1ms\n",
      "Speed: 1.8ms preprocess, 4.1ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.88, biodegradable 0.12, 4.3ms\n",
      "Speed: 1.7ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.87, biodegradable 0.13, 4.3ms\n",
      "Speed: 2.1ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.95, non_biodegradable 0.05, 4.2ms\n",
      "Speed: 2.0ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.5ms\n",
      "Speed: 1.5ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.3ms\n",
      "Speed: 1.6ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.84, non_biodegradable 0.16, 4.2ms\n",
      "Speed: 1.7ms preprocess, 4.2ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.95, non_biodegradable 0.05, 4.7ms\n",
      "Speed: 1.6ms preprocess, 4.7ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.4ms\n",
      "Speed: 2.0ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.73, biodegradable 0.27, 5.0ms\n",
      "Speed: 1.8ms preprocess, 5.0ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.57, non_biodegradable 0.43, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.97, biodegradable 0.03, 4.1ms\n",
      "Speed: 1.6ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.54, biodegradable 0.46, 4.9ms\n",
      "Speed: 1.8ms preprocess, 4.9ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.87, non_biodegradable 0.13, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.84, non_biodegradable 0.16, 4.5ms\n",
      "Speed: 1.8ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.69, non_biodegradable 0.31, 4.1ms\n",
      "Speed: 2.4ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.96, non_biodegradable 0.04, 4.6ms\n",
      "Speed: 1.8ms preprocess, 4.6ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.68, non_biodegradable 0.32, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.7ms\n",
      "Speed: 1.8ms preprocess, 4.7ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.6ms\n",
      "Speed: 1.7ms preprocess, 4.6ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.65, non_biodegradable 0.35, 4.2ms\n",
      "Speed: 2.0ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.90, non_biodegradable 0.10, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.64, biodegradable 0.36, 4.3ms\n",
      "Speed: 2.0ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.97, biodegradable 0.03, 4.1ms\n",
      "Speed: 1.7ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.98, biodegradable 0.02, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.88, biodegradable 0.12, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.80, biodegradable 0.20, 4.2ms\n",
      "Speed: 2.0ms preprocess, 4.2ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.78, biodegradable 0.22, 4.7ms\n",
      "Speed: 1.8ms preprocess, 4.7ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.67, biodegradable 0.33, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.52, non_biodegradable 0.48, 6.1ms\n",
      "Speed: 2.2ms preprocess, 6.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.74, non_biodegradable 0.26, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.77, non_biodegradable 0.23, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.90, biodegradable 0.10, 4.3ms\n",
      "Speed: 2.1ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.70, non_biodegradable 0.30, 4.6ms\n",
      "Speed: 2.2ms preprocess, 4.6ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.84, biodegradable 0.16, 4.9ms\n",
      "Speed: 1.6ms preprocess, 4.9ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.98, biodegradable 0.02, 4.3ms\n",
      "Speed: 2.2ms preprocess, 4.3ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.55, biodegradable 0.45, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.89, non_biodegradable 0.11, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.60, non_biodegradable 0.40, 4.1ms\n",
      "Speed: 1.9ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.56, biodegradable 0.44, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.83, non_biodegradable 0.17, 4.4ms\n",
      "Speed: 2.2ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.92, non_biodegradable 0.08, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.84, biodegradable 0.16, 4.8ms\n",
      "Speed: 1.9ms preprocess, 4.8ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.66, non_biodegradable 0.34, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.95, non_biodegradable 0.05, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.67, biodegradable 0.33, 4.3ms\n",
      "Speed: 1.7ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.98, biodegradable 0.02, 4.8ms\n",
      "Speed: 1.7ms preprocess, 4.8ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.97, biodegradable 0.03, 4.1ms\n",
      "Speed: 1.9ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.98, biodegradable 0.02, 6.2ms\n",
      "Speed: 2.0ms preprocess, 6.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.62, non_biodegradable 0.38, 6.3ms\n",
      "Speed: 2.2ms preprocess, 6.3ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.50, non_biodegradable 0.50, 4.1ms\n",
      "Speed: 2.3ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.3ms\n",
      "Speed: 2.1ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.90, non_biodegradable 0.10, 4.6ms\n",
      "Speed: 1.8ms preprocess, 4.6ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.2ms\n",
      "Speed: 2.2ms preprocess, 4.2ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.4ms\n",
      "Speed: 1.8ms preprocess, 4.4ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.86, non_biodegradable 0.14, 4.5ms\n",
      "Speed: 1.9ms preprocess, 4.5ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.97, non_biodegradable 0.03, 5.1ms\n",
      "Speed: 1.7ms preprocess, 5.1ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.88, non_biodegradable 0.12, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.66, biodegradable 0.34, 4.3ms\n",
      "Speed: 2.1ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.1ms\n",
      "Speed: 1.9ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.50, non_biodegradable 0.50, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.87, non_biodegradable 0.13, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.90, non_biodegradable 0.10, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.98, non_biodegradable 0.02, 4.1ms\n",
      "Speed: 2.0ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.85, non_biodegradable 0.15, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.79, non_biodegradable 0.21, 4.1ms\n",
      "Speed: 2.0ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.97, non_biodegradable 0.03, 4.1ms\n",
      "Speed: 2.0ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 1.00, biodegradable 0.00, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.99, biodegradable 0.01, 4.0ms\n",
      "Speed: 1.6ms preprocess, 4.0ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.89, biodegradable 0.11, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.67, biodegradable 0.33, 4.1ms\n",
      "Speed: 1.8ms preprocess, 4.1ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.76, biodegradable 0.24, 4.3ms\n",
      "Speed: 1.7ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.93, non_biodegradable 0.07, 5.1ms\n",
      "Speed: 2.1ms preprocess, 5.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.94, biodegradable 0.06, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.98, biodegradable 0.02, 4.5ms\n",
      "Speed: 2.4ms preprocess, 4.5ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.99, biodegradable 0.01, 4.3ms\n",
      "Speed: 2.0ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.97, biodegradable 0.03, 4.3ms\n",
      "Speed: 1.7ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.95, biodegradable 0.05, 4.3ms\n",
      "Speed: 1.6ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.8ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 2.0ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.9ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 2.0ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.7ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.84, non_biodegradable 0.16, 4.2ms\n",
      "Speed: 1.8ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.98, non_biodegradable 0.02, 4.3ms\n",
      "Speed: 2.2ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.7ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.77, non_biodegradable 0.23, 4.1ms\n",
      "Speed: 1.8ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.4ms\n",
      "Speed: 1.9ms preprocess, 4.4ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.8ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.7ms preprocess, 4.1ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.99, non_biodegradable 0.01, 4.2ms\n",
      "Speed: 1.6ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.3ms\n",
      "Speed: 1.8ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.9ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.0ms\n",
      "Speed: 2.1ms preprocess, 4.0ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.6ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.9ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.1ms\n",
      "Speed: 1.9ms preprocess, 4.1ms inference, 0.1ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.3ms\n",
      "Speed: 1.9ms preprocess, 4.3ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 non_biodegradable 0.73, biodegradable 0.27, 4.0ms\n",
      "Speed: 1.7ms preprocess, 4.0ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.91, non_biodegradable 0.09, 4.1ms\n",
      "Speed: 2.1ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 0.92, non_biodegradable 0.08, 4.1ms\n",
      "Speed: 1.7ms preprocess, 4.1ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n",
      "\n",
      "0: 64x64 biodegradable 1.00, non_biodegradable 0.00, 4.2ms\n",
      "Speed: 1.5ms preprocess, 4.2ms inference, 0.0ms postprocess per image at shape (1, 3, 64, 64)\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import random\n",
    "import numpy as np\n",
    "import time\n",
    "from ultralytics import YOLO\n",
    "\n",
    "# Load the trained model\n",
    "model = YOLO(\"./runs/classify/train2/weights/last.pt\")  # Replace with the correct path to your trained model\n",
    "\n",
    "# Initialize video capture\n",
    "cap = cv2.VideoCapture(2)  # Use 0 for laptop camera\n",
    "\n",
    "# Check if the video capture is opened\n",
    "if not cap.isOpened():\n",
    "    print(\"Error: Cannot access the camera\")\n",
    "    exit()\n",
    "\n",
    "# Read the class names from category.txt\n",
    "with open(\"utils/category.txt\", \"r\") as my_file:\n",
    "    class_list = my_file.read().split(\"\\n\")\n",
    "\n",
    "# Frame dimensions and rectangle size\n",
    "frame_wid = 740\n",
    "frame_hyt = 580\n",
    "rect_wid, rect_hyt = 300, 300  # Width and height of the rectangle\n",
    "\n",
    "last_model_time = time.time()\n",
    "model_delay = 2  # Process the model every 5 seconds\n",
    "last_label = \"\"  # Store the last label to display continuously\n",
    "\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "    if not ret:\n",
    "        print(\"Failed to capture frame\")\n",
    "        break\n",
    "\n",
    "    # Get frame dimensions\n",
    "    h, w, _ = frame.shape\n",
    "\n",
    "    # Define rectangle coordinates (centered)\n",
    "    cx, cy = w // 2, h // 2  # Center of the frame\n",
    "    x1, y1 = cx - rect_wid // 2, cy - rect_hyt // 2\n",
    "    x2, y2 = cx + rect_wid // 2, cy + rect_hyt // 2\n",
    "\n",
    "    # Ensure rectangle is within bounds\n",
    "    x1, y1, x2, y2 = max(0, x1), max(0, y1), min(w, x2), min(h, y2)\n",
    "\n",
    "    # Draw rectangle on the frame\n",
    "    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)\n",
    "\n",
    "    # Crop the rectangle area\n",
    "    cropped_frame = frame[y1:y2, x1:x2]\n",
    "\n",
    "    current_time = time.time()\n",
    "    if current_time - last_model_time >= model_delay:\n",
    "        last_model_time = current_time\n",
    "        # Convert cropped frame to RGB for the model\n",
    "        input_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)\n",
    "\n",
    "        # Perform inference\n",
    "        results = model.predict(source=input_frame, save=False, conf=0.5)\n",
    "\n",
    "        # Process results\n",
    "        if results:\n",
    "            for result in results:\n",
    "                cls_probs = result.probs\n",
    "                class_id = cls_probs.top1  # Get top-1 class\n",
    "                confidence = cls_probs.top1conf.item()  # Confidence of the top-1 class\n",
    "                last_label = f\"{class_list[class_id]}: {confidence:.2f}\"\n",
    "\n",
    "    # Draw label on the full frame\n",
    "    if last_label:\n",
    "        cv2.putText(frame, last_label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)\n",
    "\n",
    "    # Display the frame with the rectangle and label\n",
    "    cv2.imshow('Camera Feed', frame)\n",
    "\n",
    "    # Break the loop on 'q' key press\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "# Release resources\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "969d4e58-9ab2-45a5-a874-d736afc43bdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ultralytics 8.3.59 🚀 Python-3.12.3 torch-2.5.1+cu124 CPU (AMD Ryzen 7 5800H with Radeon Graphics)\n",
      "YOLO11n-cls summary (fused): 112 layers, 1,528,586 parameters, 0 gradients, 3.2 GFLOPs\n",
      "\n",
      "\u001b[34m\u001b[1mPyTorch:\u001b[0m starting from 'runs/classify/train2/weights/last.pt' with input shape (1, 3, 64, 64) BCHW and output shape(s) (1, 2) (3.0 MB)\n",
      "\u001b[31m\u001b[1mrequirements:\u001b[0m Ultralytics requirements ['onnx>=1.12.0', 'onnxslim', 'onnxruntime-gpu'] not found, attempting AutoUpdate...\n",
      "Collecting onnx>=1.12.0\n",
      "  Downloading onnx-1.17.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (16 kB)\n",
      "Collecting onnxslim\n",
      "  Downloading onnxslim-0.1.47-py3-none-any.whl.metadata (4.4 kB)\n",
      "Collecting onnxruntime-gpu\n",
      "  Downloading onnxruntime_gpu-1.20.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (4.5 kB)\n",
      "Requirement already satisfied: numpy>=1.20 in /home/kuber/myenv/lib/python3.12/site-packages (from onnx>=1.12.0) (2.0.2)\n",
      "Requirement already satisfied: protobuf>=3.20.2 in /home/kuber/myenv/lib/python3.12/site-packages (from onnx>=1.12.0) (5.29.2)\n",
      "Requirement already satisfied: sympy in /home/kuber/myenv/lib/python3.12/site-packages (from onnxslim) (1.13.1)\n",
      "Requirement already satisfied: packaging in /home/kuber/myenv/lib/python3.12/site-packages (from onnxslim) (24.1)\n",
      "Collecting coloredlogs (from onnxruntime-gpu)\n",
      "  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)\n",
      "Requirement already satisfied: flatbuffers in /home/kuber/myenv/lib/python3.12/site-packages (from onnxruntime-gpu) (24.12.23)\n",
      "Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime-gpu)\n",
      "  Downloading humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /home/kuber/myenv/lib/python3.12/site-packages (from sympy->onnxslim) (1.3.0)\n",
      "Downloading onnx-1.17.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.0 MB)\n",
      "\u001b[2K   \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m16.0/16.0 MB\u001b[0m \u001b[31m12.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hDownloading onnxslim-0.1.47-py3-none-any.whl (142 kB)\n",
      "\u001b[2K   \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m142.8/142.8 kB\u001b[0m \u001b[31m14.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading onnxruntime_gpu-1.20.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (291.5 MB)\n",
      "\u001b[2K   \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m291.5/291.5 MB\u001b[0m \u001b[31m11.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m\n",
      "\u001b[?25hDownloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)\n",
      "\u001b[2K   \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m46.0/46.0 kB\u001b[0m \u001b[31m141.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)\n",
      "\u001b[2K   \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m86.8/86.8 kB\u001b[0m \u001b[31m19.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hInstalling collected packages: onnx, humanfriendly, onnxslim, coloredlogs, onnxruntime-gpu\n",
      "Successfully installed coloredlogs-15.0.1 humanfriendly-10.0 onnx-1.17.0 onnxruntime-gpu-1.20.1 onnxslim-0.1.47\n",
      "\n",
      "\u001b[31m\u001b[1mrequirements:\u001b[0m AutoUpdate success ✅ 40.3s, installed 3 packages: ['onnx>=1.12.0', 'onnxslim', 'onnxruntime-gpu']\n",
      "\u001b[31m\u001b[1mrequirements:\u001b[0m ⚠️ \u001b[1mRestart runtime or rerun command for updates to take effect\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[34m\u001b[1mONNX:\u001b[0m starting export with onnx 1.17.0 opset 19...\n",
      "\u001b[34m\u001b[1mONNX:\u001b[0m slimming with onnxslim 0.1.47...\n",
      "\u001b[34m\u001b[1mONNX:\u001b[0m export success ✅ 40.7s, saved as 'runs/classify/train2/weights/last.onnx' (5.9 MB)\n",
      "\n",
      "Export complete (40.9s)\n",
      "Results saved to \u001b[1m/home/kuber/Desktop/Kuber/AI/Codes/Waster Management/runs/classify/train2/weights\u001b[0m\n",
      "Predict:         yolo predict task=classify model=runs/classify/train2/weights/last.onnx imgsz=64  \n",
      "Validate:        yolo val task=classify model=runs/classify/train2/weights/last.onnx imgsz=64 data=/home/kuber/Desktop/Kuber/AI/Codes/Waster Management/Dataset  \n",
      "Visualize:       https://netron.app\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'runs/classify/train2/weights/last.onnx'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "model = YOLO(\"./runs/classify/train2/weights/last.pt\")  \n",
    "# Export the model to ONNX format and save in the 'Model' folder\n",
    "model.export(format=\"onnx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e15f280e-0aa5-4f81-b8c9-88972f841424",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting onnx-tf\n",
      "  Downloading onnx_tf-1.10.0-py3-none-any.whl.metadata (510 bytes)\n",
      "Requirement already satisfied: onnx>=1.10.2 in /home/kuber/myenv/lib/python3.12/site-packages (from onnx-tf) (1.17.0)\n",
      "Requirement already satisfied: PyYAML in /home/kuber/myenv/lib/python3.12/site-packages (from onnx-tf) (6.0.2)\n",
      "INFO: pip is looking at multiple versions of onnx-tf to determine which version is compatible with other requirements. This could take a while.\n",
      "  Downloading onnx_tf-1.9.0-py3-none-any.whl.metadata (508 bytes)\n",
      "  Downloading onnx_tf-1.8.0-py3-none-any.whl.metadata (508 bytes)\n",
      "  Downloading onnx_tf-1.7.0-py3-none-any.whl.metadata (508 bytes)\n",
      "  Downloading onnx_tf-1.6.0-py3-none-any.whl.metadata (475 bytes)\n",
      "Requirement already satisfied: numpy>=1.20 in /home/kuber/myenv/lib/python3.12/site-packages (from onnx>=1.10.2->onnx-tf) (2.0.2)\n",
      "Requirement already satisfied: protobuf>=3.20.2 in /home/kuber/myenv/lib/python3.12/site-packages (from onnx>=1.10.2->onnx-tf) (5.29.2)\n",
      "Downloading onnx_tf-1.6.0-py3-none-any.whl (186 kB)\n",
      "\u001b[2K   \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m186.6/186.6 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m:01\u001b[0m:01\u001b[0m\n",
      "Installing collected packages: onnx-tf\n",
      "Successfully installed onnx-tf-1.6.0\n"
     ]
    }
   ],
   "source": [
    "!pip install onnx-tf\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}