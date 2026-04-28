---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagementquery
title: Interface (ColorManagementQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ColorManagementQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7505c0c70631d1cea504db52ef8285acde24b0593b7680c57692ebcecd4d8f2c
---

色彩管理类，用于查询色彩空间参数。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## getSupportedColorSpaces12+

PhonePC/2in1TabletTVWearable

getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>

获取支持的色彩空间列表。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace)> | 支持的色彩空间列表。若接口调用失败，返回undefined。 |

**示例：**

```
1. import { colorSpaceManager } from '@kit.ArkGraphics2D';

3. function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
4. let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
5. colorSpaces = session.getSupportedColorSpaces();
6. return colorSpaces;
7. }
```
