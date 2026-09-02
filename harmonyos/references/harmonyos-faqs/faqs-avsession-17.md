---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-17
title: 播控中心的进度条展示错误，与应用内的进度条不一致
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 播控中心的进度条展示错误，与应用内的进度条不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:22+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:872840a34f2658c6e5fb5b14af561b0bbe4d660898ff50ad91c27397de29cc31
---

## 问题现象

应用内进行音频播放，查看播控中心的进度条，发现和应用内的进度条进度不一致。

### 场景一

应用没有正确创建并初始化AVSession，导致播控中心进度条展示错误。

### 场景二

应用没有更新AVPlaybackState，导致播控中心进度条展示错误。

### 场景三

用户手动修改系统时间后，播控中心进度条展示错误。

## 背景知识

* [AVMetadata](../harmonyos-references/arkts-apis-media-i.md#avmetadata11)：描述媒体数据的相关属性，包含媒体资源的标题、作者、媒体时长等属性。
* [AVPlaybackState](../harmonyos-references/arkts-apis-avsession-i.md#avplaybackstate10)：描述媒体播放状态的属性，包含媒体资源的播放状态、播放倍速、缓冲时间等属性。
* [播控中心展示进度](../harmonyos-guides/avsession-access-scene.md#设置进度条信息)：应用如果支持在播控中心展示进度，那么在媒体资源播放中，需要设置资源的时长、播放状态（暂停、播放）、播放位置、倍速，播控中心会使用这些信息进行进度的展示：
* [PlaybackPosition](../harmonyos-references/arkts-apis-avsession-i.md#playbackposition10)中的elapsedTime代表已用时间，updateTime代表更新时间，一般使用new Date().getTime()获取本次更新进度的时间。
* 进度条计算方法：

  根据应用提供的时间戳，倍速，计算新的位置；如果应用直接更新位置，则使用应用提供的位置刷新；

## 问题定位

### 场景一

**应用没有正确创建并初始化AVSession，导致播控中心进度条展示错误：**

查看应用是否正确初始化AVSession，保障应用已[创建AVSession](../harmonyos-guides/avsession-access-scene.md#创建不同类型的会话)；[设置元数据](../harmonyos-guides/avsession-access-scene.md#设置元数据信息)，且保障duration（媒体资源时长）来源可靠；至少注册一条[控制命令](../harmonyos-guides/avsession-access-scene.md#控制命令的处理)，并[激活AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)保障控制命令有效。如下方示例：

```ts
// 设置媒体资源时长。
 private setAVMetadata() {
    let metadata: AVSessionManager.AVMetadata = {
      assetId: '0',
      title: 'TITLE',
      mediaImage: 'IMAGE',
      duration: 1000000,
    };
    this.session!.setAVMetadata(metadata).then(() => {
      console.info(`SetAVMetadata successfully`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
    });
  }
```

```ts
// 注册控制命令。
private registerSessionListener() {
    this.session!.on('play', () => {
      console.info(`on play , do pause task`);
      this.controller.start();
    });
    this.session!.on('pause', () => {
      this.controller.pause();
    });
  }
```

```ts
// 初始化Avsession并激活
async initAvsession() {
    this.session = await AVSessionManager.createAVSession(this.context, 'SESSION_NAME', this.type);
    this.setAVMetadata();
    this.registerSessionListener();
    this.RegisterTimeChange();
    this.session.activate();
  }
```

以上操作均完成后，可在播控中心正确展示信息。

### 场景二

**应用没有更新AVPlaybackState，导致播控中心进度条展示错误：**

当应用的播放状态、播放位置、倍速等发生变化时，应用需[更新AVPlaybackState](../harmonyos-guides/avsession-access-scene.md#设置播放状态)。系统的播控中心会根据应用设置的信息自行进行播放进度的计算，而不需要应用实时更新播放进度，在下一次更新AVPlaybackState前，播控中心进度条可自行计算更新展示进度。若应用始终未设置AVPlaybackState，则播控中心进度条不启动。

```ts
private setAVPlaybackState(currentState: AVSessionManager.AVPlaybackState) {
    this.session!.setAVPlaybackState(currentState, (err) => {
      if (err) {
        console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info(`SetAVPlaybackState successfully`);
      }
    });
  }
```

### 场景三

**用户手动修改系统时间后，播控中心进度条展示错误：**

播控中心进度的自动计算依赖系统时间，假设播控中心当前进度为T，系统时间为A，上次更新AVPlaybackState时更新时间updateTime为B，已播放时间elapsedTime为C，设置的播放速度为speed。

则上次更新AVPlaybackState后，播控中心进度条自动计算的逻辑为：T=(A-B)\*speed+C，故用户手动修改系统时间后，播控中心进度条可能会展示错误。

使用new Date().getTime()获取updateTime，并更新AVPlaybackState即可恢复正常。如下方示例：

```ts
// 监听公共事件，当系统时间改变时更新AVPlaybackState
async RegisterTimeChange() {
    let event: commonEventManager.CommonEventSubscribeInfo = {
      events: ['usual.event.TIME_TICK', 'usual.event.TIME_CHANGED']
    }
    commonEventManager.createSubscriber(event, (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
      if (err) {
        console.error(this.message, `createSubscriber is error, message: ${err.message}`);
        return;
      }
      console.info(this.message, `createSubscriber TIME_CHANGED`);
      if (data) {
        commonEventManager.subscribe(data, (err: BusinessError, data: commonEventManager.CommonEventData) => {
          console.info(this.message, ` subscribe TIME_CHANGED`);

          this.updateTime=new Date().getTime();
          this.currentState.position = { elapsedTime: this.elapsedTime, updateTime:this.updateTime  }
          this.setAVPlaybackState(this.currentState!);

          if (err) {
            console.error(this.message, `subscribe is error, message: ${err.message}}`);
            return;
          }
        });
      }
    });
  }
```

## 分析结论

### 场景一

应用需要正确创建并初始化AVSession，保障播控中心进度条正确展示。需保障创建AVSession，并设置元数据信息；以及至少注册一条控制命令，使播控中心正常展示进度条等相关信息。需保障元数据信息duration字段来源可靠，与应用一致。

### 场景二

当应用的播放状态变化，执行seek播放跳转、倍速播放等与进度条相关的操作时，应用需[更新AVPlaybackState](../harmonyos-guides/avsession-access-scene.md#设置播放状态)，系统的播控中心会根据应用设置的信息同步更新。

系统的播控中心会根据应用设置的信息自行进行播放进度的计算，而不需要应用实时更新播放进度，在下一次更新AVPlaybackState前，播控中心进度条可自行计算更新展示进度。若应用始终未设置AVPlaybackState，则播控中心进度条不启动。

### 场景三

播控中心进度的自动计算依赖系统时间，当用户手动修改系统时间时，播控中心进度条计算错误，将不符合预期。通过监听系统时间改变的公共事件等方式，使用new Date().getTime()获取updateTime，并更新AVPlaybackState即可恢复正常。

## 修改建议

实现播控中心的进度条的正常显示和移动，与应用保持一致，需要正确接入AVSession，并且在播放状态发生变化时（播放状态、播放位置、倍速），及时更新AVPlaybackState。其他可参考[AVSession进度条](../harmonyos-guides/avsession-access-scene.md#进度条)。
