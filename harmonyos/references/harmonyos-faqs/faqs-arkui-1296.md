---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1296
title: 如何实现文字压在底部下划线上的布局
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现文字压在底部下划线上的布局
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32af3fd6773719e605334199d5addac98bdf124c1791817c1df5c2bed2b539c3
---

## 问题现象

需要实现一个文本底部带有高亮下划线的布局。文字的宽度根据字数动态变化，下划线的宽度比文字宽度多2vp。布局要求文字压在下划线的上方，且仅压住下划线的一半。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/2lGvRkADR92dxQJeCPa7XQ/zh-cn_image_0000002628757882.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/sTFueHuuQ96z69kBvkmJTw/zh-cn_image_0000002658957199.png "点击放大")

## 背景知识

* [measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)：计算指定文本在单行布局下的宽度。此方法可以用于动态获取文本的宽度，以便进行精确的布局调整。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md)：获取组件的新旧尺寸和位置信息。此事件回调可以用于在组件尺寸发生变化时进行相应的布局调整。
* [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)：相对布局容器，支持容器内部的子元素设置相对位置关系。适用于处理界面复杂的场景，可以对多个子元素进行对齐和排列。

## 解决方案

**方案一**：

1. 确定下划线宽度。
   * **方案一**：使用this.getUIContext().getMeasureUtils().measureTextSize()方法获取当前文本的宽度。具体实现如下：

     ```ts
     // 方案一
     textWidthPx: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
       textContent: this.message,
       fontSize: this.TextSize
     });

     onPageShow(): void {
       const textWidthVp = this.getUIContext().px2vp(this.textWidthPx.width as number) + 2;
       this.lineWidth = textWidthVp + 'vp';
     }
     ```
   * **方案二**：使用onAreaChange事件回调获取文本宽度。具体实现如下：

     ```ts
     // 方案二
     .onAreaChange((oldValue: Area, newValue: Area) => {
       console.info(`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`);
       this.lineWidth = `${Number(newValue.width) + 2}vp`;
     })
     ```
2. 使用px2vp工具函数将获取到的文本宽度由px转换为vp（如果使用onAreaChange获取宽度则不需要单位转换）。
3. 使用RelativeContainer布局将下划线放置当前文本的下方。

完整示例参考如下：

```ts
@Entry
@Component
struct TextLine {
  message: string = 'HelloWorld';
  TextSize: number = 16;
  @State lineWidth: string = '';

  // 方案一
  textWidthPx: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
    textContent: this.message,
    fontSize: this.TextSize
  });

  onPageShow(): void {
    const textWidthVp = this.getUIContext().px2vp(this.textWidthPx.width as number) + 2;
    this.lineWidth = textWidthVp + 'vp';
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('title')
        .fontSize(this.TextSize)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

          // 方案二
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info(`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`);
          this.lineWidth = `${Number(newValue.width) + 2}vp`;
        })

      Column() {
      }
      .width(this.lineWidth)
      .height(12)
      .alignRules({
        center: { anchor: 'title', align: VerticalAlign.Center },
        middle: { anchor: 'title', align: HorizontalAlign.Center }
      })
      .linearGradient({ direction: GradientDirection.Left, colors: [['#a1c4fd', 0], ['#c2e9fb', 1]] })
      .offset({ y: 8 })
      .borderRadius(4)
      .zIndex(-1)
    }
    .height('100%')
    .width('100%')
  }
}
```

**方案二**：

参考官方链接：[Text组件如何给文本添加下划线](faqs-arkui-513.md)。
