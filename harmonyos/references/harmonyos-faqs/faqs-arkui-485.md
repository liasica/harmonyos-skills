---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-485
title: 如何判断组件遮挡情况，并主动隐藏被遮挡的组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何判断组件遮挡情况，并主动隐藏被遮挡的组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2f03da81c9ae57efce2c62efb20b6fea76c24267a3087afe22553b9f73bbd187
---

一般情况下，使用[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)即可。 在一些特殊场景下，例如使用了层叠布局，或者在线性布局中使用位置使得并排的兄弟组件之间产生了遮挡，由于onVisibleAreaChange的局限性，此种情况需要自己手动计算遮挡关系。推荐使用[UIInspector](../harmonyos-references/arkts-apis-uicontext-uiinspector.md)注册监听回调、[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)的getPositionToWindowWithTransform、getMeasuredSize获取组件的位置和宽高信息。

场景1：页面的元素遮挡关系后续不再发生变化，可以在页面布局时判断遮挡关系，可以监听UIInspector的layout回调，避免频繁回调消耗性能。

```ts
import { inspector, UIInspector } from '@kit.ArkUI';

@Entry
@Component
struct ComponentHide {
  uiInspector: UIInspector = this.getUIContext().getUIInspector();
  listener: inspector.ComponentObserver = this.uiInspector.createComponentObserver('inspectTarget');
  @State x: number = 170;
  @State button1Visibility: Visibility = Visibility.Visible;

  aboutToAppear(): void {
    let shouldShow: () => void = (): void => {
      let button1Info = this.getUIContext().getFrameNodeById('button1')?.getPositionToWindowWithTransform(); // vp
      let button1Size = this.getUIContext().getFrameNodeById('button1')?.getMeasuredSize(); // px
      let button1TopLeftX = this.getUIContext().vp2px(button1Info?.x); // The x-coordinate of the upper left corner of button1, with the unit of px
      let button1TopLeftY = this.getUIContext().vp2px(button1Info?.y); // The y-coordinate of the upper left corner of button1, with the unit of px
      let button1BottomRightX = button1TopLeftX + (button1Size?.width ?? 0); // The x-coordinate at the lower right corner of button1, with the unit of px
      let button1BottomRightY = button1TopLeftY + (button1Size?.height ?? 0); // The y-coordinate of the lower right corner of button1, with the unit of px

      let button2Info = this.getUIContext().getFrameNodeById('button2')?.getPositionToWindowWithTransform(); // vp
      let button2Size = this.getUIContext().getFrameNodeById('button2')?.getMeasuredSize(); // px
      let button2TopLeftX = this.getUIContext().vp2px(button2Info?.x); // The x-coordinate of the upper left corner of button2, with the unit of px
      let button2TopLeftY = this.getUIContext().vp2px(button2Info?.y); // The y-coordinate of the upper left corner of button2, with the unit of px
      let button2BottomRightX = button2TopLeftX + (button2Size?.width ?? 0); // The x-coordinate at the lower right corner of button2, with the unit being px
      let button2BottomRightY = button2TopLeftY + (button2Size?.height ?? 0); // The y-coordinate of the lower right corner of button2, with the unit of px

      let xOverlap = (button1TopLeftX < button2BottomRightX) && (button2TopLeftX < button1BottomRightX);
      let yOverlap = (button1TopLeftY < button2BottomRightY) && (button2TopLeftY < button1BottomRightY);
      if (xOverlap && yOverlap) {
        this.button1Visibility = Visibility.Hidden;
      } else {
        this.button1Visibility = Visibility.Visible;
      }
      this.listener.on('layout', shouldShow);
    }
  }

  build() {
    Column() {
      Column() {
        Button('button1')
          .position({ x: 200, y: 200 })
          .id('button1')
          .visibility(this.button1Visibility)
      }

      Column() {
        Button('button2')
          .position({ x: this.x, y: 200 })
          .onClick(() => {
            this.x = 200 - this.x; // If the component position changes, the layout will not be reconfigured and the registered shouldShow callback will not be called
          })
          .id('button2')
      }
    }
    .id('inspectTarget')
  }
}
```

场景2：页面的元素遮挡关系后续会发生变化，可以在页面绘制时判断遮挡关系，可以监听UIInspector的draw回调，会频繁回调。

```screen
import { inspector, UIInspector } from '@kit.ArkUI';

@Entry
@Component
struct ComponentHide {
  uiInspector: UIInspector = this.getUIContext().getUIInspector();
  listener: inspector.ComponentObserver = this.uiInspector.createComponentObserver('button2');
  @State x: number = 170;
  @State button1Visibility: Visibility = Visibility.Visible;

  aboutToAppear(): void {
    let shouldShow: () => void = (): void => {
      let button1Info = this.getUIContext().getFrameNodeById('button1')?.getPositionToWindowWithTransform(); // vp
      let button1Size = this.getUIContext().getFrameNodeById('button1')?.getMeasuredSize(); // px
      let button1TopLeftX = this.getUIContext().vp2px(button1Info?.x); // The x-coordinate of the upper left corner of button1, with the unit of px
      let button1TopLeftY = this.getUIContext().vp2px(button1Info?.y); // The y-coordinate of the upper left corner of button1, with the unit of px
      let button1BottomRightX = button1TopLeftX + (button1Size?.width ?? 0); // The x-coordinate at the lower right corner of button1, with the unit of px
      let button1BottomRightY = button1TopLeftY + (button1Size?.height ?? 0); // The y-coordinate of the lower right corner of button1, with the unit of px

      let button2Info = this.getUIContext().getFrameNodeById('button2')?.getPositionToWindowWithTransform(); // vp
      let button2Size = this.getUIContext().getFrameNodeById('button2')?.getMeasuredSize(); // px
      let button2TopLeftX = this.getUIContext().vp2px(button2Info?.x); // The x-coordinate of the upper left corner of button2, with the unit of px
      let button2TopLeftY = this.getUIContext().vp2px(button2Info?.y); // The y-coordinate of the upper left corner of button2, with the unit of px
      let button2BottomRightX = button2TopLeftX + (button2Size?.width ?? 0); // The x-coordinate at the lower right corner of button2, with the unit being px
      let button2BottomRightY = button2TopLeftY + (button2Size?.height ?? 0); // The y-coordinate of the lower right corner of button2, with the unit of px

      let xOverlap = (button1TopLeftX < button2BottomRightX) && (button2TopLeftX < button1BottomRightX);
      let yOverlap = (button1TopLeftY < button2BottomRightY) && (button2TopLeftY < button1BottomRightY);
      if (xOverlap && yOverlap) {
        this.button1Visibility = Visibility.Hidden;
      } else {
        this.button1Visibility = Visibility.Visible;
      }
      this.listener.on('draw', shouldShow); // The listener callbacks after the drawing is completed, with frequent calls, poor performance and high universality
    }
  }

  build() {
    Column() {
      Column() {
        Button('button1')
          .position({ x: 200, y: 200 })
          .id('button1')
          .visibility(this.button1Visibility)
      }

      Column() {
        Button('button2')
          .position({ x: this.x, y: 200 })
          .onClick(() => {
            this.x = 200 - this.x; // If the component position changes, the layout will not be reconfigured and the registered shouldShow callback will not be called
          })
          .id('button2')
      }
    }
    .id('inspectTarget')
  }
}
```
