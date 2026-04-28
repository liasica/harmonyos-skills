---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentdecorator
title: @ohos.app.ability.InsightIntentDecorator (意图装饰器定义)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.InsightIntentDecorator (意图装饰器定义)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:77cb6b65ab5faaa4d1cc9d513e92fe76d6ef93b8205c2a785f2d120f33dc976a
---

InsightIntentDecorator模块提供了几类意图装饰器，用于装饰类或方法。开发者可以[使用装饰器开发意图](../harmonyos-guides/insight-intent-decorator-development.md), 将应用的功能定义为意图，并集成到智能问答、智能搜索、智能推荐等AI入口。

* [@InsightIntentLink](js-apis-app-ability-insightintentdecorator.md#insightintentlink)装饰器：使用该装饰器装饰当前应用的uri链接，可以将该uri链接定义为意图，便于AI入口通过意图快速跳转到当前应用。该装饰器支持的参数参见[LinkIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#linkintentdecoratorinfo)。
* [@InsightIntentPage](js-apis-app-ability-insightintentdecorator.md#insightintentpage)装饰器：使用该装饰器装饰当前应用的Page页面，可以将该Page页面定义为意图，便于AI入口通过意图快速跳转到当前Page页面。该装饰器支持的参数参见[PageIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#pageintentdecoratorinfo)。
* [@InsightIntentFunction](js-apis-app-ability-insightintentdecorator.md#insightintentfunction)装饰器与[@InsightIntentFunctionMethod](js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod)装饰器：两者必须组合使用。使用[@InsightIntentFunction](js-apis-app-ability-insightintentdecorator.md#insightintentfunction)装饰器来装饰类，同时使用[@InsightIntentFunctionMethod](js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod)装饰器来装饰类中的静态函数，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。
* [@InsightIntentEntry](js-apis-app-ability-insightintentdecorator.md#insightintententry)装饰器：使用该装饰器装饰一个继承自[InsightIntentEntryExecutor](js-apis-app-ability-insightintententryexecutor.md)的类，实现意图操作并配置意图依赖的Ability组件，便于AI入口拉起依赖的Ability组件时，执行对应的意图操作。该装饰器支持的参数参见[EntryIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#entryintentdecoratorinfo)。
* [@InsightIntentForm](js-apis-app-ability-insightintentdecorator.md#insightintentform)装饰器：使用该装饰器装饰[FormExtensionAbility](js-apis-app-form-formextensionability.md)并配置FormExtensionAbility绑定的卡片名称，便于AI入口通过意图添加卡片。该装饰器支持的参数参见[FormIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#formintentdecoratorinfo)。
* [@InsightIntentEntity](js-apis-app-ability-insightintentdecorator.md#insightintententity)装饰器：使用该装饰器装饰一个继承自[IntentEntity](js-apis-app-ability-insightintent.md#intententity20)的类，可将该类定义为意图实体，用于传递意图调用时所需的参数。该装饰器支持的参数参见[IntentEntityDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intententitydecoratorinfo)。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 基本概念

PhonePC/2in1TabletTVWearable

意图可以分为标准意图和自定义意图。

系统会根据[IntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intentdecoratorinfo)中的schema与intentVersion字段，在标准意图列表查询是否存在匹配的意图。

* 如果存在匹配的意图，则对应的意图为标准意图。
* 如果不存在匹配的意图，则对应的意图为自定义意图。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry } from '@kit.AbilityKit';
```

## @InsightIntentLink

PhonePC/2in1TabletTVWearable

使用该装饰器装饰当前应用的uri链接，可以将该uri链接定义为意图，便于AI入口通过定义的意图快速跳转到当前应用。该装饰器支持的参数参见[LinkIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#linkintentdecoratorinfo)。

说明

uri链接格式需要符合[应用链接说明](../harmonyos-guides/app-uri-config.md)中的要求。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

以自定义意图为例：自定义意图的parameters需要传入标准的JSON Schema数据结构。

```
1. import { InsightIntentLink, LinkParamCategory } from '@kit.AbilityKit';

3. @InsightIntentLink({
4. intentName: 'PlayMusic',
5. domain: 'MusicDomain',
6. intentVersion: '1.0.1',
7. displayName: '播放歌曲',
8. displayDescription: '播放音乐意图',
9. icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
10. llmDescription: '支持传递歌曲名称，播放音乐',
11. keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
12. uri: 'https://www.example.com/music/',
13. paramMappings: [{
14. paramName: 'songName',
15. paramMappingName: 'music',
16. paramCategory: LinkParamCategory.LINK
17. }],
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
30. 'required': ['songName'],
31. 'additionalProperties': false
32. },
33. result: {
34. 'type': 'object',
35. 'propertyNames': {
36. 'enum': [
37. 'code',
38. 'result'
39. ]
40. },
41. 'required': [
42. 'code',
43. 'result'
44. ],
45. 'properties': {
46. 'code': {
47. 'description': '执行结果码',
48. 'type': 'number'
49. },
50. 'result': {}
51. }
52. }
53. })
54. export class ClassForLink {
55. private _playback: string = 'intention_test';

57. public set playback(value: string) {
58. this._playback = value;
59. }

61. public get playback(): string {
62. return this._playback;
63. }

65. constructor(playback: string) {
66. this._playback = playback;
67. }

69. static Function1(playbackProgress: number, playback?: number): void {
70. console.info(`Function1, playbackProgress: ${playbackProgress}.`);
71. }
72. }
```

## IntentDecoratorInfo

PhonePC/2in1TabletTVWearable

意图装饰器的通用属性，用于定义意图的基本信息（包括意图名称、意图版本号）。适用于本模块的所有装饰器。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

说明

如果根据schema与intentVersion字段，在标准意图列表存在匹配的标准意图，系统会将intentName、domain、llmDescription、keywords、parameters、result字段均设置为标准意图的相应字段值。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intentName | string | 否 | 否 | 表示意图名称，是意图的唯一标识。 |
| domain | string | 否 | 否 | 表示意图垂域，用于将意图按垂直领域分类（例如：视频、音乐、游戏），取值范围参见[各垂域的智慧分发特性列表](../service/intents-ai-distribution-characteristic-0000001901922213.md#section2656133582215)中的垂域字段。 |
| intentVersion | string | 否 | 否 | 表示意图版本号。当意图能力演进时，可通过版本号进行区分和管理。 |
| displayName | string | 否 | 否 | 表示显示给用户的意图名称。 |
| displayDescription | string | 否 | 是 | 表示显示给用户的意图描述。 |
| schema | string | 否 | 是 | 表示接入的标准意图的名称。开发者[接入标准意图](../harmonyos-guides/insight-intent-definition.md#接入标准意图)时，需要配置该字段，[创建自定义意图](../harmonyos-guides/insight-intent-definition.md#创建自定义意图)时，无需配置该字段。标准意图列表参见[附录：标准意图接入规范](../harmonyos-guides/insight-intent-access-specifications.md)。 |
| icon | ResourceStr | 否 | 是 | 表示意图图标，用于在AI入口显示。  - 当取值为字符串类型时，表示图标读取网络资源。  - 当取值为[Resource](js-apis-resource-manager.md)时，表示图标读取本地资源。 |
| llmDescription | string | 否 | 是 | 表示意图的功能，用于大型语言模型理解该意图。 |
| keywords | string[] | 否 | 是 | 表示意图的搜索关键字。 |
| parameters | Record<string, Object> | 否 | 是 | 表示意图参数的数据格式声明，用于意图调用时定义入参的数据格式。取值参见[各垂域意图Schema](../service/intents-schema-0000001901962713.md) |
| result | Record<string, Object> | 否 | 是 | 表示意图调用返回结果的数据格式声明，用于定义意图调用返回结果的数据格式。 |

## LinkIntentDecoratorInfo

PhonePC/2in1TabletTVWearable

LinkIntentDecoratorInfo继承自[IntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intentdecoratorinfo)，用于描述[@InsightIntentLink](js-apis-app-ability-insightintentdecorator.md#insightintentlink)装饰器支持的参数，例如应用间跳转需要的uri信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 表示意图的uri信息。 |
| paramMappings | [LinkIntentParamMapping](js-apis-app-ability-insightintentdecorator.md#linkintentparammapping)[] | 否 | 是 | 意图参数和uri信息的映射。 |

## LinkIntentParamMapping

PhonePC/2in1TabletTVWearable

LinkIntentParamMapping是[@InsightIntentLink](js-apis-app-ability-insightintentdecorator.md#insightintentlink)装饰器的意图参数和uri信息的映射。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| paramName | string | 否 | 否 | 表示意图参数的名称。 |
| paramMappingName | string | 否 | 是 | 表示意图参数映射名称。 |
| paramCategory | [LinkParamCategory](js-apis-app-ability-insightintentdecorator.md#linkparamcategory) | 否 | 是 | 表示意图参数类别。  若意图参数类别取值为[LINK](js-apis-app-ability-insightintentdecorator.md#linkparamcategory)，系统获取paramName字段对应的意图参数映射名称，并将该意图参数映射名称拼接到uri链接的末尾(以键值对的形式key=value，key为意图参数映射名称，value为意图参数值)。  若意图参数类别为[WANT](js-apis-app-ability-insightintentdecorator.md#linkparamcategory)，系统获取paramName字段对应的意图参数映射名称，并将该意图参数映射名称及取值通过[Want](js-apis-app-ability-want.md)的parameters字段进行传递。 |

## LinkParamCategory

PhonePC/2in1TabletTVWearable

[@InsightIntentLink](js-apis-app-ability-insightintentdecorator.md#insightintentlink)装饰器的意图参数类别，用于定义意图参数的传递形式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINK | 'link' | 表示意图参数类别为'link'。意图参数将被拼接到uri链接的末尾，以uri链接的形式传给应用。 |
| WANT | 'want' | 表示意图参数类别为'want'。意图参数将通过[Want](js-apis-app-ability-want.md)的parameters字段传给应用。 |

## @InsightIntentPage

PhonePC/2in1TabletTVWearable

使用该装饰器装饰当前应用的页面，可以将页面定义为意图，便于AI入口通过意图快速跳转到指定页面。该装饰器支持的参数参见[PageIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#pageintentdecoratorinfo)。

说明

该装饰器仅支持装饰struct页面。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```
1. import { InsightIntentPage } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. @InsightIntentPage({
6. intentName: 'SearchMusic',
7. domain: 'MusicDomain',
8. intentVersion: '1.0.1',
9. displayName: '搜索歌曲',
10. displayDescription: '搜索歌曲意图',
11. schema: 'SearchMusic',
12. uiAbility: 'Entry',
13. pagePath: './ets/pages/Index',
14. navigationId: '1',
15. navDestinationName: 'PageOne',
16. })
17. struct Index {
18. @State message: string = 'Hello World';

20. build() {
21. RelativeContainer() {
22. Text(this.message)
23. .id('HelloWorld')
24. .fontSize(50)
25. .fontWeight(FontWeight.Bold)
26. .alignRules({
27. center: { anchor: '__container__', align: VerticalAlign.Center },
28. middle: { anchor: '__container__', align: HorizontalAlign.Center }
29. })
30. }
31. .height('100%')
32. .width('100%')
33. }
34. }
```

## PageIntentDecoratorInfo

PhonePC/2in1TabletTVWearable

PageIntentDecoratorInfo继承自[IntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intentdecoratorinfo)，用于描述[@InsightIntentPage](js-apis-app-ability-insightintentdecorator.md#insightintentpage)装饰器支持的参数，例如目标页面的[NavDestination](ts-basic-components-navigation.md#navdestination10)名称。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uiAbility | string | 否 | 是 | 表示与意图绑定的UIAbility名称。 |
| pagePath | string | 否 | 否 | 表示与意图绑定的页面路径，该页面需要是一个实际存在的文件。 |
| navigationId | string | 否 | 是 | 表示与意图绑定的[Navigation组件](ts-basic-components-navigation.md#属性)的id属性。 |
| navDestinationName | string | 否 | 是 | 表示与意图绑定[NavDestination组件](ts-basic-components-navigation.md#navdestination10)的名称。 |

## @InsightIntentFunction

PhonePC/2in1TabletTVWearable

该装饰器与[@InsightIntentFunctionMethod](js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod)装饰器必须组合使用。

使用该装饰器来装饰类，同时使用[@InsightIntentFunctionMethod](js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod)装饰器来装饰类中的静态函数，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

## @InsightIntentFunctionMethod

PhonePC/2in1TabletTVWearable

该装饰器与[@InsightIntentFunction](js-apis-app-ability-insightintentdecorator.md#insightintentfunction)装饰器必须组合使用。

使用该装饰器来装饰类中的静态函数，同时使用[@InsightIntentFunction](js-apis-app-ability-insightintentdecorator.md#insightintentfunction)装饰器来装饰静态函数所属的类，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。

说明

静态方法所在的类需要通过export导出。

函数的参数名称、参数类型需要与意图定义的参数名称、参数类型保持一致。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```
1. import { InsightIntentFunction, InsightIntentFunctionMethod } from '@kit.AbilityKit';

3. @InsightIntentFunction()
4. export class ClassForFuncDemo {
5. @InsightIntentFunctionMethod({
6. intentName: 'GetWeather',
7. domain: 'LifeDomain',
8. intentVersion: '1.0.1',
9. displayName: '查询天气',
10. displayDescription: '显示天气信息',
11. icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
12. llmDescription: 'Get weather of an location',
13. parameters: {
14. 'schema': 'http://json-schema.org/draft-07/schema#',
15. 'type': 'object',
16. 'title': 'Weather Schema',
17. 'description': 'A schema for get weather of an location',
18. 'properties': {
19. 'location': {
20. 'type': 'string',
21. 'description': 'The city and state, e.g. Hangzhou',
22. 'minLength': 1
23. }
24. },
25. 'required': ['location'],
26. 'additionalProperties': false
27. }
28. })
29. static getWeather(location: string): string {
30. console.info(`location: ${location}`);
31. return 'The current temperature in Hangzhou is 24℃';
32. }
33. }
```

## FunctionIntentDecoratorInfo

PhonePC/2in1TabletTVWearable

[@InsightIntentFunctionMethod](js-apis-app-ability-insightintentdecorator.md#insightintentfunctionmethod)装饰器的参数类型，当前全部属性均继承自[IntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intentdecoratorinfo)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

## @InsightIntentEntry

PhonePC/2in1TabletTVWearable

使用该装饰器装饰一个继承自[InsightIntentEntryExecutor](js-apis-app-ability-insightintententryexecutor.md)的类，实现意图操作并配置意图依赖的Ability组件，便于AI入口拉起依赖的Ability组件时，执行对应的意图操作。该装饰器支持的参数参见[EntryIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#entryintentdecoratorinfo)。

说明

* 如果使用该装饰器接入标准意图，必须实现标准意图Json Schema中定义的所有必选参数且类型匹配。
* 如果创建自定义意图，必须实现parameters字段中定义的所有必选参数且类型匹配。
* 被装饰的类需要使用export default导出。类的属性仅支持基础类型或意图实体，返回值仅支持意图实体。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

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

## EntryIntentDecoratorInfo

PhonePC/2in1TabletTVWearable

EntryIntentDecoratorInfo继承自[IntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intentdecoratorinfo)，用于描述[@InsightIntentEntry](js-apis-app-ability-insightintentdecorator.md#insightintententry)装饰器支持的参数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | 表示与意图绑定的Ability名称。 |
| executeMode | [insightIntent.ExecuteMode](js-apis-app-ability-insightintent.md#executemode)[] | 否 | 否 | 表示意图调用执行模式。即拉起绑定的Ability时支持的执行模式。 |

## @InsightIntentForm

PhonePC/2in1TabletTVWearable

使用该装饰器装饰[FormExtensionAbility](js-apis-app-form-formextensionability.md)并配置FormExtensionAbility绑定的卡片名称，便于AI入口通过意图添加卡片。该装饰器支持的参数参见[FormIntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#formintentdecoratorinfo)。

说明

卡片名称定义的要求参见[卡片配置](../harmonyos-guides/arkts-ui-widget-configuration.md#卡片配置)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```
1. import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
2. import { insightIntent, Want, InsightIntentForm } from '@kit.AbilityKit';

4. // 使用@InsightIntentForm装饰器将该FormExtensionAbility名为widget的卡片定义为意图
5. @InsightIntentForm({
6. intentName: 'PlayMusic',
7. domain: 'MusicDomain',
8. intentVersion: '1.0.1',
9. displayName: '播放歌曲',
10. displayDescription: '播放音乐意图',
11. icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
12. llmDescription: '支持传递歌曲名称，播放音乐',
13. keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
14. parameters: {
15. '$schema': 'http://json-schema.org/draft-07/schema#',
16. 'type': 'object',
17. 'title': 'Song Schema',
18. 'description': 'A schema for describing songs and their artists',
19. 'properties': {
20. 'songName': {
21. 'type': 'string',
22. 'description': 'The name of the song',
23. 'minLength': 1
24. },
25. 'artist': {
26. 'type': 'object',
27. 'description': 'Information about the artist',
28. 'properties': {
29. 'country': {
30. 'type': 'string',
31. 'description': 'The artist\'s country of origin',
32. 'default': 'zh'
33. },
34. 'city': {
35. 'type': 'object',
36. 'description': 'The artist\' city of origin'
37. },
38. 'name': {
39. 'type': 'string',
40. 'description': 'The name of the artist',
41. 'minLength': 1
42. }
43. },
44. 'required': ['name']
45. }
46. },
47. 'required': ['songName']
48. },
49. formName: 'widget'
50. })
51. export default class EntryFormAbility extends FormExtensionAbility {
52. songName: string = '';

54. onAddForm(want: Want) {
55. // 该方法被调用时，将返回FormBindingData对象
56. let formData = '';
57. return formBindingData.createFormBindingData(formData);
58. }
59. }
```

## FormIntentDecoratorInfo

PhonePC/2in1TabletTVWearable

FormIntentDecoratorInfo继承自[IntentDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intentdecoratorinfo)，用于描述[@InsightIntentForm](js-apis-app-ability-insightintentdecorator.md#insightintentform)装饰器支持的参数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formName | string | 否 | 否 | 表示FormExtensionAbility绑定的卡片名称。 |

## @InsightIntentEntity

PhonePC/2in1TabletTVWearable

使用该装饰器装饰一个继承自[IntentEntity](js-apis-app-ability-insightintent.md#intententity20)的类，可将该类定义为意图实体，用于传递意图调用时所需的参数。该装饰器支持的参数参见[IntentEntityDecoratorInfo](js-apis-app-ability-insightintentdecorator.md#intententitydecoratorinfo)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

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
25. 'required': ['name']
26. }
27. })
28. export class ArtistClassDef implements insightIntent.IntentEntity {
29. entityId: string = 'id';
30. name: string = '';
31. }
```

## IntentEntityDecoratorInfo

PhonePC/2in1TabletTVWearable

用于描述[@InsightIntentEntity](js-apis-app-ability-insightintentdecorator.md#insightintententity)装饰器支持的参数。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityCategory | string | 否 | 否 | 表示意图实体类别。可以基于意图实体类别对意图实体进行归类 |
| parameters | Record<string, Object> | 否 | 是 | 表示意图实体的数据格式声明。用于定义意图实体的数据格式。 |
