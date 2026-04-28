---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-getmultipathquota
title: 多网配额查询
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 多网配额查询
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f845bb0aec1dfe3516f8ac7d4e4f8cc2e2f0aad5c11d5227bc6595917cb69ede
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

   ```
   1. import { netHandover } from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取多网配额。

   ```
   1. try {
   2. let multiquota : netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
   3. // 已使用配额次数
   4. console.info('getMultiPathQuotaStats multiPathQuota.used.count is:' + multiquota.used.count)
   5. // 已使用配额时间，单位为秒
   6. console.info('getMultiPathQuotaStats multiPathQuota.used.duration is:' + multiquota.used.duration)
   7. // 剩余配额次数
   8. console.info('getMultiPathQuotaStats multiPathQuota.remaining.count is:' + multiquota.remaining.count)
   9. // 剩余配额时间，单位为秒
   10. console.info('getMultiPathQuotaStats multiPathQuota.remaining.durationis:' + multiquota.remaining.duration)
   11. } catch (err) {
   12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   13. }
   ```
