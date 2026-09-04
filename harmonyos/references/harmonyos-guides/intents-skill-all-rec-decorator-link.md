---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-link
title: 基于Link的装饰器方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 任务执行类场景方案（装饰器接入方式） > 基于Link的装饰器方案
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:43+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:deee00325c29f80b8988ae8b3c6c2cf93e5275e3296c8e8dcc475272b0919e1c
---

## 概述

开发者使用@InsightIntentLink装饰器进行基于Link的意图声明，可快速将已实现的Link跳转功能接入意图框架，实现功能页面的拉起。

## 约束说明

* @InsightIntentLink装饰器包含通过Link接入意图的所有配置，因此对装饰器所在Class、变量、成员没有要求，但是必须要在被依赖的ets文件中添加装饰器才可以被编译。
* 支持开发者设置wantParameter，执行Link时，会将该参数附带到want的parameter中。
* 装饰器方式仅支持参数名映射，不做参数加工，包括取值转换、合并等情况。

## 开发示例

以购买电影票意图为例，详细说明如下：

1. 装饰器的添加位置：装饰器建议添加到处理该Link的Class上，如下所示。

   ```typescript
   import { InsightIntentLink, LinkParamCategory } from '@kit.AbilityKit';
   import { url } from '@kit.ArkTS';

   @InsightIntentLink({
     intentName: 'PurchaseMovieTickets',
     domain: 'PurchaseTickets',
     intentVersion: '1.0.1',
     displayName: '购买电影票',
     llmDescription: '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。',
     uri: 'decorator://ability.entry/main',
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
     },
     paramMappings:[
       {
         paramName: 'cinema',
         paramMappingName: 'location',
         paramCategory: LinkParamCategory.LINK
       },
       {
         paramName: 'film',
         paramMappingName: 'title',
         paramCategory: LinkParamCategory.LINK
       },
       {
         paramName: 'time',
         paramMappingName: 'time',
         paramCategory: LinkParamCategory.LINK
       }
     ]
   })
   export class PurchaseMovieTicketsLinkIntent {
      private purchaseMovieTickets(uri: string): void {
        // 从want中获取传入的链接信息。
        // 如传入的url为：decorator://ability.entry/main?location=XXX影城&title=XXX&time=2025.06.01
        try {
          let urlObject = url.URL.parseURL(uri);
          let location = urlObject.params.get('location');
          if (location === 'XXX影城') {
            // ...
          }
        } catch (error) {
          console.error('Failed to parse URL:', error);
        }
      }
    }
   ```
2. 装饰器的字段说明以及示例：@InsightIntentLink字段以及具体说明如下。

   | **字段名称** | **类型** | **必选** | **说明** |
   | --- | --- | --- | --- |
   | intentName | string | 是 | 意图名称，最大长度：64。 |
   | domain | string | 是 | 意图所属的功能垂域。 |
   | intentVersion | string | 是 | 意图的版本号，用于兼容性管理。 |
   | displayName | string | 是 | 意图的展示名称，用于界面显示，最大长度：64。 |
   | llmDescription | string | 否 | 意图的描述，详细描述该意图可实现的能力，便于大模型理解并调用，接入自定义意图时，该字段必选。 |
   | uri | string | 是 | Link跳转uri。 |
   | parameters | Record<string, object > | 否 | 意图参数定义，描述参数类型以及含义。 |
   | paramMappings | LinkIntentParamMapping[] | 否 | Link的参数映射，定义了意图入参与uri拼接参数的映射关系，如果需要参数映射或者需要添加wantParams，需要使用该字段。 |
   | result | Record<string, object > | 否 | 意图执行返回结果定义。 |

   LinkIntentParamMapping结构如下表：

   | **字段名称** | **类型** | **必选** | **说明** |
   | --- | --- | --- | --- |
   | paramName | string | 是 | 映射后的意图参数名称。 |
   | paramMappingName | string | 否 | 映射前的Link参数名称，意图调用时可将意图参数映射为Link参数，用于适配已有的Link调用。 |
   | paramCategory | LinkParamCategory | 否 | Link参数类型枚举，默认作为域名参数，设置为“link”类型；如需要wantParams，则需要设置为“want”类型。 |

   为便于大模型理解和调用，相关参数定义需要遵照[自定义意图相关信息定义规范](intents-skill-all-rec-specification.md)。
3. 添加装饰器的方式：装饰器可以直接手动添加，同时也支持一键生成装饰器，建议使用后者，此方式需要安装相应插件，详细步骤如下：

   1. 打开CodeGenie插件：在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U，可以进入DevEco CodeGenie。若使用非最新版本的DevEco Studio，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

      ![](https://media:401788444089970761)
   2. 框选想要接入意图框架功能的代码。

      ![](https://media:401788444090118762)
   3. 在选中的代码块上右键CodeGenie > Insight Intent，选择适合的装饰器。

      ![](https://media:401788444090357763)
   4. 在DevEco CodeGenie对话框中对意图定义、功能和参数等进行描述。

      ![](https://media:401788444090463764)
   5. 回车或者点击发送按钮，即可生成对应的装饰器内容。

      ![](https://media:401788444090555765)
   6. 将光标放置于要插入装饰器的位置，点击插入图标，即可在对应位置插入装饰器。

   插入前：

   ![](https://media:401788444090649766)

   插入后：

   ![](https://media:401788444090735767)
