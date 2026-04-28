---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-issupported
title: 查询是否支持星闪服务
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 查询是否支持星闪服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2415f0a6f99cd9547c498d3a7820b329c5e4710d311b6e7c8440ffc92caa5bac
---

## 场景介绍

从6.1.0(23)版本开始，新增查询是否支持星闪服务的能力。由于并非所有设备都支持星闪，使用星闪相关功能前可以主动查询当前设备是否支持星闪服务。

## 接口说明

提供查询当前设备是否支持星闪服务的方式。

| 接口名 | 描述 |
| --- | --- |
| [isNearLinkSupported](../harmonyos-references/nearlink-manager.md#isnearlinksupported)(): boolean | 主动查询当前设备是否支持星闪。 |

## 开发步骤

说明

可以在设备“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径下，查看当前设备是否支持星闪服务。

如果在不支持星闪的设备上调用星闪相关接口，可能会返回[801](../harmonyos-references/errorcode-universal.md#section801-该设备不支持此api)错误码。

1. 导入相关模块。

   ```
   1. import { manager } from '@kit.NearLinkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 发起当前设备是否支持星闪的状态查询。

   ```
   1. try {
   2. let isSupported: boolean = manager.isNearLinkSupported();
   3. if (isSupported) {
   4. console.info('NearLink is supported on this device.');
   5. } else {
   6. console.info('NearLink is not supported on this device.');
   7. }
   8. } catch (err) {
   9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   10. }
   ```
