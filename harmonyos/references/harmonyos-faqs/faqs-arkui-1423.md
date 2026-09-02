---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1423
title: 如何截取旋转后的图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何截取旋转后的图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:460bc5396cfc91efb3f78316042f5463f6b0f5cabd7beaa5334b559ed8228f0b
---

## 问题现象

当前界面的图片旋转后，截图组件通过componentSnapshot.get截取到的图片不是当前的图，是变化前的图片，那么该如何实现截图为当前图片？

## 背景知识

* [组件截图模块](../harmonyos-references/js-apis-arkui-componentsnapshot.md)可以对已加载的组件和未加载的组件进行截图。组件截图只能够截取组件大小的区域，超出的区域在截图中不会呈现；兄弟节点堆叠在组件区域内，截图时兄弟组件不会呈现；缩放、平移、旋转等图形变换属性只对被截图组件的子组件生效；对目标组件本身应用图形变换属性不生效，显示的还是图形变换前的效果。
* [componentSnapshot.get](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12-1)方法通过组件标识[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)对相应组件进行截图，并通过回调返回截图数据，id不同，返回的截图也会不同。

## 解决方案

组件截图componentSnapshot不支持旋转属性，因为旋转可能会存在超过父组件的行为。如果要截取带旋转属性的图片，需要给Image组件包裹一个父组件，截屏时截父组件。

```ts
Button('click to generate UI snapshot for solution')
  .onClick(() => {
    this.getUIContext().getComponentSnapshot().get('imageForSolution', (error: Error, pixmap: image.PixelMap) => {
      if (error) {
        return;
      }
      this.pixmapForSolution = pixmap;
    });
  }).margin(10);
```

## 常见FAQ

Q：如何对支持滚动的UI组件（如List组件、Scroll组件、Web组件）进行长截图？

A：使用控制器Scroller和WebviewController，并结合组件截图模块componentSnapshot实现长截图功能，详情可参考[长截图开发实践](../best-practices/bpta-long-snapshot-practice.md)。

Q：使用组件截图componentSnapshot时，与截图组件同区域不同层级的其他组件是否也会被截图？

A：只会对相关id的组件进行截图，组件上下层级不受影响。

Q：修改组件截图区域中状态变量后立刻截图，截图仍然是修改状态变量前的图片，如何获取修改状态变量后的截图？

A：使用[布局回调](../harmonyos-references/js-apis-arkui-inspector.md)，在布局回调方法中截图。

关键代码如下：

```ts
Button('click to generate UI snapshot for FAQ')
  .onClick(async () => {
    this.listener.on('draw', this.onDrawComplete);
    this.text = '你好';
  }).margin(10);
```

完整示例参考如下：

```ts
import { image } from '@kit.ImageKit';
import { inspector } from '@kit.ArkUI';

@Entry
@Component
struct SnapshotExample {
  @State pixmapForSolution: image.PixelMap | undefined = undefined;
  @State angle: number = 0;
  @State pixmapForFAQ: image.PixelMap | undefined = undefined;
  @State text: string = 'Hello World';
  listener: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('imageForFAQ');
  onDrawComplete: () => void = (): void => {
    this.getUIContext().getComponentSnapshot().get('imageForFAQ', (error: Error, pixmap: image.PixelMap) => {
      if (error) {
        return;
      }
      this.pixmapForFAQ = pixmap;
    }, { scale: 2, waitUntilRenderFinished: true });
  };

  build() {
    Column() {
      Row() {
        Image(this.pixmapForSolution)
          .width('45%').height(200)
          .border({ color: Color.Black, width: 2 })
          .margin(5);
        Row() {
          Image($r('app.media.startIcon'))
            .autoResize(true)
            .width('45%')
            .height(200)
            .margin(5)
            .rotate({ angle: this.angle })
            .onClick(() => {
              // 旋转180度
              this.angle = 180;
            });
        }
        .id('imageForSolution'); // 获取image父组件的组件id

      };

      Button('click to generate UI snapshot for solution')
        .onClick(() => {
          this.getUIContext().getComponentSnapshot().get('imageForSolution', (error: Error, pixmap: image.PixelMap) => {
            if (error) {
              return;
            }
            this.pixmapForSolution = pixmap;
          });
        }).margin(10);
      Row() {
        Image(this.pixmapForFAQ).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5);
        Text(this.text).id('imageForFAQ');
      };

      Button('click to generate UI snapshot for FAQ')
        .onClick(async () => {
          this.listener.on('draw', this.onDrawComplete);
          this.text = '你好';
        }).margin(10);
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center);
  }
}
```
