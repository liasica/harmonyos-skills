---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1256
title: Scroll容器嵌套RelativeContainer组件时无法滚动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Scroll容器嵌套RelativeContainer组件时无法滚动
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d9388bd8cfef81be02e0257db89c9c85123e82235ed6011e58e442a816ed30f6
---

## 问题现象

Scroll组件中嵌套RelativeContainer组件时，Scroll组件无法滚动。

问题示例代码如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
      data?.setWindowLayoutFullScreen(true); // 设置沉浸式布局，与知识内容无关仅为全屏展示效果
    });
  }

  build() {
    Scroll(this.scroller) {
      RelativeContainer() {
        Column({ space: 10 }) {
          Text('组件1')
            .fontColor(Color.White)
            .width('90%')
            .height('90%')
            .borderRadius(25)
            .textAlign(TextAlign.Center)
            .backgroundColor('#0a59f7');
          Text('组件2')
            .fontColor(Color.White)
            .width('90%')
            .height('90%')
            .borderRadius(25)
            .textAlign(TextAlign.Center)
            .backgroundColor('#0a59f7');
        }
        .width('100%');
      }
    }
    .width('100%')
    .height('100%');
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/swOAF5qES5efuvq5aTiBHQ/zh-cn_image_0000002628755406.png "点击放大")

## 背景知识

* [Scroll组件](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当Scroll子组件的布局尺寸超过Scroll组件的尺寸时，内容可以滚动。
* [RelativeContainer组件](../harmonyos-references/ts-container-relativecontainer.md)：相对布局组件，用于复杂场景中元素对齐的布局。

## 问题定位

RelativeContainer组件的默认高度是根据其父容器的高度确定。如果RelativeContainer组件没有设置具体的高度值，RelativeContainer组件会自动继承父组件的高度，而不是子组件高度。

由此可见，当Scroll组件的子组件是RelativeContainer组件，且RelativeContainer组件未设置高于Scroll组件的高度时，会违反Scroll组件的子组件总高度必须大于Scroll组件高度的滚动条件，导致无法滚动。

**说明** 

RelativeContainer组件的width属性、height属性参数设置"auto"时，表示RelativeContainer组件宽度和高度自适应子组件的宽度和高度。

## 分析结论

Scroll组件中嵌套RelativeContainer组件时，Scroll组件无法滚动的原因是：

RelativeContainer组件默认继承Scroll组件的高度，导致RelativeContainer组件高度无法超过Scroll组件高度，进而导致Scroll组件无法滚动。

## 修改建议

* 方案一：RelativeContainer组件height属性参数设置"auto"。

  RelativeContainer组件height属性参数设置"auto"时，需要保证RelativeContainer子组件的高度高于Scroll组件高度。

  **说明** 

  当width设置"auto"时，如果水平方向上子组件以容器作为锚点，则"auto"不会生效（即视为不设置width），也会导致无法滚动，垂直方向上同理。

  完整示例代码如下：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct OptionOne {
    scroller: Scroller = new Scroller();

    aboutToAppear(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
        data?.setWindowLayoutFullScreen(true); // 设置沉浸式布局，与知识内容无关仅为全屏展示效果
      });
    }

    build() {
      Scroll(this.scroller) {
        RelativeContainer() {
          Column({ space: 10 }) {
            Text('组件1')
              .width('90%')
              .height('90%')
              .borderRadius(25)
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5');
            Text('组件2')
              .width('90%')
              .height('90%')
              .borderRadius(25)
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5');
          }
          .width('100%');
        }
        .height('auto') // 自适应子组件高度
        .width('auto'); // 自适应子组件宽度
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* 方案二：[Flex组件](../harmonyos-references/ts-container-flex.md)、[Column组件](../harmonyos-references/ts-container-column.md)代替RelativeContainer组件。

  以Column组件为例，Column组件会自适应子组件高度。

  完整示例代码如下：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct OptionTwo {
    scroller: Scroller = new Scroller();

    aboutToAppear(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
        data?.setWindowLayoutFullScreen(true); // 设置沉浸式布局，与知识内容无关仅为全屏展示效果
      });
    }

    build() {
      // Column组件代替RelativeContainer组件
      Scroll(this.scroller) {
        Column({ space: 10 }) {
          Text('组件1')
            .width('90%')
            .height('90%')
            .borderRadius(25)
            .textAlign(TextAlign.Center)
            .backgroundColor('#f1f3f5');
          Text('组件2')
            .width('90%')
            .height('90%')
            .borderRadius(25)
            .textAlign(TextAlign.Center)
            .backgroundColor('#f1f3f5');
        }
        .width('100%');
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* 方案三：RelativeContainer组件嵌套Scroll组件。

  完整示例代码如下：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct OptionThree {
    scroller: Scroller = new Scroller();

    aboutToAppear(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => {
        data?.setWindowLayoutFullScreen(true); // 设置沉浸式布局，与知识内容无关仅为全屏展示效果
      });
    }

    build() {
      // RelativeContainer组件嵌套Scroll组件
      RelativeContainer() {
        Scroll(this.scroller) {
          Column({ space: 10 }) {
            Text('组件1')
              .width('90%')
              .height('90%')
              .borderRadius(25)
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5');
            Text('组件2')
              .width('90%')
              .height('90%')
              .borderRadius(25)
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5');
          }
          .width('100%');
        };
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

**说明** 

由于方案二、方案三会更改布局，推荐使用方案一。
