---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1354
title: XComponent实现多个画面切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > XComponent实现多个画面切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bbda25fb7dd62ee54f7b0559ad1b852905208f506fefd726e711600eec9c1813
---

## 问题现象

竖屏状态下有A，B两个XComponent上下排列显示视频直播画面，如何实现全屏状态下显示两个大小不同的视频画面？

## 背景知识

* 使用[Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)组件，通过绑定变量，设置宽，高，边距来修改视频的位置。
* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)是为媒体源提供播放能力的API。
* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置主窗口的显示方向属性，使用callback异步回调。

## 解决方案

1. 使用层叠布局，创建2个XComponent组件，组件id设置唯一，通过height，margin设置组件的位置布局。
2. 创建AVPlayer实例对象和控制器XComponentController，获取不同组件的id，实现音频播放。
3. 设置按钮切换横屏，实时改变XComponent组件的宽高和位置，通过setPreferredOrientation实现多个画面切换。

完整示例参考如下：

```screen
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { media } from '@kit.MediaKit';
import { common } from '@kit.AbilityKit';

function setAVPlayerCallback(avPlayer: media.AVPlayer) {
  if (avPlayer === undefined) {
    return;
  }
  // 监听播放状态机AVPlayerState切换的事件
  avPlayer?.on('stateChange', async (state: string) => {
    switch (state) {
      case 'idle':
        hilog.info(0X0000, 'testTag', 'AVPlayer state idle called.');
        break;
      case 'initialized':
        hilog.info(0X0000, 'testTag', 'AVPlayer state initialized called.');
        break;
      case 'prepared':
        hilog.info(0X0000, 'testTag', 'AVPlayer state prepared called.');
        hilog.info(0X0000, 'testTag', 'AVPlayer start to play.');
        break;
      case 'playing':
        hilog.info(0X0000, 'testTag', 'AVPlayer state playing called.');
        avPlayer?.play();
        break;
      case 'paused':
        hilog.info(0X0000, 'testTag', 'AVPlayer state paused called.');
        avPlayer?.pause();
        break;
      case 'completed':
        hilog.info(0X0000, 'testTag', 'AVPlayer state completed called.');
        avPlayer?.reset();
        break;
      case 'stopped':
        hilog.info(0X0000, 'testTag', 'AVPlayer state stopped called.');
        break;
      case 'released':
        hilog.info(0X0000, 'testTag', 'AVPlayer state released called.');
        avPlayer?.release();
        break;
      default:
        break;
    }
  });
}

class AvPlayerInstance {
  private static instance: AvPlayerInstance;
  private objects = new Map<string, media.AVPlayer>();

  public static getObjectContext(): AvPlayerInstance {
    if (!AvPlayerInstance.instance) {
      AvPlayerInstance.instance = new AvPlayerInstance();
    }
    return AvPlayerInstance.instance;
  }

  getObject(value: string): media.AVPlayer | undefined {
    return this.objects.get(value);
  }

  setObject(key: string, objectClass: media.AVPlayer): void {
    this.objects.set(key, objectClass);
  }
}

@Entry
@Component
struct Index {
  @State xAh: string = '30%';
  @State xBw: string = '100%';
  @State xbM: string = '70%';
  @State xbMl: string = '0%';
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private surfaceId: string = '';
  private surfaceId2: string = '';
  xComponentController1: XComponentController = new XComponentController();
  xComponentController2: XComponentController = new XComponentController();

  async avPlayerLiveDemo(value: string, file: string) {
    // 创建avPlayer实例对象
    let avPlayer: media.AVPlayer = await media.createAVPlayer();
    // 创建状态机变化回调函数
    setAVPlayerCallback(avPlayer);
    let fileDescriptor = await this.context.resourceManager.getRawFd(file);
    avPlayer.fdSrc = fileDescriptor;
    AvPlayerInstance.getObjectContext().setObject(value, avPlayer);
  }

  aboutToAppear() {
    this.avPlayerLiveDemo('valueA', 'test.mp4'); // 此处'test.mp4'等资源仅作示例，请开发者自行替换。

    this.avPlayerLiveDemo('valueB', 'test2.mp4'); // 此处'test2.mp4'等资源仅作示例，请开发者自行替换。
    console.info('aboutToAppear start');
  }

  // 层叠布局创建2个XComponent组件，组件id设置唯一
  build() {
    Column() {
      Stack({ alignContent: Alignment.Top }) {
        XComponent({
          id: 'A',
          type: XComponentType.SURFACE,
          controller: this.xComponentController1
        })
          .width('100%')
          .height(this.xAh)
          .onLoad(async () => {
            console.info('onload start');
            this.surfaceId = this.xComponentController1.getXComponentSurfaceId();
            let player = AvPlayerInstance.getObjectContext().getObject('valueA');
            if (player !== undefined) {
              player.surfaceId = this.surfaceId;
              await player.prepare();
            }
            player?.play(); // 音频播放
          })
          .align(Alignment.TopStart)
          .id('xcomponent');

        XComponent({
          id: 'B',
          type: XComponentType.SURFACE,
          controller: this.xComponentController2
        })
          .width(this.xBw)
          .height('35%')
          .onLoad(async () => {
            this.surfaceId2 = this.xComponentController2.getXComponentSurfaceId();
            let player = AvPlayerInstance.getObjectContext().getObject('valueB');
            if (player !== undefined) {
              player.surfaceId = this.surfaceId2;
              await player.prepare();
            }
            player?.play();
          })
          .id('xcomponent')
          .align(Alignment.End)
          .margin({ top: this.xbM, left: this.xbMl });
      }.height('80%');

      Button('切换屏幕').onClick(() => { // 实时改变XComponent组件的宽高和位置。
        this.xAh = '100%';
        this.xBw = '50%';
        this.xbM = '20%';
        this.xbMl = '50%';
        window.getLastWindow(this.context, (err, win) => {
          let currentOrientation = win.getPreferredOrientation();
          if (currentOrientation == window.Orientation.PORTRAIT) {
            win.setPreferredOrientation(window.Orientation.LANDSCAPE); // 通过setPreferredOrientation实现多个画面切换。
          } else {
            win.setPreferredOrientation(window.Orientation.PORTRAIT); // 通过setPreferredOrientation实现多个画面切换。
          }
        });
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
