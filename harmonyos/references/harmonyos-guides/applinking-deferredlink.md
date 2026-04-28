---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/applinking-deferredlink
title: 通过延迟链接跳转至应用详情页
breadcrumb: 指南 > 应用服务 > App Linking Kit（应用链接服务） > 通过延迟链接跳转至应用详情页
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:33d2e4bfe8976bbb75b8e50b49f033c4397a0d9904caafb475c5f25eec5e21ec
---

## 场景介绍

从5.0.3(15)版本开始，新增支持延迟链接能力。

当被分享用户未安装应用时，通过延迟链接能力，应用首次打开时，调用延迟链接接口，系统仍能获取用户之前点击的应用相关链接。在获取链接后，应用可直接跳转至对应的详情页，无需先跳转至应用首页，从而提升用户体验和链接的转化率。

例如：华为阅读结合App Linking Kit延迟链接能力，实现了即使用户未安装应用，点击链接完成下载并首次打开时，仍能直接跳转至预设页面（如书籍详情页）。与传统方式（需先打开APP再手动定位内容）相比，操作步骤减少了43%。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/w_8fPDr0QDu74VWL4ngbCQ/zh-cn_image_0000002552958806.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=9F31ACD3DA3AB0B2E741CF627326F272C4F0ECAEFCE3242461DA00EFAF176939)

## 原理机制

### 一次性机制

延迟链接只能获取一次，获取后，系统会从缓存中删除该链接；后续调用时，返回为空。

### 缓存机制

* 缓存时效性：系统缓存链接的最大时长为10分钟，超过则自动删除该缓存链接。
* 缓存条数限制：系统最多缓存的链接条目数为50条，超过则自动删除最早的缓存链接。

## 前提条件

1. 目标方应用已[配置App Linking应用链接](app-linking-startupapp.md)。
2. 该能力目前仅适用于5.0.3(15)及以上版本的HarmonyOS应用。

## 约束与限制

* 支持Phone、Tablet设备。并且从6.1.0(23)版本开始，新增支持PC/2in1设备。
* 只能获取通过App Linking域名校验的应用链接，请参见[在AGC为应用创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名)。建议在首次启动签署隐私协议后再调用延迟链接接口，确保此时域名校验通过。

## 开发步骤

1. 获取延迟链接。

   1. 在入口类文件页面Index.ets中添加如下代码。当应用首次启动时，调用[deferredLink.popDeferredLink()](../harmonyos-references/applinking-deferredlink-api.md#popdeferredlink)接口，获取用户此前点击的该应用相关链接。

      ```
      1. import { deferredLink } from '@kit.AppLinkingKit';
      2. import { hilog } from '@kit.PerformanceAnalysisKit';

      4. @Entry
      5. @Component
      6. struct Index {
      7. pageStack: NavPathStack = new NavPathStack();
      8. build() {
      9. Column() {
      10. Navigation(this.pageStack) {
      11. Button("获取延迟链接").onClick(() => {
      12. // 应用首次启动时，获取用户此前点击的该应用相关链接
      13. deferredLink.popDeferredLink().then((link: string) => {
      14. hilog.info(0x0000, 'testTag', `Succeeded in getting deferred link, result: ${link}`);
      15. }).catch(() => {
      16. // 发生未知错误
      17. hilog.error(0x0000, 'testTag', `Failed to get deferred link.`);
      18. })
      19. })
      20. // ...
      21. }
      22. // ...
      23. }
      24. }
      25. }
      ```
   2. 根据自身业务逻辑配置链接，实现跳转到对应的详情页面。

      ```
      1. import { deferredLink } from '@kit.AppLinkingKit';
      2. import { hilog } from '@kit.PerformanceAnalysisKit';
      3. import { url } from '@kit.ArkTS';

      5. @Entry
      6. @Component
      7. struct Index {
      8. pageStack: NavPathStack = new NavPathStack();
      9. build() {
      10. Column() {
      11. Navigation(this.pageStack) {
      12. Button("获取延迟链接").onClick(() => {
      13. // 应用首次启动时，获取用户此前点击的该应用相关链接
      14. deferredLink.popDeferredLink().then((link: string) => {
      15. hilog.info(0x0000, 'testTag', `Succeeded in getting deferred link, result: ${link}`);
      16. // 若延迟链接不为空，开发者可根据自身业务逻辑配置链接，跳转至详情页面
      17. if (link) {
      18. // 根据业务逻辑配置链接，自行跳转至详情页面
      19. // 如传入的url为：<https://www.example.com/product?pageName=productDetail>
      20. // 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理，示例如下：
      21. try {
      22. let urlObject = url.URL.parseURL(link);
      23. let pageName = urlObject.params.get('pageName');
      24. this.pageStack.pushPath({ name: pageName });
      25. } catch (error) {
      26. hilog.error(0x0000, 'testTag', `Failed to parse url.`);
      27. }
      28. }
      29. }).catch(() => {
      30. // 发生未知错误
      31. hilog.error(0x0000, 'testTag', `Failed to get deferred link.`);
      32. })
      33. })
      34. // ...
      35. }
      36. // ...
      37. }
      38. }
      39. }
      ```
2. 验证应用被拉起效果。

   拉起方应用可调用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口，传入目标应用的链接，从而拉起目标应用。

   openLink接口提供了两种拉起目标应用的方式，开发者可根据业务需求进行选择。

   * 方式一： 仅以App Linking的方式打开应用。

     将appLinkingOnly参数设为true，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则抛异常给开发者进行处理。

     适用于无法打开目标应用时，开发者做了相应的异常处理。例如：拉起方应用集成了ArkWeb，当目标应用不存在时，可通过ArkWeb打开链接。
   * 方式二： 以App Linking优先的方式打开应用。

     将appLinkingOnly参数设为false或者不传，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则尝试以浏览器打开链接的方式打开应用。

     适用于无法打开目标应用时，开发者未做任何处理。此时目标应用不存在时，会通过系统浏览器打开链接。

   本文为了方便验证App Linking的配置是否正确，选择方式一，示例如下。

   1. 在“entry/src/main/ets/common”目录下添加GlobalContext.ets文件，开发初始化和获取应用上下文的接口。

      ```
      1. import { common } from '@kit.AbilityKit';

      3. export class GlobalContext {
      4. private static context: common.UIAbilityContext;

      6. public static initContext(context: common.UIAbilityContext): void {
      7. GlobalContext.context = context;
      8. }

      10. public static getContext(): common.UIAbilityContext {
      11. return GlobalContext.context;
      12. }
      13. }
      ```
   2. 在“entry/src/main/ets/entryability/EntryAbility.ets”文件中导入GlobalContext，在onCreate方法中使用GlobalContext.initContext(this.context)初始化全局应用上下文。
   3. 在“entry/src/main/ets/pages/Index.ets”文件中，使用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口打开应用。

      ```
      1. import { hilog } from '@kit.PerformanceAnalysisKit';
      2. import { BusinessError } from '@kit.BasicServicesKit';
      3. import { GlobalContext } from '../common/GlobalContext';

      5. @Entry
      6. @Component
      7. struct Index {
      8. build() {
      9. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
      10. .width('87%')
      11. .height('5%')
      12. .margin({ bottom: '12vp' })
      13. .onClick(() => {
      14. let context = GlobalContext.getContext();
      15. let link: string = "https://www.example.com/product?pageName=productDetail";
      16. // 仅以App Linking的方式打开应用
      17. context.openLink(link, { appLinkingOnly: true })
      18. .then(() => {
      19. hilog.info(0x0000, 'testTag', `Succeeded in opening link.`);
      20. })
      21. .catch((error: BusinessError) => {
      22. hilog.error(0x0000, 'testTag', `Failed to open link, code: ${error.code}, message: ${error.message}`);
      23. })
      24. })
      25. }
      26. }
      ```
3. 安装拉起方应用，点击拉起方应用中的跳转按钮。

   如果此时目标方应用未安装，会抛出系统异常。
4. 安装目标方应用后，会根据获取的延迟链接直接跳转到目标方应用的详情页面。
