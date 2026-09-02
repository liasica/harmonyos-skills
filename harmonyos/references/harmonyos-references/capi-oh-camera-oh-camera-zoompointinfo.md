---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-zoompointinfo
title: OH_Camera_ZoomPointInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > OH_Camera_ZoomPointInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2130352bcb55480fc9d1f6874b24db0432f0089a299cd8ea664ec83789baabc6
---

```c
typedef struct OH_Camera_ZoomPointInfo {...} OH_Camera_ZoomPointInfo
```

## 概述

描述变焦点信息。

**起始版本：** 26.0.0

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float zoomRatio | 变焦比例。  **起始版本：** 26.0.0 |
| uint32\_t equivalentFocalLength | 等效焦距。  **起始版本：** 26.0.0 |
