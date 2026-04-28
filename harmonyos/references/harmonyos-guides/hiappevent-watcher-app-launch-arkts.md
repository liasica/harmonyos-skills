---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-launch-arkts
title: 订阅启动耗时事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 启动耗时事件 > 订阅启动耗时事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4759f2d4b64b1c79701f74f7259d098bdeeb0be8ffea3840262734dc34b1990a
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对用户运行应用工程生成的启动耗时事件订阅为例，说明开发步骤。

1. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，添加系统事件的订阅，示例代码如下：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

   3. hiAppEvent.addWatcher({
   4. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   5. name: "watcher",
   6. // 开发者可以订阅感兴趣的系统事件，此处是订阅了启动耗时事件
   7. appEventFilters: [
   8. {
   9. domain: hiAppEvent.domain.OS,
   10. names: [hiAppEvent.event.APP_LAUNCH]
   11. }
   12. ],
   13. // 开发者可以自行实现订阅回调函数，以便对订阅获取到的事件数据进行自定义处理
   14. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
   15. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   16. for (const eventGroup of appEventGroups) {
   17. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   18. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   19. for (const eventInfo of eventGroup.appEventInfos) {
   20. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   21. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo=${JSON.stringify(eventInfo)}`);
   22. }
   23. }
   24. }
   25. });
   ```

   注意

   * 在订阅APP\_LAUNCH事件后，应用启动完成生成APP\_LAUNCH事件触发回调的过程中，若应用出现退出或崩溃，onReceive回调接口可能不会被触发，从而导致事件回调处理失败。当应用重新启动时，回调函数会将之前未完成回调的事件内容传递给应用，导致onReceive回调**可能在一次应用启动过程中被多次调用**。
   * **不建议在onReceive中执行任何关键业务逻辑**（例如移除事件观察者、资源释放等操作），否则可能导致业务代码重复执行、资源被多次释放，从而引发程序错误甚至应用崩溃。
   * 建议开发者将 onReceive 仅用于事件的接收和简单记录。
2. 点击DevEco Studio界面中的运行按钮，运行应用工程，添加系统事件订阅者，退出应用，再次点击桌面应用图标，触发一次启动耗时事件。
3. 应用工程再次启动可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent onReceive: domain=OS
   2. HiAppEvent eventName=APP_LAUNCH
   3. HiAppEvent eventInfo={"domain":"OS","name":"APP_LAUNCH","eventType":4,"params":{"animation_finish_time":662,"bundle_name":"com.example.myapplication","bundle_version":"1.0.0","extend_time":0,"icon_input_time":1709367533224,"process_name":"com.example.myapplication","start_type":0,"time":1709367533901}}
   ```
