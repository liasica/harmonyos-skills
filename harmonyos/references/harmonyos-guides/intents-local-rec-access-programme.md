---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-local-rec-access-programme
title: 接入方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 位置推荐方案 > 接入方案
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:081a52c352b02d2e4125d9ba8a21a57ae1cc0edd54d0d156a9da235fa488aa38
---

## 方案概述

位置感知推荐能力支持开发者云侧共享位置信息与关联推荐的内容，结合实时位置、设备状态与习惯标签完成系统智慧决策，在小艺建议智慧推荐更符合用户诉求的内容信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/NBWN2_DhQU2N58Rt5J0Q9Q/zh-cn_image_0000002736434535.png)

## 开通近场服务权限

近场服务是华为软硬协同解决方案中的关键能力环节，旨在帮助商家触达更多HarmonyOS用户，并为这些用户提供更精准、更优质的服务。开通近场服务的步骤详情参考：[近场服务-申请开通权限](../app/agc-help-xiaoyi-create-formalstate-service-0000002349016144.md)。

## 意图声明

以“搜索旅游攻略”特性为例，开发者首先要注册“查看旅游攻略”（ViewTravelGuides），其他意图见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图声明。insight\_intent.json文件需要放置在任意一个module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```json5
{
  // 应用支持的意图列表
  // 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
  "insightIntents": [
    {
      // 意图名称
      // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
      // 应用内意图名称唯一，不允许出现相同的名称定义
      "intentName": "ViewTravelGuides",
      // 意图所属的垂域
      "domain": "TravelDomain",
      // 意图版本号
      // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
      "intentVersion": "1.0.1",
      // 意图调用逻辑入口
      "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
      "uiAbility": {
        // 意图所在ability
        "ability": "EntryAbility",
        // UIAbility支持前后台两种执行模式
        "executeMode": [
          "background",
          "foreground"
        ]
      }
    }
  ]
}
```

## 端侧前台意图调用

开发者需自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面，如旅游攻略落地页）的能力，ViewTravelGuides的意图调用字段定义见查看旅游攻略（ViewTravelGuides）。

步骤如下：

1. 继承InsightIntentExecutor；
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法；
3. 通过意图名称，识别查看旅游攻略意图(ViewTravelGuides)，在对应的方法中传递意图参数（param），并拉起对应落地页（点击推荐卡片跳转的界面，如旅游攻略落地页）。

```typescript
import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 意图调用样例
 */
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
  private static readonly VIEW_TRAVEL_GUIDES = 'ViewTravelGuides';
  /**
   * override 执行前台UIAbility意图
   *
   * @param name 意图名称
   * @param param 意图参数
   * @param pageLoader 窗口
   * @returns 意图调用结果
   */
  onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
    Promise<insightIntent.ExecuteResult> {
    // 根据意图名称分发处理逻辑，接入方可根据实际业务实现页面跳转
    switch (name) {
      case InsightIntentExecutorImpl.VIEW_TRAVEL_GUIDES:
        return this.viewTravelGuides(param, pageLoader);
      default:
        break;
    }
    const data: insightIntent.ExecuteResult = {
      code: -1,
      result: {
        message: 'unknown intent'
      }
    };
    return Promise.resolve(data);
  }

  /**
   * 实现调用查看旅游攻略功能
   *
   * @param param 意图参数
   * @param pageLoader 窗口
   */
  private viewTravelGuides(param: Record<string, Object>,
    pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    return new Promise((resolve, reject) => {
      pageLoader.loadContent('pages/TravelGuidePage')
        .then(() => {
          const entityId: string = (typeof param.entityId === 'string') ? param.entityId : '';
          console.info(`Intent param, entityId: ${entityId}`);
          const data: insightIntent.ExecuteResult = {
            code: 0,
            result: {
              message: 'Intent execute succeed'
            }
          };
          resolve(data);
        })
        .catch((err: BusinessError) => {
          console.error(`Intent execute failed, Code: ${err?.code}, message: ${err?.message}`);
          const data: insightIntent.ExecuteResult = {
            code: -1,
            result: {
              message: 'Intent execute failed'
            }
          };
          reject(data);
        });
    })
  }
}
```
