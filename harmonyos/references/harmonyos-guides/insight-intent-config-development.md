---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-config-development
title: 使用配置文件开发意图
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 意图框架开发指导 > 开发意图 > 使用配置文件开发意图
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c6b6b4495c55a29b1992cf871ca460227fa9746e0ef5db984fbd1451612d739
---

## 简介

从API version 11及以上版本，支持通过配置文件开发意图。主要包含两个环节：

1. 通过[insight\_intent.json配置文件](insight-intent-config-development.md#insight_intentjson配置文件说明)定义意图，声明意图执行器的代码路径、绑定的Ability组件等意图信息。
2. 通过[InsightIntentExecutor](../harmonyos-references/js-apis-app-ability-insightintentexecutor.md#insightintentexecutor)实现意图执行逻辑。

不同Ability组件类型需要配置的字段与需要实现的意图执行器，如下所示：

| 组件类型 | 意图配置 | 意图执行器 |
| --- | --- | --- |
| UIAbility | 需要在insight\_intent.json文件中配置"uiAbility"字段。 | 当"executeMode"字段为"foreground"时，实现onExecuteInUIAbilityForegroundMode，通过startAbility启动意图绑定的UIAbility组件。  当"executeMode"字段为"background"时，实现onExecuteInUIAbilityBackgroundMode，通过[Call调用](../harmonyos-references/js-apis-app-ability-uiability.md#后台通信能力)启动意图绑定的UIAbility组件。 |
| UIExtensionAbility | 需要在insight\_intent.json文件中配置"uiExtension"字段。 | 实现onExecuteInUIExtensionAbility。 |
| 卡片(FormExtensionAbility) | 需要在insight\_intent.json文件中配置"form"字段。 | 无需单独执行器。 |

## 接口说明

意图执行器实现需要继承[InsightIntentExecutor](../harmonyos-references/js-apis-app-ability-insightintentexecutor.md#insightintentexecutor)，实现[onExecuteInUIAbilityForegroundMode](../harmonyos-references/js-apis-app-ability-insightintentexecutor.md#onexecuteinuiabilityforegroundmode)等方法。开发者响应意图执行通过onExecuteInUIAbilityForegroundMode等接口实现，在不同的意图执行模式下，接口的触发时机也不同。针对不同意图执行模式的意图回调执行时机见各个回调的API说明。

## 开发步骤

### 意图绑定UIAbility组件

通过DevEco Studio工具可视化创建意图，操作及开发步骤如下。

1. 选中模块或模块下的文件，右键单击New > Insight Intent，进入意图框架配置界面。
2. 选择意图垂域、意图框架入口代码文件名以及意图配置。意图配置包含意图名称和绑定的Ability组件。
3. 点击Finish，完成意图框架创建。

   此时将在module目录 > src > main > resources > base > profile中，生成insight\_intent.json文件，可在该文件查看当前意图框架配置的相关信息。

   ```
   1. {
   2. "insightIntents": [
   3. {
   4. "domain": "MusicDomain",
   5. "intentName": "PlayMusic",
   6. "intentVersion": "1.0.1",
   7. "srcEntry": "./ets/insightintents/PlayMusicExecutor.ets",
   8. "uiAbility": {
   9. "ability": "MusicPlayerAbility",
   10. "executeMode": [
   11. "foreground",
   12. "background"
   13. ]
   14. }
   15. }
   16. ]
   17. }
   ```
4. 在module目录 > src > main > ets > insightintents目录下生成入口代码文件。开发者在意图执行函数中实现意图的功能代码。

   ```
   1. // 本示例对应意图配置中的'srcEntry'字段对应的文件
   2. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';
   4. // ···

   6. export default class PlayMusicExecutor extends InsightIntentExecutor {
   7. // 由于意图配置中'executeMode'配置了'foreground'前台模式执行，故需要实现该接口
   8. async onExecuteInUIAbilityForegroundMode(intentName: string, params: Record<string, Object>,
   9. windowStage: window.WindowStage): Promise<insightIntent.ExecuteResult> {
   10. // 实现播放逻辑
   11. // ···
   12. const result: insightIntent.ExecuteResult = {
   13. code: 0
   14. };
   15. return Promise.resolve(result);
   16. }

   18. // 由于意图配置中'executeMode'配置了'background'后台模式执行，故需要实现该接口
   19. async onExecuteInUIAbilityBackgroundMode(intentName: string,
   20. params: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
   21. // 后台控制逻辑
   22. const result: insightIntent.ExecuteResult = {
   23. code: 0
   24. };
   25. return Promise.resolve(result);
   26. }
   27. }
   ```

   [PlayMusicExecutor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/InsightIntentConfigDevelopment/entry/src/main/ets/insightintents/PlayMusicExecutor.ets#L15-L50)

说明

配置文件范式仅提供基础执行能力，参数格式需开发者与系统入口协商。

开发者也可以选择按规范手动创建意图配置文件和意图执行器。需要关注如下注意点：

* 必须声明绑定的Ability组件和支持的意图执行模式。
* 配置文件必须命名为"insight\_intent.json"。
* 配置文件存放路径为"resources/base/profile"。
* 配置文件关键字段遵循相应的约束。

### 意图绑定UIExtensionAbility组件

参考[意图绑定UIAbility组件](insight-intent-config-development.md#意图绑定uiability组件)完成工程创建。

意图配置示例：

```
1. {
2. "insightIntents": [
3. {
4. "domain": "MusicDomain",
5. "intentName": "PlayMusic",
6. "intentVersion": "1.0.1",
7. "srcEntry": "./ets/insightintents/ExtensionExecutor.ets",
8. "uiExtension": {
9. "ability": "MusicExtensionAbility"
10. }
11. }
12. ]
13. }
```

意图执行器实现：

```
1. import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';

3. export default class ExtensionExecutor extends InsightIntentExecutor {
4. // 由于意图配置了uiExtension，故需要实现该接口
5. async onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
6. pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
7. const result: insightIntent.ExecuteResult = {
8. code: 0
9. };
10. return Promise.resolve(result);
11. }
12. }
```

[ExtensionExecutor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/InsightIntentConfigDevelopment/entry/src/main/ets/insightintents/ExtensionExecutor.ets#L15-L28)

系统入口通过UIExtensionComponent组件执行该意图。

### 意图绑定卡片

参考[意图绑定UIAbility组件](insight-intent-config-development.md#意图绑定uiability组件)完成工程创建。

意图配置示例：

```
1. {
2. "insightIntents": [
3. {
4. "domain": "MusicDomain",
5. "intentName": "PlayMusic",
6. "intentVersion": "1.0.1",
7. "srcEntry": "./ets/insightintents/WidgetExecutor.ets",
8. "form": {
9. "ability": "PlayerWidgetAbility",
10. "formName": "mini_player"
11. }
12. }
13. ]
14. }
```

系统入口通过FormComponent组件展示卡片内容。

## insight\_intent.json配置文件说明

意图配置文件insight\_intent.json位于工程的"resources/base/profile"目录，用于声明意图配置信息。其中，"insightIntents"数组包含通过配置文件开发的所有意图配置信息，数组中的属性如下：

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| intentName | 表示意图名称，是意图的唯一标识。取值为首字母大写、包含字母和数字的字符串。 | 字符串 | 否 |
| domain | 表示意图垂域名称，用于将意图按具体领域分类（例如：视频、音乐、游戏）。 | 字符串 | 否 |
| intentVersion | 表示意图版本号。当意图能力演进时，可通过版本号进行区分和管理。支持用点分隔开的三段数据序列，例如"1.0.1"。 | 字符串 | 否 |
| srcEntry | 表示意图执行文件相对路径。取值为长度不超过127字节的字符串。 | 字符串 | 否 |
| uiAbility | 表示意图绑定的UIAbility组件信息。包含"ability"字段和"executeMode"字段。  - ability：必选字段，表示UIAbility组件名称，取值与module.json5配置文件[abilities标签](module-configuration-file.md#abilities标签)的"name"字段保持一致。  - executeMode：必选字段，表示执行模式，取值范围是"foreground"和"background"。  - 取值为"foreground"，表示支持在UIAbility组件前台启动时执行意图逻辑。  - 取值为"background"，表示支持在UIAbility组件后台启动时执行意图逻辑。 | 对象 | 是 |
| uiExtension | 表示意图绑定的UIExtensionAbility组件信息。仅包含"ability"必选字段，表示UIExtensionAbility组件名称，取值与module.json5配置文件[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)的"name"字段保持一致。 | 对象 | 是 |
| form | 表示意图绑定的卡片信息。包含"ability"字段和"formName"字段。  - ability：必选字段，表示FormExtensionAbility组件名称，取值与module.json5配置文件[extensionAbilities标签](module-configuration-file.md#extensionabilities标签) 的"name"字段保持一致。  - formName：必选字段，表示卡片名称，取值与[卡片配置](arkts-ui-widget-configuration.md#卡片配置)的"name"字段保持一致。 | 对象 | 是 |
| displayName | 表示意图显示名称。 | 字符串 | 是 |
| displayDescription | 表示意图显示描述。 | 字符串 | 是 |
| icon | 表示意图图标。支持网络资源和本地资源。 | 字符串 | 是 |
| keywords | 表示意图的搜索关键字。 | 字符串数组 | 是 |
| inputParams | 表示意图参数的数据格式声明，用于意图调用时定义入参的数据格式。 | 对象 | 是 |
| outputParams | 表示意图调用返回结果的数据格式声明，用于定义意图调用返回结果的数据格式。 | 对象 | 是 |
| entities | 表示意图实体定义，用于数据传递。 | 对象 | 是 |
