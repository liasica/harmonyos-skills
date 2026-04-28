---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all-user
title: 开放权限（用户授权）
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表 > 开放权限（用户授权）
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cbbe2d4a6a8eebffa69428d8fb839968cc09873ef3d9a98ab6f93dd835e82a47
---

此列表内所有权限均为用户授权（user\_grant）的开放权限，面向所有应用开放。

该类型权限不仅需要在安装包中申请权限，还需要在应用动态运行时，通过发送弹窗的方式请求用户授权。在用户手动允许授权后，应用才会真正获取相应权限，从而成功访问操作目标对象。

## 申请方式

以下权限的授权方式均为[user\_grant（用户授权）](app-permission-mgmt-overview.md#user_grant用户授权)，申请方式请参考[声明权限](declare-permissions.md) > [向用户申请授权](request-user-authorization.md)。

## ohos.permission.ACCESS\_BLUETOOTH

允许应用接入蓝牙并使用蓝牙功能。

包括扫描和发现外围蓝牙设备、与外围蓝牙设备配对和连接等操作，同时支持低功耗蓝牙的广播和扫描功能。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：10

## ohos.permission.MEDIA\_LOCATION

允许应用访问用户媒体文件中的地理位置信息。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

## ohos.permission.APP\_TRACKING\_CONSENT

允许应用读取开放匿名设备标识符。

注意

在申请此权限时，是否弹窗向用户请求授权，取决于“要求应用请求关联”的开关状态。

* 如果开关关闭，当应用请求权限时，系统不会弹窗，默认授予应用权限。
* 如果开关开启，当应用请求权限时，系统将弹窗，需要用户确认才能授予应用权限。

“要求应用请求关联”的开关状态可在“设置 > 隐私与安全 > 跨应用关联”页面中查看。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.ACTIVITY\_MOTION

允许应用读取用户的运动状态。

例如，判断用户是否处于运动中、记录用户行走步数。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

## ohos.permission.CAMERA

允许应用使用相机。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.DISTRIBUTED\_DATASYNC

允许不同设备间的数据交换。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

## ohos.permission.LOCATION\_IN\_BACKGROUND

允许应用在后台运行时获取设备位置信息。

**申请流程**：

1. 在“module.json5”配置文件中[声明权限](declare-permissions.md)。

   由于在申请后台位置权限前，必须先申请前台位置权限，因此开发者在配置时，应同时配置后台位置权限和前台位置权限。前台位置权限的申请有两种允许情况：

   * 申请前台模糊位置权限：声明权限[ohos.permission.APPROXIMATELY\_LOCATION](permissions-for-all-user.md#ohospermissionapproximately_location)。
   * 申请前台精确位置权限：同时声明权限[ohos.permission.APPROXIMATELY\_LOCATION](permissions-for-all-user.md#ohospermissionapproximately_location)和[ohos.permission.LOCATION](permissions-for-all-user.md#ohospermissionlocation)。
2. 应用调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)拉起弹窗向用户申请对应的前台位置权限。
3. 若用户点击弹窗允许应用使用前台位置权限，应用可以引导用户在系统应用“设置”中，授予后台位置权限；若用户点击弹窗禁止应用使用前台位置权限，应用可以引导用户在系统应用“设置”中授权，或通过调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)再次拉起权限设置弹窗，引导用户授权。

当前系统提供了长时任务机制，对于需要在后台使用位置的应用，结合自身业务场景，可通过申请LOCATION类型的长时任务和前台位置权限的方式在后台获取位置，而不必申请后台位置权限。请参考：[长时任务指导](continuous-task.md)。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

## ohos.permission.LOCATION

允许应用获取设备位置信息。

**申请条件**：需要与模糊位置权限[ohos.permission.APPROXIMATELY\_LOCATION](permissions-for-all-user.md#ohospermissionapproximately_location)一起，才可申请此权限。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

## ohos.permission.APPROXIMATELY\_LOCATION

允许应用获取设备模糊位置信息。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.MICROPHONE

允许应用使用麦克风。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：8

## ohos.permission.READ\_CALENDAR

允许应用读取日历信息。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：8

## ohos.permission.WRITE\_CALENDAR

允许应用添加、移除或更改日历活动。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：8

## ohos.permission.READ\_HEALTH\_DATA

允许应用读取用户的健康数据。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

## ohos.permission.ACCESS\_NEARLINK

允许应用接入星闪并使用星闪能力，例如配对、连接外围设备等。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：12

## ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY

允许应用访问公共目录下Download目录及子目录。

说明

该权限级别发生变更，为保证兼容性，在当前版本请继续采用[受限权限申请方式](declare-permissions-in-acl.md)申请使用该权限。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**支持设备**：PC/2in1 | Tablet

**起始版本**：11

**变更信息：** API 11，权限级别为system\_basic；从API 12开始，变更为normal。

## ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY

允许应用访问公共目录下的Documents目录及子目录。

说明

该权限级别发生变更，为保证兼容性，在当前版本请继续采用[受限权限申请方式](declare-permissions-in-acl.md)申请使用该权限。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**支持设备**：PC/2in1 | Tablet

**起始版本**：11

**变更信息：** API 11，权限级别为system\_basic；从API 12开始，变更为normal。

## ohos.permission.CUSTOM\_SCREEN\_CAPTURE

允许应用获取屏幕图像。

应用获取此权限后，可进行截屏等操作。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**支持设备**：PC/2in1 | Tablet | Phone

**起始版本**：14

**变更信息**：API 14-20，该权限仅支持在平板、PC/2in1设备上申请；从API 21开始，增加支持在手机上申请。

## ohos.permission.READ\_MEDIA

允许应用读取用户外部存储中的媒体文件信息。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

**废弃版本**：22

**替代方案**：

请参考[文件权限组废弃替代方案](app-permission-group-list.md#文件deprecated)。

## ohos.permission.WRITE\_MEDIA

允许应用读写用户外部存储中的媒体文件信息。

**权限级别**：normal

**授权方式**：用户授权（user\_grant）

**起始版本**：7

**废弃版本**：22

**替代方案**：

请参考[文件权限组废弃替代方案](app-permission-group-list.md#文件deprecated)。
