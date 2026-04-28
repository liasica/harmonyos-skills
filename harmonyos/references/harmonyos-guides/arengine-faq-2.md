---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-2
title: 摄像头被遮挡一段时间后再放开，输出的位姿有跳变
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 摄像头被遮挡一段时间后再放开，输出的位姿有跳变
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:59d212a828dbfc451cd8fd8e26f015ac5d7af9f66fa6e0265967b5eac2edc1d6
---

## 现象描述

使用运动跟踪能力时，摄像头被遮挡一段时间后再放开遮挡，调用[HMS\_AREngine\_ARPose\_GetPoseRaw](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_getposeraw)函数获取的平移分量或旋转分量存在较大跳变。

## 可能原因

AR Engine通过摄像头采集数据感知当前设备在现实世界中的位姿，摄像头被遮挡后，AR Engine无法准确感知设备在现实世界的位姿变化，放开遮挡后，如果继续调用[HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update)，AR Engine会尝试基于遮挡前识别到的数据进行恢复，如果当前摄像头采集数据和遮挡前类似，就可能会导致错误匹配到旧的结果，从而产生数据跳变。

## 处理步骤

如果开发者通过[HMS\_AREngine\_ARCamera\_GetTrackingState](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstate)函数获取的状态为ARENGINE\_TRACKING\_STATE\_PAUSED，可以通过函数[HMS\_AREngine\_ARCamera\_GetTrackingStateReason](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstatereason)进一步获取暂停原因，如暂停原因是ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES或ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION，建议在您的应用中提示用户，并在恢复后（[HMS\_AREngine\_ARCamera\_GetTrackingState](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_gettrackingstate)获取的状态为：ARENGINE\_TRACKING\_STATE\_TRACKING时）重新做session初始化，见：[创建AR会话](arengine-c-arsession.md#创建ar会话)。
