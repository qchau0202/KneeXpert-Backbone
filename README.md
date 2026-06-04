# KneeXpert Backbone API

X-ray KL grading (0–4) with ensemble learning and Grad-CAM. Weights live in `xray/models/`.

## Setup

```bash
cd backbone
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --host 0.0.0.0 --port 9000 --reload
```

Health check: `GET http://localhost:9000/health`

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Service status and available models |
| POST | `/api/xray/predict` | Single image (KneeXpert) — `file`, optional `model_names` |
| POST | `/predict` | Batch images (demo-compatible) |

**Models** (weights in `xray/models/`):

| ID | Weights file |
|----|----------------|
| `densenet201_deep_mlp_v1` | `densenet201-deep_mlp_v1.pth` |
| `densenet201_deep_mlp_v2` | `densenet201-deep_mlp_v2.pth` |
| `densenet201_standard_head` | `densenet201-standard_heap.pth` |
| `resnet101_linear_head` | `resnet101-linear_head.pth` |
| `resnet50_deep_mlp` | `resnet50-deep_mlp.pth` |
| `resnet50_dropout_regularised` | `resnet50-dropout_regularised.pth` |
| `vgg19_batch_normalised` | `vgg19-batch_normalised.pth` |
| `vgg19_standard_head` | `vgg19-standard_head.pth` |

Pass `model_names=all` (default) to evaluate every available checkpoint. Ensemble = mean softmax across selected models.

## KneeXpert

Set `VITE_BACKBONE_URL=http://localhost:9000` in KneeXpert `.env` (see `.env.example`).
