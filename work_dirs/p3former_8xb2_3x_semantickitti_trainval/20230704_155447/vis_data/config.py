dataset_type = '_SemanticKittiDataset'
data_root = '/home/han/data/semantickitti/'
class_names = [
    'car', 'bicycle', 'motorcycle', 'truck', 'bus', 'person', 'bicyclist',
    'motorcyclist', 'road', 'parking', 'sidewalk', 'other-ground', 'building',
    'fence', 'vegetation', 'trunck', 'terrian', 'pole', 'traffic-sign'
]
labels_map = dict({
    0: 19,
    1: 19,
    10: 0,
    11: 1,
    13: 4,
    15: 2,
    16: 4,
    18: 3,
    20: 4,
    30: 5,
    31: 6,
    32: 7,
    40: 8,
    44: 9,
    48: 10,
    49: 11,
    50: 12,
    51: 13,
    52: 19,
    60: 8,
    70: 14,
    71: 15,
    72: 16,
    80: 17,
    81: 18,
    99: 19,
    252: 0,
    253: 6,
    254: 5,
    255: 7,
    256: 4,
    257: 4,
    258: 3,
    259: 4
})
learning_map_inv = dict({
    0: 10,
    1: 11,
    2: 15,
    3: 18,
    4: 20,
    5: 30,
    6: 31,
    7: 32,
    8: 40,
    9: 44,
    10: 48,
    11: 49,
    12: 50,
    13: 51,
    14: 70,
    15: 71,
    16: 72,
    17: 80,
    18: 81,
    19: 0
})
metainfo = dict(
    classes=[
        'car', 'bicycle', 'motorcycle', 'truck', 'bus', 'person', 'bicyclist',
        'motorcyclist', 'road', 'parking', 'sidewalk', 'other-ground',
        'building', 'fence', 'vegetation', 'trunck', 'terrian', 'pole',
        'traffic-sign'
    ],
    seg_label_mapping=dict({
        0: 19,
        1: 19,
        10: 0,
        11: 1,
        13: 4,
        15: 2,
        16: 4,
        18: 3,
        20: 4,
        30: 5,
        31: 6,
        32: 7,
        40: 8,
        44: 9,
        48: 10,
        49: 11,
        50: 12,
        51: 13,
        52: 19,
        60: 8,
        70: 14,
        71: 15,
        72: 16,
        80: 17,
        81: 18,
        99: 19,
        252: 0,
        253: 6,
        254: 5,
        255: 7,
        256: 4,
        257: 4,
        258: 3,
        259: 4
    }),
    max_label=259)
input_modality = dict(use_lidar=True, use_camera=False)
backend_args = None
pre_transform = [
    dict(
        type='LoadPointsFromFile',
        coord_type='LIDAR',
        load_dim=4,
        use_dim=4,
        backend_args=None),
    dict(
        type='_LoadAnnotations3D',
        with_bbox_3d=False,
        with_label_3d=False,
        with_panoptic_3d=True,
        seg_3d_dtype='np.int32',
        seg_offset=65536,
        dataset_type='semantickitti',
        backend_args=None),
    dict(type='PointSegClassMapping')
]
train_pipeline = [
    dict(
        type='LoadPointsFromFile',
        coord_type='LIDAR',
        load_dim=4,
        use_dim=4,
        backend_args=None),
    dict(
        type='_LoadAnnotations3D',
        with_bbox_3d=False,
        with_label_3d=False,
        with_panoptic_3d=True,
        seg_3d_dtype='np.int32',
        seg_offset=65536,
        dataset_type='semantickitti',
        backend_args=None),
    dict(type='PointSegClassMapping'),
    dict(
        type='RandomChoice',
        transforms=[[{
            'type':
            '_LaserMix',
            'num_areas': [3, 4, 5, 6],
            'pitch_angles': [-25, 3],
            'pre_transform': [{
                'type': 'LoadPointsFromFile',
                'coord_type': 'LIDAR',
                'load_dim': 4,
                'use_dim': 4
            }, {
                'type': '_LoadAnnotations3D',
                'with_bbox_3d': False,
                'with_label_3d': False,
                'with_panoptic_3d': True,
                'seg_3d_dtype': 'np.int32',
                'seg_offset': 65536,
                'dataset_type': 'semantickitti'
            }, {
                'type': 'PointSegClassMapping'
            }],
            'prob':
            0.5
        }],
                    [{
                        'type':
                        '_PolarMix',
                        'instance_classes': [0, 1, 2, 3, 4, 5, 6, 7],
                        'swap_ratio':
                        0.5,
                        'rotate_paste_ratio':
                        1.0,
                        'pre_transform': [{
                            'type': 'LoadPointsFromFile',
                            'coord_type': 'LIDAR',
                            'load_dim': 4,
                            'use_dim': 4
                        }, {
                            'type': '_LoadAnnotations3D',
                            'with_bbox_3d': False,
                            'with_label_3d': False,
                            'with_panoptic_3d': True,
                            'seg_3d_dtype': 'np.int32',
                            'seg_offset': 65536,
                            'dataset_type': 'semantickitti'
                        }, {
                            'type': 'PointSegClassMapping'
                        }],
                        'prob':
                        0.5
                    }]],
        prob=[0.2, 0.8]),
    dict(
        type='RandomFlip3D',
        sync_2d=False,
        flip_ratio_bev_horizontal=0.5,
        flip_ratio_bev_vertical=0.5),
    dict(
        type='GlobalRotScaleTrans',
        rot_range=[-0.78539816, 0.78539816],
        scale_ratio_range=[0.95, 1.05],
        translation_std=[0.1, 0.1, 0.1]),
    dict(
        type='Pack3DDetInputs',
        keys=['points', 'pts_semantic_mask', 'pts_instance_mask'])
]
test_pipeline = [
    dict(
        type='LoadPointsFromFile',
        coord_type='LIDAR',
        load_dim=4,
        use_dim=4,
        backend_args=None),
    dict(
        type='_LoadAnnotations3D',
        with_bbox_3d=False,
        with_label_3d=False,
        with_panoptic_3d=True,
        seg_3d_dtype='np.int32',
        seg_offset=65536,
        dataset_type='semantickitti',
        backend_args=None),
    dict(type='PointSegClassMapping'),
    dict(
        type='Pack3DDetInputs',
        keys=['points', 'pts_semantic_mask', 'pts_instance_mask'])
]
train_dataloader = dict(
    batch_size=2,
    num_workers=4,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type='RepeatDataset',
        times=1,
        dataset=dict(
            type='_SemanticKittiDataset',
            data_root='/home/han/data/semantickitti/',
            data_prefix=dict(
                pts='',
                img='',
                pts_instance_mask='',
                pts_semantic_mask='',
                pts_panoptic_mask=''),
            ann_file='semantickitti_infos_trainval.pkl',
            pipeline=[
                dict(
                    type='LoadPointsFromFile',
                    coord_type='LIDAR',
                    load_dim=4,
                    use_dim=4,
                    backend_args=None),
                dict(
                    type='_LoadAnnotations3D',
                    with_bbox_3d=False,
                    with_label_3d=False,
                    with_panoptic_3d=True,
                    seg_3d_dtype='np.int32',
                    seg_offset=65536,
                    dataset_type='semantickitti',
                    backend_args=None),
                dict(type='PointSegClassMapping'),
                dict(
                    type='RandomChoice',
                    transforms=[[{
                        'type':
                        '_LaserMix',
                        'num_areas': [3, 4, 5, 6],
                        'pitch_angles': [-25, 3],
                        'pre_transform': [{
                            'type': 'LoadPointsFromFile',
                            'coord_type': 'LIDAR',
                            'load_dim': 4,
                            'use_dim': 4
                        }, {
                            'type': '_LoadAnnotations3D',
                            'with_bbox_3d': False,
                            'with_label_3d': False,
                            'with_panoptic_3d': True,
                            'seg_3d_dtype': 'np.int32',
                            'seg_offset': 65536,
                            'dataset_type': 'semantickitti'
                        }, {
                            'type': 'PointSegClassMapping'
                        }],
                        'prob':
                        0.5
                    }],
                                [{
                                    'type':
                                    '_PolarMix',
                                    'instance_classes':
                                    [0, 1, 2, 3, 4, 5, 6, 7],
                                    'swap_ratio':
                                    0.5,
                                    'rotate_paste_ratio':
                                    1.0,
                                    'pre_transform': [{
                                        'type': 'LoadPointsFromFile',
                                        'coord_type': 'LIDAR',
                                        'load_dim': 4,
                                        'use_dim': 4
                                    }, {
                                        'type':
                                        '_LoadAnnotations3D',
                                        'with_bbox_3d':
                                        False,
                                        'with_label_3d':
                                        False,
                                        'with_panoptic_3d':
                                        True,
                                        'seg_3d_dtype':
                                        'np.int32',
                                        'seg_offset':
                                        65536,
                                        'dataset_type':
                                        'semantickitti'
                                    }, {
                                        'type':
                                        'PointSegClassMapping'
                                    }],
                                    'prob':
                                    0.5
                                }]],
                    prob=[0.2, 0.8]),
                dict(
                    type='RandomFlip3D',
                    sync_2d=False,
                    flip_ratio_bev_horizontal=0.5,
                    flip_ratio_bev_vertical=0.5),
                dict(
                    type='GlobalRotScaleTrans',
                    rot_range=[-0.78539816, 0.78539816],
                    scale_ratio_range=[0.95, 1.05],
                    translation_std=[0.1, 0.1, 0.1]),
                dict(
                    type='Pack3DDetInputs',
                    keys=['points', 'pts_semantic_mask', 'pts_instance_mask'])
            ],
            metainfo=dict(
                classes=[
                    'car', 'bicycle', 'motorcycle', 'truck', 'bus', 'person',
                    'bicyclist', 'motorcyclist', 'road', 'parking', 'sidewalk',
                    'other-ground', 'building', 'fence', 'vegetation',
                    'trunck', 'terrian', 'pole', 'traffic-sign'
                ],
                seg_label_mapping=dict({
                    0: 19,
                    1: 19,
                    10: 0,
                    11: 1,
                    13: 4,
                    15: 2,
                    16: 4,
                    18: 3,
                    20: 4,
                    30: 5,
                    31: 6,
                    32: 7,
                    40: 8,
                    44: 9,
                    48: 10,
                    49: 11,
                    50: 12,
                    51: 13,
                    52: 19,
                    60: 8,
                    70: 14,
                    71: 15,
                    72: 16,
                    80: 17,
                    81: 18,
                    99: 19,
                    252: 0,
                    253: 6,
                    254: 5,
                    255: 7,
                    256: 4,
                    257: 4,
                    258: 3,
                    259: 4
                }),
                max_label=259),
            modality=dict(use_lidar=True, use_camera=False),
            ignore_index=19,
            backend_args=None)))
test_dataloader = dict(
    batch_size=1,
    num_workers=1,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='RepeatDataset',
        times=1,
        dataset=dict(
            type='_SemanticKittiDataset',
            data_root='/home/han/data/semantickitti/',
            data_prefix=dict(
                pts='',
                img='',
                pts_instance_mask='',
                pts_semantic_mask='',
                pts_panoptic_mask=''),
            ann_file='semantickitti_infos_val.pkl',
            pipeline=[
                dict(
                    type='LoadPointsFromFile',
                    coord_type='LIDAR',
                    load_dim=4,
                    use_dim=4,
                    backend_args=None),
                dict(
                    type='_LoadAnnotations3D',
                    with_bbox_3d=False,
                    with_label_3d=False,
                    with_panoptic_3d=True,
                    seg_3d_dtype='np.int32',
                    seg_offset=65536,
                    dataset_type='semantickitti',
                    backend_args=None),
                dict(type='PointSegClassMapping'),
                dict(
                    type='Pack3DDetInputs',
                    keys=['points', 'pts_semantic_mask', 'pts_instance_mask'])
            ],
            metainfo=dict(
                classes=[
                    'car', 'bicycle', 'motorcycle', 'truck', 'bus', 'person',
                    'bicyclist', 'motorcyclist', 'road', 'parking', 'sidewalk',
                    'other-ground', 'building', 'fence', 'vegetation',
                    'trunck', 'terrian', 'pole', 'traffic-sign'
                ],
                seg_label_mapping=dict({
                    0: 19,
                    1: 19,
                    10: 0,
                    11: 1,
                    13: 4,
                    15: 2,
                    16: 4,
                    18: 3,
                    20: 4,
                    30: 5,
                    31: 6,
                    32: 7,
                    40: 8,
                    44: 9,
                    48: 10,
                    49: 11,
                    50: 12,
                    51: 13,
                    52: 19,
                    60: 8,
                    70: 14,
                    71: 15,
                    72: 16,
                    80: 17,
                    81: 18,
                    99: 19,
                    252: 0,
                    253: 6,
                    254: 5,
                    255: 7,
                    256: 4,
                    257: 4,
                    258: 3,
                    259: 4
                }),
                max_label=259),
            modality=dict(use_lidar=True, use_camera=False),
            ignore_index=19,
            test_mode=True,
            backend_args=None)))
val_dataloader = dict(
    batch_size=1,
    num_workers=1,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='RepeatDataset',
        times=1,
        dataset=dict(
            type='_SemanticKittiDataset',
            data_root='/home/han/data/semantickitti/',
            data_prefix=dict(
                pts='',
                img='',
                pts_instance_mask='',
                pts_semantic_mask='',
                pts_panoptic_mask=''),
            ann_file='semantickitti_infos_val.pkl',
            pipeline=[
                dict(
                    type='LoadPointsFromFile',
                    coord_type='LIDAR',
                    load_dim=4,
                    use_dim=4,
                    backend_args=None),
                dict(
                    type='_LoadAnnotations3D',
                    with_bbox_3d=False,
                    with_label_3d=False,
                    with_panoptic_3d=True,
                    seg_3d_dtype='np.int32',
                    seg_offset=65536,
                    dataset_type='semantickitti',
                    backend_args=None),
                dict(type='PointSegClassMapping'),
                dict(
                    type='Pack3DDetInputs',
                    keys=['points', 'pts_semantic_mask', 'pts_instance_mask'])
            ],
            metainfo=dict(
                classes=[
                    'car', 'bicycle', 'motorcycle', 'truck', 'bus', 'person',
                    'bicyclist', 'motorcyclist', 'road', 'parking', 'sidewalk',
                    'other-ground', 'building', 'fence', 'vegetation',
                    'trunck', 'terrian', 'pole', 'traffic-sign'
                ],
                seg_label_mapping=dict({
                    0: 19,
                    1: 19,
                    10: 0,
                    11: 1,
                    13: 4,
                    15: 2,
                    16: 4,
                    18: 3,
                    20: 4,
                    30: 5,
                    31: 6,
                    32: 7,
                    40: 8,
                    44: 9,
                    48: 10,
                    49: 11,
                    50: 12,
                    51: 13,
                    52: 19,
                    60: 8,
                    70: 14,
                    71: 15,
                    72: 16,
                    80: 17,
                    81: 18,
                    99: 19,
                    252: 0,
                    253: 6,
                    254: 5,
                    255: 7,
                    256: 4,
                    257: 4,
                    258: 3,
                    259: 4
                }),
                max_label=259),
            modality=dict(use_lidar=True, use_camera=False),
            ignore_index=19,
            test_mode=True,
            backend_args=None)))
val_evaluator = dict(
    type='_PanopticSegMetric',
    thing_class_inds=[0, 1, 2, 3, 4, 5, 6, 7],
    stuff_class_inds=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    min_num_points=50,
    id_offset=65536,
    dataset_type='semantickitti',
    learning_map_inv=dict({
        0: 10,
        1: 11,
        2: 15,
        3: 18,
        4: 20,
        5: 30,
        6: 31,
        7: 32,
        8: 40,
        9: 44,
        10: 48,
        11: 49,
        12: 50,
        13: 51,
        14: 70,
        15: 71,
        16: 72,
        17: 80,
        18: 81,
        19: 0
    }))
test_evaluator = dict(
    type='_PanopticSegMetric',
    thing_class_inds=[0, 1, 2, 3, 4, 5, 6, 7],
    stuff_class_inds=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    min_num_points=50,
    id_offset=65536,
    dataset_type='semantickitti',
    learning_map_inv=dict({
        0: 10,
        1: 11,
        2: 15,
        3: 18,
        4: 20,
        5: 30,
        6: 31,
        7: 32,
        8: 40,
        9: 44,
        10: 48,
        11: 49,
        12: 50,
        13: 51,
        14: 70,
        15: 71,
        16: 72,
        17: 80,
        18: 81,
        19: 0
    }))
vis_backends = [dict(type='LocalVisBackend')]
visualizer = dict(
    type='Det3DLocalVisualizer',
    vis_backends=[dict(type='LocalVisBackend')],
    name='visualizer')
grid_shape = [480, 360, 32]
model = dict(
    type='_P3Former',
    data_preprocessor=dict(
        type='_Det3DDataPreprocessor',
        voxel=True,
        voxel_type='cylindrical',
        voxel_layer=dict(
            grid_shape=[480, 360, 32],
            point_cloud_range=[0, -3.14159265359, -4, 50, 3.14159265359, 2],
            max_num_points=-1,
            max_voxels=-1)),
    voxel_encoder=dict(
        type='SegVFE',
        feat_channels=[64, 128, 256, 256],
        in_channels=6,
        with_voxel_center=True,
        feat_compression=16,
        return_point_feats=False),
    backbone=dict(
        type='_Asymm3DSpconv',
        grid_size=[480, 360, 32],
        input_channels=16,
        base_channels=32,
        norm_cfg=dict(type='BN1d', eps=1e-05, momentum=0.1),
        more_conv=True,
        out_channels=256),
    decode_head=dict(
        type='_P3FormerHead',
        num_classes=20,
        num_queries=128,
        embed_dims=256,
        point_cloud_range=[0, -3.14159265359, -4, 50, 3.14159265359, 2],
        assigner_zero_layer_cfg=dict(
            type='mmdet.HungarianAssigner',
            match_costs=[
                dict(
                    type='mmdet.FocalLossCost',
                    weight=1.0,
                    binary_input=True,
                    gamma=2.0,
                    alpha=0.25),
                dict(type='mmdet.DiceCost', weight=2.0, pred_act=True)
            ]),
        assigner_cfg=dict(
            type='mmdet.HungarianAssigner',
            match_costs=[
                dict(
                    type='mmdet.FocalLossCost',
                    gamma=4.0,
                    alpha=0.25,
                    weight=1.0),
                dict(
                    type='mmdet.FocalLossCost',
                    weight=1.0,
                    binary_input=True,
                    gamma=2.0,
                    alpha=0.25),
                dict(type='mmdet.DiceCost', weight=2.0, pred_act=True)
            ]),
        sampler_cfg=dict(type='_MaskPseudoSampler'),
        loss_mask=dict(
            type='mmdet.FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,
            reduction='mean',
            loss_weight=1.0),
        loss_dice=dict(type='mmdet.DiceLoss', loss_weight=2.0),
        loss_cls=dict(
            type='mmdet.FocalLoss',
            use_sigmoid=True,
            gamma=4.0,
            alpha=0.25,
            loss_weight=1.0),
        num_decoder_layers=6,
        cls_channels=(256, 256, 20),
        mask_channels=(256, 256, 256, 256, 256),
        thing_class=[0, 1, 2, 3, 4, 5, 6, 7],
        stuff_class=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        ignore_index=19),
    train_cfg=None,
    test_cfg=dict(mode='whole'))
default_scope = 'mmdet3d'
default_hooks = dict(
    timer=dict(type='IterTimerHook'),
    logger=dict(type='LoggerHook', interval=50),
    param_scheduler=dict(type='ParamSchedulerHook'),
    checkpoint=dict(type='CheckpointHook', interval=5),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    visualization=dict(type='Det3DVisualizationHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
    dist_cfg=dict(backend='nccl'))
log_processor = dict(type='LogProcessor', window_size=50, by_epoch=True)
log_level = 'INFO'
load_from = 'pretrain_weight/semantickitti_test_65.3.pth'
resume = False
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=36, val_interval=1)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')
lr = 0.0008
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=dict(type='AdamW', lr=0.0008, weight_decay=0.01))
param_scheduler = [
    dict(
        type='MultiStepLR',
        begin=0,
        end=36,
        by_epoch=True,
        milestones=[24, 32],
        gamma=0.2)
]
custom_imports = dict(
    imports=[
        'p3former.backbones.cylinder3d',
        'p3former.data_preprocessors.data_preprocessor',
        'p3former.decode_heads.p3former_head', 'p3former.segmentors.p3former',
        'p3former.task_modules.samplers.mask_pseduo_sampler',
        'evaluation.metrics.panoptic_seg_metric',
        'datasets.semantickitti_dataset', 'datasets.transforms.loading',
        'datasets.transforms.transforms_3d'
    ],
    allow_failed_imports=False)
launcher = 'pytorch'
work_dir = './work_dirs/p3former_8xb2_3x_semantickitti_trainval'
