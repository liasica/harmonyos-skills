---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-publish
title: 发布公共事件
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 进程线程通信 > 使用公共事件进行进程间通信 > 发布公共事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c549a2b94babd97e2031c57024b800a0df40b2789e3c04b203ff6d109839b901
---

## 场景介绍

当需要发布某个公共事件时，可以通过[publish()](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagerpublish)方法发布事件。发布的公共事件可以携带数据，供订阅者解析并进行下一步处理。

注意

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

   ```
   1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const TAG: string = 'ProcessModel';
   5. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L15-L21)
2. 传入需要发布的事件名称和回调函数，发布事件。

   ```
   1. // 发布公共事件，其中的event字段需要替换为实际的事件名称。
   2. commonEventManager.publish('event', (err: BusinessError) => {
   3. if (err) {
   4. hilog.error(DOMAIN_NUMBER, TAG,
   5. `Publish failed, code is ${JSON.stringify(err.code)}, message is ${JSON.stringify(err.message)}`);
   6. } else {
   7. // ...
   8. hilog.info(DOMAIN_NUMBER, TAG, `Publish success`);
   9. }
   10. });
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L116-L127)

## 发布携带信息的公共事件

携带信息的公共事件，可以发布为无序公共事件、有序公共事件和粘性事件，可以通过参数[CommonEventPublishData](../harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata.md)的isOrdered、isSticky的字段进行设置。

1. 导入模块。

   ```
   1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const TAG: string = 'ProcessModel';
   5. const DOMAIN_NUMBER: number = 0xFF00;
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L15-L21)
2. 构建需要发布的公共事件信息。

   ```
   1. // 公共事件相关信息
   2. let options: commonEventManager.CommonEventPublishData = {
   3. code: 1, // 公共事件的初始代码
   4. data: 'initial data', // 公共事件的初始数据
   5. };
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L41-L47)
3. 传入需要发布的事件名称、需要发布的指定信息和回调函数，发布事件。

   ```
   1. // 发布公共事件，其中的event字段需要替换为实际的事件名称。
   2. commonEventManager.publish('event', options, (err: BusinessError) => {
   3. if (err) {
   4. hilog.error(DOMAIN_NUMBER, TAG,
   5. `Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
   6. } else {
   7. // ...
   8. hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in publishing common event.`);
   9. }
   10. });
   ```

   [CreatSubscribeInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/common_event/CommonEvent/entry/src/main/ets/filemanager/CreatSubscribeInfo.ets#L134-L145)
