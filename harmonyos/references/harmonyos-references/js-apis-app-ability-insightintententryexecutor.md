---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintententryexecutor
title: @ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:32e0afd32e5c48ea0349590af80e3b61a7168741e2c9f8a6876451c1dd653f01
---

本模块提供[@InsightIntentEntry](js-apis-app-ability-insightintentdecorator.md#insightintententry)装饰器的意图执行基类，必须与@InsightIntentEntry装饰器联合使用。

开发者需要在继承该基类的子类中，实现[onExecute()](js-apis-app-ability-insightintententryexecutor.md#onexecute)意图执行回调，并使用@InsightIntentEntry装饰器来装饰子类。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InsightIntentEntryExecutor } from '@kit.AbilityKit';
```

## InsightIntentEntryExecutor<T>

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| executeMode | [insightIntent.ExecuteMode](js-apis-app-ability-insightintent.md#executemode) | 否 | 否 | 表示意图执行模式。即拉起绑定的Ability组件时支持的执行模式。 |
| context | [InsightIntentContext](js-apis-app-ability-insightintentcontext.md) | 否 | 否 | 表示意图执行上下文。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 否 | 是 | 表示windowStage实例对象，和[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)接口的windowStage实例是同一个，可用于加载意图执行的页面。仅当executeMode字段取值为UI\_ABILITY\_FOREGROUND（即意图执行需要将UIAbility显示在前台时），该属性生效。 |
| uiExtensionSession | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 否 | 是 | 表示UIExtensionContentSession实例对象，和[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)接口的UIExtensionContentSession实例是同一个，可用于加载意图执行的页面。仅当executeMode字段取值为UI\_EXTENSION\_ABILITY（即意图执行需要拉起UIExtensionAbility时），该属性生效。 |

### onExecute

PhonePC/2in1TabletTVWearable

onExecute(): Promise<insightIntent.IntentResult<T>>

当AI入口触发意图执行时，系统将会拉起该类绑定的Ability组件，并触发该回调，开发者可以在该回调中实现需要执行的意图操作。使用Promise异步回调。

该接口的调用时机与意图执行模式的对应关系如下：

| 意图执行模式 | 接口调用时机和顺序 |
| --- | --- |
| [UI\_ABILITY\_FOREGROUND](js-apis-app-ability-insightintent.md#executemode)  UIAbility前台模式 | - 若UIAbility冷启动，意图执行时UIAbility生命周期触发顺序：[onCreate](js-apis-app-ability-uiability.md#oncreate)、[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)、onExecute、[onForeground](js-apis-app-ability-uiability.md#onforeground)。  - 若UIAbility热启动，且启动时UIAbility处于后台，意图执行时UIAbility生命周期触发顺序：[onNewWant](js-apis-app-ability-uiability.md#onnewwant)、onExecute、[onForeground](js-apis-app-ability-uiability.md#onforeground)。  - 若UIAbility热启动，且启动时UIAbility处于前台，意图执行时UIAbility生命周期触发顺序：onExecute。 |
| [UI\_ABILITY\_BACKGROUND](js-apis-app-ability-insightintent.md#executemode)  UIAbility后台模式 | - 若UIAbility冷启动，意图执行时UIAbility生命周期触发顺序：[onCreate](js-apis-app-ability-uiability.md#oncreate)、onExecute、[onBackground](js-apis-app-ability-uiability.md#onbackground)。  - 若UIAbility热启动，意图执行时UIAbility生命周期触发顺序：onExecute。 |
| [UI\_EXTENSION\_ABILITY](js-apis-app-ability-insightintent.md#executemode)  UIExtension模式 | 意图执行时UIExtensionAbility生命周期触发顺序：[onCreate](js-apis-app-ability-uiextensionability.md#oncreate)、[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)、onExecute、[onForeground](js-apis-app-ability-uiextensionability.md#onforeground)。 |

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<insightIntent.IntentResult<T>> | Promise对象。返回[insightIntent.IntentResult<T>](js-apis-app-ability-insightintent.md#intentresultt20)对象，表示意图执行结果。 |

**示例**

```
1. import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const LOG_TAG: string = 'testTag-EntryIntent';

6. // 使用@InsightIntentEntry装饰器定义意图
7. @InsightIntentEntry({
8. intentName: 'PlayMusic',
9. domain: 'MusicDomain',
10. intentVersion: '1.0.1',
11. displayName: '播放歌曲',
12. displayDescription: '播放音乐意图',
13. icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
14. llmDescription: '支持传递歌曲名称，播放音乐',
15. keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
16. abilityName: 'EntryAbility',
17. executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
18. parameters: {
19. 'schema': 'http://json-schema.org/draft-07/schema#',
20. 'type': 'object',
21. 'title': 'Song Schema',
22. 'description': 'A schema for describing songs and their artists',
23. 'properties': {
24. 'songName': {
25. 'type': 'string',
26. 'description': 'The name of the song',
27. 'minLength': 1
28. }
29. },
30. 'required': ['songName']
31. }
32. })
33. export default class PlayMusicDemo extends InsightIntentEntryExecutor<string> {
34. songName: string = '';

36. onExecute(): Promise<insightIntent.IntentResult<string>> {
37. hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo executeMode %{public}s', JSON.stringify(this.executeMode));
38. hilog.info(0x0000, LOG_TAG, '%{public}s', JSON.stringify(this));
39. let storage = new LocalStorage();
40. storage.setOrCreate('songName', this.songName);
41. // 根据executeMode参数的不同情况，提供不同拉起PlayMusicPage页面的方式。
42. if (this.executeMode == insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND) {
43. this.windowStage?.loadContent('pages/PlayMusicPage', storage);
44. } else if (this.executeMode == insightIntent.ExecuteMode.UI_EXTENSION_ABILITY) {
45. this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
46. }
47. // 定义意图的执行结果
48. let result: insightIntent.IntentResult<string> = {
49. code: 123,
50. result: 'result'
51. }
52. hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
53. // 以Promise的方式返回意图执行结果
54. return Promise.reject(result);
55. }
56. }
```
