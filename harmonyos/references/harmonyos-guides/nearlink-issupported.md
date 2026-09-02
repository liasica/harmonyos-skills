---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-issupported
title: 查询是否支持星闪
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 查询是否支持星闪
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2d04a1a630c22a604dad257e8b80f8ab48131c2de53a90ce564e262f36c844dd
---

## 场景介绍

从6.1.0(23)版本开始，新增查询是否支持星闪的能力。由于并非所有设备都支持星闪，使用星闪相关功能前可以主动查询当前设备是否支持星闪。

## 接口说明

提供查询当前设备是否支持星闪的方式。

| 接口名 | 描述 |
| --- | --- |
| [isNearLinkSupported](../harmonyos-references/nearlink-manager.md#isnearlinksupported)(): boolean | 主动查询当前设备是否支持星闪。 |

## 开发步骤

**说明** 

可以在设备“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径下，查看当前设备是否支持星闪。

如果在不支持星闪的设备上调用星闪相关接口，可能会返回[801](../harmonyos-references/errorcode-universal.md#section801-该设备不支持此api)错误码。

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { manager } from '@kit.NearLinkKit';
   ```
2. 发起当前设备是否支持星闪的状态查询。

   ```typescript
   try {
     let supported: boolean = manager.isNearLinkSupported();
     // ...
     if (supported) {
       hilog.info(this.domainId, this.logTag, `NearLink is supported on this device.`);
       // ...
     } else {
       hilog.info(this.domainId, this.logTag, `NearLink is not supported on this device.`);
       // ...
     }
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
