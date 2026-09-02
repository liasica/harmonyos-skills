---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-755
title: Swiper滑动控制视频暂停播放
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper滑动控制视频暂停播放
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6dbd91e819b21513f9a44c7684c565dbbfa5c78165704c5d9cdfc838e9e5d0ed
---

## 问题现象

Swiper里嵌套不同的视频，滑动Swiper时（比如从第一个Item滑动到第二个Item），如何让之前的Item暂停视频播放？

## 背景知识

* [Video](../harmonyos-references/ts-media-components-video.md)组件视频播放后默认不会自动暂停，而是会继续播放，只有通过[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)的[pause](../harmonyos-references/ts-media-components-video.md#pause)方法可以暂停播放。另外还可以通过VideoController的[stop](../harmonyos-references/ts-media-components-video.md#stop)方法控制视频重新播放。
* [Swiper](../harmonyos-references/ts-container-swiper.md)组件滑动时默认不会触发VideoController的pause方法，但是Swiper滑动时会触发[onChange](../harmonyos-references/ts-container-swiper.md#onchange)事件。

## 解决方案

Swiper滑动时触发onChange事件，在onChange方法里调用VideoController的pause方法即可实现滑动过程控制视频暂停播放。

```ts
@Entry
@Component
struct demoExample {
  private controllerList: VideoController[] =
    [new VideoController(), new VideoController(), new VideoController(), new VideoController()];
  @State swiperIndex: number = 0;

  build() {
    Swiper() {
      ForEach([0, 1, 2, 3], (item: number) => {
        Column() {
          Text(`第 ${item + 1} 个组件页`)
            .width('100%')
            .backgroundColor(Color.White)
            .textAlign(TextAlign.Center)
            .fontSize(20);
          Video({
            // 此处'www.xxx.com/yyy.mp4'仅作为示例
            src: 'www.xxx.com/yyy.mp4',
            controller: this.controllerList[item]
          })
            .objectFit(ImageFit.Contain)
            .controls(true)
            .autoPlay(false)
            .loop(true)
            .height(200);
        };
      });
    }
    .loop(true)
    .backgroundColor(Color.Black)
    .onChange((index: number) => {
      const preIndex = index > 0 ? index - 1 : 3;
      const nextIndex = index < 3 ? index + 1 : 0;
      this.controllerList[preIndex].pause();
      this.controllerList[nextIndex].pause();
      this.swiperIndex = index;
    });
  }
}
```

## 常见FAQ

Q：如果要视频切回来之后重新播放，应该如何设置？

A：只需将上述样例代码中onChange方法里调用的pause()方法换成stop()即可。

**说明** 

这里切回来之后显示的还是暂停时的那一帧内容，在点击播放时会重新播放。

Q：如果Video组件设置了预览图和视频路径，如何在视频播放暂停时如何由当前帧重置到预览图？

A：可使用Stack堆叠Image和Video，通过状态控制Image的显示/隐藏，实现暂停时展示预览图、播放时隐藏的效果。
