---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-appreportqoe
title: 应用传输体验反馈
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 > 应用传输体验反馈
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:103f3d0292298e739eba398da66f62fc2d926112d27f2e9a1ff70018a8c9e83e
---

## 场景介绍

当应用传输体验发生变化时，应用将传输体验和传输的业务类型信息通过实时反馈接口传输给系统网络业务模块，系统网络业务模块进行精细化调度，实现网络加速。

例如：视频类App播放过程中卡顿，将卡顿信息上报后，Network Boost Kit将信息反馈给系统网络加速模块，该模块会记录播放卡顿信息，并根据当前网络情况，启用网络加速能力。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-netquality.md#netqualityreportqoe)。

| 接口名 | 描述 |
| --- | --- |
| reportQoe(appQoe: AppQoe): void | 应用反馈传输体验信息。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. import { netQuality } from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用reportQoe接口将应用传输体验信息通知给系统。

   ```
   1. try{
   2. let serviceType: netQuality.ServiceType = 'shortVideo';
   3. let qoeType: netQuality.BadQoeCause = 'serverErr';
   4. let appQoE: netQuality.AppQoe = {
   5. serviceType,
   6. qoeType
   7. };
   8. netQuality.reportQoe(appQoE);
   9. } catch (err) {
   10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   11. }
   ```
