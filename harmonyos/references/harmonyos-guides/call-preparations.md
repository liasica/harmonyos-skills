---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/call-preparations
title: 开发准备
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bccea8bdeba848884e7c57f410c13a50fbcbe00ecd00cc6f94f0f13ee9666e24
---

在开通应用内通话服务之前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

## 开通Push Kit（推送服务）

如[与相关Kit的关系](call-introduction.md#与相关kit的关系)所述，开发者在开通Call Service Kit之前，需要开通Push Kit（推送服务），开通方法详见[开通推送服务](push-config-setting.md)。

## 申请权限

开发者需要根据实际场景申请对应权限，具体申请方式请参见[声明权限](declare-permissions.md)。

| 权限 | 使用场景 | 备注 |
| --- | --- | --- |
| [ohos.permission.MICROPHONE](permissions-for-all-user.md#ohospermissionmicrophone) | 用于在语音通话中，使用麦克风。 | 必须申请。 |
| [ohos.permission.CAMERA](permissions-for-all-user.md#ohospermissioncamera) | 用于在视频通话中，使用相机。 | 如果应用支持视频通话业务，则需要申请。 |

## 示例代码

该指南涉及到的示例代码均为片段，全量示例代码请参考：[Samplecode](https://gitcode.com/harmonyos_samples/callkit-samplecode-voipdemo-arkts)。
