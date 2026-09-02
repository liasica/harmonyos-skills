---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-decorator-development
title: 使用装饰器开发意图
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 方舟智能开发框架开发指导 > 意图框架开发指导 > 开发意图 > 使用装饰器开发意图
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8c0b65af098a0b89e8fc1431499a938cc7e26601fbe1c1ec5f50ad01af4525ef
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

   ```json
   {
     "insightIntentsSrcEntry": [
       {
         "srcEntry": "./ets/insightintents/ViewLogisticsImpl.ets"
       }
     ]
   }
   ```
2. 实现意图执行器。

   开发标准意图无需开发者自行定义意图的大语言模型描述、意图参数定义和意图执行结果定义，根据"schema"字段和"intentVersion"字段匹配[附录：标准意图接入规范](insight-intent-access-specifications.md)中的标准意图。意图执行器需要从InsightIntentEntryExecutor<T>类继承，实现onExecute()方法。

   ```typescript
   import { InsightIntentEntryExecutor, insightIntent, InsightIntentEntry } from '@kit.AbilityKit';

   class ViewLogisticsResultDef {
     public msg?: string = '';
   }

   @InsightIntentEntry({
     intentName: 'ViewLogistics',
     domain: 'LocalDomain',
     intentVersion: '1.0.1',
     displayName: '查询快递',
     displayDescription: '根据快递单号查询快递信息',
     schema: 'ViewLogistics',
     icon: $r('app.media.viewLogistics'), // 请将$r('app.media.viewLogistics')替换为实际资源文件
     abilityName: 'EntryAbility',
     executeMode: [insightIntent.ExecuteMode.UI_ABILITY_BACKGROUND]
   })
   export default class ViewLogisticsImpl extends InsightIntentEntryExecutor<ViewLogisticsResultDef> {
     public trackingNo?: string = '';
     public entityId?: string = '';

     onExecute(): Promise<insightIntent.IntentResult<ViewLogisticsResultDef>> {
       // 执行查询快递逻辑
       let result: insightIntent.IntentResult<ViewLogisticsResultDef> = {
         code: 0,
         result: {
           msg: 'the logistics is being delivered'
         }
       };
       return Promise.resolve(result);
     };
   }
   ```

意图执行过程：

1. 系统入口响应用户“查询单号为12345的快递”的请求，匹配到该应用的"ViewLogistics"意图，通过意图框架触发该应用的"ViewLogistics"意图执行。
2. 由于意图绑定了"EntryAbility"组件、配置了insightIntent.ExecuteMode.UI\_ABILITY\_BACKGROUND执行模式，在意图执行过程中，"ViewLogistics"意图绑定的"EntryAbility"组件会通过[Call调用](../harmonyos-references/js-apis-app-ability-uiability.md#后台通信能力)启动，意图执行过程中，ViewLogisticsImpl类的属性"trackingNo"会被赋值，进而执行onExecute()方法，将意图执行结果通过意图框架返回给系统入口。
3. 系统入口将意图执行结果转换为自然语言呈现给用户。

### 通过意图装饰器开发自定义意图

以开发“播放音乐”自定义意图举例，需要定义意图的大语言模型描述、意图搜索关键字、意图参数定义和意图执行结果定义。

1. 在insight\_intent.json配置文件中的"insightIntentsSrcEntry"字段声明意图执行文件。

   ```json
   {
     "insightIntentsSrcEntry": [
       {
         "srcEntry": "./ets/insightintents/PlayMusicImpl.ets"
       }
     ]
   }
   ```
2. 实现意图执行器。

   开发自定义意图需要开发者定义意图的大语言模型描述、意图搜索关键字、意图参数定义和意图执行结果定义。意图执行器需要从InsightIntentEntryExecutor<T>类继承，实现onExecute()方法。

   ```typescript
   // `insight_intent.json`文件的"insightIntentsSrcEntry"字段的实现
   import { InsightIntentEntryExecutor, insightIntent, InsightIntentEntry } from '@kit.AbilityKit';

   // 意图执行返回值数据格式定义
   class PlayMusicResultDef {
     public msg?: string = '';
   }

   // 意图定义
   @InsightIntentEntry({
     intentName: 'PlayMusic',
     domain: 'MusicDomain',
     intentVersion: '1.0.1',
     displayName: '播放歌曲',
     displayDescription: '播放音乐意图',
     icon: $r('app.media.playMusic'), // 请将$r('app.media.playMusic')替换为实际资源文件
     llmDescription: '支持传递歌曲名称，播放音乐',
     keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
     abilityName: 'EntryAbility',
     executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
     parameters: {
       'type': 'object',
       'description': 'A schema for describing songs and their artists',
       'properties': {
         'songName': {
           'type': 'string',
           'description': 'The name of the song',
           'minLength': 1
         },
         'singer': {
           'type': 'string',
           'description': 'The name of the singer',
           'minLength': 1
         }
       },
       'required': ['songName']
     }
   })
   export default class PlayMusicImpl extends InsightIntentEntryExecutor<PlayMusicResultDef> {
     public songName: string = '';
     public singer?: string = '';

     onExecute(): Promise<insightIntent.IntentResult<PlayMusicResultDef>> {
       // 执行音乐播放逻辑
       let result: insightIntent.IntentResult<PlayMusicResultDef> = {
         code: 123,
         result: {
           msg: 'play music succeed'
         }
       };
       return Promise.resolve(result);
     };
   }
   ```

意图执行过程：

1. 系统入口响应用户“播放歌手A的歌曲B”的请求，匹配到该应用的"PlayMusic"意图，通过意图框架触发该应用的"PlayMusic"意图执行。
2. 意图绑定了"EntryAbility"组件、配置了insightIntent.ExecuteMode.UI\_ABILITY\_FOREGROUND执行模式，在意图执行过程中，"PlayMusic"意图绑定的"EntryAbility"组件会通过startAbility启动，PlayMusicImpl类的属性"songName"和"singer"会被赋值，进而执行onExecute()方法，将意图执行结果通过意图框架返回给系统入口。
3. 系统入口将意图执行结果转换为自然语言呈现给用户。

### （可选）通过开发意图实体传递复杂参数

由系统入口传递给应用的数据默认为基础类型。如果需要复杂数据（例如，播放音乐时需要传入的歌手信息包括歌手姓名、国籍等多个字段），需要采用对象类型，并使用[@InsightIntentEntity](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententity)装饰器装饰。被装饰的对象称为意图实体。

以播放音乐为例，用户告诉系统入口希望播放的音乐名称与歌手信息，系统入口根据音乐名称和歌手信息拉起对应音乐界面，播放该音乐。

为了实现该场景，开发者可以将歌手信息定义为意图实体，并开发意图实体。具体步骤如下：

1. 定义意图实体。

   开发者将歌手信息（包括名称、国家、城市）定义为类，并使用@InsightIntentEntity装饰器将该类定义为意图实体。装饰器的parameters属性列出了类的数据成员、数据格式及每个成员的必选性。

   ```typescript
   import { insightIntent, InsightIntentEntity } from '@kit.AbilityKit';

   @InsightIntentEntity({
     entityCategory: 'artist entity category',
     parameters: {
       '$id': '/schemas/ArtistClassDef',
       'type': 'object',
       'description': 'Information about the artist',
       'properties': {
         'country': {
           'type': 'string',
           'description': 'The artist\'s country of origin',
           'default': 'zh'
         },
         'city': {
           'type': 'string',
           'description': 'The artist\'s city of origin'
         },
         'name': {
           'type': 'string',
           'description': 'The name of the artist',
           'minLength': 1
         }
       },
       // name为必选参数
       'required': ['name']
     }
   })
   export class ArtistClassDef implements insightIntent.IntentEntity {
     public entityId: string = '0x11';
     public country?: string = '';
     public city?: string = '';
     public name: string = '';
   }
   ```
2. 使用意图实体。添加[@InsightIntentEntry](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententry)装饰器的意图使用音乐名称和歌手信息（ArtistClassDef意图实体）作为播放音乐的入参。

   ```typescript
   import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor, InsightIntentEntity } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const LOG_TAG: string = 'testTag-EntryIntent';

   @InsightIntentEntity({
     entityCategory: 'artist entity category',
     // @InsightIntentEntry装饰器中parameters中已描述ArtistClassDef意图实体信息，此处parameters可不写
   })
   export class ArtistClassDef implements insightIntent.IntentEntity {
     public entityId: string = '0x11';
     public country?: string = '';
     public city?: string = '';
     public name: string = '';
   }

   // 使用@InsightIntentEntry装饰器定义意图
   @InsightIntentEntry({
     intentName: 'PlayMusic',
     domain: 'MusicDomain',
     intentVersion: '1.0.1',
     displayName: '播放歌曲',
     displayDescription: '播放音乐意图',
     icon: $r('app.media.app_icon'), // 请将$r('app.media.app_icon')替换为实际资源文件
     llmDescription: '支持传递歌曲名称，播放音乐',
     keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
     abilityName: 'EntryAbility',
     executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
     parameters: {
       'schema': 'http://json-schema.org/draft-07/schema#',
       'type': 'object',
       'title': 'Song Schema',
       'description': 'A schema for describing songs and their artists',
       'properties': {
         'songName': {
           'type': 'string',
           'description': 'The name of the song',
           'minLength': 1
         },
         'artist': {
           'type': 'object',
           'description': 'Information about the artist',
           'properties': {
             'country': {
               'type': 'string',
               'description': 'The artist\'s country of origin',
               'default': 'zh'
             },
             'city': {
               'type': 'string',
               'description': 'The artist\'s city of origin'
             },
             'name': {
               'type': 'string',
               'description': 'The name of the artist',
               'minLength': 1
             }
           },
           'required': ['name']
         }
       },
       'required': ['songName']
     }
   })
   export default class PlayMusicDemo extends InsightIntentEntryExecutor<string> {
     public songName: string = '';
     // 使用意图实体
     public artist?: ArtistClassDef;

     onExecute(): Promise<insightIntent.IntentResult<string>> {
       hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo executeMode %{public}s', JSON.stringify(this.executeMode));
       hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo artist %{public}s', JSON.stringify(this.artist));
       let storage = new LocalStorage();
       storage.setOrCreate('songName', this.songName);
       storage.setOrCreate('artist', this.artist);
       // 根据 `executeMode` 参数的不同情况，提供不同的方式拉起 `PlayMusicPage` 页面。
       if (this.executeMode == insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND) {
         this.windowStage?.loadContent('pages/PlayMusicPage', storage);
       } else if (this.executeMode == insightIntent.ExecuteMode.UI_EXTENSION_ABILITY) {
         this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
       }
       // 定义意图的执行结果
       let result: insightIntent.IntentResult<string> = {
         code: 123,
         result: 'execute success'
       }
       hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
       return Promise.resolve(result);
     }
   }
   ```

### （可选）通过开发意图实体支持应用内数据查询

从API版本26.0.0开始，支持开发查询应用内数据的意图实体。由系统入口传递给应用的数据通常为静态参数。如需基于应用内实时数据执行意图，可通过动态查询意图实体实现。

以播放音乐为例，当用户告知系统入口需要播放自定义歌单中的歌曲时，为使系统入口能够感知应用内歌单信息，开发者可将歌单信息定义为可查询意图实体，并在实体中描述歌单ID、歌单名称、显示名称、创建者等字段。意图实体需要继承[insightIntent.AppIntentEntity](../harmonyos-references/js-apis-app-ability-insightintent.md#appintententity)类并使用[@InsightIntentEntity](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententity)进行装饰。

系统入口可基于这些字段查询应用内可用歌单。例如，可以通过歌单ID、歌单名称、创建者筛选目标歌单，再将匹配结果用于后续意图执行。

为实现该场景，开发者可将歌单信息定义为可查询意图实体，并实现[onQueryEntity](../harmonyos-references/js-apis-app-ability-insightintent.md#onqueryentity)意图实体查询接口。具体步骤如下：

1. 定义支持查询的意图实体。

   开发者将歌单信息（包括歌单ID、歌单名称、显示名称、创建者）定义为继承自[insightIntent.AppIntentEntity](../harmonyos-references/js-apis-app-ability-insightintent.md#appintententity)的类，并使用[@InsightIntentEntity](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententity)装饰器将该类定义为可查询意图实体。[IntentEntityDecoratorInfo](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#intententitydecoratorinfo)中的supportedQueryProperties属性声明支持通过歌单ID、歌单名称、创建者筛选目标歌单。

   parameters属性需要列出实体的数据成员及其数据格式。这些属性对应继承自[insightIntent.AppIntentEntity](../harmonyos-references/js-apis-app-ability-insightintent.md#appintententity)类中定义的实体字段（例如entityId、playlistName、owner等）。当属性在[IntentEntityDecoratorInfo](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#intententitydecoratorinfo)的supportedQueryProperties中声明时，需要为该属性添加title，用于配置该查询条件的界面显示名称。

   [onQueryEntity](../harmonyos-references/js-apis-app-ability-insightintent.md#onqueryentity)接口需要根据传入的查询参数[QueryEntityParam](../harmonyos-references/js-apis-app-ability-insightintent.md#queryentityparam)返回符合条件的实体列表。推荐在[QueryEntityParam](../harmonyos-references/js-apis-app-ability-insightintent.md#queryentityparam)中的[queryType](../harmonyos-references/js-apis-app-ability-insightintent.md#querytype)为[ALL](../harmonyos-references/js-apis-app-ability-insightintent.md#querytype)时返回意图实体全部信息（例如返回所有歌单列表）；在[queryType](../harmonyos-references/js-apis-app-ability-insightintent.md#querytype)为[BY\_PROPERTY](../harmonyos-references/js-apis-app-ability-insightintent.md#querytype)时，根据QueryEntityParam中的parameters属性值筛选符合条件的信息（例如同时传入歌单名称和创建者时，返回歌单名称和创建者均匹配的歌单列表）。

   ```typescript
   import { insightIntent, InsightIntentEntity, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const LOG_TAG: string = 'testTag';

   // 意图实体定义
   @InsightIntentEntity({
     entityCategory: 'playlist_entity_category',
     parameters: {
       '$id': '/schemas/AppPlaylistEntity',
       'type': 'object',
       'description': 'Playlist entity with dynamic query support',
       'properties': {
         'entityId': {
           'type': 'string',
           'description': 'Playlist unique identifier',
           'title': '歌单id'
         },
         'playlistName': {
           'type': 'string',
           'description': 'Playlist name',
           'title': '歌单名称'
         },
         'owner': {
           'type': 'string',
           'description': 'Playlist owner',
           'title': '创建者'
         },
         'displayName': {
           'type': 'string',
           'description': 'Playlist display name',
         }
       },
       'required': ['playlistName', 'displayName']
     },
     supportedQueryProperties: ['entityId', 'playlistName', 'owner'] // 支持通过歌单ID、歌单名称、创建者筛选目标歌单
   })
   export class AppPlaylistEntity extends insightIntent.AppIntentEntity<AppPlaylistEntity> {
     public entityId: string = 'default';
     public playlistName: string = '';
     public displayName: string = '';
     public owner: string = '';

     async onQueryEntity(params: insightIntent.QueryEntityParam): Promise<Array<AppPlaylistEntity>> {
       const playlists: AppPlaylistEntity[] = [
         this.createEntity('p001', '夜跑歌单', '夜跑歌单', 'Alice'),
         this.createEntity('p002', '通勤歌单', '通勤歌单', 'Bob'),
         this.createEntity('p003', '睡前轻音乐', '睡前轻音乐', 'Alice')
       ];

       if (params.queryType === insightIntent.QueryType.ALL) {
         return playlists;
       }

       const query = params.parameters ?? {};
       const validKeys = Object.keys(query).filter((key) => ['entityId', 'playlistName', 'owner'].includes(key));
       if (validKeys.length === 0) {
         return [];
       }

       return playlists.filter((item) => {
         return validKeys.every((key) => {
           const queryValue = query[key];
           if (key === 'entityId') {
             return item.entityId === queryValue;
           }
           if (key === 'playlistName') {
             return item.playlistName === queryValue;
           }
           if (key === 'owner') {
             return item.owner === queryValue;
           }
           return false;
         });
       });
     }

     private createEntity(entityId: string, playlistName: string, displayName: string, owner: string): AppPlaylistEntity {
       const entity = new AppPlaylistEntity();
       entity.entityId = entityId;
       entity.playlistName = playlistName;
       entity.displayName = displayName;
       entity.owner = owner;
       return entity;
     }
   }
   ```
2. 使用可查询意图实体：添加[@InsightIntentEntry](../harmonyos-references/js-apis-app-ability-insightintentdecorator.md#insightintententry)装饰器的意图使用音乐名称和歌单信息（AppPlaylistEntity意图实体）作为播放音乐的入参。系统入口在调用意图前，会先根据歌单ID、歌单名称或者创建者查询应用内歌单信息。

   ```typescript
   // 使用@InsightIntentEntry装饰器定义意图
   @InsightIntentEntry({
     intentName: 'PlayMusicList',
     domain: 'MusicListDomain',
     intentVersion: '1.0.1',
     displayName: '播放歌单歌曲',
     displayDescription: '播放指定歌单中的歌曲',
     icon: $r('app.media.playMusicList'), // 请将$r('app.media.playMusicList')替换为实际资源文件
     llmDescription: '支持传递歌曲名称和歌单信息，播放歌单中的音乐',
     keywords: ['歌单播放', '播放歌单歌曲', 'PlayMusic'],
     abilityName: 'EntryAbility',
     executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
     parameters: {
       'type': 'object',
       'title': 'Playlist Schema',
       'description': 'A schema for describing song names and playlist information',
       'properties': {
         'songName': {
           'type': 'string',
           'description': 'The name of the song',
           'minLength': 1
         },
         'playlist': {
           'type': 'object',
           'description': 'Information about the playlist',
           'properties': {
             'playlistName': {
               'type': 'string',
               'description': 'The name of the playlist',
               'minLength': 1
             },
             'displayName': {
               'type': 'string',
               'description': 'The displayName of the playlist'
             },
             'owner': {
               'type': 'string',
               'description': 'The owner of the playlist',
             },
             'entityId': {
               'type': 'string',
               'description': 'The unique identifier of the playlist'
             }
           },
           'required': ['playlistName', 'displayName']
         }
       },
       'required': ['songName']
     }
   })
   export default class PlayMusicListImpl extends InsightIntentEntryExecutor<string> {
     public songName: string = '';
     // 使用可查询意图实体
     public playlist?: AppPlaylistEntity;

     onExecute(): Promise<insightIntent.IntentResult<string>> {
       hilog.info(0x0000, LOG_TAG, 'PlayMusicListImpl executeMode %{public}s', JSON.stringify(this.executeMode));
       hilog.info(0x0000, LOG_TAG, 'PlayMusicListImpl playlist %{public}s', JSON.stringify(this.playlist));
       // 定义意图的执行结果
       let result: insightIntent.IntentResult<string> = {
         code: 123,
         result: 'execute success'
       }
       hilog.info(0x0000, LOG_TAG, 'PlayMusicListImpl return %{public}s', JSON.stringify(result));
       return Promise.resolve(result);
     }
   }
   ```
