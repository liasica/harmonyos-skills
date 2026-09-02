---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-42
title: 音量变化监听过程中失效
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 音量变化监听过程中失效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2187b25cd8b55d833491e9190ab12c7e41e2cfbd639954a63d17ea09cb879d89
---

## 问题现象

按照如下代码设置音量监听，运行过程中，突然会打印Destructor is successful，之后收不到音量变化监听事件。

```ts
registerVolumeChange() {
    let audioManager = audio.getAudioManager();
    let volumeManager = audioManager.getVolumeManager();
    volumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC,
      (streamVolumeEvent: audio.StreamVolumeEvent) => {
        console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
        console.info(`Volume level: ${streamVolumeEvent.volume} `);
        console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
      });
  }
```

## 背景知识

* 在编程语言中，局部变量的作用域和生命周期是理解程序行为的关键概念之一。局部变量是在函数内部声明的变量，它们的作用域仅限于函数内部。这意味着局部变量只能在声明它们的函数内部被访问和使用。当函数被调用时，局部变量会被创建并分配内存。这些变量的生命周期与函数的执行周期紧密相关，即局部变量在函数执行期间存在，一旦函数执行结束，局部变量所占用的内存空间就会被释放。
* 管理系统音量的接口由audioVolumeManager提供，在使用之前，需要使用[getVolumeManager()](../harmonyos-references/arkts-apis-audio-audiomanager.md#getvolumemanager9)获取audioVolumeManager实例，可以通过设置监听事件来监听系统音量的变化，详情可以参考：[监听系统音量变化](../harmonyos-guides/volume-management.md#监听系统音量变化)。

## 问题定位

检查日志发现打印了如下日志，说明audioVolumeManager已被销毁，需要分析代码确认VolumeManager被销毁的原因：

```txt
[Destructor]Destructor is successful.
```

检查代码发现audioVolumeManager变量在函数中就通过let进行了声明，这会导致函数执行结束后audioVolumeManager变量被释放，因此后续无法监听到音量变化。

## 分析结论

audioVolumeManager在错误的地方进行了声明导致执行完函数后相应变量被释放，因此后续无法正常监听音量变化。

## 修改建议

通过将audioVolumeManager和组件进行绑定，将volumeManager定义为组件的成员变量。在需要调用的地方，通过访问成员变量[监听系统音量变化](../harmonyos-guides/volume-management.md#监听系统音量变化)。

```ts
import {audio} from '@kit.AudioKit';

@Entry
@Component
struct Index{
  private audioManager = audio.getAudioManager();
  private volumeManager = this.audioManager.getVolumeManager();

  aboutToAppear(): void {
    this.registerVolumeChange();
  }
  build() {
    Column();
  }
  registerVolumeChange(){
    this.volumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
      console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
      console.info(`Volume level: ${streamVolumeEvent.volume} `);
      console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
    });
  }
}
```

## 总结

如果是需要长期使用的变量，不能在函数中进行声明，否则会使得函数结束时变量也被释放。

## 常见FAQ

Q：如何不通过监听音量调节获取当前系统音量大小？

A：通过[AudioManager](../harmonyos-references/arkts-apis-audio-audiomanager.md)管理音频音量和音频设备，使用[getvolumebystream](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)接口获取指定流的音量。
