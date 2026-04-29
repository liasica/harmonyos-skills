---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-image-feature-picker-c
title: 接入全局取色
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发指导（C/C++） > 接入全局取色
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a854e05da139a4c1ff921b68e60c1a0fed3485184200c6e361a4667bf0695a0
---

接入全局取色功能，用户可以使用手指或者手写笔操作取色器在屏幕上移动，在目标位置抬起手指/抬起手写笔，会生成该位置色值对应的图像信息。

## 场景介绍

在应用中拉起全局取色，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/hH5VAznjS8iVsb90_uzqRQ/zh-cn_image_0000002558764978.png?HW-CC-KV=V1&HW-CC-Date=20260429T053336Z&HW-CC-Expire=86400&HW-CC-Sign=431D4FA3852537CE963AE2C16551DC34640686D9B2D5ED7361AF5A05BBB3FF69)

支持获取当前屏幕上选中位置的色值和色域空间。

## 限制与约束

全局取色能力支持设备：Tablet、PC/2in1，并且从5.1.1(19)版本开始，新增支持设备：Phone（只支持部分机型）。

## 接口说明

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_GCP\_StartColorPicker](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_startcolorpicker) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_onresult) onResultCallback, void \*userData) | 启动取色器。此API用于启动取色器，在取色器移动时不显示色值。 |
| int32\_t [HMS\_GCP\_StartColorPickerWithColorValue](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_startcolorpickerwithcolorvalue) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_onresult) onResultCallback, void \*userData) | 启动取色器。此API用于启动取色器，在取色器移动时显示色值。 |

## 接入步骤

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libcolorpicker_ndk.z.so  libhilog_ndk.z.so)
```

### 导入模块

```
1. #include "color_picker/native_gcp_api.h"
2. #include "hilog/log.h"
```

### 示例代码

native\_gcp\_api.h提供HMS\_GCP\_StartColorPicker()和HMS\_GCP\_StartColorPickerWithColorValue()两种方式启动全局取色功能。

通过调用HMS\_GCP\_StartColorPicker()，实现启动取色器。

注意

该启动方法不支持实时显示色值。

```
1. void onSuccessCallback(void *userData, HMS_GCP_PickedColorInfo pickedColorInfo, const int32_t code) {
2. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked code is: %{public}d", code);
3. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Red is: %{public}d", pickedColorInfo.color.red);
4. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Green is:%{public}d ", pickedColorInfo.color.green);
5. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Blue is: %{public}d", pickedColorInfo.color.blue);
6. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Alpha is:%{public}d ", pickedColorInfo.color.alpha);
7. delete userData;
8. }
9. void startPick() {
10. int32_t posX = 200;
11. int32_t posY = 200;
12. void *userData = nullptr;
13. HMS_GCP_StartColorPicker(posX, posY, onSuccessCallback, userData);
14. }
```

通过调用HMS\_GCP\_StartColorPickerWithColorValue()，实现启动取色器。

注意

该启动方法支持实时显示色值。

```
1. void onSuccessCallback(void *userData, HMS_GCP_PickedColorInfo pickedColorInfo, const int32_t code) {
2. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked code is: %{public}d", code);
3. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Red is: %{public}d", pickedColorInfo.color.red);
4. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Green is:%{public}d ", pickedColorInfo.color.green);
5. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Blue is: %{public}d", pickedColorInfo.color.blue);
6. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Alpha is:%{public}d ", pickedColorInfo.color.alpha);
7. delete userData;
8. }
9. void startPickWithColorValue() {
10. int32_t posX = 200;
11. int32_t posY = 200;
12. void *userData = nullptr;
13. HMS_GCP_StartColorPickerWithColorValue(posX, posY, onSuccessCallback, userData);
14. }
```
