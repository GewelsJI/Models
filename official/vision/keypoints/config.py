# -*- coding: utf-8 -*-
# MegEngine is Licensed under the Apache License, Version 2.0 (the "License")
#
# Copyright (c) 2014-2020 Megvii Inc. All rights reserved.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT ARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
class Config:
    # ---- train configuration ----
    initial_lr = 3e-4
    lr_ratio = 0.1

    batch_size = 32
    epochs = 200
    warm_epochs = 1
    weight_decay = 1e-5

    # ---- data configuration ----
    # - path
    data_root = "/data/coco_data/"

    # - normalize
    img_mean = [0.485 * 255, 0.456 * 255, 0.406 * 255]
    img_std = [0.229 * 255, 0.224 * 255, 0.225 * 255]

    # - shape
    input_shape = (256, 192)
    output_shape = (64, 48)

    # - heat maps
    keypoint_num = 17
    heat_kernel = [2.6, 2.0, 1.7, 1.4]
    heat_thr = 1e-2
    heat_range = 255

    # ---- augmentation ---

    half_body_transform = True
    extend_boxes = True

    # - extend
    x_ext = 0.6
    y_ext = 0.6

    # - half body
    num_keypoints_half_body = 3
    prob_half_body = 0.3
    upper_body_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    lower_body_ids = [11, 12, 13, 14, 15, 16]

    keypoint_flip_order = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

    # - scale
    scale_prob = 1
    scale_range = [0.7, 1.3]

    # - rotate
    rotation_prob = 0.6
    rotate_range = [-45, 45]

    # ---- testing settings ----
    test_aug_border = 10
    test_x_ext = 0.10
    test_y_ext = 0.10
    test_gaussian_kernel = 17
    second_value_aug = True

    vis_colors = [
        [255, 0, 0],
        [255, 85, 0],
        [255, 170, 0],
        [255, 255, 0],
        [170, 255, 0],
        [85, 255, 0],
        [0, 255, 0],
        [0, 255, 85],
        [0, 255, 170],
        [0, 255, 255],
        [0, 170, 255],
        [0, 85, 255],
        [0, 0, 255],
        [85, 0, 255],
        [170, 0, 255],
        [255, 0, 255],
        [255, 0, 170],
        [255, 0, 85],
        [255, 85, 85],
        [255, 170, 85],
        [255, 170, 170],
    ]

    vis_skeletons = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [5, 6],
        [5, 7],
        [7, 9],
        [6, 8],
        [8, 10],
        [5, 11],
        [6, 12],
        [11, 12],
        [11, 13],
        [13, 15],
        [12, 14],
        [14, 16],
    ]
