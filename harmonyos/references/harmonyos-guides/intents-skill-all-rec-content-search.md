---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-content-search
title: 内容搜索方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 本地搜索方案 > 接入方案 > 内容搜索方案
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c3431592bac77aab7f7d8ae12d9df5670ec17ec11745f0fb6dcdaf4a0655fca3
---

## 方案概述

当用户使用应用/元服务时，开发者可以按照标准意图Schema（具体意图详见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)）向系统共享数据（数据包含用户行为和内容实体），并实现意图调用（空调用与传参调用）。已实现用户点击卡片后，可后台执行功能（例如播放指定歌曲）或跳转至指定内容页面（例如指定的歌曲播放页面）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/CRnkuVnuRJmnPM9dDxM8bQ/zh-cn_image_0000002736434557.png)

## 意图声明

以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```json5
{
  // 应用支持的意图列表
  // 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
  "insightIntents": [
    {
      // 意图名称
      // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
      // 应用内意图名称唯一，不允许出现相同的名称定义
      "intentName": "PlayMusic",
      // 意图所属的垂域
      "domain": "MusicDomain",
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

## 意图共享

构建意图对象，并且调用[insightIntent.shareIntent](../harmonyos-references/intents-arkts-api-insightintent.md#shareintent-1)，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。

以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图，并进行了shareIntent调用。

```typescript
import { insightIntent } from '@kit.IntentsKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('shareIntent')
          .onClick(() => {
            let playMusicIntent: insightIntent.InsightIntent = {
              intentName: 'PlayMusic',
              intentVersion: '1.0.1',
              identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
              intentActionInfo: {
                actionMode: 'EXECUTED',
                executedTimeSlots: {
                  executedStartTime: 1637393112000,
                  executedEndTime: 1637393212000
                },
                currentPercentage: 50
              },
              intentEntityInfo: {
                entityName: 'Music',
                entityId: 'C10194368',
                entityGroupId: 'C10194321312',
                displayName: '测试歌曲1',
                description: 'NA',
                logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png',
                keywords: ['华为音乐', '化妆'],
                rankingHint: 99,
                expirationTime: 1637393212000,
                metadataModificationTime: 1637393212000,
                activityType: ['1', '2', '3'],
                artist: ['测试歌手1', '测试歌手2'],
                lyricist: ['测试词作者1', '测试词作者2'],
                composer: ['测试曲作者1', '测试曲作者2'],
                albumName: '测试专辑',
                duration: 244000,
                playCount: 100000,
                musicalGenre: ['流行', '华语', '金曲', '00后'],
                isPublicData: false
              }
            };
            // 共享数据接口  意图数组可以是更多的实体
            // 根据实际代码上下文自行传入合适的context
            insightIntent.shareIntent(this.getUIContext().getHostContext(), [playMusicIntent]).then(() => {
              console.info('shareIntent succeed');
            }).catch((err: BusinessError) => {
              console.error(`shareIntent failed, Code: ${err?.code}, message: ${err?.message}`);
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 端侧意图调用

开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）或后台执行的能力，PlayMusic的意图调用字段定义见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别播放歌曲意图（PlayMusic），在对应的方法中传递意图参数（param），并拉起对应落地页（如播放歌曲落地页）或后台执行（播放歌曲）。

```typescript
import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 意图调用样例
 */
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
  private static readonly PLAY_MUSIC = 'PlayMusic';

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
    // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
    switch (name) {
      case InsightIntentExecutorImpl.PLAY_MUSIC:
        return this.playMusic(param, pageLoader);
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
   * 实现调用播放歌曲功能
   *
   * @param param 意图参数
   * @param pageLoader 窗口
   */
  private playMusic(param: Record<string, Object>,
    pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    return new Promise((resolve, reject) => {
      pageLoader.loadContent('pages/SongPage')
        .then(() => {
          const items: Array<PlayMusicEntity> = (param.items instanceof Array) ? param.items : [];
          const entityId: string = items[0]?.entityId;
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
    });
  }
}

interface PlayMusicEntity {
  entityId: string;
}
```
