---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-image-feature-picker-c
title: 接入全局取色
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发指导（C/C++） > 接入全局取色
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:28+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:221df84f323b98cd3b624e1a3d82aed8ec7f4cbc16538e1f87f1cd97527f56c1
---

接入全局取色功能，用户可以使用手指或者手写笔操作取色器在屏幕上移动，在目标位置抬起手指/抬起手写笔，会生成该位置色值对应的图像信息。

## 场景介绍

在应用中拉起全局取色，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/llHoHMlSRAuSoNAch-9AEQ/zh-cn_image_0000002806108981.png)

支持获取当前屏幕上选中位置的色值和色域空间。

## 约束与限制

全局取色能力支持设备：Tablet、PC/2in1，并且从5.1.1(19)版本开始，新增支持设备：Phone（只支持部分机型）。

## 接口说明

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_GCP\_StartColorPicker](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_startcolorpicker) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_onresult) onResultCallback, void \*userData) | 启动取色器。取色器移动时不显示色值。 |
| int32\_t [HMS\_GCP\_StartColorPickerWithColorValue](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_startcolorpickerwithcolorvalue) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_onresult) onResultCallback, void \*userData) | 启动取色器。取色器移动时显示色值。 |

## 开发步骤

1. 在CMake脚本中链接动态库。

   ```c
   target_link_libraries(entry PUBLIC libace_napi.z.so libcolorpicker_ndk.z.so  libhilog_ndk.z.so)
   ```
2. 导入模块。

   ```c
   #include "color_picker/native_gcp_api.h"
   #include "hilog/log.h"
   ```
3. 调用相关接口，实现启动全局取色器。

   native\_gcp\_api.h提供HMS\_GCP\_StartColorPicker()和HMS\_GCP\_StartColorPickerWithColorValue()两种方式启动全局取色功能。

   * 调用[HMS\_GCP\_StartColorPicker()](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_startcolorpicker)，在取色器移动时不显示色值。
   * 调用[HMS\_GCP\_StartColorPickerWithColorValue()](../harmonyos-references/pen-imagefeaturepicker-c.md#hms_gcp_startcolorpickerwithcolorvalue)，在取色器移动时显示色值。

     ```
     // 公共回调函数。
     void onSuccessCallback(void *userData, HMS_GCP_PickedColorInfo pickedColorInfo, const int32_t code) {
         OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked code is: %{public}d", code);
         OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Red is: %{public}d", pickedColorInfo.color.red);
         OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Green is:%{public}d ", pickedColorInfo.color.green);
         OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Blue is: %{public}d", pickedColorInfo.color.blue);
         OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "penkit", "picked Alpha is:%{public}d ", pickedColorInfo.color.alpha);
         delete userData;
     }

     // 调用HMS_GCP_StartColorPicker()，在取色器移动时不显示色值。
     void startPick() {
         int32_t posX = 200;
         int32_t posY = 200;
         void *userData = nullptr;
         HMS_GCP_StartColorPicker(posX, posY, onSuccessCallback, userData);
     }

     // 调用HMS_GCP_StartColorPickerWithColorValue()，在取色器移动时显示色值。
     void startPickWithColorValue() {
         int32_t posX = 200;
         int32_t posY = 200;
         void *userData = nullptr;
         HMS_GCP_StartColorPickerWithColorValue(posX, posY, onSuccessCallback, userData);
     }
     ```
