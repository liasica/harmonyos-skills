---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-5
title: Pura X设备人脸识别黑屏
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > Pura X设备人脸识别黑屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0387b0d2cd689ac7a108f7b44d2d2805a33f640c05e8bee1a0e71dd9cc881319
---

## 问题现象

PuraX设备内屏人脸识别时，出现黑屏。

## 背景知识

* 折叠屏拉起相机需要根据折叠屏状态选择拉起不同的相机，可以参考：[适配不同折叠状态的摄像头](../harmonyos-guides/camera-foldable-display.md)。
* 在相机位置转换时，可以使用[CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)中的枚举值来表示相机位置，人脸识别功能调用的相机是前置相机，需要使用CAMERA\_POSITION\_FRONT参数。

## 问题定位

* 查看代码中相机转换时使用的相机类型是否是CAMERA\_POSITION\_FRONT。
* 查看应用是否引用了低版本三方SDK。

## 分析结论

若代码中相机转换时使用的相机类型不是CAMERA\_POSITION\_FRONT，则为相机选择错误导致的黑屏。若代码中引用了低版本三方SDK，排查低版本三方SDK是否存在兼容性问题导致黑屏，可以考虑升级三方SDK版本。

## 修改建议

* 在代码中修改人脸识别时调用的相机为CAMERA\_POSITION\_FRONT。
* 升级三方SDK版本。
