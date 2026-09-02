---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-appfreezewarning-events-arkts
title: 订阅应用冻屏告警事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏告警事件 > 订阅应用冻屏告警事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:032563005e19bf44229fd234cbddd7ffe36e00129c775907d5e52db08ae95cc8
---

## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅应用冻屏告警事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以订阅应用冻屏告警事件为例，说明开发步骤。

1. 在DevEco Studio中，新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

   ```ts
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下：

   ```ts
   hiAppEvent.addWatcher({
     // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
     name: "watcher",
     // 开发者可以订阅感兴趣的系统事件，此处是订阅了应用冻屏告警事件
     appEventFilters: [
       {
         domain: hiAppEvent.domain.OS,
         names: [hiAppEvent.event.appFreezeWarning]
       }
     ],
     // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
     onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
       hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
       for (const eventGroup of appEventGroups) {
         // 开发者可以根据事件集合中的事件名称区分不同的系统事件
         hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
         for (const eventInfo of eventGroup.appEventInfos) {
           // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.eventType=${eventInfo.eventType}`);
           // 开发者可以获取到应用冻屏告警事件发生的时间戳
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${eventInfo.params['time']}`);
           // 开发者可以获取到应用冻屏告警事件发生时应用的前台/后台状态
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.foreground=${eventInfo.params['foreground']}`);
           // 开发者可以获取到应用冻屏告警事件发生时应用的唯一关联id
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.app_running_unique_id=${eventInfo.params['app_running_unique_id']}`);
           // 开发者可以获取到应用冻屏告警事件发生时应用的版本信息
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_version=${eventInfo.params['bundle_version']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_version_code=${eventInfo.params['bundle_version_code']}`);
           // 开发者可以获取到应用冻屏告警事件发生时应用的包名
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_name=${eventInfo.params['bundle_name']}`);
           // 开发者可以获取到应用冻屏告警事件发生时应用的进程名称
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.process_name=${eventInfo.params['process_name']}`);
           // 开发者可以获取到应用冻屏告警事件发生时应用的进程id
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.pid=${eventInfo.params['pid']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uid=${eventInfo.params['uid']}`);
           // 开发者可以获取到应用冻屏告警事件发生的异常类型、异常原因
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.exception=${JSON.stringify(eventInfo.params['exception'])}`);
           // 开发者可以获取到应用冻屏告警事件发生时日志信息
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.hilog.size=${eventInfo.params['hilog'].length}`);
           // 开发者可以获取到应用冻屏告警事件发生时主线程未处理消息
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.event_handler.size=${eventInfo.params['event_handler'].length}`);
           // 开发者可以获取到应用冻屏告警事件发生时同步binder调用信息
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.peer_binder.size=${eventInfo.params['peer_binder'].length}`);
           // 开发者可以获取到应用冻屏告警事件发生时全量线程调用栈
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.threads.size=${eventInfo.params['threads'].length}`);
           // 开发者可以获取到应用冻屏告警事件发生时内存信息
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.memory=${JSON.stringify(eventInfo.params['memory'])}`);
           // 开发者可以获取到应用冻屏告警事件的故障进程存活时间
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.process_life_time=${eventInfo.params['process_life_time']}`);
         }
       }
     }
   });
   ```
3. 编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，新增按钮触发冻屏告警事件。示例代码如下：

   ```ts
     @Entry
     @Component
     struct Index {
       build() {
         RelativeContainer() {
           Column() {
             Button("appFreezeWarning", { stateEffect:true, type: ButtonType.Capsule})
               .width('75%')
               .height(50)
               .margin(15)
               .fontSize(20)
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                // 在按钮点击函数中构造一个appFreezeWarning场景，触发应用冻屏告警事件
                 const t = Date.now();
                 while (Date.now() - t <= 6500) {}
               })
           }.width('100%')
         }
         .height('100%')
         .width('100%')
       }
     }
   ```
4. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreezeWarning”，触发一次应用冻屏告警事件。

### 验证观察者是否订阅到应用冻屏告警事件

等待约一分钟后，可以在Log窗口看到对系统事件数据的处理日志：

```text
HiAppEvent onReceive: domain=OS
HiAppEvent eventName=APPFREEZE_WARNING
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APPFREEZE_WARNING
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1776946769389
HiAppEvent eventInfo.params.foreground=true
HiAppEvent eventInfo.params.app_running_unique_id=215456512336951247
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.bundle_version_code=1000000
HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=39067
HiAppEvent eventInfo.params.uid=20010043
HiAppEvent eventInfo.params.exception={"message":"App main thread is not response!Main handler dump start time: 2026-04-23 20:19:28.903","name":"THREAD_BLOCK_3S"}
HiAppEvent eventInfo.params.hilog.size=77
HiAppEvent eventInfo.params.event_handler.size=6
HiAppEvent eventInfo.params.peer_binder.size=0
HiAppEvent eventInfo.params.threads.size=28
HiAppEvent eventInfo.params.memory={"rss":161080,"sys_avail_mem":1361464,"sys_free_mem":796232,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":56960692}
HiAppEvent eventInfo.params.process_life_time=18
```
