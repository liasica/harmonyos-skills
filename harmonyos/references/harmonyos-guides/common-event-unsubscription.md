---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-unsubscription
title: 取消动态订阅公共事件
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 取消动态订阅公共事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0579f3528eea0171d945fa4cbc65aecc4bf579a9cc0f229bd6b69ccf116965fb
---

## 场景介绍

动态订阅者完成业务需求后，应主动取消订阅。通过调用[unsubscribe()](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerunsubscribe)方法，取消订阅事件。

## 接口说明

| 接口名 | 接口描述 |
| --- | --- |
| [unsubscribe](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerunsubscribe)(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>) | 取消订阅公共事件。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = 'ProcessModel';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 根据[动态订阅公共事件](common-event-subscription.md)章节的步骤来订阅某个事件。
3. 调用CommonEvent中的[unsubscribe()](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerunsubscribe)方法取消订阅某事件。

   ```typescript
   // subscriberCustom为订阅事件时创建的订阅者对象
   if (subscriberCustom !== null) {
     commonEventManager.unsubscribe(subscriberCustom, (err: BusinessError) => {
       if (err) {
         hilog.error(DOMAIN_NUMBER, TAG,
           `Failed to unsubscribe. code is ${err.code}, message is ${err.message}`);
       } else {
         hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in unsubscribing.`);
         subscriberCustom = null;
       }
     })
   }
   ```
