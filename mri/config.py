"""MRI pipeline configuration — paths and inference hyperparameters."""

from pathlib import Path

MRI_ROOT = Path(__file__).resolve().parent
BACKBONE_ROOT = MRI_ROOT.parent
WEIGHTS_DIR = MRI_ROOT / "models"
CATEGORIES_JSON = MRI_ROOT / "categories.json"

MACS_CHECKPOINT = WEIGHTS_DIR / "best_macs_net.pth"
DEIT_CHECKPOINT = WEIGHTS_DIR / "best_deit_small_multilabel_main.pth"

MACS_IMG_SIZE = 128
DEIT_IMG_SIZE = 224

SLICE_START_FRAC = 0.15
SLICE_END_FRAC = 0.85
MIN_FOREGROUND_RATIO = 0.01
MAX_SAMPLES_PER_STUDY = 12
MAX_GALLERY_SLICES = 4

AGG_METHOD = "max"
DROPOUT_RATE = 0.25
DROP_PATH_RATE = 0.15

# DeiT was trained with MACS-cleaned input in the proposed (online) configuration.
PIPELINE_MODE = "online"

# Pre-loaded dev sample (skip client upload during testing)
SAMPLE_MRI_FILENAME = "Effusion.nii.gz"
SAMPLE_MRI_PATH = BACKBONE_ROOT / SAMPLE_MRI_FILENAME
