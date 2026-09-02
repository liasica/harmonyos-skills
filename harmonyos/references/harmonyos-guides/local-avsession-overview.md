---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/local-avsession-overview
title: 本地媒体会话概述
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 本地媒体会话概述
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c7c150d379f1f00ed2655d98aca0c580746a6c19d2e563fc91961e6a88b04240
---

## 交互过程

本地媒体会话的数据源均在设备本地，交互过程如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ULufIx2ZTWK6T5SuJbvWow/zh-cn_image_0000002706674582.png)

此过程中涉及两大角色，媒体会话提供方和媒体会话控制方。

**说明** 

媒体会话控制方为系统应用，三方应用可以成为媒体会话提供方。

本地媒体会话中，媒体会话提供方通过媒体会话管理器和媒体会话控制方进行信息交互：

1. 媒体会话提供方通过AVSessionManager创建AVSession对象。
2. 媒体会话提供方通过AVSession对象，设置会话元数据（媒体ID、标题、媒体时长等）、会话播放属性（播放状态、播放倍速、播放位置等）。
3. 媒体会话控制方通过AVSessionManager创建AVSessionController对象。
4. 媒体会话控制方通过AVSessionController对象可以监听对应会话元数据变化、播放属性变化等。
5. 媒体会话控制方通过AVSessionController对象还可以向媒体会话发送控制命令。
6. 媒体会话提供方通过AVSession对象可以监听来自媒体会话控制方的控制命令，例如：“play”播放、“playNext”播放下一首、“fastForward”快进、“setSpeed”设置播放倍速等。

## 媒体会话管理器

媒体会话管理器（AVSessionManager），提供了创建AVSession、创建AVSessionController、发送系统控制事件以及对AVSession状态进行监听的相关类型和函数。

实际上，AVSessionManager与AVSession、AVSessionController对象不同，并不是一个具体的对象，而是媒体会话的模块命名域。在实际编程过程中，可以通过如下方式引入：

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';
```

模块命名域中的所有方法都可以作为AVSessionManager的方法。

例如，媒体会话提供方通过AVSessionManager创建媒体会话的示例如下所示：

**说明** 

以下示例代码仅展示创建AVSession对象的接口调用，应用在真正使用时，需要确保AVSession对象实例在应用后台播放期间一直存在，避免被系统回收、释放，导致后台播放音频时被系统管控。

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
          // 创建session。
          let context = this.getUIContext().getHostContext() as Context;
          let session: AVSessionManager.AVSession = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');
          console.info(`session create done : sessionId : ${session.sessionId}`);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

更多关于AVSessionManager的方法，请参考API文档：[模块描述](../harmonyos-references/arkts-apis-avsession.md)。
