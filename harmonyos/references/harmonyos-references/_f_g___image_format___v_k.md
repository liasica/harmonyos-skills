---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_format___v_k
title: FG_ImageFormat_VK
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_ImageFormat_VK
category: harmonyos-references
scraped_at: 2026-04-28T08:15:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbe2ad2dfdc2a890363e1ee29036aa4371404b6bb89e6b61d4a873ba04785445
---

## 概述

PhoneTabletTV

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_vk.h](frame__generation__vk_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| VkFormat [inputColorFormat](_f_g___image_format___v_k.md#inputcolorformat) | 真实渲染帧颜色缓冲区图像格式。 |
| VkFormat [inputDepthStencilFormat](_f_g___image_format___v_k.md#inputdepthstencilformat) | 深度模板缓冲区图像格式。 |
| VkFormat [outputColorFormat](_f_g___image_format___v_k.md#outputcolorformat) | 预测帧缓冲区图像格式。 |

## 结构体成员变量说明

PhoneTabletTV

### inputColorFormat

PhoneTabletTV

```
1. VkFormat FG_ImageFormat_VK::inputColorFormat
```

**描述**

真实渲染帧颜色缓冲区图像格式。

### inputDepthStencilFormat

PhoneTabletTV

```
1. VkFormat FG_ImageFormat_VK::inputDepthStencilFormat
```

**描述**

深度模板缓冲区图像格式。

### outputColorFormat

PhoneTabletTV

```
1. VkFormat FG_ImageFormat_VK::outputColorFormat
```

**描述**

预测帧缓冲区图像格式。
