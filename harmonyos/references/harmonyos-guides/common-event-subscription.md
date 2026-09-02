---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-subscription
title: 动态订阅公共事件
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 动态订阅公共事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a6a44eaa9e8e31a2ff95905195cf1d7adbc9df1bb2973960610a831f2723397c
---

## 场景介绍

动态订阅是指当应用在运行状态时对某个公共事件进行订阅，在运行期间如果有订阅的事件发布，订阅了这个事件的应用将会收到该事件及其传递的参数。

例如，某应用希望在其运行期间收到电量过低的事件，并根据该事件降低其运行功耗，那么该应用便可动态订阅电量过低事件，收到该事件后关闭一些非必要的任务来降低功耗。

订阅部分系统公共事件需要先[申请权限](determine-application-mode.md)，订阅这些事件所需要的权限请见[系统定义的公共事件](../harmonyos-references/commoneventmanager-definitions.md)。

**说明** 

订阅者对象的生命周期需要接入方管理，不再使用时需[取消动态订阅公共事件](common-event-unsubscription.md)后主动销毁释放，避免进程内订阅者数量超过200个导致其他业务订阅失败以及内存泄漏。

动态订阅的公共事件回调受应用状态影响。当应用处于后台时，无法接收到动态订阅公共事件。当应用从后台切换到前台时，最多可以回调切回前30s内监听的公共事件。

分身应用与主应用之间的公共事件相互隔离，相互无法接收到对方发送的公共事件。

## 接口说明

详细接口见[@ohos.commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md)。

| 接口名 | 接口描述 |
| --- | --- |
| [createSubscriber](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber)(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void | 创建订阅者对象（callback）。 |
| [createSubscriber](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber-1)(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber> | 创建订阅者对象（promise）。 |
| [subscribe](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagersubscribe)(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void | 订阅公共事件。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = 'ProcessModel';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 创建订阅者信息，详细的订阅者信息数据类型及包含的参数请见[CommonEventSubscribeInfo](../harmonyos-references/js-apis-inner-commonevent-commoneventsubscribeinfo.md)文档介绍。

   * 自定义公共事件：应用定义的公共事件。

     ```typescript
     // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
     let subscriberCustom: commonEventManager.CommonEventSubscriber | null = null;
     // 订阅者信息，其中的'event'字段需要替换为实际的事件名称。
     let subscribeInfoCustom: commonEventManager.CommonEventSubscribeInfo = {
       events: ['event']  // 订阅自定义公共事件
     };
     ```
   * 系统公共事件：CES内部定义的公共事件，当前仅支持系统应用和系统服务发布，例如HAP安装、更新、卸载等公共事件。目前支持的系统公共事件请参见[系统定义的公共事件](../harmonyos-references/commoneventmanager-definitions.md)。

     ```typescript
     // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
     let subscriberSystem: commonEventManager.CommonEventSubscriber | null = null;
     // 订阅者信息，按需替换对应的公共事件。
     let subscribeInfoSystem: commonEventManager.CommonEventSubscribeInfo = {
       events: [commonEventManager.Support.COMMON_EVENT_SCREEN_OFF]  // 订阅灭屏公共事件
     };
     ```
3. 创建订阅者，保存返回的订阅者对象subscriber，用于执行后续的订阅、退订、接收事件回调等操作。

   ```typescript
   // 创建订阅者回调
   commonEventManager.createSubscriber(subscribeInfoCustom,
     (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
       if (err) {
         hilog.error(DOMAIN_NUMBER, TAG,
           `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
         return;
       }
       hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in creating subscriber.');
       subscriberCustom = data;
     })
   ```
4. 创建订阅回调函数，订阅回调函数会在接收到事件时触发。订阅回调函数返回的data内包含了公共事件的名称、发布者携带的数据等信息，公共事件数据的详细参数和数据类型请见[CommonEventData](../harmonyos-references/js-apis-inner-commonevent-commoneventdata.md)文档介绍。

   ```typescript
   // 订阅公共事件回调
   if (subscriberCustom !== null) {
     commonEventManager.subscribe(subscriberCustom,
       (err: BusinessError, data: commonEventManager.CommonEventData) => {
         if (err) {
           hilog.error(DOMAIN_NUMBER, TAG,
             `Failed to subscribe common event. Code is ${err.code}, message is ${err.message}`);
           return;
         }
         hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in subscribing, data is ${JSON.stringify(data)}`);
       })
   } else {
     hilog.error(DOMAIN_NUMBER, TAG, `Need create subscriber`);
   }
   ```

## 示例代码

* [公共事件的订阅和发布](https://gitcode.com/HarmonyOS_Samples/custom-common-event)
