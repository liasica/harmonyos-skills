---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tri-fold-2
title: 三折叠设备横屏播放视频时退出全屏，无法回归竖屏显示
breadcrumb: FAQ > 多设备场景 > 手机 > 三折叠常见问题 > 三折叠设备横屏播放视频时退出全屏，无法回归竖屏显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ee5ec1c926e49ed12b2f144beab1b6c058a2103306b1d39eed26588c5238e632
---

## 问题现象

三折叠设备，应用从单屏展开到三屏再折叠回单屏，点击视频全屏后，横屏播放，退出视频全屏，应用页面无法回归竖屏显示。

## 背景知识

* [module.json5](../harmonyos-guides/module-configuration-file.md)文件内的[abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签下的orientation字段可配置应用启动时的屏幕方向。
* 代码中调用[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口，可改变屏幕方向，注意窗口将一直保持最后一次设置窗口方向的效果，因此在退出需要改变方向显示的内容页面时需要重新调用此方法恢复屏幕方向。

## 问题定位

1. 查阅代码中module.json5文件内的abilities标签下的orientation字段的值，例如下面设置应用启动方向为竖屏显示。

   ```screen
   "abilities": [
     {
       "orientation": "portrait",
     }
   ]
   ```
2. 查阅代码中是否调用setPreferredOrientation接口改变了屏幕方向，例如下面设置屏幕方向为横屏。

   ```screen
   this.windowStage?.getMainWindow((err: BusinessError, data: window.Window) => {
     if (err.code) {
       return
     }
     data.setPreferredOrientation(window.Orientation.LANDSCAPE)
   })
   ```

## 分析结论

应用代码中调用了setPreferredOrientation接口改变了屏幕方向，但是退出页面时没有进行方向恢复，导致该场景下，进入页面屏幕方向被改成了横向，退出页面没有进行方向恢复，造成了三屏折回单屏，全屏横向播放视频退出后，屏幕依然是横向。

## 修改建议

检查setPreferredOrientation接口调用处的代码逻辑，保证所有用例场景下，如果有修改屏幕方向的代码：setPreferredOrientation(window.Orientation.LANDSCAPE)，就需要有屏幕方向恢复的代码：setPreferredOrientation(window.Orientation.PORTRAIT)。

```screen
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoOrientation {
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
          if (e !== undefined) {
            if (e.fullscreen === true) {
              window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => { // 获取window实例
                const errCode: number = err.code;
                if (errCode) {
                  console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
                  return;
                }
                let windowClass = data;
                windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE);
              });
            } else {
              window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
                const errCode: number = err.code;
                if (errCode) {
                  console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
                  return;
                }
                let windowClass = data;
                windowClass.setPreferredOrientation(window.Orientation.PORTRAIT);
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
