---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-subscribe-event
title: 订阅空间事件
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 订阅空间事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b087164a53a4c1688f5345a8ab886d27a2a74adcbaae3843e471cdbbe6ed7326
---

## 场景介绍

Enterprise Space Kit为应用提供订阅空间事件的能力，当前支持订阅空间切换事件。应用订阅空间切换事件后，当空间切换时，会告知应用，并执行应用自定义的动作。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#subscribeevent)。

| 接口名 | 描述 |
| --- | --- |
| [subscribeEvent](../harmonyos-references/enterprisespace-spacemanager.md#subscribeevent)(eventId: [EventType](../harmonyos-references/enterprisespace-spacemanager.md#eventtype)[], callback: AsyncCallback<[EventData](../harmonyos-references/enterprisespace-spacemanager.md#eventdata)>): number | 订阅空间事件，在相关事件触发时，通知应用侧。使用callback异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块和相关依赖模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[subscribeEvent](../harmonyos-references/enterprisespace-spacemanager.md#subscribeevent)接口，设置订阅空间事件，并查看打印信息。

   ```
   1. try {
   2. const subscribeId = spaceManager.subscribeEvent([spaceManager.EventType.EVENT_WORKSPACE_SWITCHED],
   3. (error: BusinessError, data: spaceManager.EventData) => {
   4. if (error) {
   5. console.error(`error info:${error?.code}, err message:${error?.message}`);
   6. } else {
   7. console.info(`event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}`);
   8. }
   9. });
   10. console.info(`Succeeded in subscribing event. subscribeId: ${subscribeId}`);
   11. } catch (err) {
   12. console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
   13. }
   ```
