---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1630
title: 如何实现沉浸式效果与List列表滑动联动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现沉浸式效果与List列表滑动联动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:18976ea466885ad79e7c3df15a29210d22fe6ddcefd3ffd63bffad048ced9aa0
---

## 问题现象

如何实现List列表的滑动联动页面沉浸式效果？在进入页面时，页面的状态栏处于沉浸式状态，向上滑动时逐渐修改透明度将状态栏的沉浸式效果关闭。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/hL3Gjp_WRkiOguwFAKHKaw/zh-cn_image_0000002628617582.gif "点击放大")

## 背景知识

* [沉浸式模式](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)通常指让应用的界面更加专注于内容，不希望用户被无关元素干扰。在移动端应用中，全屏窗口元素包括状态栏、应用界面和导航栏，沉浸式页面开发常通过将应用页面延伸到状态栏和导航栏的方式，来达到以下目的：使页面和避让区域的色调统一，为用户提供更好的视觉体验。最大程度利用屏幕可视区域，使页面获得更大的布局空间。提供完全沉浸的体验，让用户沉浸其中，不被其他事物所干扰。
* [onReachStart](../harmonyos-references/ts-container-list.md#onreachstart)方法在列表到达起始位置时触发。List初始化时如果initialIndex为0会触发一次，List滚动到起始位置时触发一次。
* [onWillScroll](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)方法为滚动事件回调，滚动组件滚动前触发。可以通过该回调返回值指定滚动组件将要滚动的偏移。

## 解决方案

1. 设置组件的[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性，扩展组件的安全区域到状态栏和导航栏，从而实现沉浸式。
2. 渐变效果的实现：onReachStart事件在滚动开始时，将opacityNum设为0，使背景透明。onWillScroll事件在滚动过程中，更新scrollSum并计算opacityNum。opacityNum的值为scrollSum/200，确保其在0到1之间。当scrollSum超过200时，opacityNum保持在1，背景颜色不再变化。

示例代码如下：

```ts
import display from '@ohos.display';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct TabTopScroll {
  arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
  @State opacityNum: number = 0;
  scrollSum: number = 0;
  @State safeTopHeight: number = 0;
  uiContext = this.getUIContext();

  aboutToAppear(): void {
    let type = window.AvoidAreaType.TYPE_SYSTEM;
    try {
      window.getLastWindow(this.uiContext?.getHostContext(), (err: BusinessError, windowClass) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        let avoidArea = windowClass.getWindowAvoidArea(type);
        let screenInfo = display.getDefaultDisplaySync();
        this.safeTopHeight = avoidArea.topRect.height / screenInfo.densityPixels;
      });
    } catch (exception) {
      console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  build() {
    Column() {
      Flex() {
      }
      .padding({
        left: 10,
        right: 10,
        bottom: this.safeTopHeight,
        top: 10
      })
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .backgroundColor(`rgba(70,130,180,${this.opacityNum >= 1 ? 1 : this.opacityNum})`)
      .position({ x: 0, y: 0 })
      .height(66 + this.safeTopHeight)
      .zIndex(99);

      Column() {
        this.listControllerBuilder();
      }
      .translate({
        y: -(this.safeTopHeight + 5)
      })
      .width('100%')
      .backgroundColor('#F1F3F5')
      .height(`calc(100% + ${this.safeTopHeight + 5}vp)`);
    }
    .width('100%')
    .height('100%');
  }

  @Builder
  listControllerBuilder() {
    List({ space: 20, initialIndex: 0 }) {
      ListItem() {
        Image($r('app.media.mountain')) // 此处'mountain'仅作示例，请开发者自行替换。
          .height(300)
          .width('100%');
      };

      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text('' + item)
            .margin({ left: '5%' })
            .width('90%')
            .height(100)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF);
        }
        .align(Alignment.Center);
      }, (item: string) => item);
    }
    .onReachStart(() => {
      this.opacityNum = 0;
    })
    .onWillScroll((scrollOffset: number) => {
      this.scrollSum += scrollOffset;
      this.opacityNum = this.scrollSum / 200;
    })
    .listDirection(Axis.Vertical) // 排列方向
    .scrollBar(BarState.Off)
    .friction(0.6)
    .chainAnimation(false)
    .edgeEffect(EdgeEffect.Spring) // 配合EdgeEffect.Spring可以触发list回弹效果
    .nestedScroll({
      scrollForward: NestedScrollMode.PARENT_FIRST,
      scrollBackward: NestedScrollMode.SELF_FIRST
    })
    .width('100%');
  }
}
```
