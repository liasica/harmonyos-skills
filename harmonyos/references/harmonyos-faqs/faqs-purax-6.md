---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-6
title: 折叠屏切换展开态，视频弹幕只显示半屏
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 折叠屏切换展开态，视频弹幕只显示半屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5c3f983e6f39922db94e09636760552b823326d1129824fdbbe040e1a43e2abb
---

## 问题现象

视频应用从折叠屏折叠态切换到展开态后，视频弹幕显示区域未动态切换，依然只显示一小块。

## 背景知识

* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)开启窗口尺寸变化的监听。仅在主线程调用。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。

## 问题定位

通过查看页面布局及代码，发现视频弹幕显示区域通过Canvas绘制，建议检查代码中是否使用了on('windowSizeChange')监听窗口尺寸的变化，并在变化的回调中，动态修改Canvas弹幕显示区域的尺寸，来适配折叠态与展开态的窗口尺寸。若Canvas画布的尺寸固定，未随折叠状态变化动态变化，会导致切换到展开态时依旧展示的折叠态的尺寸。

## 分析结论

应用未使用on('windowSizeChange')监听折叠屏的折叠态与展开态时的窗口尺寸变化，将Canvas画布显示尺寸固定，此时从折叠态切换到展开态时，画布尺寸依旧是折叠态时的大小，导致视频弹幕看起来就只显示半屏区域。

## 修改建议

可以使用on('windowSizeChange')监听折叠状态变化，根据新窗口尺寸调整Canvas画布尺寸，如下以Canvas占屏幕一半为例：

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct CanvasExample {
  @State canvasWidth: number = 0;
  @State canvasHeight: number = 0;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  getWindow(): window.Window {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowStage = context.windowStage;
    let windowClass = windowStage.getMainWindowSync();
    return windowClass;
  }

  onPageShow(): void {
    let windowClass: window.Window = this.getWindow();
    let properties = windowClass.getWindowProperties();
    let rect = properties.windowRect;
    this.canvasWidth = this.getUIContext().px2vp(rect.width);
    this.canvasHeight = this.getUIContext().px2vp(rect.height);
  }

  // 初始化折叠检测
  aboutToAppear() {
    let windowClass: window.Window = this.getWindow();
    // 监听窗口尺寸的变化
    windowClass.on('windowSizeChange', (data) => {
      this.canvasWidth = this.getUIContext().px2vp(data.width);
      this.canvasHeight = this.getUIContext().px2vp(data.height);
    });
  }

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffff')
        .onReady(() => {
          this.context.fillStyle = '#D1D1D6';
          this.context.fillRect(0, 30, this.canvasWidth * 0.5, this.canvasHeight * 0.5);
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
