---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-glossary
title: Health Service Kit术语
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > Health Service Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:35d275f6efd3fa1555cab3d8b76cd4f8a527ccb94b7346f7a6e5f3b47c54ec17
---

## A

### Activity Report；实时三环数据

华为运动健康App中展示的实时运动数据，包括步数、活动热量、锻炼时长、活动小时数以及目标类数据。从5.1.1(19)版本开始，开发者可通过readActivityReport接口读取用户授权范围内的实时三环数据，用于在应用内为用户提供运动进度反馈。

## D

### Data Source；数据源

标识运动健康数据来源的应用或设备信息，包含设备名称、类别、制造商、型号等设备信息。每条运动健康数据必须关联数据源信息才能进行保存、读取和删除操作，数据源通过DataSourceId进行关联标识。

### Daily Activities；日常活动

用户在日常生活中产生的活动数据，通过采样数据形式记录，包括步数、热量消耗、移动距离、是否中高强度活动、爬高海拔差、是否站立等指标。该数据源包括手机、手表、手环等多种设备，数据更新频率为10分钟级。

## P

### Permission；权限

访问运动健康服务数据的访问许可，分为读权限和写权限。运动健康服务遵循权限最小化原则，应用只能申请与业务相符的数据权限。用户授权权限与应用申请权限的交集决定了应用实际可操作的数据范围。

### Privacy Authorization；隐私授权

用户同意运动健康服务隐私协议的授权过程。用户首次使用运动健康服务时需要同意隐私协议，该授权依赖运动健康App完成。开发者调用相关接口时若返回隐私未同意错误码，需引导用户打开运动健康App完成隐私授权。

## U

### User Authorization；用户授权

用户主动授权应用访问其运动健康数据的操作过程。用户通过华为账号登录授权界面，自主选择授权的数据类型，可仅授权部分数据权限。用户授权与应用申请权限的交集决定了应用实际可操作的数据范围。

## W

### Workout；运动场景化数据开放能力

穿戴设备与生态应用之间的运动数据实时同步和交互机制。从Lite Wearable 6.1.1(24)版本开始支持，包括运动联动的配置、开启、暂停、恢复、停止，以及数据订阅和融合数据下发等功能，实现运动数据的实时共享。
