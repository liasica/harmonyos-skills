---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-9
title: 平板切换自由多窗模式后，页面横向滑动失效
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板切换自由多窗模式后，页面横向滑动失效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f47a914c6de440bc8902f317802ce8979ee51caad944eab2ad152805ae5e80b3
---

## 问题现象

页面在全屏模式下左滑到下一个页面后，切换自由多窗模式，此时页面无法右滑回到上一页。

## 背景知识

* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [窗口模式](../best-practices/bpta-multi-device-window-mode.md)：应用窗口模式指应用主窗口启动时的显示方式。HarmonyOS目前支持全屏、分屏、自由悬浮窗口三种应用窗口模式。在应用窗口模式变化时，通常伴随窗口尺寸变化，以及页面布局或功能差异。

## 问题定位

1. 建议检查代码中PanGesture滑动手势事件中onActionUpdate和onActionEnd方法中设定的偏移量阈值是否是固定的。
2. 如果设定为固定值，检查应用有没有通过on('windowSizeChange')方法实现对窗口尺寸大小变化的监听。在窗口变化时无法及时动态改变滑动阈值，会导致自由多窗情况下滑动不到设定的距离，无法完成滑动返回上一页的操作。

## 分析结论

应用没有通过on('windowSizeChange')方法实现对窗口尺寸大小变化的监听，因此在动态切换到自由多窗后，PanGesture手势事件的判定值没有及时更新到自由多窗下的尺寸，导致滑动距离无法达到判定值，无法滑动切换页面。

## 修改建议

通过on('windowSizeChange')方法实现对窗口尺寸大小变化的监听，并在不同窗口尺寸下，设置不同的滑动距离。

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  // 初始化参数，这里会初始化为AppStorage中存储的值
  @State winWidth: number | undefined = 0;
  @State winHeight: number | undefined = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.All });

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
    this.winWidth = rect.width;
    this.winHeight = rect.height;
  }

  aboutToAppear() {
    let windowClass: window.Window = this.getWindow();
    // 监听窗口尺寸的变化
    windowClass?.on('windowSizeChange', (data) => {
      this.winWidth = data.width;
      this.winHeight = data.height;
    });
  }

  build() {
    Column() {
      Column() {
        // 实际开发中结合两者大小变化，动态调整滑动距离的触发条件
        Text(`滑动距离动态变化 X:${this.offsetX}  Y:${this.offsetY}`);
        Text(`窗口尺寸大小width:${this.winWidth},height:${this.winHeight}`);
      }
      .width('100%')
      .height('100%')
      .padding(20)
      .margin(50)
      // 手指滑动触发该手势事件
      .gesture(
        PanGesture(this.panOption)
          .onActionUpdate((event: GestureEvent) => {
            if (event) {
              this.offsetX = event.offsetX;
              this.offsetY = event.offsetY;
            }
          })
      );
    };
  }
}
```
