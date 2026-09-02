---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-6
title: 横屏播放视频导致页面布局异常如何解决
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 横屏播放视频导致页面布局异常如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:25+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cd293c5fdf92d42e7f99b481ec9188cc9ec9eddefff92329e85a52b56734e77d
---

## 问题现象

应用打开正常显示，点击某一视频横屏播放后，返回上一页，页面显示错位异常。其根本原因是系统的旋转特性针对窗口级别生效，当视频页面通过setPreferredOrientation()将窗口设为横屏时，同一窗口下的所有页面都会被强制进入横屏布局，退出视频页面时若未及时恢复竖屏方向，就会导致上一页面布局错位。

## 背景知识

* [横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)：横竖屏切换功能实现应用内既支持竖屏显示也支持横屏显示的效果。横竖屏切换时，页面尺寸同步发生变化。
* [窗口方向](../best-practices/bpta-multi-device-window-direction.md)：横竖屏切换功能是指应用内同时支持竖屏和横屏显示。当不同页面需要采用不同显示方向时，需在应用逻辑中动态调整窗口方向以实现该效果。

## 问题定位

1. 当应用无论竖屏还是横屏启动，页面显示正常，说明应用初次加载监听了屏幕大小，并正确设置了页面尺寸。
2. 当应用从横屏的视频页面切换回竖屏状态时，建议检查代码中是否使用on('windowSizeChange')监听了设备尺寸变化，判断当前是横屏还是竖屏。
3. 检查异常的页面是否通过判断当前是横屏还是竖屏，分别展示不同的布局。
4. 系统的旋转特性是针对窗口实现的，无法让单个页面独立进行旋转操作。当通过setPreferredOrientation()修改窗口方向为横屏时，同一窗口下的所有页面都会受到影响，导致其他页面也被强制变为横屏布局。

## 分析结论

应用在进入视频横屏时监听了屏幕方向变化，退出视频播放页面时，页面还根据横屏状态获取的屏幕尺寸进行页面布局，导致应用在返回上一页时，页面显示错位异常现象。此外，由于系统的旋转特性是针对窗口级别的，当横屏视频页面修改窗口方向时，同一窗口下的其他页面也会被强制进入横屏布局状态。

## 修改建议

### 方案一：通过窗口方向接口动态切换横竖屏

在触发横竖屏切换的事件（如视频全屏事件）中，通过setPreferredOrientation()修改方向，退出全屏时同样恢复竖屏状态。

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoPage {
  @State videoSrc: Resource = $rawfile('example.mp4'); // 实际开发替换为实际视频资源
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  private isAutoPlay: boolean = true;
  private showControls: boolean = true;
  private isShortcutKeyEnabled: boolean = false;
  controller: VideoController = new VideoController();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        currentProgressRate: this.curRate, // 设置播放速度
        controller: this.controller,
      })
        .width('100%')
        .height(600)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .enableShortcutKey(this.isShortcutKeyEnabled)
        .onFullscreenChange((e?: FullscreenObject) => {
          if (e != undefined) {
            if (e.fullscreen == true) {
              window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => { // 获取window实例
                let windowClass = data;
                windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE); // 点击全屏后，旋转为横屏显示
              });
            } else {
              window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => { // 获取window实例
                let windowClass = data;
                windowClass.setPreferredOrientation(window.Orientation.PORTRAIT); // 退出全屏后，旋转为竖屏显示
              });
            }
          }
        });
    };
  }
}

interface FullscreenObject {
  fullscreen: boolean;
}
```

### 方案二：使用独立UIAbility实现页面级横竖屏隔离

如果希望某个特定页面可以进行横竖屏转换，而完全不影响其他页面，建议将该页面放在独立的UIAbility中（与其他页面分开），在需要打开的时候通过启动该UIAbility实现相关功能。这样可以避免窗口旋转影响其他页面的布局。具体参考[启动UIAbility的指定页面](../harmonyos-guides/uiability-intra-device-interaction.md#启动uiability的指定页面)。

### 方案三：使用Navigation页面级旋转特性

Navigation中也提供了页面级的旋转特性，该功能仅支持ArkTS接口。通过Navigation的页面级旋转，可以实现单个页面的横竖屏切换而不影响其他页面。具体参考[横竖屏开发指导](../best-practices/bpta-landscape-and-portrait-development.md#section161651074615)。
