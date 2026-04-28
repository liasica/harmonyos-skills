---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-decorator-development
title: 使用装饰器开发意图
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 意图框架开发指导 > 开发意图 > 使用装饰器开发意图
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b70769b3d1f6a4d31a8681e89ccc894bb03f79097b93b6d52c19cb14cfabdf24
---

## 使用场景

从 API version 20开始，支持通过装饰器开发意图，支持将现有功能通过装饰器快速集成至系统入口。典型场景介绍如下。

| 意图调用场景 | 常见意图举例 | 意图开发方式 |
| --- | --- | --- |
| 拉起应用 | - 播放音乐。  - 打开购物软件直达商品详情页。 | - 通过[@InsightIntentEntry](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententry)创建新的意图逻辑，绑定UIAbility组件或UIExtensionAbility组件。  - 通过[@InsightIntentLink](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentlink)将uri链接转换为意图。  - 通过[@InsightIntentPage](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentpage) 将页面路由转换为意图。 |
| 查询或更新信息 | - 查询天气。  - 修改应用配置或更新。 | - 通过[@InsightIntentFunctionMethod](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod) 将函数调用转换为系统意图。  - 通过[@InsightIntentEntry](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententry)创建新的意图逻辑，绑定UIAbility组件的后台执行模式或ServiceExtensionAbility组件。 |
| 添加服务卡片 | - 添加天气卡片。 | - 通过[@InsightIntentForm](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentform)开发意图。 |

## 运行机制

| 功能 | 意图开发 | 意图执行 |
| --- | --- | --- |
| 使用[@InsightIntentEntry](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententry)开发意图 | 1. 开发者新增意图执行文件，若该执行文件未被其他文件导入，需要通过insight\_intent.json文件的"insightIntentsSrcEntry"字段配置意图执行文件路径，使其参与编译。  2. 通过装饰器定义意图需要绑定Ability组件、定义意图执行模式。 | 系统入口匹配意图，根据意图执行模式触发Ability组件的启动和意图执行。 |
| 使用[@InsightIntentLink](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentlink)开发意图 | 开发者定义Link跳转意图，支持已有的uri链接和新增uri链接。 | 系统入口匹配意图，传递uri链接，通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)触发意图执行，意图执行时的入参处理见[LinkIntentParamMapping](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#linkintentparammapping)的paramCategory说明。 |
| 使用[@InsightIntentPage](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentpage)开发意图 | 开发者定义页面跳转意图，配置意图对应的UIAbility组件、[页面路由](arkts-routing.md)的路径和[Navigation](arkts-navigation-architecture.md)路径。 | 1. 系统入口通过startAbility启动意图绑定的UIAbility组件。若意图未绑定UIAbility组件，则启动意图所在module的[mainElement](module-configuration-file.md#配置文件标签)对应的UIAbility组件。  2. 意图执行时，若应用未启动，在UIAbility的首页加载后跳转到意图对应的页面；若应用已启动，由当前页面跳转到意图对应的页面。  3. 意图执行时，参数会被传递给目标页面。  4. "navigationId"字段或"navDestinationName"字段匹配失败时，退化为"pagePath"字段对应的页面跳转。 |
| 使用[@InsightIntentFunctionMethod](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod)开发意图 | 开发者为静态方法定义意图，静态方法可以是已有方法或新增方法。 | 系统入口通过[Call调用](../harmonyos-references/js-apis-app-ability-uiability.md#后台通信能力)启动意图所在module的[mainElement](module-configuration-file.md#配置文件标签)对应的UIAbility组件。 |
| 使用[@InsightIntentForm](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintentform)开发意图 | 开发者定义卡片意图，卡片可以是已有卡片或新增卡片。 | 系统入口通过FormComponent组件创建意图卡片。 |

## 开发步骤

本章节以通过@InsightIntentEntry开发标准意图和自定义意图举例，其他装饰器开发标准意图和自定义意图与@InsightIntentEntry相似，可以结合API参考开发其他类型的意图。

### 通过意图装饰器开发标准意图

以通过@InsightIntentEntry装饰器开发[查看快递](insight-intent-access-specifications.md#查看快递)标准意图举例。

1. 在insight\_intent.json配置文件中的"insightIntentsSrcEntry"字段声明意图执行文件。

   ```
   1. {
   2. "insightIntentsSrcEntry": [
   3. {
   4. "srcEntry": "./ets/insightintents/ViewLogisticsImpl.ets"
   5. }
   6. ]
   7. }
   ```
2. 实现意图执行器。

   开发标准意图无需开发者自行定义意图的大语言模型描述、意图参数定义和意图执行结果定义，根据"schema"字段和"intentVersion"字段匹配[附录：标准意图接入规范](insight-intent-access-specifications.md)中的标准意图。意图执行器需要从InsightIntentEntryExecutor<T>类继承，实现onExecute()方法。

   ```
   1. import { InsightIntentEntryExecutor, insightIntent, InsightIntentEntry } from '@kit.AbilityKit';

   3. class ViewLogisticsResultDef {
   4. public msg?: string = '';
   5. }

   7. @InsightIntentEntry({
   8. intentName: 'ViewLogistics',
   9. domain: 'LocalDomain',
   10. intentVersion: '1.0.1',
   11. displayName: '查询快递',
   12. displayDescription: '根据快递单号查询快递信息',
   13. schema: 'ViewLogistics',
   14. icon: $r('app.media.viewLogistics'), // 请将$r('app.media.viewLogistics')替换为实际资源文件
   15. abilityName: 'EntryAbility',
   16. executeMode: [insightIntent.ExecuteMode.UI_ABILITY_BACKGROUND]
   17. })
   18. export default class ViewLogisticsImpl extends InsightIntentEntryExecutor<ViewLogisticsResultDef> {
   19. public trackingNo?: string = '';
   20. public entityId?: string = '';

   22. onExecute(): Promise<insightIntent.IntentResult<ViewLogisticsResultDef>> {
   23. // 执行查询快递逻辑
   24. let result: insightIntent.IntentResult<ViewLogisticsResultDef> = {
   25. code: 0,
   26. result: {
   27. msg: 'the logistics is being delivered'
   28. }
   29. };
   30. return Promise.resolve(result);
   31. };
   32. }
   ```

   [ViewLogisticsImpl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/OrnamentIntent/entry/src/main/ets/insightintents/ViewLogisticsImpl.ets#L16-L49)

意图执行过程：

1. 系统入口响应用户“查询单号为12345的快递”的请求，匹配到该应用的"ViewLogistics"意图，通过意图框架触发该应用的"ViewLogistics"意图执行。
2. 由于意图绑定了"EntryAbility"组件、配置了insightIntent.ExecuteMode.UI\_ABILITY\_BACKGROUND执行模式，在意图执行过程中，"ViewLogistics"意图绑定的"EntryAbility"组件会通过[Call调用](../harmonyos-references/js-apis-app-ability-uiability.md#后台通信能力)启动，意图执行过程中，ViewLogisticsImpl类的属性"trackingNo"会被赋值，进而执行onExecute()方法，将意图执行结果通过意图框架返回给系统入口。
3. 系统入口将意图执行结果转换为自然语言呈现给用户。

### 通过意图装饰器开发自定义意图

以开发“播放音乐”自定义意图举例，需要定义意图的大语言模型描述、意图搜索关键字、意图参数定义和意图执行结果定义。

1. 在insight\_intent.json配置文件中的"insightIntentsSrcEntry"字段声明意图执行文件。

   ```
   1. {
   2. "insightIntentsSrcEntry": [
   3. {
   4. "srcEntry": "./ets/insightintents/PlayMusicImpl.ets"
   5. }
   6. ]
   7. }
   ```
2. 实现意图执行器。

   开发自定义意图需要开发者定义意图的大语言模型描述、意图搜索关键字、意图参数定义和意图执行结果定义。意图执行器需要从InsightIntentEntryExecutor<T>类继承，实现onExecute()方法。

   ```
   1. // `insight_intent.json`文件的"insightIntentsSrcEntry"字段的实现
   2. import { InsightIntentEntryExecutor, insightIntent, InsightIntentEntry } from '@kit.AbilityKit';

   4. // 意图执行返回值数据格式定义
   5. class PlayMusicResultDef {
   6. public msg?: string = '';
   7. }

   9. // 意图定义
   10. @InsightIntentEntry({
   11. intentName: 'PlayMusic',
   12. domain: 'MusicDomain',
   13. intentVersion: '1.0.1',
   14. displayName: '播放歌曲',
   15. displayDescription: '播放音乐意图',
   16. icon: $r('app.media.playMusic'), // 请将$r('app.media.playMusic')替换为实际资源文件
   17. llmDescription: '支持传递歌曲名称，播放音乐',
   18. keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
   19. abilityName: 'EntryAbility',
   20. executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
   21. parameters: {
   22. 'type': 'object',
   23. 'description': 'A schema for describing songs and their artists',
   24. 'properties': {
   25. 'songName': {
   26. 'type': 'string',
   27. 'description': 'The name of the song',
   28. 'minLength': 1
   29. },
   30. 'singer': {
   31. 'type': 'string',
   32. 'description': 'The name of the singer',
   33. 'minLength': 1
   34. }
   35. },
   36. 'required': ['songName']
   37. }
   38. })
   39. export default class PlayMusicImpl extends InsightIntentEntryExecutor<PlayMusicResultDef> {
   40. public songName: string = '';
   41. public singer?: string = '';

   43. onExecute(): Promise<insightIntent.IntentResult<PlayMusicResultDef>> {
   44. // 执行音乐播放逻辑
   45. let result: insightIntent.IntentResult<PlayMusicResultDef> = {
   46. code: 123,
   47. result: {
   48. msg: 'play music succeed'
   49. }
   50. };
   51. return Promise.resolve(result);
   52. };
   53. }
   ```

   [PlayMusicImpl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/OrnamentIntent/entry/src/main/ets/insightintents/PlayMusicImpl.ets#L16-L71)

意图执行过程：

1. 系统入口响应用户“播放歌手A的歌曲B”的请求，匹配到该应用的"PlayMusic"意图，通过意图框架触发该应用的"PlayMusic"意图执行。
2. 意图绑定了"EntryAbility"组件、配置了insightIntent.ExecuteMode.UI\_ABILITY\_FOREGROUND执行模式，在意图执行过程中，"PlayMusic"意图绑定的"EntryAbility"组件会通过startAbility启动，PlayMusicImpl类的属性"songName"和"singer"会被赋值，进而执行onExecute()方法，将意图执行结果通过意图框架返回给系统入口。
3. 系统入口将意图执行结果转换为自然语言呈现给用户。

### （可选）通过开发意图实体传递复杂参数

由系统入口传递给应用的数据默认为基础类型。如果需要复杂数据（例如，播放音乐时需要传入的歌手信息包括歌手姓名、国籍等多个字段），需要采用对象类型，并使用[@InsightIntentEntity](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententity)装饰器装饰。被装饰的对象称为意图实体。

以播放音乐为例，用户告诉小艺希望播放的音乐名称与歌手信息，小艺根据音乐名称和歌手信息拉起对应音乐界面，播放该音乐。

为了实现该场景，开发者可以将歌手信息定义为意图实体，并开发意图实体。具体步骤如下：

1. 定义意图实体。

   开发者将歌手信息（包括名称、国家、城市）定义为类，并使用@InsightIntentEntity装饰器将该类定义为意图实体。装饰器的parameters属性列出了类的数据成员、数据格式及每个成员的必选性。

   ```
   1. import { insightIntent, InsightIntentEntity } from '@kit.AbilityKit';

   3. @InsightIntentEntity({
   4. entityCategory: 'artist entity category',
   5. parameters: {
   6. '$id': '/schemas/ArtistClassDef',
   7. 'type': 'object',
   8. 'description': 'Information about the artist',
   9. 'properties': {
   10. 'country': {
   11. 'type': 'string',
   12. 'description': 'The artist\'s country of origin',
   13. 'default': 'zh'
   14. },
   15. 'city': {
   16. 'type': 'string',
   17. 'description': 'The artist\'s city of origin'
   18. },
   19. 'name': {
   20. 'type': 'string',
   21. 'description': 'The name of the artist',
   22. 'minLength': 1
   23. }
   24. },
   25. // name为必选参数
   26. 'required': ['name']
   27. }
   28. })
   29. export class ArtistClassDef implements insightIntent.IntentEntity {
   30. public entityId: string = '0x11';
   31. public country?: string = '';
   32. public city?: string = '';
   33. public name: string = '';
   34. }
   ```

   [ArtistClassDef.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/OrnamentIntent/entry/src/main/ets/insightintents/ArtistClassDef.ets#L16-L51)
2. 使用意图实体。添加[@InsightIntentEntry](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententry)装饰器的意图使用音乐名称和歌手信息（ArtistClassDef意图实体）作为播放音乐的入参。

   ```
   1. import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor, InsightIntentEntity } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const LOG_TAG: string = 'testTag-EntryIntent';

   6. @InsightIntentEntity({
   7. entityCategory: 'artist entity category',
   8. // @InsightIntentEntry装饰器中parameters中已描述ArtistClassDef意图实体信息，此处parameters可不写
   9. })
   10. export class ArtistClassDef implements insightIntent.IntentEntity {
   11. public entityId: string = '0x11';
   12. public country?: string = '';
   13. public city?: string = '';
   14. public name: string = '';
   15. }

   17. // 使用@InsightIntentEntry装饰器定义意图
   18. @InsightIntentEntry({
   19. intentName: 'PlayMusic',
   20. domain: 'MusicDomain',
   21. intentVersion: '1.0.1',
   22. displayName: '播放歌曲',
   23. displayDescription: '播放音乐意图',
   24. icon: $r('app.media.app_icon'), // 请将$r('app.media.app_icon')替换为实际资源文件
   25. llmDescription: '支持传递歌曲名称，播放音乐',
   26. keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
   27. abilityName: 'EntryAbility',
   28. executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
   29. parameters: {
   30. 'schema': 'http://json-schema.org/draft-07/schema#',
   31. 'type': 'object',
   32. 'title': 'Song Schema',
   33. 'description': 'A schema for describing songs and their artists',
   34. 'properties': {
   35. 'songName': {
   36. 'type': 'string',
   37. 'description': 'The name of the song',
   38. 'minLength': 1
   39. },
   40. 'artist': {
   41. 'type': 'object',
   42. 'description': 'Information about the artist',
   43. 'properties': {
   44. 'country': {
   45. 'type': 'string',
   46. 'description': 'The artist\'s country of origin',
   47. 'default': 'zh'
   48. },
   49. 'city': {
   50. 'type': 'string',
   51. 'description': 'The artist\'s city of origin'
   52. },
   53. 'name': {
   54. 'type': 'string',
   55. 'description': 'The name of the artist',
   56. 'minLength': 1
   57. }
   58. },
   59. 'required': ['name']
   60. }
   61. },
   62. 'required': ['songName']
   63. }
   64. })
   65. export default class PlayMusicDemo extends InsightIntentEntryExecutor<string> {
   66. public songName: string = '';
   67. // 使用意图实体
   68. public artist?: ArtistClassDef;

   70. onExecute(): Promise<insightIntent.IntentResult<string>> {
   71. hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo executeMode %{public}s', JSON.stringify(this.executeMode));
   72. hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo artist %{public}s', JSON.stringify(this.artist));
   73. let storage = new LocalStorage();
   74. storage.setOrCreate('songName', this.songName);
   75. storage.setOrCreate('artist', this.artist);
   76. // 根据 `executeMode` 参数的不同情况，提供不同的方式拉起 `PlayMusicPage` 页面。
   77. if (this.executeMode == insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND) {
   78. this.windowStage?.loadContent('pages/PlayMusicPage', storage);
   79. } else if (this.executeMode == insightIntent.ExecuteMode.UI_EXTENSION_ABILITY) {
   80. this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
   81. }
   82. // 定义意图的执行结果
   83. let result: insightIntent.IntentResult<string> = {
   84. code: 123,
   85. result: 'execute success'
   86. }
   87. hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
   88. return Promise.resolve(result);
   89. }
   90. }
   ```

   [PlayMusicDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/OrnamentIntent/feature/src/main/ets/insightintents/PlayMusicDemo.ets#L16-L107)
