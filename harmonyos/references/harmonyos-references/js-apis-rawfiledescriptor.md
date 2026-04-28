---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rawfiledescriptor
title: RawFileDescriptor
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > ArkTS API > global > RawFileDescriptor
category: harmonyos-references
scraped_at: 2026-04-28T08:06:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:241f8d532fb7d15a13507966aee055aa74f413af57e090672b02025dabeab1b4
---

本模块提供rawfile文件所在hap的descriptor信息。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { resourceManager } from '@kit.LocalizationKit'
```

## RawFileDescriptor

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 否 | 否 | 文件描述符。 |
| offset | number | 否 | 否 | 起始偏移量。 |
| length | number | 否 | 否 | 文件长度。 |
