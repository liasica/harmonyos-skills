---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/display-specification
title: 显示规格
breadcrumb: 指南 > 应用体验建议 > 应用基础功能和兼容性体验建议 > 系统特性与基础功能 > 显示规格
category: harmonyos-guides
scraped_at: 2026-09-30T07:35:45+08:00
doc_updated_at: 2026-09-29
content_hash: sha256:b5da5f34f577d89cf5a3def81362f1bf42c7a76c63967c8fd800ebbe54218fc3
---

## 图片色域管理

|  |  |
| --- | --- |
| **描述** | 应用/元服务，图片送显时建议做正确的色域转换和色域信息传递，保证系统能正确的处理颜色； |
| **类型** | 建议 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机，智能穿戴，轻量级智能穿戴 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | 图片色域信息，如P3，sRGB等见[ColorSpace](../harmonyos-references/arkts-apis-image-pixelmap.md#applycolorspace11) |

## HDR视频显示

|  |  |
| --- | --- |
| **描述** | 应用/元服务，正确显示HDR效果或SDR效果； |
| **类型** | 建议 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机，智能穿戴，轻量级智能穿戴 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | HDR视频要正确转到SDR显示或传递正确的Metadata和色域信息； |

## HDR图片显示

|  |  |
| --- | --- |
| **描述** | 应用/元服务，正确显示HDR效果或SDR效果； |
| **类型** | 建议 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机，智能穿戴，轻量级智能穿戴 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | HDR图片要正确转到SDR显示或传递正确的Metadata和色域信息； |

## 图像位宽设置

|  |  |
| --- | --- |
| **描述** | 应用/元服务，不建议使用RGB565格式送显； |
| **类型** | 建议 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机，智能穿戴，轻量级智能穿戴 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | RGB565精度低，通常会有色阶现象，不建议使用；推荐使用RGB888, 见[PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7) |

## 清晰度管理

|  |  |
| --- | --- |
| **描述** | 应用/元服务，不建议配置NONE档位插值算法实现缩放 |
| **类型** | 建议 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机，智能穿戴，轻量级智能穿戴 |
| **应用形态适用性** | 鸿蒙应用，鸿蒙元服务 |
| **说明** | NONE插值对应Nearest算法，通常会引入锯齿现象，不建议使用；见**[ImageInterpolation](../harmonyos-references/ts-basic-components-image.md#imageinterpolation)** |
