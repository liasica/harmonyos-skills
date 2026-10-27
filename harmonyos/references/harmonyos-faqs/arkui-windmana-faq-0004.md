---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0004
title: 屏幕常亮设置常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 屏幕常亮设置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:28+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:0ac2d9218c6959cac90f87f68de746a4f71510ffa5cf3b69f1c0ec8f0dc71f7d
---

**Q：在投屏场景下，用户没有屏幕交互操作，也不希望手机跟随系统设置的休眠时间自动熄屏，而是保持屏幕常亮，该如何设置屏幕为常亮状态？如何在用户长时间没有进行屏幕交互的情况下，设置手机屏幕常亮？**

**A**：遇到用户长时间没有屏幕交互的场景，例如视频播放、投屏、导航等场景，为了避免息屏影响用户体验，可以通过[setWindowKeepScreenOn](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9)接口，将入参isKeepScreenOn属性设置为true来保证屏幕常亮。具体步骤如下：

1. 获取当前屏幕窗口对象。
2. 调用setWindowKeepScreenOn方法设置窗口保持屏幕常亮状态，默认不会常亮。

视频播放时设置屏幕常亮，视频暂停时取消屏幕常亮。示例代码如下：

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct SetScreenStatePage {
  private controller: VideoController = new VideoController();
  private previewUris: Resource = $r('app.media.startIcon');
  private innerResource: Resource = $r('app.media.videoTest');

  setScreenState(isKeepScreenOn: boolean) {
    // 获取当前窗口实例
    window.getLastWindow(this.getUIContext().getHostContext()).then((curWindow) => {
      // 设置屏幕是否常亮
      curWindow.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
        if (err.code) {
          console.error(`Failed to set the screen. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info(`Succeeded in setting the screen ${isKeepScreenOn}.`);
      });
    }).catch((err: string) => {
      console.error(`Failed to obtain the top window.. Cause code:: ${err}`);
    });
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Video({
        src: this.innerResource,
        previewUri: this.previewUris,
        controller: this.controller
      })
        .controls(true)
        .autoPlay(false)
        .objectFit(ImageFit.Contain)
        .onStart(() => {
          this.setScreenState(true);
          console.info('视频播放时设置屏幕常亮');
        })
        .onPause(() => {
          this.setScreenState(false);
          console.info('视频暂停时恢复系统息屏');
        });
    }
  }
}
```

运行结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/s3LOX_78S7e-K9uzts7bHQ/zh-cn_image_0000002795314303.png "点击放大")

**Q：为什么设置了屏幕常亮，但是在APP里依然会息屏？**

**A**：仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动熄屏功能。

**Q：录音场景下，setWindowKeepScreenOn接口会不会被系统管控？**

**A**：录音场景系统不会管控屏幕常亮，跟随业务设置。

**Q：自动化测试场景下如何设置屏幕常亮？**

**A**：可以通过hdc shell power-shell timeout命令设置屏幕常亮时间。测试前设置永不熄屏（需保持充电），测试后恢复默认熄屏时间（例如10分钟）：

```bash
# 测试前：设置永不熄屏（需保持充电）
hdc shell power-shell timeout -o 2147483647

# 测试后：恢复默认熄屏时间（例如10分钟）
hdc shell power-shell timeout -o 600000
```

**Q：是否可以通过系统设置实现屏幕常亮？**

**A**：系统设置中最长可设置10分钟的屏幕休眠时间，无法实现真正的屏幕常亮。如需保持屏幕常亮，需在代码中调用[setWindowKeepScreenOn](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9)方法，将isKeepScreenOn参数设置为true。
