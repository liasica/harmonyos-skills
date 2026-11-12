---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-page
title: 基于Page的装饰器方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 任务执行类场景方案（装饰器接入方式） > 基于Page的装饰器方案
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1a1651ce1e4186af081630209944bad74e21336d624d98688135ac209767ff2b
---

## 概述

开发者使用@InsightIntentPage装饰器进行基于Page的意图声明，可快速将已有的Navigation页面接入意图框架，实现功能页面的拉起。

## 约束说明

* 仅支持Navigation页面架构跳转。
* 该跳转不能有自定义上下文依赖，比如必须打开前置页面才能跳转，开发者需要进行验证，确认兜底策略。
* 跳转页面时，默认使用Navigation页面栈进行push，如果开发者需要实现其他跳转逻辑，则需要自行适配。

## 开发示例

以购买电影票的意图为例，详细说明如下：

1. 装饰器添加位置：基于Page的装饰器需要添加在Entry页面组件上，建议在目标页面中进行声明。

   ```typescript
   import { InsightIntentPage } from '@kit.AbilityKit';

   class PurchaseMovieTicketsParam {
     public cinema?: string = '';
     public film?: string = '';
     public time?: string = '';
   }

   @Builder
   export function purchaseMovieTicketsIntentPageBuilder(pageName: string, param: object) {
     PurchaseMovieTicketsIntentPage({ param: param });
   }

   @InsightIntentPage({
     intentName: 'PurchaseMovieTickets',
     domain: 'PurchaseTickets',
     intentVersion: '1.0.1',
     displayName: '购买电影票',
     llmDescription: '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。',
     uiAbility: 'EntryAbility',
     pagePath: './ets/pages/MainPage',
     navDestinationName: 'PurchaseMovieTicketsIntentPage',
     parameters: {
       'type': 'object',
       'properties': {
         'cinema': {
           'type': 'string',
           'description': '目标影院名称，仅支持平台合作的影院'
         },
         'film': {
           'type': 'string',
           'description': '目标电影名称，需为当前上映或即将上映且在影院排片列表中的电影'
         },
         'time': {
           'type': 'string',
           'description': '放映时间，必须为未来的场次，且需为影院当天有效排片时间；时间格式应为\'YYYY-MM-DD HH:MM\'（例如\'2025-07-01 19:30\'）'
         }
       },
       'required': ['cinema', 'film', 'time']
     }
   })
   @Entry
   @Component
   struct PurchaseMovieTicketsIntentPage {
     param: PurchaseMovieTicketsParam = new PurchaseMovieTicketsParam();
     cinema: string = '';
     film: string = '';
     time: string = '';
     aboutToAppear(): void {
       this.cinema = this.param?.cinema ?? '';
       this.film = this.param?.film ?? '';
       this.time = this.param?.time ?? '';
     }
     build() {
       NavDestination(){
         Text(`${this.cinema} ${this.film} ${this.time}`)
           .fontSize(30)
           .fontWeight(FontWeight.Bolder)
       }
       .title('IntentPage')
       .width('100%')
     }
   }
   ```
2. 装饰器的字段说明以及示例：@InsightIntentPage字段以及具体说明如下。

   | 字段名称 | 类型 | 必选 | 说明 |
   | --- | --- | --- | --- |
   | intentName | string | 是 | 意图名称，最大长度：64。 |
   | domain | string | 是 | 意图所属的功能垂域。 |
   | intentVersion | string | 是 | 意图的版本号，用于兼容性管理。 |
   | displayName | string | 是 | 意图的展示名称，用于界面显示，最大长度：64。 |
   | llmDescription | string | 否 | 意图的描述，详细描述该意图可实现的能力，便于大模型理解并调用。 |
   | parameters | Record<string, object> | 否 | 意图参数定义，描述参数类型以及含义。 |
   | uiAbility | string | 否 | 页面依赖的UiAbility名，如果不传递默认使用EntryAbility。 |
   | pagePath | string | 是 | Navigation组件所在页面的路径，路径基于Module的根目录的相对路径。 |
   | navDestinationName | string | 否 | Navigation子页面名称，如果不填写，则跳转到pagePath指定的页面。 |

   为便于大模型理解和调用，相关参数定义需要遵照[自定义意图相关信息定义规范](intents-skill-all-rec-specification.md)。
3. 装饰器的添加方式：装饰器可以直接手动添加，同时也支持一键生成装饰器，建议使用后者，此方式需要安装相应插件，详细步骤如下。

   1. 打开CodeGenie插件：在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U，可以进入DevEco CodeGenie。若使用非最新版本的DevEco Studio，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/2a9jMA1dT2SDyIhAFEb0uw/zh-cn_image_0000002815560161.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADB7D49E6C6DA851056F307F0F2EB1C11DF23B89478F9E15770405F9E1217A09)
   2. 框选想要接入意图框架功能的代码。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/jXfSbvuFSvSLx3-jmF0vFw/zh-cn_image_0000002815400245.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D52B17AE2D112A47F4E79A10DB08E6709819E4FE65E896BDFB38013A456DFB86)
   3. 在选中的代码块上右键CodeGenie > Insight Intent，选择适合的装饰器。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Yn6YLxZsQXiw3oVwNxmbYA/zh-cn_image_0000002786520670.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB7B794531C59D4A000B000E5D1B9AF83018CF56CE52F6FEC7E6DABC16EA348E)
   4. 在DevEco CodeGenie对话框中对意图定义，功能，参数等进行描述。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/iQ2UohNaSpyzG_XIooJxOw/zh-cn_image_0000002786360742.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=91C09184A8D51854F8AFF8BAB4E52CBD3B4940A3408C673981213368CBE3FB04)
   5. 回车或者点击发送按钮，即可生成对应的装饰器内容。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/SaCOdG7MQlG9ziDwAz9J9A/zh-cn_image_0000002815560163.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABFADFF063EACA074CCCE20518DC8DDFF15E60BC94D9EB647616CEDE00189EAA)
   6. 将光标放置于要插入装饰器的位置，点击插入图标，即可在对应位置插入装饰器。

      插入前：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/XWS5NiLMRqCW54_866gL7w/zh-cn_image_0000002815400247.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=21B81C1762B79EB02DBCC5B2CBABD0867F45369458B15651EBF2BA59B67FCC46)

      插入后：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/3qM6Kz_uTZSo800tn1aF9A/zh-cn_image_0000002786520672.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B87B7B40A3573B215D597AA817FBE1D4D71D583C1ACCA97CE8D1EA4BB51EF533)
