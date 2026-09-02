---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-49
title: 如何判断设备正在播放音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何判断设备正在播放音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7d0bb2daf9c735cfc2922b490e221280863a4b4369791bc3b6d4e6e1b92827f9
---

## 问题现象

其他平台有API可以判断是否有音频正在播放，HarmonyOS系统如何判断？

## 背景知识

[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)表示播放音频流类型的枚举。[isStreamActive](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isstreamactive20)获取指定音频流是否为活跃状态。[getCurrentAudioRendererInfoArraySync](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiorendererinfoarraysync10)获取当前音频渲染器的信息。

## 解决方案

开发者可通过[isStreamActive](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isstreamactive20)接口获取指定音频流（如音乐、视频等）是否为活跃状态，活跃即正在播放。当需要获取是否有任意音频流在播放时，可通过getCurrentAudioRendererInfoArraySync接口获取音频流列表，并通过isStreamActive判断音频流是否活跃，从而判断当前是否有音频正在播放。

```screen
import { audio } from '@kit.AudioKit';

@Entry
@Component
export struct CheckRendererDemo {
  promptAction = this.getUIContext().getPromptAction();

  build() {
    Column({ space: 10 }) {
      Button('检查是否有音频正在播放')
        .width('100%')
        .onClick(async () => {
          this.promptAction.showToast({
            message: checkIsRenderer() ? '有音频正在播放' : '没有音频正在播放'
          });
        });
    }
    .padding(20)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}

function checkIsRenderer(): boolean {
  let isRenderer: boolean = false;
  let audioManager = audio.getAudioManager();
  let audioStreamManager = audioManager.getStreamManager();
  let array: audio.AudioRendererChangeInfoArray = audioStreamManager.getCurrentAudioRendererInfoArraySync(); // 查询音频设备
  for (let i = 0; i < array.length; i++) {
    let audioRendererInfo = array[i].rendererInfo;
    console.info(`RendererChange on is called for ${i}`, JSON.stringify(audioRendererInfo));
    try {
      let isStreamActive = audioStreamManager.isStreamActive(audioRendererInfo.usage); // 判断设备状态是否活跃，是否在播放
      console.info(`RendererChange IsStreamActive: ${isStreamActive}.`);
      if (isStreamActive) {
        isRenderer = true;
        break;
      }
    } catch (err) {
      console.error(`RendererChange. code: ${err.code}, message: ${err.message}`);
    }
  }
  return isRenderer;
}
```
