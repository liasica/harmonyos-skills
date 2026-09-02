---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-deployment-4
title: 折叠屏或分栏模式下观看视频时，画面拉伸
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 常见问题 > 折叠屏或分栏模式下观看视频时，画面拉伸
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a4991f1fd144962de7d9fee043dfc80c5027ee3a21e76e0c3b2964451794a263
---

## 问题现象

* 折叠屏折叠态下，应用横屏观看视频，视频画面发生拉伸现象。
* 分栏模式下，应用观看视频，视频画面发生拉伸现象。

## 背景知识

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)：提供用于图形绘制和媒体数据写入的Surface，XComponent负责将Surface嵌入到视图中，支持应用自定义Surface位置和大小。
* [Video](../harmonyos-references/ts-media-components-video.md)：用于播放视频文件并控制其播放状态的组件。Video组件只提供简单的视频播放功能，无法支持复杂的视频播放控制场景。
* [AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)：播放管理类，用于管理和播放媒体资源。在调用AVPlayer接口前，需要先通过createAVPlayer()构建一个AVPlayer实例。

## 问题定位

目前系统提供了Video和AVPlayer两种视频播放组件。可以通过DevEco Testing或代码检查来确认使用的是哪种组件。

* Video视频组件，建议检查代码中是否设置objectFit视频显示模式为Fill模式，该模式下视频不保持宽高比，会导致画面出现拉伸。
* 若使用的是AVPlayer视频组件，此时建议检查代码VideoScaleType视频缩放模式属性的设置值，该属性设置成VIDEO\_SCALE\_TYPE\_FIT时，会将视频拉伸至与窗口等大，导致画面拉伸。
* 通常AVPlayer会搭配XComponent使用，此时建议检查代码中视频的宽高比与XComponent持有Surface的显示区域的宽高比是否一致，如果宽高比不一致，会导致画面拉伸。

## 分析结论

* Video组件视频显示模式设置不正确导致视频画面发生拉伸现象。
* AVPlayer组件视频缩放模式设置不正确导致视频画面发生拉伸现象。
* AVPlayer组件中视频的宽高比跟XComponent持有Surface的显示区域的宽高比不一致，导致画面拉伸。

## 修改建议

* 修改Video视频显示模式[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性为Auto或者Contain，确保视频保持宽高比缩放。
* 在横竖屏切换时或在切换到分栏模式时，可以先用avPlayer.on('stateChange')监听视频状态变化，在监听到状态prepared时，获取视频的宽和高，并动态更改XComponent的Surface显示区域的宽高。

  ```screen
  import { media } from '@kit.MediaKit';
  import { display } from '@kit.ArkUI';

  // 1.创建视频播放器组件
  @Entry
  @Component
  struct VideoPlayerDemo {
    private avPlayer: media.AVPlayer | null = null; // AVPlayer实例
    private surfaceId: string = ''; // 播放窗口SurfaceID
    private xComponentController: XComponentController = new XComponentController();
    private videoWidth: number | undefined = 0;
    private videoHeight: number | undefined = 0;

    // 2.构建UI布局
    build() {
      Column() {
        // 视频播放窗口组件
        XComponent({
          id: "XComponent",
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .onLoad(() => {
            // 获取SurfaceID并初始化播放器
            this.surfaceId = this.xComponentController.getXComponentSurfaceId();
            this.initAVPlayer();
          })
          .width('100%')
          .height('100%');
      }
      .width('100%')
      .height('100%');
    }

    // 3.初始化播放器
    async initAVPlayer() {
      try {
        // 创建AVPlayer实例
        this.avPlayer = await media.createAVPlayer();
        // 设置监听事件
        this.avPlayer.on('stateChange', async (state: string) => {
          if (state === 'initialized') {
            // 设置播放窗口
            this.avPlayer!.surfaceId = this.surfaceId;
            await this.avPlayer!.prepare();
          } else if (state === 'prepared') {
            await this.avPlayer!.play(); // 自动开始播放
            // 获取视频原始宽高
            this.videoWidth = this.avPlayer?.width;
            this.videoHeight = this.avPlayer?.height;
            this.adjustSurfaceSize();
          }
        });
        // 监听屏幕旋转
        display.on('change', () => {
          this.adjustSurfaceSize();
        });
        // 设置播放源（本地文件或网络地址）
        this.avPlayer.url = 'https://xxx.mp4'; // 替换为实际地址
      } catch (error) {
        console.error(`Player initialization failed: ${error}`);
      }
    }

    private adjustSurfaceSize() {
      if (!this.videoWidth || !this.videoHeight) {
        return;
      }
      // 获取当前屏幕方向
      const displayInfo = display.getDefaultDisplaySync();
      const isPortrait = displayInfo.width < displayInfo.height;
      // 计算保持原始比例的显示尺寸
      let displayWidth = 0;
      let displayHeight = 0;
      if (isPortrait) {
        // 竖屏模式下保持视频宽度，高度按比例计算
        displayWidth = displayInfo.width;
        displayHeight = displayWidth * this.videoHeight / this.videoWidth;
      } else {
        // 横屏模式下保持视频高度，宽度按比例计算
        displayHeight = displayInfo.height;
        displayWidth = displayHeight * this.videoWidth / this.videoHeight;
      }
      // 更新XComponent尺寸
      this.xComponentController.setXComponentSurfaceRect({
        surfaceWidth: displayWidth,
        surfaceHeight: displayHeight
      });
    }

    // 4.组件销毁时释放资源
    aboutToDisappear() {
      if (this.avPlayer) {
        this.avPlayer.release();
        this.avPlayer = null;
      }
    }
  }
  ```
