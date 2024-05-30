#!/bin/bash

# custom config
DATA=/raid/biplab/taha
TRAINER=CoCoOp

DATASET=$1
CFG=vit_b16_c4_ep10_batch1_ctxv1 # config file  # number of context tokens
SHOTS=16  # number of shots (1, 2, 4, 8, 16)

SEED=$2  # class-specific context (False or True)



DIR=output/base2new/train_base/${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED}
if [ -d "$DIR" ]; then
    echo "Oops! The results exist at ${DIR} (so skip this job)"
else
    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    DATASET.NUM_SHOTS ${SHOTS}\
    DATASET.SUBSAMPLE_CLASSES base
fi
