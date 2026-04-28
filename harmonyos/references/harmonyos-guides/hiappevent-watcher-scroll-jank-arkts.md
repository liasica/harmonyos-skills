---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-scroll-jank-arkts
title: 订阅滑动丢帧事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 滑动丢帧事件 > 订阅滑动丢帧事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c9c20e7dab8c15729a8c74a6345d3ee30d4f60060479ac5f6842abc89f98aa3
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对用户滑动列表触发丢帧生成的滑动丢帧事件订阅为例，说明开发步骤。

1. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，添加系统事件的订阅，示例代码如下：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

   3. hiAppEvent.addWatcher({
   4. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   5. name: "watcher",
   6. // 开发者可以订阅感兴趣的系统事件，此处是订阅了滑动丢帧事件
   7. appEventFilters: [
   8. {
   9. domain: hiAppEvent.domain.OS,
   10. names: [hiAppEvent.event.SCROLL_JANK]
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
2. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个List组件，在列表的滑动事件中添加耗时操作，示例代码如下：

   ```
   1. struct Index {
   2. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
   3. build() {
   4. List({ space: 10 }) {
   5. ForEach(this.arr, (item: number) => {
   6. ListItem() {
   7. Text(`${item}`)
   8. .width('100%')
   9. .height(100)
   10. .fontSize(20)
   11. .fontColor(Color.White)
   12. .textAlign(TextAlign.Center)
   13. .borderRadius(10)
   14. .backgroundColor(0x007DFF)
   15. }
   16. })
   17. }
   18. .onScrollIndex((firstIndex: number) => {
   19. let i = 1;
   20. while (i<20000) { // 在列表滑动事件中做一些耗时操作
   21. console.log("do something");
   22. i++;
   23. }
   24. })
   25. }
   26. }
   ```
3. 点击DevEco Studio界面中的运行按钮，运行应用工程，在页面中滑动列表，当系统检测到故障时触发滑动丢帧事件。
4. 每次滑动操作发生超过50ms卡顿场景，间隔5~35秒，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent onReceive: domain=OS
   2. HiAppEvent eventName=SCROLL_JANK
   3. HiAppEvent eventInfo={"domain":"OS","name":"SCROLL_JANK","eventType":1,"params":{"ability_name":"EntryAbility","begin_time":1710322495739,"bundle_name":"com.example.myapplication1","bundle_version":"1.0.0","duration":801,"external_log":["/data/storage/el2/log/watchdog/SCROLL_JANK_20250402192812_6033.txt"],"log_over_limit":false,"max_app_frametime":3,"max_app_seq_frames":0,"max_render_frametime":8,"max_render_seq_frames":0,"process_name":"com.example.myapplication1","time":1710322497495,"total_app_frames":98,"total_app_missed_frames":0,"total_render_frames":80,"total_render_missed_frames":0}}
   ```
