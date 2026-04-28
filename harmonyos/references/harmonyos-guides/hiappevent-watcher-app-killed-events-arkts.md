---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events-arkts
title: 订阅应用终止事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用终止事件 > 订阅应用终止事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5335f2648ae061fb0aaca2836f5c7ccd7cee00c6774779e6dca9b85f307b29ec
---

## 应用终止事件规格说明

请参考[应用终止事件介绍](hiappevent-watcher-app-killed-events.md)。

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

为确保开发阶段顺利接收事件回调，建议采用以下方案：创建新的Native C++工程，在ArkTs代码中实现订阅，搭配C++代码的故障注入代码构造故障以触发应用终止事件。

1. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块：

   ```
   1. import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下：

   ```
   1. hiAppEvent.addWatcher({
   2. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   3. name: "watcher",
   4. // 开发者可以订阅感兴趣的系统事件，此处是订阅了应用终止事件
   5. appEventFilters: [
   6. {
   7. domain: hiAppEvent.domain.OS,
   8. names: [hiAppEvent.event.APP_KILLED]
   9. }
   10. ],
   11. // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
   12. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
   13. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   14. for (const eventGroup of appEventGroups) {
   15. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   16. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   17. for (const eventInfo of eventGroup.appEventInfos) {
   18. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   19. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
   20. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
   21. // 开发者可以获取到应用终止事件发生的时间戳
   22. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${eventInfo.params['time']}`);
   23. // 开发者可以获取到应用的前后台状态
   24. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.foreground=${eventInfo.params['foreground']}`);
   25. // 开发者可以获取到应用终止事件发生的原因
   26. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.reason=${eventInfo.params['reason']}`);
   27. }
   28. }
   29. }
   30. });
   ```
3. 以下为故障注入功能，需要使用C++代码实现，编辑"napi\_init.cpp"，新增以下代码：

   ```
   1. #include <thread>

   3. static void NativeLeak()
   4. {
   5. constexpr int leak_size_per_time = 500000;
   6. while (true) {
   7. char *p = (char *)malloc(leak_size_per_time + 1);
   8. if (!p) {
   9. break;
   10. }
   11. memset(p, 'a', leak_size_per_time);
   12. std::this_thread::sleep_for(std::chrono::milliseconds(10));
   13. }
   14. }

   16. static napi_value Leak(napi_env env, napi_callback_info info) {
   17. std::thread t1(NativeLeak);
   18. t1.detach();
   19. return {};
   20. }
   ```
4. 编辑"napi\_init.cpp"文件，将Leak注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. { "leak", nullptr, Leak, nullptr, nullptr, nullptr, napi_default, nullptr }, // 新增这行
   5. };
   6. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   7. return exports;
   8. }
   ```
5. 编辑"index.d.ts"文件，定义ArkTS接口：

   ```
   1. export const leak: () => void;
   ```
6. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，在build下增加OnClick功能，并调用Leak接口的示例代码：

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import testNapi from 'libentry.so';

   4. const DOMAIN = 0x0000;

   6. @Entry
   7. @Component
   8. struct Index {
   9. @State message: string = 'Start To Leak';

   11. build() {
   12. Row() {
   13. Column() {
   14. Text(this.message)
   15. .fontSize($r('app.float.page_text_font_size'))
   16. .fontWeight(FontWeight.Bold)
   17. .onClick(() => {
   18. if (this.message != 'Leaking') {
   19. this.message = 'Leaking';
   20. hilog.info(DOMAIN, 'testTag', 'Start leaking');
   21. testNapi.leak();
   22. }
   23. })
   24. }
   25. .width('100%')
   26. }
   27. .height('100%')
   28. }
   29. }
   ```
7. 点击DevEco Studio界面中的运行按钮，运行应用工程，点击屏幕中间的“Start To Leak”按钮，等待2-3分钟，待触发RssThresholdKiller类型的管控终止。
8. 应用被终止后，重新打开应用，会触发终止事件上报，系统会回调应用的onReceive函数，可以在Log窗口看到对系统事件数据的处理日志。

   应用终止事件采样栈示例：

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=APP_KILLED
   3. HiAppEvent eventInfo.params.time=1717597063727
   4. HiAppEvent eventInfo.params.reason="RssThresholdKiller"
   5. HiAppEvent eventInfo.params.foreground=true
   ```
