---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-597
title: 如何绘制有图片超出弹窗边框的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何绘制有图片超出弹窗边框的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:820efac0de24bb994cc4d8bcda12000a28750262c1f6680b4ad8211722a6a164
---

## 问题现象

如何实现如下图所示这一类弹窗，使图片超出弹窗上边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/iCIgLn98Q9SKG8mzklAEmA/zh-cn_image_0000002658791975.png "点击放大")

## 背景知识

* 通过[UIContext.getPromptAction().openCustomDialog()](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口弹出的弹窗内容样式完全按照dialogContent中设置的样式显示。
* 通过[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小。使用[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)配合[Column](../harmonyos-references/ts-container-column.md)和[Row](../harmonyos-references/ts-container-row.md)容器自定义显示区域，为了展现页面内组件堆叠顺序，可通过[zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)属性设置。
* [Stack](../harmonyos-references/ts-container-stack.md)堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

对于使用@Builder自定义构建函数作为UI内容的弹窗来说，都有一种通用的方法设置上述效果。基本思路是：将整个弹窗UI内容的根容器组件设为透明背景，实际显示可见UI内容的容器作为子组件放置这个透明背景的父容器中，与图像堆叠而成。图像的一部分显示在有可见UI内容的容器上，一部分显示在透明背景上。

这种堆叠布局可以采用Stack堆叠布局实现，也可以使用zIndex设置显示层级，同时margin控制布局上移的方式实现。以下分别以openCustomDialog全局自定义弹窗和bindSheet半模态弹窗两种弹窗为例，分别展示两种方法的具体实现。

* 场景一：openCustomDialog全局自定义弹窗使用Stack布局实现图片超出弹窗边框效果。

  弹窗的核心实现代码如下：

  ```ts
  @Builder
  function customDialogBuilder(close: () => void) {
    Stack() {
      Column() {
        Row() {
          SymbolGlyph($r('sys.symbol.xmark'))
            .onClick(() => {
              close();
            })
        }
        .width('100%')
        .height(20)
        .justifyContent(FlexAlign.End)

        Text('Test').fontSize(24).margin({ top: 30, bottom: 10 })

        Button('关闭弹窗').onClick(() => {
          close();
        })
      }
      .borderRadius(8)
      .padding(10)
      .margin({ top: 40 })  // 留出图片占位
      .backgroundColor(Color.White)
      .width('100%')
      .height('auto')

      Image($r('app.media.startIcon'))
        .width(80)
    }
    .alignContent(Alignment.Top)
    .margin({ right: 20, left: 20 })
    .backgroundColor(Color.Transparent)
  }
  ```

  使用UIContext.getPromptAction().openCustomDialog()调用弹窗的示例如下：

  ```ts
  @Builder
  function customDialogBuilder(close: () => void) {
    Stack() {
      Column() {
        Row() {
          SymbolGlyph($r('sys.symbol.xmark'))
            .onClick(() => {
              close();
            })
        }
        .width('100%')
        .height(20)
        .justifyContent(FlexAlign.End)

        Text('Test').fontSize(24).margin({ top: 30, bottom: 10 })

        Button('关闭弹窗').onClick(() => {
          close();
        })
      }
      .borderRadius(8)
      .padding(10)
      .margin({ top: 40 })  // 留出图片占位
      .backgroundColor(Color.White)
      .width('100%')
      .height('auto')

      Image($r('app.media.startIcon'))
        .width(80)
    }
    .alignContent(Alignment.Top)
    .margin({ right: 20, left: 20 })
    .backgroundColor(Color.Transparent)
  }

  @Component
  struct Scene1 {
    build() {
      Button("场景一")
        .onClick(() => {
          let uiContext = this.getUIContext();
          let contentNode = new ComponentContent(uiContext, wrapBuilder(customDialogBuilder), () => {
            uiContext.getPromptAction().closeCustomDialog(contentNode);
          });
          uiContext.getPromptAction().openCustomDialog(contentNode);
        })
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/DRa3oxu0TAij6aZzcXyF5w/zh-cn_image_0000002628552600.png "点击放大")

* 场景二：bindSheet半模态弹窗使用zIndex+margin实现图片超出弹窗边框效果。
  1. 设置bindSheet背景色为透明，隐藏bindSheet自带的关闭按钮。

     ```ts
     .bindSheet($$this.isShow, customBindSheet(), {
       height: this.sheetHeight,
       // 设置bindSheet的背景色为透明色
       backgroundColor: '#00000000',
       // 隐藏bindSheet自带的关闭按钮
       showClose: false,
       radius: LengthMetrics.vp(0),
     })
     ```
  2. 通过.zIndex(999)设置Image组件的显示层级为最高。

     ```ts
     Image($r('app.media.startIcon'))
       .width(80)
       .clip(false)
       .margin({ left: 10 })
         // 设置图片的层级为最高，显示在最上层
       .zIndex(999)
     ```
  3. 通过.zIndex(1)设置容器Row的显示层级最低，并使用.margin({ top: -40 })设置Row向上偏移。

     ```ts
     Row() {
       Blank()
       Image($r('app.media.startIcon'))
         .height(25)
         .width(25)
         .margin({ top: 10, right: 10 })
     }
     // 设置图片的层级为最低，显示在图片下层
     .zIndex(1)
     // 设置容器向上偏移
     .margin({ top: -40 })
     ```

  通过bindSheet绑定弹窗的示例如下：

  ```ts
  @Builder
  export function customBindSheet() {
    Column() {
      Image($r('app.media.startIcon'))
        .width(80)
        .clip(false)
        .margin({ left: 10 })
          // 设置图片的层级为最高，显示在最上层
        .zIndex(999)
      Row() {
        Blank()
        Image($r('app.media.startIcon'))
          .height(25)
          .width(25)
          .margin({ top: 10, right: 10 })
      }
      // 设置图片的层级为最低，显示在图片下层
      .zIndex(1)
      // 设置容器向上偏移
      .margin({ top: -40 })
      .borderRadius({ topLeft: 20, topRight: 20 })
      .width('100%')
      .height(380)
      .backgroundColor(Color.White)
      .alignItems(VerticalAlign.Top)
      .justifyContent(FlexAlign.SpaceBetween)
    }
    .width('100%')
    .height('100%')
    // 设置column的背景色为透明色
    .backgroundColor(Color.Transparent)
    .justifyContent(FlexAlign.Start)
    .alignItems(HorizontalAlign.Start)
  }

  @Component
  struct Scene2 {
    @State isShow: boolean = false;
    sheetHeight: number = 400;

    build() {
      Button("场景二")
        .onClick(() => {
          this.isShow = true;
        })
        .bindSheet($$this.isShow, customBindSheet(), {
          height: this.sheetHeight,
          // 设置bindSheet的背景色为透明色
          backgroundColor: '#00000000',
          // 隐藏bindSheet自带的关闭按钮
          showClose: false,
          radius: LengthMetrics.vp(0),
        })
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/WO6NW-upTgO1iNJ37Dwdmg/zh-cn_image_0000002658911915.png "点击放大")

两种场景的完整示例代码如下：

```ts
import { ComponentContent, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct DialogOverflow {
  build() {
    Column({ space: 20 }) {
      Scene1()
      Scene2()
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}

@Builder
function customDialogBuilder(close: () => void) {
  Stack() {
    Column() {
      Row() {
        SymbolGlyph($r('sys.symbol.xmark'))
          .onClick(() => {
            close();
          })
      }
      .width('100%')
      .height(20)
      .justifyContent(FlexAlign.End)

      Text('Test').fontSize(24).margin({ top: 30, bottom: 10 })

      Button('关闭弹窗').onClick(() => {
        close();
      })
    }
    .borderRadius(8)
    .padding(10)
    .margin({ top: 40 })  // 留出图片占位
    .backgroundColor(Color.White)
    .width('100%')
    .height('auto')

    Image($r('app.media.startIcon'))
      .width(80)
  }
  .alignContent(Alignment.Top)
  .margin({ right: 20, left: 20 })
  .backgroundColor(Color.Transparent)
}

@Component
struct Scene1 {
  build() {
    Button("场景一")
      .onClick(() => {
        let uiContext = this.getUIContext();
        let contentNode = new ComponentContent(uiContext, wrapBuilder(customDialogBuilder), () => {
          uiContext.getPromptAction().closeCustomDialog(contentNode);
        });
        uiContext.getPromptAction().openCustomDialog(contentNode);
      })
  }
}

@Builder
export function customBindSheet() {
  Column() {
    Image($r('app.media.startIcon'))
      .width(80)
      .clip(false)
      .margin({ left: 10 })
        // 设置图片的层级为最高，显示在最上层
      .zIndex(999)
    Row() {
      Blank()
      Image($r('app.media.startIcon'))
        .height(25)
        .width(25)
        .margin({ top: 10, right: 10 })
    }
    // 设置图片的层级为最低，显示在图片下层
    .zIndex(1)
    // 设置容器向上偏移
    .margin({ top: -40 })
    .borderRadius({ topLeft: 20, topRight: 20 })
    .width('100%')
    .height(380)
    .backgroundColor(Color.White)
    .alignItems(VerticalAlign.Top)
    .justifyContent(FlexAlign.SpaceBetween)
  }
  .width('100%')
  .height('100%')
  // 设置column的背景色为透明色
  .backgroundColor(Color.Transparent)
  .justifyContent(FlexAlign.Start)
  .alignItems(HorizontalAlign.Start)
}

@Component
struct Scene2 {
  @State isShow: boolean = false;
  sheetHeight: number = 400;

  build() {
    Button("场景二")
      .onClick(() => {
        this.isShow = true;
      })
      .bindSheet($$this.isShow, customBindSheet(), {
        height: this.sheetHeight,
        // 设置bindSheet的背景色为透明色
        backgroundColor: '#00000000',
        // 隐藏bindSheet自带的关闭按钮
        showClose: false,
        radius: LengthMetrics.vp(0),
      })
  }
}
```
