---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adsserviceextensionability
title: "@ohos.advertising.AdsServiceExtensionAbility (广告扩展服务)"
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS API > @ohos.advertising.AdsServiceExtensionAbility (广告扩展服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:459ffd1212df48716a2ccc9123c7f5ed72062df5c79260b1c501638ef1ca46ec
---

本模块为设备厂商提供广告扩展能力，设备厂商可自主实现请求广告的回调。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 约束限制

为保障系统安全性和稳定性，防止 AdsServiceExtensionAbility 滥用系统资源，系统对其能力进行管控，不支持以下模块的引用：

* [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md)
* [@ohos.file.photoAccessHelper (相册管理模块)](arkts-apis-photoaccesshelper.md)
* [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md)
* [@ohos.telephony.sms (短信服务)](js-apis-sms.md)
* [@ohos.contact (联系人)](js-apis-contact.md)

## 导入模块

```typescript
import { RespCallback } from '@kit.AdsKit';
```

## RespCallback

(respData: Map<string, Array<advertising.Advertisement>>): void

广告请求回调。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **名称** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| respData | Map<string, Array<advertising.[Advertisement](js-apis-advertisement.md#advertisement)>> | 是 | 广告请求回调数据，是以广告位ID为键，存储请求到的广告内容的映射集合。 |

**示例：**

```typescript
import { advertising, RespCallback } from '@kit.AdsKit';

function setRespCallback(respCallback: RespCallback) {
  const respData: Map<string, Array<advertising.Advertisement>> = new Map();
  // 设置广告返回数据
  // ...
  respCallback(respData);
}
```
