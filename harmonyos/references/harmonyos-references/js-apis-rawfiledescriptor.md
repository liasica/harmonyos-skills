---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rawfiledescriptor
title: RawFileDescriptor
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > ArkTS API > global > RawFileDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:01:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bade894f8bb3a9bafb7251afd4aa70dc21e2b81e24056b1ad4eb34ea876c97ee
---

本模块提供rawfile文件所在HAP包的文件描述符信息，包括文件描述符、rawfile文件的起始偏移和文件长度。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { resourceManager } from '@kit.LocalizationKit'
```

## RawFileDescriptor

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 否 | 否 | 文件描述符。 |
| offset | number | 否 | 否 | 起始偏移量，表示rawfile文件在HAP包中的起始位置。单位为Byte。 |
| length | number | 否 | 否 | 文件长度，表示rawfile文件的大小。单位为Byte。 |
