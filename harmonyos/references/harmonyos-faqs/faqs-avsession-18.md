---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-18
title: 视频播放时，播控中心状态不正确，且无法暂停视频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 视频播放时，播控中心状态不正确，且无法暂停视频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f46b118e92ac1cabf32dca4a9992c1850d9897ff91334279d01709ae1d897a77
---

## 问题现象

用户在应用中打开视频查看页面，当用户操作开始播放视频后，发现在播控中心的状态不正确。当前视频已经为在播放状态，而播控中心上显示的播放状态为暂停状态，与实际播放状态不符。而且，用户尝试在播控中心上点击按钮后，发现无响应，播控中心按钮仍为暂停状态。

可以参见如下现象演示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/ghqvPOG4QmG36m5S2j9A5g/zh-cn_image_0000002658912001.png "点击放大")

## 背景知识

* [@ohos.multimedia.avsession (媒体会话管理)](../harmonyos-references/js-apis-avsession.md)：媒体会话管理提供媒体播控相关功能的接口，目的是让应用接入播控中心。
  + [AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)：会话，可用于设置元数据、播放状态信息等操作。
  + [AVSessionController](../harmonyos-references/arkts-apis-avsession-avsessioncontroller.md)：会话控制器，可用于查看会话ID，完成对会话发送命令及事件，获取会话元数据、播放状态信息等操作。
  + [AVCastController](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md)：投播控制器，可用于投播场景下，完成播放控制、远端播放状态监听、远端播放状态信息获取等操作。
* [应用接入AVSession场景介绍](../harmonyos-guides/avsession-access-scene.md)：对于不同的场景，将会在系统的播控中心看到不同的UI呈现。同时，在不同的场景下，应用的接入处理也需要遵循不同的规范约束。

相关API简单介绍：

* [avSession.createAVSession](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)：创建会话对象，一个Ability只能存在一个会话，重复创建会失败。
* [setAVPlaybackState](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)：设置会话播放状态。

## 问题定位

1. 确认是否使用了@ohos.multimedia.avsession (媒体会话管理)的能力。在代码中全局检索关键字@kit.AVSessionKit，如果如下的信息，则说明使用了该能力。

   ```ts
   import { avSession } from '@kit.AVSessionKit';
   // ...
   ```
2. 确认是否使用了createAVSession()创建AVSession实例。要接入播控中心，就必须通过该API创建AVSession的实例并激活媒体会话，视频应用选择会话类型为video，开发者可根据应用的类型选择对应的会话，参见[创建不同类型的会话](../harmonyos-guides/avsession-access-scene.md#创建不同类型的会话)。

   在代码中检索关键字avSession.createAVSession，如果有可以查询到，则说明创建了AVSession的实例。
3. 确认是否使用了setAVPlaybackState()设置会话状态，将视频播放信息上报到播控中心，从而达到播控中心与应用的状态同步，包括播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等。在代码中检索关键字setAVPlaybackState，如果没有检索到则说明应用没有设置会话状态，从而导致本问题现象。如果有如下信息，则说明应用有设置会话状态，可能是因为会话状态设置逻辑有问题导致状态同步失败。

## 分析结论

应用通过AVSessionKit接入了播控中心，但是并没有同步会话状态，或者同步会话状态的逻辑处理有问题，从而导致了本问题的发生。

## 修改建议

根据视频播放的情况，采集当前视频的播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等信息，并通过setAVPlaybackState同步给播控中心。

参考如下代码示例，相关完整的介绍参见[播控中心控制应用播放](../best-practices/bpta-vdeocast.md#section537628143614)：

```ts
public setAvSessionPlayState(playbackState: avSession.AVPlaybackState) {
  if (this.session) {
    this.session.setAVPlaybackState(playbackState, (err: BusinessError) => {
      if (err) {
        console.error(TAG, `SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        console.info(TAG, 'SetAVPlaybackState successfully');
      }
    });
  }
}
```

```ts
private updateIsPlay(isPlay: boolean) {
  // *调用AvSessionController工具类的setAvSessionPlayState，同步视频播放信息*
  this.setAvSessionPlayState({
    // *视频播放状态信息*
    state: isPlay ? avSession.PlaybackState.PLAYBACK_STATE_PLAY : avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
    // *视频当前播放位置信息*
    position: {
      elapsedTime: this.currentTime * 1000,
      updateTime: new Date().getTime()
    }
  });
}
```
