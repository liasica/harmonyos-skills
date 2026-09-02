---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-25
title: 应用拍摄出现偏色如何解决
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 应用拍摄出现偏色如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:adff5ee6de3b014a8c4e51984803a6918e9de700d59ebffeb0a172603f286d3d
---

## 问题现象

应用强光环境下使用自定义相机拍照，效果偏白。

## 背景知识

* 白平衡：主要用于调整图像中的颜色平衡，确保在不同光源下拍摄的照片或视频能够呈现出自然的白色，白平衡的调整可以有效地去除图像中的偏色现象，使图像看起来更加真实和美观。
* [AutoExposure](../harmonyos-references/arkts-apis-camera-autoexposure.md)：自动曝光类，对设备自动曝光（AE）操作。用于调整图像的亮度，允许摄影师根据拍摄环境的光线条件手动调整图像的明暗程度，确保照片能够正确地表现景物的细节。
* [setWhiteBalanceMode](../harmonyos-references/arkts-apis-camera-whitebalance.md#setwhitebalancemode20)：设置白平衡模式。

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | mode | [WhiteBalanceMode](../harmonyos-references/arkts-apis-camera-e.md#whitebalancemode20) | 是 | 设置相机中的白平衡模式，如自动、阴天、白炽光等模式。 |
* [setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)：设置色彩空间。

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | colorSpace | [colorSpaceManager.ColorSpace](../harmonyos-references/js-apis-colorspacemanager.md#colorspace) | 是 | 色彩空间，通过[getSupportedColorSpaces](../harmonyos-references/arkts-apis-camera-colormanagementquery.md#getsupportedcolorspaces12)接口获取。 |

## 问题定位

1. 应用中全局搜索setWhiteBalanceMode，查看有无白平衡模式的相关设置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/VD-KFqOdQHurSZm8tZKgLg/zh-cn_image_0000002628552462.png "点击放大")
2. 相机在背光情况下拍摄时，需要增加曝光补偿以照亮主体；而在强光环境下，需要减少曝光补偿以避免画面过度曝光。应用中全局搜索[setExposureBias](../harmonyos-references/arkts-apis-camera-autoexposure.md#setexposurebias11)，查看有无曝光补偿的相关设置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/4jyae98kRIqHc7C_-Q1pqw/zh-cn_image_0000002658911785.png "点击放大")

## 分析结论

用户在强光环境下拍照，应用未进行白平衡及曝光补偿的优化设置，导致拍摄的照片效果偏白。

## 修改建议

1. 强光环境下，应用根据光线环境，通过setWhiteBalanceMode接口设置合适的[白平衡模式](../harmonyos-references/arkts-apis-camera-e.md#whitebalancemode20)或者通过[setWhiteBalance](../harmonyos-references/arkts-apis-camera-whitebalance.md#setwhitebalance20)接口设置白平衡值。
2. 强光环境下，应用需要减少曝光补偿以避免画面过度曝光，通过setExposureBias设置曝光补偿值。

## 常见FAQ

Q：设置了正确的曝光和白平衡模式之后，为什么还会有偏色？

A：代码中未使用setColorSpace来设置色彩空间，此时画面默认为SDR拍摄效果，容易产生画面偏色问题。
