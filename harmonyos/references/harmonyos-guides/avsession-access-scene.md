---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-access-scene
title: 应用接入AVSession场景介绍
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 应用接入AVSession场景介绍
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:84ecb0085debbb13fcc263a7e13f0e2683e1d65b59f9eed2f9d043207616a096
---

音视频应用在实现音视频功能的同时，需要接入媒体会话即AVSession Kit，本文结合典型案例，介绍接入AVSession的展示与控制场景，为开发者提供适配参考。

对于不同的场景，将会在系统的播控中心呈现不同的UI。同时，在不同的场景下，应用的接入处理也需要遵循不同的规范约束。

## 哪些场景下需要接入AVSession

AVSession会对后台音频播放、VoIP通话进行约束。因此，长音频应用、听书类应用、长视频应用、VoIP类应用等都需要接入AVSession。当应用在没有创建接入AVSession的情况下进行了上述业务，那么系统会在检测到应用后台时，停止对应的音频播放，静音通话声音，以达到约束应用行为的目的。这种约束，应用上架前在本地就可以验证。

对于其他使用到音频播放的应用，比如游戏、直播等场景，接入AVSession是可选项，取决于应用是否有后台播放的使用诉求。若应用需要后台播放，那么接入AVSession仍然是必须的，否则业务的正常功能会受到限制。

当应用需要实现后台播放等功能时，需要使用[BackgroundTasks Kit](background-task-overview.md)（后台任务管理）的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。

## 接入流程

应用接入AVSession流程分为如下几个步骤：

1. 确定应用需要创建的会话类型，[创建对应的会话](avsession-access-scene.md#创建不同类型的会话)，不同类型决定了播控中心展示的控制模板样式。
2. 按需[创建后台任务](avsession-access-scene.md#创建后台任务)。
3. [设置必要的元数据（Metadata）](avsession-access-scene.md#设置元数据信息)，以在播控中心展示相应的信息，包括但不限于：当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。
4. [设置播放相关的状态](avsession-access-scene.md#设置播放状态)，包括但不限于：当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体ID（activeItemId）、自定义媒体数据（extras）等属性。
5. 按需[注册不同的控制命令](avsession-access-scene.md#控制命令的处理)，包括但不限于：播放/暂停、上下一首、快进快退、收藏、循环模式、进度条。
6. 应用退出或者无对应业务时，注销会话。

## 创建不同类型的会话

AVSession在构造方法中支持不同的类型参数，由 [AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10) 定义，不同的类型代表了不同场景的控制能力，对于播控中心来说，会展示不同的控制模板。

* audio类型，播控中心的控制样式为：收藏、上一首、播放/暂停、下一首、循环模式。
* video类型，播控中心的控制样式为：快退、上一首、播放/暂停、下一首、快进。
* voice\_call类型，通话类型。

使用代码示例：

**说明** 

以下示例代码仅展示创建AVSession对象的接口调用，应用在真正使用时，需要确保AVSession对象实例在应用后台播放业务活动期间一直存在，避免被系统回收、释放，导致后台发声时被系统管控。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          // 开始创建并激活媒体会话。
          // 创建session。
          let context = this.getUIContext().getHostContext() as Context;
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
          // 激活接口要在元数据、控制命令注册完成之后再执行。
          await session.activate();
          console.info(`session create done : sessionId : ${session.sessionId}`);
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 创建后台任务

当应用需要实现后台播放等功能时，需要使用[BackgroundTasks Kit](background-task-overview.md)（后台任务管理）的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。

对媒体类播放来说，需要申请[AUDIO\_PLAYBACK BackgroundMode](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)的长时任务。

## 设置元数据信息

应用通过[setAVMetadata](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)将当前媒体会话的元数据信息设置给系统，系统播控中心会根据应用设置的元数据信息进行展示。

### 元数据信息

元数据信息[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)包括：当前媒体的ID（assetId）、上一首媒体的ID（previousAssetId）、下一首媒体的ID（nextAssetId）、标题（title）、专辑作者（author）、艺术家（artist）、专辑名称（album）、词作者（writer）、媒体图片（mediaImage）和媒体时长（duration）等。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          try {
            let context = this.getUIContext().getHostContext() as Context;
            // 假设已经创建了一个session，如何创建session可以参考之前的案例。
            let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');
            // 设置必要的媒体信息。
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
              title: 'TITLE',
              mediaImage: 'IMAGE',
              artist: 'ARTIST',
            };
            session.setAVMetadata(metadata).then(() => {
              console.info(`SetAVMetadata successfully`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
              // ...
            });
          } catch (err) {
            if (err) {
              console.error(`AVSession create Error: Code: ${err.code}, message: ${err.message}`);
              // ...
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

### 设置歌词字段信息

元数据信息[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)中包含歌词字段，应用可以通过设置歌词字段来满足某些场景的歌词内容展示，当前支持设置两种歌词字段：

* lyric字段：播放资源的完整歌词内容，系统播控中心页面会根据该字段信息展示歌词内容。应用需将歌词内容拼接为一个字符串传入。
* singleLyricText字段：单条歌词内容，系统蓝牙模块会根据该字段信息进行某些场景（如蓝牙音箱）的歌词内容展示。

**说明** 

* lyric字段仅支持LRC格式（时间标签+歌词信息，如[00:25.44]歌词信息）的歌词内容，若应用传入其他格式的歌词内容，系统播控中心存在解析失败从而导致歌词显示异常问题。
* lyric字段和singleLyricText字段的大小均不允许超过40960字节，否则会由于系统传输限制导致歌词信息设置失效。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

          // 把歌词信息设置给AVSession。
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
            // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n。
            lyric: 'lrc格式歌词内容',
            // singleLyricText字段存储单条歌词文本，不包含时间戳。
            // 例如："单条歌词内容"。
            singleLyricText: '单条歌词内容',
          };
          session.setAVMetadata(metadata).then(() => {
            console.info(`SetAVMetadata successfully`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
            // ...
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

### 设置进度条信息

元数据信息[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)中包含播放资源时长duration字段（单位为ms），应用如果希望在系统播控中心界面展示播放资源的进度条，需要在duration字段中填写正确的资源播放时长信息。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

          // 设置媒体资源时长。
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            duration: 23000, // 资源的时长，以ms为单位。
          };
          session.setAVMetadata(metadata).then(() => {
            console.info(`SetAVMetadata successfully`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
            // ...
          });

          // 设置状态： 播放状态，进度位置，播放倍速，缓存的时间。
          let playbackState: AVSessionManager.AVPlaybackState = {
            state: AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY, // 播放状态。
            position: {
              elapsedTime: 1000, // 已经播放的位置，以ms为单位。
              updateTime: new Date().getTime(), // 应用更新当前位置时的时间戳，以ms为单位。
            },
            speed: 1.0, // 可选，默认是1.0，播放的倍速，按照应用内支持的speed进行设置，系统不做校验。
            bufferedTime: 14000, // 可选，资源缓存的时间，以ms为单位。
          };
          session.setAVPlaybackState(playbackState, (err) => {
            if (err) {
              console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
              // ...
            } else {
              console.info(`SetAVPlaybackState successfully`);
              // ...
            }
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

系统的播控中心会根据应用设置的信息自动计算播放进度，而不需要应用实时更新播放进度；但是当应用的state、position、speed信息发生变化的时候，必须同步更新AVPlaybackState信息，否则系统播控中心展示的应用状态信息、进度条信息等会出现异常。

应用在真实播放开始时，再上报进度起始position；若播放存在缓冲状态，可以先上报播放状态为AVSessionManager.PlaybackState.PLAYBACK\_STATE\_BUFFERING，来通知系统不刷新进度。

关于进度条有一些特殊情况需要处理：

1. 歌曲支持试听

   （1）应用不需要设置完整的歌曲时长，只需要设置歌曲的试听时长。当应用仅设置歌曲的试听时长而不是完整时长，用户在播控中心触发进度控制时，应用收到的时长也是VIP试听时长内的相对时间戳位置，而不是完整歌曲的绝对时间戳位置，应用需要重新计算歌曲从零开始的绝对时间戳进行实际响应处理。

   （2）如果应用设置完整歌曲时长，但需要系统支持试听片段，也可以在播放时上报起始进度position，当收到的seek指令超过试听片段时，上报试听截止position，系统播控的进度会跟随回弹。
2. 歌曲不支持试听

   如果歌曲不支持试听，那么理论上应用内也不支持播放，这时可以把 duration 设置为 -1，以通知系统不显示实际的时长。
3. 广告等内容的时长设置

   对于有前贴片广告、后贴片广告的资源来说，建议按以下方式处理：

   * 播放广告时，单独设置广告的时长 duration。
   * 当进入到正片播放的时候，则重新设置一次新的时长，以与广告进行区分。

### 历史歌单

针对音乐/听书类应用，播控中心提供一系列快捷播放能力，包括一键启动冷启动续播、以及历史歌单功能，其中歌单功能中支持显示的音频媒体内容有：音乐歌单、有声书专辑、播客专辑等。视频媒体内容、直播类媒体内容暂不支持歌单。应用在端侧注册并适配后台启动模式的[播放意图](intents-habit-rec-access-programme.md)，即可实现接入上述功能。接入后的体验自检，可以参考[快捷播放](quick-playback.md)。

开发者可参考下述示例，完成注册播放意图、设置歌单信息、实现意图启动播放。

**注册播放意图**

应用按照播放业务，选择PlayMusicList意图（音乐类应用）或者PlayAudio意图（听书类应用）其一注册。编辑对应的意图配置PROJECT\_HOME/entry/src/main/resources/base/profile/insight\_intent.json文件，实现播放意图注册。

注册示例如下：

```typescript
{
    // 应用支持的意图列表。
    "insightIntents": [
        {
            // 意图名称。
            // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义。
            // 应用内意图名称唯一，不允许出现相同的名称定义。
            "intentName": "PlayMusicList", // 音乐类PlayMusicList，听书或有声书类PlayAudio。
            // 意图所属的垂域。
            "domain": "MusicDomain", // 音乐类MusicDomain，听书或有声书类AudioDomain。
            // 意图版本号。
            // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用。
            "intentVersion": "1.0.1",
            // 意图调用代码逻辑入口。
            "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
            "uiAbility": {
                // 意图所在module、ability，以及代码相对路径入口。
                "ability": "EntryAbility",
                // UIAbility支持前后台两种执行模式。
                "executeMode": [
                    "background", // 播控一键冷启动、历史歌单功能需要应用支持意图后台启动。
                    "foreground"
                ]
            }
        }
    ]
}
```

**设置歌单信息**

通过[setAVMetadata](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)接口设置当前播放的歌单（专辑）信息，歌单（专辑）信息由下面几个字段组成：

* avQueueName: 歌单的名称，接入歌单必选
* avQueueId: 歌单的唯一标识id，接入歌单必选
* avQueueImage: 歌单的图片资源，接入歌单必选

系统媒体信息根据应用上报实时刷新，若应用接入歌单功能，则确保在[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)中一直携带歌单数据。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...
async function setListener(context: Context) {
  // 假设已经创建了一个session，如何创建session可以参考之前的案例。
  let type: AVSessionManager.AVSessionType = 'audio';
  let session: AVSessionManager.AVSession;
  try {
    session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to create AVSession. Code: ${error.code}, message: ${error.message}`);
    return;
  }
  // 将歌单信息设置给AVSession。
  let metadata: AVSessionManager.AVMetadata = {
    // 下面内容均由应用设置。
    assetId: 'musicid123',
    avQueueName: 'myQueue',
    avQueueId: 'myQueue123',
    avQueueImage: 'PIXELMAP_OBJECT',
  };
  session.setAVMetadata(metadata).then(() => {
    console.info(`SetAVMetadata successfully`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
  // ...
}
// ...
```

**实现意图启动播放**

当应用接入歌单功能后，用户在系统播控中心界面可以播放应用的歌单，也可以在应用进程释放后，通过系统播控中心再次冷启动应用后台播放。

* 用户触发歌单播放时，系统会将歌单的唯一标识id传回应用，应用可以在意图调用接口中，通过解析意图参数(intentParam)中的entityId，获取到歌单的id，实现对应歌单的播放。
* 用户触发播控冷启动播放时，系统会在意图参数(intentParam)的包含空歌单id，即解析出得的entityId为空字符串，**由应用来决定播放内容**，可以实现为续播上一次的播放内容。
* **系统会在后台冷启动应用的播放，需要在播放前先设置[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)，注册[播控控制回调](avsession-access-scene.md#控制命令的处理)，并申请播音长时任务。**

  ```typescript
  import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  /**
   * 意图调用样例。
   */
  export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
    /**
     * override 执行后台启动UIAbility意图。
     *
     * @param intentName 意图名称。
     * @param intentParam 意图参数。
     * @returns 意图调用结果。
     */
    async onExecuteInUIAbilityBackgroundMode(intentName: string, intentParam: Record<string, Object>):
      Promise<insightIntent.ExecuteResult> {
      // 根据意图名称分发处理逻辑。
      switch (intentName) {
        case 'PlayMusicList':
          // PlayMusicList参照如下解析方式。
          const entityId: string = (typeof intentParam.entityId === 'string') ? intentParam.entityId : '';
          return this.playFunc(entityId);
        case 'PlayAudio':
          // PlayAudio参照如下解析方式。
          let data = intentParam as Record<string, string>;
          return this.playFunc(data.entityId);
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
     * 实现调用播放功能。
     *
     * @param entityId 播放内容id。
     */
    private playFunc(entityId: string): Promise<insightIntent.ExecuteResult> {
      // entityId 不为空，表示用户指定内容（歌单/专辑）播放。
      // entityId 为空（entityId.length == 0），由应用自行决定播放内容，续播历史内容或者是推荐内容。
      // 此时是后台拉起应用播放，除了初始化播放资源，还需要设置AVMetadata，注册播控控制回调，并申请播音长时任务。
      // TODO 实现具体的播放业务。
      return Promise.resolve({
        code: 0,
        result: {
          message: 'Intent execute succeed'
        }
      } as insightIntent.ExecuteResult)
    }
  }
  ```

### 媒体资源金标

元数据信息[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)中提供了displayTags字段用于展示媒体资源金标（应用音频音源的标识）。应用设置displayTags字段信息后，系统的播控中心界面会同步展示，当前系统只支持展示Audio Vivid标识。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

          // 把媒体音源信息设置给AVSession。
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            // 标识该媒体音源是Audio Vivid。
            displayTags: AVSessionManager.DisplayTag.TAG_AUDIO_VIVID,
          };
          session.setAVMetadata(metadata).then(() => {
            console.info(`SetAVMetadata successfully`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
            // ...
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 设置播放状态

应用通过[setAVPlaybackState](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)将当前的播放状态信息设置给系统，系统播控中心界面会严格根据应用传递的播放状态信息进行同步显示。

### 播放状态信息

播放状态信息[AVPlaybackState](../harmonyos-references/arkts-apis-avsession-i.md#avplaybackstate10)包括：当前媒体的播放状态（state）、播放位置（position，包含elapsedTime已播放时长和updateTime更新时间戳）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体ID（activeItemId）、自定义媒体数据（extras）等。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');

          // 播放器逻辑··· 引发媒体信息与播放状态的变更。
          // 简单设置一个播放状态 - 暂停 未收藏。
          let playbackState: AVSessionManager.AVPlaybackState = {
            state: AVSessionManager.PlaybackState.PLAYBACK_STATE_PAUSE,
            isFavorite: false
          };
          session.setAVPlaybackState(playbackState, (err: BusinessError) => {
            if (err) {
              console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
              // ...
            } else {
              console.info(`SetAVPlaybackState successfully`);
              // ...
            }
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 控制命令的处理

### 支持的控制命令

应用接入AVSession，通过on接口可以注册控制命令，实现播控中心界面上对应的控制按钮操作。

**说明** 

创建AVSession后，请先注册应用支持的控制命令，再激活Session。

音视频类应用支持的控制命令列表：

| 控制命令 | 功能说明 |
| --- | --- |
| [play](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10) | 播放命令。 |
| [pause](../harmonyos-references/arkts-apis-avsession-avsession.md#onpause10) | 暂停命令。 |
| [stop](../harmonyos-references/arkts-apis-avsession-avsession.md#onstop10) | 停止命令。 |
| [playNext](../harmonyos-references/arkts-apis-avsession-avsession.md#onplaynext10) | 播放下一首命令。 |
| [playPrevious](../harmonyos-references/arkts-apis-avsession-avsession.md#onplayprevious10) | 播放上一首命令。 |
| [fastForward](../harmonyos-references/arkts-apis-avsession-avsession.md#onfastforward10) | 快进命令。 |
| [rewind](../harmonyos-references/arkts-apis-avsession-avsession.md#onrewind10) | 快退命令。 |
| [playWithAssetId](../harmonyos-references/arkts-apis-avsession-avsession.md#onplaywithassetid20) | 根据某个资源id进行播放命令。 |
| [seek](../harmonyos-references/arkts-apis-avsession-avsession.md#onseek10) | 跳转命令。 |
| [setSpeed](../harmonyos-references/arkts-apis-avsession-avsession.md#onsetspeed10) | 设置播放速率命令。 |
| [setLoopMode](../harmonyos-references/arkts-apis-avsession-avsession.md#onsetloopmode10) | 设置循环模式命令。 |
| [toggleFavorite](../harmonyos-references/arkts-apis-avsession-avsession.md#ontogglefavorite10) | 设置是否收藏命令。 |
| [skipToQueueItem](../harmonyos-references/arkts-apis-avsession-avsession.md#onskiptoqueueitem10) | 设置播放列表其中某项被选中播放的命令。 |
| [handleKeyEvent](../harmonyos-references/arkts-apis-avsession-avsession.md#onhandlekeyevent10) | 设置按键事件的命令。 |
| [commonCommand](../harmonyos-references/arkts-apis-avsession-avsession.md#oncommoncommand10) | 设置自定义控制命令。 |

通话类应用支持的控制：

| 控制命令 | 功能说明 |
| --- | --- |
| [answer](../harmonyos-references/arkts-apis-avsession-avsession.md#onanswer11) | 接听电话的命令。 |
| [hangUp](../harmonyos-references/arkts-apis-avsession-avsession.md#onhangup11) | 通话挂断的命令。 |
| [toggleCallMute](../harmonyos-references/arkts-apis-avsession-avsession.md#ontogglecallmute11) | 通话静音或解除静音的命令。 |

### 处理不支持的控制命令

应用若不支持某些控制命令操作（如应用不支持“上一首”命令的控制处理），可以通过off接口注销对应的控制命令，系统播控中心界面会置灰显示或者不显示对应的控制按钮，以明确提示用户应用不支持该控制操作。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

          // 取消指定session下的相关监听。
          session.off('play');
          session.off('pause');
          session.off('stop');
          session.off('playNext');
          session.off('playPrevious');
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

### 快进快退

系统支持三种快进/快退的时长，应用可以通过接口进行设置；同时注册快进/快退的回调命令，以响应控制。

**说明** 

应用注册快进/快退及上/下一首资源切换的命令时，在播控中心的显示存在实际差异。

* **当AVSessionType是audio时：**

  | 应用注册的事件组合 | 播放中心显示按钮 | 按钮是否可用 |
  | --- | --- | --- |
  | 未注册任何事件 | “上一首”、“下一首” | 所有按钮置灰，无法点击。 |
  | 注册上一首/下一首事件 | “上一首”、“下一首” | 注册上一首事件 →“上一首”按钮可用。  注册下一首事件 →“下一首”按钮可用。  未注册对应事件的按钮不可用。 |
  | 注册快进/快退事件 | “上一首”、“下一首” | 所有按钮置灰，无法点击。 |
  | 注册上一首/下一首及快进/快退事件 | “上一首”、“下一首” | 注册上一首事件 →“上一首”按钮可用。  注册下一首事件 →“下一首”按钮可用。  未注册对应事件的按钮不可用。 |
* **当AVSessionType是video时：**

  | 应用注册的事件组合 | 播放中心显示按钮 | 按钮是否可用 |
  | --- | --- | --- |
  | 未注册任何事件 | “快进”、“快退” | 所有按钮置灰，无法点击。 |
  | 注册上一首/下一首事件 | “上一首”、“下一首” | 注册上一首事件 →“上一首”按钮可用。  注册下一首事件 →“下一首”按钮可用。  未注册对应事件的按钮不可用。 |
  | 注册快进/快退事件 | “快进”、“快退” | 注册快进事件 →“快进”按钮可用。  注册快退事件 →“快退”按钮可用。  未注册对应事件的按钮不可用。 |
  | 注册上一首/下一首及快进/快退事件 | “快进”、“快退” | 注册快进事件 →“快进”按钮可用。  注册快退事件 →“快退”按钮可用。  未注册对应事件的按钮不可用。 |

  ```typescript
  import { avSession as AVSessionManager } from '@kit.AVSessionKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  // ...

  @Entry
  @Component
  struct Index {
    @State message: string = 'hello world';
    // ...

    build() {
      Column() {
        // ...
        Text(this.message)
          .onClick(async () => {
            let context = this.getUIContext().getHostContext() as Context;
            // 假设已经创建了一个session，如何创建session可以参考之前的案例。
            let type: AVSessionManager.AVSessionType = 'audio';
            let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
            // ...

            // 设置支持的快进快退的时长设置给AVSession。
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
              title: 'TITLE',
              mediaImage: 'IMAGE',
              skipIntervals: AVSessionManager.SkipIntervals.SECONDS_10,
            };
            session.setAVMetadata(metadata).then(() => {
              console.info(`SetAVMetadata successfully`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
              // ...
            });

            session.on('fastForward', (time?: number) => {
              console.info(`on fastForward , do fastForward task`);
              // ...
              // do some tasks ···
            });
            session.on('rewind', (time?: number) => {
              console.info(`on rewind , do rewind task`);
              // ...
              // do some tasks ···
            });
            // ...
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

### 实现收藏功能

音乐类应用可以通过注册收藏的控制命令[on('toggleFavorite')](../harmonyos-references/arkts-apis-avsession-avsession.md#ontogglefavorite10)实现收藏功能。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
          // ...
          session.on('toggleFavorite', (assetId) => {
            console.info(`on toggleFavorite `);
            // ...
            // 应用收到收藏命令，进行收藏处理。

            // 应用内完成或者取消收藏，把新的收藏状态设置给AVSession。
            let playbackState: AVSessionManager.AVPlaybackState = {
              isFavorite: true,
            };
            session.setAVPlaybackState(playbackState).then(() => {
              console.info(`SetAVPlaybackState successfully`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
              // ...
            });
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

### 实现循环模式功能

针对音乐类应用，系统的播控中心界面会默认展示循环模式的控制操作，目前系统支持四种固定的循环模式控制，参考: [LoopMode](../harmonyos-references/arkts-apis-avsession-e.md#loopmode10)。

播控中心支持固定的四种循环模式的切换，即： 随机播放、顺序播放、单曲循环、列表循环。应用收到循环模式切换的指令并切换后，需要向系统上报切换后的LoopMode。

若应用内支持的LoopMode不在系统固定的四个循环模式内，需要选择四个固定循环模式其一向系统上报，由应用自定。

实现参考：

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
          // ...

          // 应用启动时/内部切换循环模式，需要把应用内的当前的循环模式设置给AVSession。
          let playBackState: AVSessionManager.AVPlaybackState = {
            loopMode: AVSessionManager.LoopMode.LOOP_MODE_SINGLE,
          };
          session.setAVPlaybackState(playBackState).then(() => {
            console.info(`set AVPlaybackState successfully`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
            // ...
          });

          // 应用注册循环模式的控制监听。
          session.on('setLoopMode', (mode) => {
            console.info(`on setLoopMode ${mode}`);
            // ...
            // 应用收到设置循环模式的指令后，应用自定下一个模式，切换完毕后通过AVPlaybackState上报切换后的LoopMode。
            let playBackState: AVSessionManager.AVPlaybackState = {
              loopMode: AVSessionManager.LoopMode.LOOP_MODE_SINGLE,
            };
            session.setAVPlaybackState(playBackState).then(() => {
              console.info(`set AVPlaybackState successfully`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
              // ...
            });
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

### 实现进度条控制功能

应用如果支持[进度条显示](avsession-access-scene.md#设置进度条信息)，则需要同步支持进度条控制功能，即注册seek控制指令。当用户在播控中心界面拖动进度条时，应用会收到对应的回调，应用需要正确响应，参考实现：

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // 假设已经创建了一个session，如何创建session可以参考之前的案例。
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
          // ...

          session.on('seek', (time: number) => {
            console.info(`on seek , the time is ${time}`);
            // ...

            // 由于应用内seek可能会触发较长的缓冲等待，可以先把状态设置为 Buffering。
            let playbackState: AVSessionManager.AVPlaybackState = {
              state: AVSessionManager.PlaybackState.PLAYBACK_STATE_BUFFERING, // Buffering state.
            };
            session.setAVPlaybackState(playbackState, (err) => {
              if (err) {
                console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
                // ...
              } else {
                console.info(`SetAVPlaybackState successfully`);
                // ...
              }
            });

            // 应用响应seek命令，使用应用内播放器完成seek实现。

            // 应用内更新新的位置后，也需要同步更新状态给系统。
            playbackState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY; // 播放状态。
            playbackState.position = {
              elapsedTime: time, // 已经播放的位置，以ms为单位。
              updateTime: new Date().getTime(), // 应用更新当前位置的时间戳，以ms为单位。
            }
            session.setAVPlaybackState(playbackState, (err) => {
              if (err) {
                console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
                // ...
              } else {
                console.info(`SetAVPlaybackState successfully`);
                // ...
              }
            });
          });

          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 适配媒体通知

当应用按照上述流程正确接入AVSession，设置元数据信息、正确的播放状态信息并注册了控制指令，应用进入播放状态时，系统通知和锁屏界面会展示播放的应用信息。

## 适配蓝牙按键与有线按键事件

应用正确接入AVSession后，可以通过注册控制指令的方式来实现监听蓝牙、有线耳机的按键事件，AVSession提供了如下两种实现方式：

* 方式一（推荐使用）：

  应用可以根据[控制命令的处理](avsession-access-scene.md#控制命令的处理)按需注册需要的控制命令，目前支持转换的AVSession控制命令如下：

  | 控制命令 | 功能说明 |
  | --- | --- |
  | play | 播放命令。 |
  | pause | 暂停命令。 |
  | stop | 停止命令。 |
  | playNext | 播放下一首命令。 |
  | playPrevious | 播放上一首命令。 |
  | fastForward | 快进命令。 |
  | rewind | 快退命令。 |

  ```typescript
  import { avSession as AVSessionManager } from '@kit.AVSessionKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  // ...

  @Entry
  @Component
  struct Index {
    @State message: string = 'hello world';
    // ...

    build() {
      Column() {
        // ...
        Text(this.message)
          .onClick(async () => {
            try {
              let context = this.getUIContext().getHostContext() as Context;
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
              // ...
              // 设置必要的媒体信息，务必设置，否则接收不到控制事件。
              let metadata: AVSessionManager.AVMetadata = {
                assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
                title: 'TITLE',
                mediaImage: 'IMAGE',
                artist: 'ARTIST'
              };
              session.setAVMetadata(metadata).then(() => {
                console.info(`SetAVMetadata successfully`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
                // ...
              });
              // 一般在监听器中会对播放器做相应逻辑处理。
              // 处理完后需要通过set接口同步播放相关信息，参考上面的用例。
              session.on('play', () => {
                console.info(`on play , do play task`);
                // ...
                // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('play')取消监听。
                // 处理完毕后，请使用setAVPlayState上报播放状态。
              });
              session.on('pause', () => {
                console.info(`on pause , do pause task`);
                // ...
                // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('pause')取消监听。
                // 处理完毕后，请使用setAVPlayState上报播放状态。
              });
              // ...
            } catch (err) {
              if (err) {
                console.error(`AVSession create Error: Code: ${err.code}, message: ${err.message}`);
                // ...
              }
            }
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* 方式二：

  通过AVSession注册[on('handleKeyEvent')](../harmonyos-references/arkts-apis-avsession-avsession.md#onhandlekeyevent10)命令。该回调接口会直接转发媒体按键事件[KeyEvent](../harmonyos-references/js-apis-keyevent.md)。应用需要自行识别按键事件的类型，并响应事件实现对应的功能。目前支持转发的按键事件类型如下：

  | 按键类型([KeyCode](../harmonyos-references/js-apis-keycode.md#keycode)) | 功能说明 |
  | --- | --- |
  | KEYCODE\_MEDIA\_PLAY\_PAUSE | 多媒体键：播放/暂停 |
  | KEYCODE\_MEDIA\_STOP | 多媒体键：停止 |
  | KEYCODE\_MEDIA\_NEXT | 多媒体键：下一首 |
  | KEYCODE\_MEDIA\_PREVIOUS | 多媒体键：上一首 |
  | KEYCODE\_MEDIA\_REWIND | 多媒体键：快退 |
  | KEYCODE\_MEDIA\_FAST\_FORWARD | 多媒体键：快进 |
  | KEYCODE\_MEDIA\_PLAY | 多媒体键：播放 |
  | KEYCODE\_MEDIA\_PAUSE | 多媒体键：暂停 |

  ```typescript
  import { avSession as AVSessionManager } from '@kit.AVSessionKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  // ...

  @Entry
  @Component
  struct Index {
    @State message: string = 'hello world';
    // ...

    build() {
      Column() {
        // ...
        Text(this.message)
          .onClick(async () => {
            let context = this.getUIContext().getHostContext() as Context;
            let type: AVSessionManager.AVSessionType = 'audio';
            let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
            // ...
            // 设置必要的媒体信息，务必设置，否则接收不到按键事件。
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
              title: 'TITLE',
              mediaImage: 'IMAGE',
              artist: 'ARTIST'
            };
            session.setAVMetadata(metadata).then(() => {
              console.info(`SetAVMetadata successfully`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
              // ...
            });
            session.on('handleKeyEvent', (event) => {
              // 解析keycode，应用需要根据keycode对播放器做相应逻辑处理。
              console.info(`on handleKeyEvent, keyCode=${event.key.code}`);
              // ...
            });
            // ...
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

**说明** 

1. 方式一与方式二均需要应用正确设置元数据信息（AVMetadata），并注册相应的控制命令接口，否则会无法接收到控制指令与按键事件。
2. 方式一与方式二，选择其一接入即可，无需同时接入，系统推荐按照方式一接入。

## 示例代码

* [媒体会话-提供方](https://gitcode.com/HarmonyOS_Samples/media-provider)
