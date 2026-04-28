---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preparation
title: 申请相机开发的权限
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 申请相机开发的权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:55+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:711d80c575bee08ae7ea817837ade482a87a18c73f95fc05cc61653a3c0bb907
---

相机应用开发的主要流程包含开发准备、设备输入、会话管理、预览、拍照和录像等。

在开发相机应用时，需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限，需要的权限如下表。在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。

* 使用相机拍摄前，需要申请**ohos.permission.CAMERA**相机权限。
* 当需要使用麦克风同时录制音频时，需要申请**ohos.permission.MICROPHONE**麦克风权限。
* 当需要拍摄的图片/视频显示地理位置信息时，需要申请**ohos.permission.MEDIA\_LOCATION**，来访问用户媒体文件中的地理位置信息。

以上权限均需要配置文件权限声明和通过弹窗向用户申请授权，具体申请方式及校验方式，请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

* 当需要读取图片或视频文件时，请优先使用媒体库[Picker选择媒体资源](photoaccesshelper-photoviewpicker.md)。
* 当需要保存图片或视频文件时，请优先使用[安全控件保存媒体资源](photoaccesshelper-savebutton.md)。

说明

仅应用需要克隆、备份或同步用户公共目录的图片、视频类文件时，可申请ohos.permission.READ\_IMAGEVIDEO、ohos.permission.WRITE\_IMAGEVIDEO权限来读写图片视频文件，申请方式请参考[申请受控权限](declare-permissions-in-acl.md)，通过AGC审核后才能使用。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合[特殊场景](restricted-permissions.md#ohospermissionread_imagevideo)的应用被允许申请受限权限。
