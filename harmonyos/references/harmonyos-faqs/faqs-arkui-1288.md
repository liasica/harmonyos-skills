---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1288
title: 动态文字填充
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 动态文字填充
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dd4cd8554cda7d943544e50a6d7891cbddda42d2e4198234150b9fc78d27a4f6
---

## 问题现象

如何实现点击文字填充“横线”，“横线”可换行。

## 背景知识

* [Span](../harmonyos-references/ts-basic-components-span.md)：作为[Text](../harmonyos-references/ts-basic-components-text.md)、[ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md)组件的子组件，用于显示行内文本的组件。
* [decoration](../harmonyos-references/ts-basic-components-span.md#decoration)：设置文本装饰线样式及其颜色。
* [@State](../harmonyos-guides/arkts-state.md)：被@State装饰的变量称为状态变量，使普通变量具备状态属性。当状态变量改变时，会触发其直接绑定的UI组件渲染更新。

## 解决方案

1. 使用Span组件作为横线内容容器，结合@State状态管理实现动态内容更新。
2. 通过点击事件触发数据填充，动态修改文本内容。
3. 利用decoration属性设置下划线效果。

```ts
import display from '@ohos.display';
import window from '@ohos.window';

export class DeviceScreen {
  /**
   * Get the device size.
   *
   * @returns promise of window.
   */
  public static getDeviceSize(context: Context): Promise<window.Window> {
    return window.getLastWindow(context);
  }

  /**
   * Get the screen width.
   *
   * @returns screen width.
   */
  public static getDeviceWidth(): number {
    let displayObject = display.getDefaultDisplaySync();
    let screenPixelWidth = displayObject.width;
    let screenDensityDPI = displayObject.densityDPI;
    return screenPixelWidth * (160 / screenDensityDPI);
  }

  /**
   * Get the screen height.
   *
   * @returns screen height.
   */
  public static getDeviceHeight(): number {
    let displayObject = display.getDefaultDisplaySync();
    let screenPixelHeight = displayObject.height;
    let screenDensityDPI = displayObject.densityDPI;
    return screenPixelHeight * (160 / screenDensityDPI);
  }

  public static getStatusHeight(): number {
    let topRectHeight = AppStorage.get<number>('topRectHeight') as number;
    return topRectHeight;
  }

  public static getNavigationHeight(): number {
    let bottomRectHeight = AppStorage.get<number>('bottomRectHeight') as number;
    return bottomRectHeight;
  }
}

@Entry
@Component
struct DynamicTextFill {
  @State options: string[] = ['儿', '往', '出', '林', '雨', '花', '细', '鱼', '东'];
  @State inputText: string = '';

  build() {
    Column() {
      Text() {
        Span('请从以下九个字中点选一句五言诗:')
        if (this.inputText) {
          Span(this.inputText).decoration({
            type: TextDecorationType.Underline, // 设置下划线样式
            color: Color.Black,
          })
        } else {
          Span('__________，')
        }
      }
      .fontSize(17)
      .fontColor('#333333')
      .fontWeight(FontWeight.Normal)
      .lineHeight(26)
      .margin({ left: 15, top: 10, right: 15 })

      Grid() {
        ForEach(this.options, (item: string) => {
          GridItem() {
            Column() {
              Text(item)
                .fontSize(17)
                .fontColor('#333333')
                .fontWeight(FontWeight.Bold)
            }
            .width('100%')
            .height('100%')
            .justifyContent(FlexAlign.Center)
            .backgroundColor(Color.White)
          }
          .aspectRatio(1)
          .onClick(() => {
            this.inputText += `${item}`;
          })
        }, (item: string, index?: number) => JSON.stringify(item) + index)
      }
      .width(DeviceScreen.getDeviceWidth() - 65 * 2)
      .columnsTemplate('1fr 1fr 1fr')
      .rowsGap(0.5)
      .columnsGap(0.5)
      .margin({ top: 60 })
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#F5F5F5')
  }
}
```
