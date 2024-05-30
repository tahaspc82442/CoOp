#!/bin/bash

# custom config
DATA=/raid/biplab/taha
TRAINER=CoCoOp
SHOTS=16
SUB=new
DATASET=$1
CFG=vit_b16_c4_ep10_batch1_ctxv1
SEED=1

# Ensure DATASET is provided
if [ -z "$DATASET" ]; then
  echo "Usage: $0 <DATASET>"
  exit 1
fi

python train.py \
  --root ${DATA} \
  --seed ${SEED} \
  --trainer ${TRAINER} \
  --dataset-config-file configs/datasets/${DATASET}.yaml \
  --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
  --output-dir output/evaluation/${TRAINER}/${CFG}_${SHOTS}shots/${DATASET}/seed${SEED} \
  --model-dir output/base2new/train_base/${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED} \
  --load-epoch 10 \
  --eval-only \
  DATASET.NUM_SHOTS ${SHOTS} \
  DATASET.SUBSAMPLE_CLASSES ${SUB}
