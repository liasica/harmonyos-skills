---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/applinking-direct-to-ag
title: 通过直达应用市场能力跳转至应用市场下载详情页
breadcrumb: 指南 > 应用服务 > App Linking Kit（应用链接服务） > 通过直达应用市场能力跳转至应用市场下载详情页
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6fb697135d70024b15c5f1a1f2e2a04ca5a2498692d86a3bcc9d569ec45327e6
---

## 场景介绍

从5.0.3(15)版本开始，新增支持直达应用市场能力。

当成功配置App Linking应用链接后，可以构建App Linking直达应用市场下载详情页链接。当应用已安装时，点击链接直接跳转应用；当应用未安装时，点击链接跳转应用市场下载详情页，引导用户下载应用。

| 华为分享打开场景 | 其他社交APP打开场景 |
| --- | --- |
|  |  |

## 原理机制

### 链接生效机制

直达应用市场链接配置后不是即时生效的，一般要24小时生效，也有可能出现48小时生效的情况。

## 前提条件

1. 目标方应用已[配置App Linking应用链接](app-linking-startupapp.md)。
2. 目标方HarmonyOS应用必须已上架，具体可参见“[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)”。

## 约束与限制

只能获取通过App Linking域名校验的应用链接，请参见[在AGC为应用创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名)。

## 开发步骤

1. 配置直达应用市场能力。

   1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
   2. 在项目列表中点击目标方应用所在的项目。
   3. 在左侧导航栏中选择“增长 > App Linking > 应用链接”，点击“操作”列的“直达应用市场”。

      说明

      只有[在AGC创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名)状态为“成功”时，才支持配置直达应用市场链接。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/b3J6aPv_Rb6BdfBtZbo9lA/zh-cn_image_0000002583478805.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=DFEB0E3A1180BBA2A7FD8C95B4F3B43F143442638830DBB1074D81E363E3A6B8)
   4. 在配置页面，下拉选择与该域名关联的在架应用，为应用配置直达应用市场链接。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/W74mQl77QBa0JwMGesA0dg/zh-cn_image_0000002552799156.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=9B78FEA89E5C0BF1CE3BA48648FD8D09F5C85358D7F9AB283731652798DC4EE1)

      * 可以点击“添加应用”为多个应用配置直达链接，当该域名下关联的在架应用全部配置后，无法再添加应用。
      * 可以根据以下规则配置直达链接。

        | 路径 | 匹配规则 |
        | --- | --- |
        | path | 精确匹配 |
        | pathStartWith | 前缀匹配 |
        | pathRegex | 正则表达式匹配 |

        + 如果[在module.json5中配置关联的网址域名](app-linking-startupapp.md#在modulejson5中配置关联的网址域名)时，未配置path、pathStartWith或pathRegex，必须是如下匹配规则之一：

          pathRegex，匹配路径：.\*

          path，手动输入精确匹配的路径（不允许以“/”开头，不允许出现双斜杠“//”和“..”，允许包含字母（a-z、A-Z）、数字（0-9）、正斜杠“/”、点“.”、下划线“\_”和连字符“-”）
        + （不推荐）如果[在module.json5中配置关联的网址域名](app-linking-startupapp.md#在modulejson5中配置关联的网址域名)时，path匹配规则中配置了pathRegex，且值为.\*，可以包含如下匹配规则：

          pathRegex，匹配路径：.\*

          path，手动输入精确匹配的路径（不允许以“/”开头，不允许出现双斜杠“//”和“..”，允许包含字母（a-z、A-Z）、数字（0-9）、正斜杠“/”、点“.”、下划线“\_”和连字符“-”）
        + 其他场景需要根据[在module.json5中配置关联的网址域名](app-linking-startupapp.md#在modulejson5中配置关联的网址域名)时配置的path匹配规则进行选择。
      * 可以点击“删除链接”删除当前关联应用的直达应用市场链接。
   5. 配置完成后，点击页面顶部的“发布”，会跳转到“应用链接”列表页面。

      如下图，“是否配置直达应用市场”显示“是”，表示链接配置成功。

      说明

      链接配置成功后，一般需要24~48小时才能生效，请耐心等待。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/7fqHKucqRPmQVdFBoA3VJA/zh-cn_image_0000002583438851.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=3F88195D0A3460E1517A825CB60C09637FB52361FB5F5C3D188088A7CBBE6A32)
2. 验证应用被拉起效果。

   * 方式一：将直达应用市场链接地址存入备忘录中，并点击验证该链接是否可以拉起应用。
   * 方式二：通过openLink接口拉起应用。

     1. 拉起方应用需调用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口，并将appLinkingOnly参数设为false或者不传，以App Linking优先的方式打开应用。

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
        3. 在“entry/src/main/ets/pages/Index.ets”文件中，使用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口配置跳转链接。

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
           16. context.openLink(link, { appLinkingOnly: false })
           17. .then(() => {
           18. hilog.info(0x0000, 'testTag', `Succeeded in opening link.`);
           19. })
           20. .catch((error: BusinessError) => {
           21. hilog.error(0x0000, 'testTag', `Failed to open link, code: ${error.code}, message: ${error.message}`);
           22. })
           23. })
           24. }
           25. }
           ```
     2. 安装拉起方应用，点击拉起方应用中的跳转按钮。

        此时目标应用未安装，若有App Linking相匹配的应用，点击链接会跳转应用市场下载详情页，引导用户安装应用；若无App Linking相匹配的应用，则继续尝试以浏览器打开链接的方式打开应用。
     3. 安装目标方应用后，点击拉起方应用的跳转按钮，会直接打开应用。

## FAQ

### 使用ArkWeb拉起目标应用，当目标应用未安装时，会直接跳转到应用市场下载详情页面吗？

当开发者通过系统浏览器或ArkWeb拉起目标应用时，如果目标应用未安装，不会直接跳转应用市场，需要开发者根据自身业务自行实现跳转应用市场的能力。详细可参见“Web和应用的跳转与拉起”开发实践中的《[ArkWeb页面指定应用跳转](../best-practices/bpta-web-app-jump-and-pull-up.md#section37419543116)》章节。

### 哪些服务支持接入App Linking Kit的直达应用市场能力？

支持的服务如下：

华为分享、碰一碰分享、短信、畅联以及其他支持openLink API的场景。

不支持的服务如下：

浏览器、扫码（规划中，上线后自动生效，无需适配）。

### 直达链接的路径（path、pathStartWith或pathRegex）可以配置多少条？

每个应用支持配置1条。
