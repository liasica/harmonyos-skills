---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-web-fling-jank-events-arkts
title: 订阅ArkWeb抛滑丢帧事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > ArkWeb抛滑丢帧事件 > 订阅ArkWeb抛滑丢帧事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9a2c37c593216fa6f937a658b9d7ee2b0116645933ce6ba2e9a24120417c0b2a
---

## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅ArkWeb抛滑丢帧事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以订阅ArkWeb抛滑丢帧事件为例，说明开发步骤。

1. 在DevEco Studio中新建工程，选择“Empty Ability”，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块：

   ```
   1. // 该变量在/pages/ArkWebPage.ets文件中进行定义，用于实现webId到网页url的映射
   2. import { webIdToUrlMap } from '../pages/ArkWebPage';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下：

   ```
   1. // 添加ArkWeb抛滑丢帧事件观察者
   2. hiAppEvent.addWatcher({
   3. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   4. name: 'webJankWatcher',
   5. // 开发者可以订阅感兴趣的系统事件，此处是订阅了ArkWeb抛滑丢帧事件
   6. appEventFilters: [
   7. {
   8. domain: hiAppEvent.domain.OS,
   9. names: [hiAppEvent.event.SCROLL_ARKWEB_FLING_JANK]
   10. }
   11. ],
   12. // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
   13. onReceive: (domain: string, appEventGroups: Array<hiAppEvent. AppEventGroup>) => {
   14. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   15. for (const eventGroup of appEventGroups) {
   16. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   17. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   18. for (const eventInfo of eventGroup.appEventInfos) {
   19. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   20. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
   21. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
   22. // 开发者可以获取到开始抛滑事件的时间戳
   23. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.start_time=${eventInfo.params['start_time']}`);
   24. // 开发者可以获取到抛滑动效持续的时间长度
   25. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.duration=${eventInfo.params['duration']}`);
   26. // 开发者可以获取到发生卡顿的的web页面对应的Id
   27. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.web_id=${eventInfo.params['web_id']}`);
   28. // 开发者可以获取抛滑阶段发生丢帧的最大时长
   29. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.max_app_frame_time=${eventInfo.params['max_app_frame_time']}`);
   30. const webId: number = eventInfo.params['web_id'];
   31. //webIdToUrlMap是一个定义的变量，用于实现webId到url的映射，通过系统侧获取的web_id查询到发生丢帧的网页
   32. const currentUrl = webIdToUrlMap.get(webId);
   33. // 开发者可以获取到发生卡顿的页面
   34. hilog.info(0x0000, 'testTag', `HiAppEvent get currentUrl=${currentUrl}`);
   35. }
   36. }
   37. }
   38. });
   ```
3. 在工程中的“entry > src > main > ets > pages”目录下，新增ArkWebPage.ets文件，在build下加载web网页，并定期下发耗时任务阻塞应用主线程触发丢帧，示例代码如下：

   ```
   1. import web_webview from '@ohos.web.webview';

   3. // 用于存储web_id到url的映射
   4. export const webIdToUrlMap = new Map<number, string>();

   6. @Entry
   7. @Component
   8. struct ArkWebPage {
   9. controller = new web_webview.WebviewController();

   11. build() {
   12. Column() {
   13. Web({ src: 'https://baidu.com',
   14. controller: this.controller
   15. })
   16. .height('100%')
   17. .onPageBegin((event) => {
   18. // 每次跳转到新页面都更新webId到url的映射关系，便于后续通过系统侧提供的web_id查询到发生丢帧的网页
   19. if (event) {
   20. const newUrl = event.url;
   21. const webId = this.controller.getWebId();
   22. webIdToUrlMap.set(webId, newUrl);
   23. }
   24. })
   25. .onPageEnd(() => {
   26. // 每2s阻塞应用主线程200ms
   27. setInterval(() => {
   28. const endTime = Date.now() + 200;
   29. while (Date.now() < endTime) {}
   30. }, 2000);
   31. })
   32. }
   33. }
   34. }
   ```

   注意

   如果一个页面需包含多个Web网页，需创建多个webview组件，每个webview组件加载一个网页。
4. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其onClick函数中跳转到Web页面。示例代码如下：

   ```
   1. // 按钮跳转到易出现滑动丢帧的web场景，触发ArkWeb抛滑丢帧事件。
   2. Button('ArkWebFlingJank ArkTs')
   3. .type(ButtonType.Capsule)
   4. .margin({
   5. top: 20
   6. })
   7. .backgroundColor('#0D9FFB')
   8. .width('80%')
   9. .height('5%')
   10. .onClick(() => {
   11. router.pushUrl({url: 'pages/ArkWebPage'});
   12. })
   ```
5. 编辑工程中的“entry > src > main > resources > base > profile > main\_pages.json”文件，配置ArkWebPage路由页面。

   ```
   1. {
   2. "src": [
   3. "pages/Index",
   4. "pages/ArkWebPage"
   5. ]
   6. }
   ```
6. 编辑工程中的“entry > src > main > module.json5”文件，添加网络访问权限。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.INTERNET"
   4. }
   5. ],
   ```

   说明

   Web组件详细的使用方式请参考[ArkWeb简介](web-component-overview.md)文档
7. 点击DevEco Studio界面中的运行按钮，运行应用工程。然后在应用界面中点击按钮“ArkWebFlingJank ArkTs”，跳转到网页，等待页面加载完成，滑动页面，当系统检测到故障时触发ArkWeb抛滑丢帧事件。
8. 每次抛滑过程中发生卡顿50ms及以上场景，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=SCROLL_ARKWEB_FLING_JANK
   3. HiAppEvent eventInfo.params.start_time=1765892111768
   4. HiAppEvent eventInfo.params.duration=1554
   5. HiAppEvent eventInfo.params.web_id=1
   6. HiAppEvent eventInfo.params.max_app_frame_time=195
   7. HiAppEvent get currentUrl=https://www.baidu.com
   ```
