---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-customization-customconfig
title: @ohos.customization.customConfig (定制配置)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.customization.customConfig (定制配置)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a493d0234d582c660d1eb054b83d6f846184afbdc392279ca4416248adb4c87e
---

本模块接口为应用提供定制配置的获取能力，如渠道号等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { customConfig } from '@kit.BasicServicesKit';
```

## customConfig.getChannelId

PhonePC/2in1TabletTVWearable

getChannelId(): string

获取应用的预装渠道号。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

\*\*系统能力：\*\*SystemCapability.Customization.CustomConfig

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 渠道号 |

**示例：**

```
1. import { customConfig } from '@kit.BasicServicesKit';

3. let channelId: string = customConfig.getChannelId();
4. console.info('app channelId is ' + channelId);
```
