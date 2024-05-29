
import os
import pickle
import math
import random
from collections import defaultdict

from dassl.data.datasets import DATASET_REGISTRY, Datum, DatasetBase
from dassl.utils import read_json, write_json, mkdir_if_missing, listdir_nohidden




def read_and_split_data(image_dir, p_trn=0.5, p_val=0.2, ignored=[], new_cnames=None):
    categories = listdir_nohidden(image_dir)
    categories = [c for c in categories if c not in ignored]
    print(categories)   
    categories.sort()
     
    p_tst = 1 - p_trn - p_val
    print(f"Splitting into {p_trn:.0%} train, {p_val:.0%} val, and {p_tst:.0%} test")



read_and_split_data(image_dir='/raid/biplab/taha/Ucmerced/Images')