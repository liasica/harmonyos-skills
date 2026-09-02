---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-27
title: 视频通话时切换摄像头，画面呈现异常颜色
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 视频通话时切换摄像头，画面呈现异常颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8eb033a718670567a544831ad64bd05f15b513eeb643d94c2a296ac6c9870c85
---

## 问题现象

视频通话时切换摄像头，画面呈现异常颜色，不符合用户使用习惯。

## 背景知识

* 偏色是指因光线反射、显影处理不当或设备设置误差导致图像色彩偏离真实的现象，常见于照片拍摄、扫描及打印等环节。
* [setWhiteBalanceMode](../harmonyos-references/arkts-apis-camera-whitebalance.md#setwhitebalancemode20)：设置白平衡模式。

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | mode | [WhiteBalanceMode](../harmonyos-references/arkts-apis-camera-e.md#whitebalancemode20) | 是 | 白平衡模式。 |
* [setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)：设置色彩空间。

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | colorSpace | [colorSpaceManager.ColorSpace](../harmonyos-references/js-apis-colorspacemanager.md#colorspace) | 是 | 色彩空间，通过[getSupportedColorSpaces](../harmonyos-references/arkts-apis-camera-colormanagementquery.md#getsupportedcolorspaces12)接口获取。 |

## 问题定位

1. 排查代码中是否设置了setWhiteBalanceMode来开启白平衡模式。未开启白平衡模式，画面颜色校正不准，导致视频通话时切换摄像头，画面偏色。
2. 排查代码中是否使用setColorSpace来设置色彩空间，未设置的话，画面默认为SDR拍摄效果，容易产生画面偏色问题。

## 分析结论

1. 未设置setWhiteBalanceMode开启白平衡模式，导致视频通话时切换摄像头，画面偏色。
2. 未使用setColorSpace来设置色彩空间，导致视频通话时切换摄像头，画面偏色。

## 修改建议

[自定义相机功能](https://gitee.com/harmonyos_samples/CustomCamera)中使用[setWhiteBalanceMode](../harmonyos-references/arkts-apis-camera-whitebalance.md#setwhitebalancemode20)开启白平衡模式和[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)设置色彩空间，支持P3广色域以及HDR的功能。
