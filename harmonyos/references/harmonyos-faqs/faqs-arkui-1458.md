---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1458
title: Video初始化阶段闪屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Video初始化阶段闪屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9475a19bdb4ef63480c971d547d02f3f1ba91ae05421f071fa1c08c74b67a821
---

## 问题现象

Video组件在加载本地视频时，会出现视频加载首页闪屏现象。

## 背景知识

[Video](../harmonyos-references/ts-media-components-video.md)组件是用于播放视频文件并控制其播放状态的组件，组件参数中的[previewUri](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)字段用于控制视频播放预览页面，可以通过给视频组件设置预览图解决闪屏问题。Video组件的[visibility](../harmonyos-references/ts-universal-attributes-visibility.md)属性可用来控制组件显隐状态，对Video组件进行显隐性控制可避免闪屏。

## 解决方案

方案一：可以对Video组件的previewUri字段进行设置，添加Video组件的预览图片。

方案二：可以对Video组件的visibility属性进行设置，设置当Video组件进入start状态时，在start方法的回调里，控制Video组件显示。

```ts
@Entry
@Component
struct VideoPage {
  build() {
    Row() {
      Column() {
        Text('before');
        // 根据实际业务传入视频地址
        VideoComponent({ url: '' });
        Text('after');
      }
      .width('100%');
    }
    .height('100%');
  }
}

@Component
struct VideoComponent {
  @State isVisible: Visibility = Visibility.Hidden;
  controller: VideoController = new VideoController();
  private url: string = '';

  build() {
    Row() {
      Video({ src: this.url, controller: this.controller })
        .visibility(this.isVisible)
        .autoPlay(true)
        .loop(true)
        .controls(false)
        .width('100%')
        .height('200vp')
        .onStart(() => {
          setTimeout(() => {
            this.isVisible = Visibility.Visible;
          }, 100);
        })
        .onPrepared(() => {
          this.controller.setCurrentTime(0, SeekMode.NextKeyframe);
        });
    };
  }
}
```
