---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1372
title: 如何实现一个自定义高度的底部弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现一个自定义高度的底部弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c2ada7b7544ccb0826252b3faa41323ed2909b256f9bce0471106595558116c4
---

## 问题现象

需要实现的底部弹窗可以设置一个最大高度。同时，实现的底部弹窗需要从下往上出现。

* 如果弹窗内部视图的高度超过了这个最大高度，弹窗内部的视图就以这个自定义最大高度进行滚动展示；
* 如果弹窗内部视图的高度没有超过这个最大高度，那么弹窗内部视图就完全展示；

## 背景知识

组件的[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)属性用于设置约束尺寸，组件布局时，进行尺寸范围限制。

对于组件的显示方式，转场主要通过[transition](../harmonyos-references/ts-transition-animation-component.md)属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

## 解决方案

首先，通过使用容器组件的constraintSize属性对视图进行高度限制，constraintSize的优先级高于Width和Height，constraintSize里面的maxHeight小于Height时，就会滚动展示。接着，实现弹窗从底部向上显示，通过设置组件transition属性的转场参数。

示例代码如下：

```screen
@CustomDialog
struct CustomDialogExample {
  // 最大可滚动区域高度
  maxScrollHeight: number = 70;
  // 视图是否显示，用于底部弹窗出现与消失时的动效处理
  @Link showFlag: Visibility;
  controller: CustomDialogController;
  scroller: Scroller = new Scroller;
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

  build() {
    Column({ space: 5 }) {
      RelativeContainer() {
        Text('标题')
          .fontSize(17)
          .fontColor(Color.Black)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
            center: { anchor: '__container__', align: VerticalAlign.Center }
          });
      }
      .width('100%')
      .height(48);

      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(50)
              .backgroundColor(0xFFFFFF)
              .borderColor(Color.Black)
              .fontSize(16)
              .textAlign(TextAlign.Center);
            Divider()
              .vertical(false)
              .strokeWidth(0.5)
              .width('60%');
          }, (item: string) => item);
        }.width('100%');
      }
      .edgeEffect(EdgeEffect.Spring)
      .scrollSnap({
        snapAlign: ScrollSnapAlign.START,
        snapPagination: 400,
        enableSnapToStart: true,
        enableSnapToEnd: true
      })
      // 使用constraintSize方法可以设置约束尺寸，组件布局时，进行尺寸范围限制
      .constraintSize({ maxHeight: this.maxScrollHeight + '%' });

    }
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#f5f5f5')
    .borderRadius({
      topLeft: '16',
      topRight: '16'
    })
    .visibility(this.showFlag)
    .transition(TransitionEffect.OPACITY.animation({ duration: 200 })  // 弹窗出现与消失的动效
      .combine(TransitionEffect.translate({ y: 100 })),
      (transitionIn: boolean) => {
        if (!transitionIn) {
          this.controller.close();
        }
      }
    );
  }
}

@Entry
@Component
struct CustomDialogDemo {
  // 最大可滚动区域高度
  @State maxScrollHeight: number = 70;
  @State settingDialogShowFlag: Visibility = Visibility.Visible;
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({
      maxScrollHeight: this.maxScrollHeight,
      showFlag: this.settingDialogShowFlag
    }),
    alignment: DialogAlignment.Bottom,
    width: '100%',
    // customStyle需要设置为true，否则底部弹窗出现的动效会有问题
    customStyle: true,
    autoCancel: true,
    // 修改点击弹窗外部区域和返回操作时弹窗消失的方式，这里的处理会有一个动效。否则弹窗会以默认的方式消失
    onWillDismiss: () => {
      this.settingDialogShowFlag = Visibility.Hidden;
    }
  });

  build() {
    Column() {
      Row({ space: 5 }) {
        Row() {
          Button('减10')
            .onClick(() => {
              this.maxScrollHeight -= 10;
            });
        };

        Row() {
          Text(this.maxScrollHeight + '%')
            .width('40%')
            .height(45)
            .textAlign(TextAlign.Center)
            .backgroundColor('#f5f5f5');
        };

        Row() {
          Button('加10')
            .onClick(() => {
              this.maxScrollHeight += 10;
            });
        };
      };

      Button('打开底部弹窗')
        .onClick(() => {
          this.settingDialogShowFlag = Visibility.Visible;
          this.dialogController.open();
        });
    }.justifyContent(FlexAlign.Center).width('100%').height('100%');
  }
}
```
