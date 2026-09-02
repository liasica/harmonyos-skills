---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-getmultipathquota
title: 多网配额查询
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 多网配额查询
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:bbe8166b20917226cb4e687dbe45ba750d3a079ffe2dfb675b25568d604c2200
---

## 场景介绍

由于多网络加速受到配额的管控，应用可以获取当前剩余的多网并发配额信息，合理分配使用多网络加速的次数和时长。应用配额以24小时的周期进行刷新。配额（次数或时长）耗尽会限制使用，此时请求多网会抛出错误码，24小时后会重新分配。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-nethandover.md#nethandovergetmultipathquotastats)。

| 接口名 | 描述 |
| --- | --- |
| getMultiPathQuotaStats(): MultiPathQuota | 获取多网配额。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```typescript
   import { netHandover } from '@kit.NetworkBoostKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取多网配额。

   ```typescript
   try {
     let multiquota : netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
     // 已使用配额次数
     console.info('getMultiPathQuotaStats multiPathQuota.used.count is:' + multiquota.used.count)
     // 已使用配额时间，单位为秒
     console.info('getMultiPathQuotaStats multiPathQuota.used.duration is:' + multiquota.used.duration)
     // 剩余配额次数
     console.info('getMultiPathQuotaStats multiPathQuota.remaining.count is:' + multiquota.remaining.count)
     // 剩余配额时间，单位为秒
     console.info('getMultiPathQuotaStats multiPathQuota.remaining.duration is:' + multiquota.remaining.duration)
   } catch (err) {
     console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   }
   ```
