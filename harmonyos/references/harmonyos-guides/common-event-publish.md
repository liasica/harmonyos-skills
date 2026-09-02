---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-publish
title: 发布公共事件
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 发布公共事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:45c8587c274dcd0df096d7804c934b3ca399a94ce9ec942c0525e797c614ef8f
---

## 场景介绍

当需要发布某个公共事件时，可以通过[publish()](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerpublish)方法发布事件。发布的公共事件可以携带数据，供订阅者解析并进行下一步处理。

**须知** 

已发出的粘性公共事件后来订阅者也可以接收到，其他公共事件都需要先订阅再接收，订阅参考[公共事件订阅章节](common-event-subscription.md)。

## 接口说明

详细接口见[接口文档](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerpublish)。

| 接口名 | 接口描述 |
| --- | --- |
| publish(event: string, callback: AsyncCallback<void>) | 发布公共事件。 |
| publish(event: string, options: [CommonEventPublishData](../harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata.md), callback: AsyncCallback<void>) | 指定发布信息并发布公共事件。 |

## 发布不携带信息的公共事件

不携带信息的公共事件，只能发布无序公共事件。

1. 导入模块。

   ```typescript
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = 'ProcessModel';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 传入需要发布的事件名称和回调函数，发布事件。

   ```typescript
   // 发布公共事件，其中的event字段需要替换为实际的事件名称。
   commonEventManager.publish('event', (err: BusinessError) => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG,
         `Publish failed, code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err.message)}`);
     } else {
       // ...
       hilog.info(DOMAIN_NUMBER, TAG, `Publish success`);
     }
   });
   ```

## 发布携带信息的公共事件

携带信息的公共事件，可以发布为无序公共事件、有序公共事件和粘性事件，可以通过参数[CommonEventPublishData](../harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata.md)的isOrdered、isSticky的字段进行设置。

1. 导入模块。

   ```typescript
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = 'ProcessModel';
   const DOMAIN_NUMBER: number = 0xFF00;
   ```
2. 构建需要发布的公共事件信息。

   ```typescript
   // 公共事件相关信息
   let options: commonEventManager.CommonEventPublishData = {
     code: 1, // 公共事件的初始代码
     data: 'initial data', // 公共事件的初始数据
   };
   ```
3. 传入需要发布的事件名称、需要发布的指定信息和回调函数，发布事件。

   ```typescript
   // 发布公共事件，其中的event字段需要替换为实际的事件名称。
   commonEventManager.publish('event', options, (err: BusinessError) => {
     if (err) {
       hilog.error(DOMAIN_NUMBER, TAG,
         `Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
     } else {
       // ...
       hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in publishing common event.`);
     }
   });
   ```
