---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event-arkts
title: 订阅音频卡顿事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 音频卡顿事件 > 订阅音频卡顿事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fd2f30a5bb30156a3e0c827ed12572580c76254295d0f77329d723a70b9c9c1d
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对应用音频播放触发丢帧生成的音频卡顿事件订阅为例，说明开发步骤。

1. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，添加系统事件的订阅。

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

   3. hiAppEvent.addWatcher({
   4. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   5. name: "watcher",
   6. // 开发者可以订阅感兴趣的系统事件，此处是订阅了应用音频卡顿事件
   7. appEventFilters: [
   8. {
   9. domain: hiAppEvent.domain.OS,
   10. names: [hiAppEvent.event.AUDIO_JANK_FRAME]
   11. }
   12. ],
   13. // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
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
2. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个模拟写入音频数据的回调函数normalCallback，在该回调中模拟卡顿主动返回INVALID（不送数据）来触发卡顿故障事件。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. let g_invalidCount = 0;
   3. function normalCallback(buffer: ArrayBuffer) {
   4. if (g_invalidCount > 0) {
   5. g_invalidCount--;
   6. return audio.AudioDataCallbackResult.INVALID;
   7. }
   8. //在此添加写数据逻辑
   9. return audio.AudioDataCallbackResult.VALID;
   10. }
   ```
3. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个卡顿触发按钮，改变INVALID返回次数，模拟相应音频卡顿。

   ```
   1. Row() {
   2. Button("卡顿").onClick(async () => {
   3. g_invalidCount = 30;
   4. })
   5. }
   ```
4. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，在创建AudioRender实例时，进行耗时操作回调

   ```
   1. audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建AudioRenderer实例
   2. if (!err) {
   3. console.info(`${TAG}: creating AudioRenderer success`);
   4. this.renderModel = renderer;
   5. if (this.renderModel !== undefined) {
   6. this.renderModel.on('writeData', normalCallback);
   7. }
   8. } else {
   9. console.info(`${TAG}: creating AudioRenderer failed, error: ${err.message}`);
   10. }
   11. });
   ```
5. AudioRender正常播放时，点击卡顿按钮，即可触发耗时回调，触发音频卡顿事件。
6. 每次音频卡顿触发后，可以在Log窗口看到对系统事件数据的处理日志。

   ```
   1. HiAppEvent onReceive: domain=OS
   2. HiAppEvent eventName=AUDIO_JANK_FRAME
   3. HiAppEvent eventInfo={"domain":"OS","name":"AUDIO_JANK_FRAME","eventType":1,"params":{"bundle_name":"com.samples.audio","bundle_version":"1.0.0","fault_type":"application","happen_time":3240511783,"max_frame_time":260,"process_name":"","time":1755587168818}}
   ```
