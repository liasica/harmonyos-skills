---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-photoaccesshelper-mediaassetprogresshandler
title: Interface (MediaAssetProgressHandler)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (MediaAssetProgressHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:17+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:40cbda1a89c63dc74c034674edb41f41bf759463d3d4ec62b96df15b39e72072
---

媒体资产进度处理器，应用于onProgress方法中获取媒体资产进度。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 15开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onProgress15+

PhonePC/2in1TabletTV

onProgress(progress: number): void

当所请求的视频资源返回进度时系统会回调此方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | 返回的进度百分比，范围为[0, 100]。 |
