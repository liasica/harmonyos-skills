---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1409
title: Text组件字符超过特定长度时，超出部分如何隐藏与显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Text组件字符超过特定长度时，超出部分如何隐藏与显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fe76ed6845118402cd26b64c920bf5587e67916ea7f828bda2f7293b9d70b854
---

## 问题现象

在Text中显示文本时，如果文本超过一定长度，通常会有超出部分隐藏与显示的需求，例如：当最多显示的行数为2，组件宽度比例为0.4时，该如何实现？

## 背景知识

* [measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)方法能够根据文本信息计算文本宽度。
* [getAllDisplays](../harmonyos-references/js-apis-display.md#displaygetalldisplays9)方法能够获取display对象，display对象的width属性为屏幕的宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/r1xThnd5Q-SCmDhTNqZpnw/zh-cn_image_0000002658842531.png "点击放大")

## 解决方案

1. 首先设定的文本长度计算方式：设定文本长度 = 屏幕宽度 \* 最大行数 \* 组件宽度比例。屏幕宽度可以使用[getAllDisplays](../harmonyos-references/js-apis-display.md#displaygetalldisplays9)获取。
2. 然后使用[measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)方法测量实际文本宽度，比较“设定文本长度”与“实际文本宽度”进行大小比较，判断是否需要隐藏。
3. 当需要隐藏时，只展示“设定长度”的文本内容，超出部分显示为“...”。当点击“…”时将该文本变为“…收起”，显示隐藏部分内容。

完整示例参考如下：

```ts
import { MeasureUtils } from '@kit.ArkUI';
import curves from '@ohos.curves';
import { BusinessError } from '@ohos.base';
import display from '@ohos.display';

@Entry
@Component
struct Index {
  // 长文本
  longMessage: string = '走在繁华的城市街头，明空感到无比紧张。他的心跳如雷鼓般擂动着胸膛，使得身上的伪装仿佛随时都要被揭开。然而，他仍然保持着冷静，凭借着过人的胆识与智慧，成功地躲过了敌人的层层封锁。\n' +
    '\n' +
    '　　最终，明空来到了敌对帮派的老巢。此时此刻，那里的守卫正沉浸在欢庆的氛围中，丝毫没有察觉到即将来临的危机。明空深吸一口气，压抑住内心的激动，悄然潜入了这座古老的建筑。';
  // 最大显示行数
  @State lines: number = 2;
  // 长文本状态（展开 or 收起）
  @State collapseText: string = '...';
  // 屏幕宽度（单位px）
  screenWidth: number = 0;
  // 是否需要显示"展开"字样（注：当文本长度较短时就不需要“展开”）
  @State isExpanded: boolean = false;
  uiContext: UIContext = this.getUIContext();
  uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  // 测量文本宽度（单位px）
  textWidth: number = this.uiContextMeasure.measureText({
    textContent: this.longMessage,
    fontSize: 20
  });
  // 获取当前所有的display对象
  promise: Promise<Array<display.Display>> = display.getAllDisplays();

  aboutToAppear() {
    console.info(`文本宽度为：${this.textWidth}`);
    this.promise.then((data: Array<display.Display>) => {
      console.info(`所有的屏幕信息：${JSON.stringify(data)}`);
      // 单位为像素
      this.screenWidth = data[0]["width"];
      // 屏幕宽度 * 最大行数 * 组件宽度比例 和 文字测量宽度
      this.isExpanded = this.screenWidth * this.lines * 0.4 <= this.textWidth;
    }).catch((err: BusinessError) => {
      console.error(`Failed to obtain all the display objects. Code: ${JSON.stringify(err)}`);
    });
  }

  build() {
    Row() {
      Column() {
        if (this.isExpanded) {
          Stack({ alignContent: Alignment.BottomEnd }) {
            Text(this.longMessage)
              .fontSize(20)
              .fontColor(Color.Black)
              .maxLines(this.lines)
              .width("40%")
            Row() {
              Text(this.collapseText)
                .fontSize(20)
                .backgroundColor(Color.White)
            }
            .justifyContent(FlexAlign.End)
            .onClick(() => {
              if (this.collapseText == '...') {
                this.collapseText = '...收起';
                // 展开动画
                this.uiContext.animateTo({
                  duration: 150,
                  curve: curves.springMotion(0.5, 0.8),
                }, () => {
                  this.lines = -1; // 使得设置的最大行属性无效
                });
              } else {
                this.collapseText = '...';
                // 收起动画
                this.uiContext.animateTo(
                  {
                    duration: 100,
                    curve: Curve.Friction,
                  }, () => {
                  this.lines = 2; // 只显示2行
                });
              }
            })
          }
        }
        else {
          Text(this.longMessage)
            .fontSize(20)
            .fontColor(Color.Black)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 常见FAQ

Q：如何设置文字超出宽度后继续显示，不要滚动？

A：只使用textOverflow属性不能实现这种效果，可以使用Row嵌套Text，再动态设置文字宽度来实现类似效果。

```ts
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextDemo {
  textString: string = '我是超长文本，超出的部分显示。I am an extra long text';
  @State textWidth: number = 0;
  uiContext: UIContext = this.getUIContext();
  uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: number = 14;

  aboutToAppear(): void {
    // 计算文字宽度
    this.textWidth = this.uiContextMeasure.measureText({
      textContent: this.textString,
      fontSize: this.textSize
    });
  }

  build() {
    Column() {
      Row() {
        Text(this.textString)
          .fontSize(this.textSize)
          .maxLines(1)
          .width(this.textWidth+'px')
          .backgroundColor(Color.Pink)
      }
      .width(250)
      .border({ width: 1 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Start)
  }
}
```
