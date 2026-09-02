---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-getstate
title: 查询星闪开关状态
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 查询星闪开关状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5e552e303798d2161bdf5da70eb7482104245a5855e86339dbb607434750468c
---

## 场景介绍

使用星闪前需要在设置应用里手动打开星闪。可以通过主动查询或订阅通知方式获取星闪状态，星闪状态变化为STATE\_ON时可以进行相应的业务流程。

## 接口说明

提供2种获取星闪开关状态的方式，主动查询和订阅状态变化。

| 接口名 | 描述 |
| --- | --- |
| [getState](../harmonyos-references/nearlink-manager.md#getstate)(): NearlinkState | 主动查询星闪开关状态。 |
| [on](../harmonyos-references/nearlink-manager.md#on-statechange)(type: 'stateChange', callback: Callback<NearlinkState>): void | 订阅星闪开关状态变化事件。使用callback异步回调。 |
| [off](../harmonyos-references/nearlink-manager.md#off-statechange)(type: 'stateChange', callback?: Callback<NearlinkState>): void | 取消订阅星闪开关状态变化事件。使用callback异步回调。 |

## 开发步骤

**说明** 

可以在设备“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径下，打开或关闭星闪，触发开关状态的变化。

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { manager } from '@kit.NearLinkKit';
   ```
2. 发起星闪状态查询。

   ```typescript
   try {
     let state: manager.NearlinkState = manager.getState();
     hilog.info(this.domainId, this.logTag, `NearLink state: ${JSON.stringify(state)}`);
     // ...
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 或者通过注册的方式订阅星闪开关状态变化。

   ```typescript
   let onReceiveEvent: (data: manager.NearlinkState) => void = (data: manager.NearlinkState) => {
     hilog.info(this.domainId, this.logTag, `NearLink state changed: ${JSON.stringify(data)}`);
     // ...
   };
   try {
     manager.on('stateChange', onReceiveEvent);
     hilog.info(this.domainId, this.logTag, `Subscribed to stateChange`);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
4. 取消订阅星闪开关状态变化，其中onReceiveEvent是步骤3中定义的回调函数。

   ```typescript
   try {
     manager.off('stateChange');
     hilog.info(this.domainId, this.logTag, `Unsubscribed from stateChange`);
   } catch (err) {
     hilog.error(this.domainId, this.logTag,
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
