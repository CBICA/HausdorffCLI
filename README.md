# Hausdorff95

A simple CLI that calculates Hausdorff-95 distance for 2 binary images.

## Installation

```powershell
conda create -p ./venv python=3.6.5 -y
conda activate ./venv
pip install -e .
```

## Usage

```powershell
python ./Hausdorff95.py -gt ./data/gt.nii.gz -m ./data/mask.nii.gz
```