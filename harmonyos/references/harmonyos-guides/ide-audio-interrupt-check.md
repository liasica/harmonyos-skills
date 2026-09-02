---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-audio-interrupt-check
title: "@correctness/audio-interrupt-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/audio-interrupt-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1f8f03c84f79f9c8144693de6c4ebe697b5438f09c17dbdea24564022300cfb6
---

建议应用在播放或录制音频的场景中，监听音频焦点中断回调事件，并响应。

改善[音视频播放](audio-playback-concurrency.md#处理音频焦点变化)体验场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/audio-interrupt-check": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { audio } from '@kit.AudioKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
// An identifier specifying whether the audio stream is being played. In actual development, this parameter corresponds to the module related to the audio playback state.
let isPlay: boolean;
// An identifier specifying whether to duck the volume down. In actual development, this parameter corresponds to the module related to the audio volume.
let isDucked: boolean;
// An identifier specifying whether the start operation is successful.
let started: boolean;
media.createAVPlayer((error: BusinessError, player) => {
  if (player) {
    console.info('Succeeded in creating AVPlayer');
        player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
      // When audio focus changes, the AudioRenderer receives the interruptEvent callback and performs processing based on the content in the callback.
      // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
      // Note: In the default focus strategy, INTERRUPT_HINT_RESUME maps to the force type INTERRUPT_SHARE, and others map to INTERRUPT_FORCE. Therefore, the value of forceType does not need to be checked.
      // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
      if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
        // If the value of interruptEvent.forceType is INTERRUPT_FORCE, the system has performed audio-related processing, and the application needs to update its state and make adjustments accordingly.
        switch (interruptEvent.hintType) {
          case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
            // The system has paused the audio stream (focus is temporarily lost). To ensure state consistency, the application needs to switch to the audio paused state.
            // Temporarily losing focus: After other audio streams release focus, the current audio stream will receive the audio focus event corresponding to resume and automatically resume the playback.
            // A simplified processing indicating several operations for switching the application to the audio paused state.
            isPlay = false;
            break;
          case audio.InterruptHint.INTERRUPT_HINT_STOP:
            // The system has stopped the audio stream (focus is permanently lost). To ensure state consistency, the application needs to switch to the audio paused state.
            // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
            // A simplified processing indicating several operations for switching the application to the audio paused state.
            isPlay = false;
            break;
          case audio.InterruptHint.INTERRUPT_HINT_DUCK:
            // The system has ducked the volume down (to 20% of the normal volume by default).
            // A simplified processing indicating several operations for switching the application to the volume decreased state.
            isDucked = true;
            break;
          case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
            // The system has restored the audio volume to normal.
            // A simplified processing indicating several operations for switching the application to the normal volume state.
            isDucked = false;
            break;
          default:
            break;
        }
      } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
        // If the value of interruptEvent.forceType is INTERRUPT_SHARE, the application can take action or ignore as required.
        switch (interruptEvent.hintType) {
          case audio.InterruptHint.INTERRUPT_HINT_RESUME:
            // The paused audio stream can be played. It is recommended that the application continue to play the audio stream and switch to the audio playing state.
            // If the application does not want to continue the playback, it can ignore the event.
            // To continue the playback, the application needs to call start(), and use the identifier variable started to record the execution result of start().
            isPlay = true;
            started = true;
            break;
          default:
            break;
        }
      }
    });
    player.on('audioOutputDeviceChangeWithInfo', ()=>{
        console.error(`createAVPlayer audioOutputDeviceChangeWithInfo`);
    });
  } else {
    console.error(`Failed to create AVPlayer, error message:${error.message}`);
  }
});
```

## 反例

```screen
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
export class AudioInterruptReport {
  demoCallBack() {
    media.createAVPlayer((error: BusinessError, player) => {
      if (player) {
        player.on('audioOutputDeviceChangeWithInfo', ()=>{
            console.error(`createAudioRenderer outputDeviceChangeWithInfo`);
        })
        console.info('Succeeded in creating AVPlayer');
      } else {
        console.error(`Failed to create AVPlayer, error message:${error.message}`);
      }
    });
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
