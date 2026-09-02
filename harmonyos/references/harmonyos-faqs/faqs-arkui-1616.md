---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1616
title: 如何通过RelativeContainer实现列表的统一格式布局
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何通过RelativeContainer实现列表的统一格式布局
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:108d18009cd6134bafcc05202a6c23a41571a4fc0bb36ea32a4bef791c61803c
---

## 问题现象

使用RelativeContainer组件开发时，希望通过RelativeContainer实现统一格式的列表展示布局，但出现无法根据子组件大小自适应，存在撑满父组件、全屏、尺寸显示异常等问题，该如何实现？

## 背景知识

[RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)为相对布局组件，用于元素对齐的布局。其支持容器内部的子组件设置相对位置关系，对多个子组件进行对齐和排列。子组件可以指定兄弟组件或父容器作为锚点，基于锚点进行相对位置布局。

## 解决方案

RelativeContainer作为子组件不设置高度时，默认撑满父组件布局，导致全屏问题，通过给RelativeContainer设置height('auto')属性自适应子组件高度解决。使用[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件动态获取并设置对应组件宽高属性，然后实时渲染，达到预期布局效果。示例代码如下：

```ts
@Entry
@Component
struct AdjustComponentSizeByAreaChange17 {
  @State knowLedgeList: string[] = ['1', '2', '3', '4', '5', '6', '7', '8'];
  @State heightArr: number[] = [];

  build() {
    Column() {
      List() {
        ForEach(this.knowLedgeList, (index: number) => {
          ListItem() {
            RelativeContainer() {
              Line()
                .width(0.5)
                .height(this.heightArr[index] + 2)
                .backgroundColor(Color.Black)
                .id(`line${index}`)
                .margin({ left: 20, top: 0 })
                .offset({ x: 0, y: 8 });
              Text(`mode${index}：RelativeContainer统一格式列表展示`)
                .fontSize(25)
                .offset({ x: 20, y: 0 })
                .margin({ right: 50 })
                .alignRules({
                  top: { anchor: `line${index}`, align: VerticalAlign.Top },
                  left: { anchor: `line${index}`, align: HorizontalAlign.End },
                })
                .onAreaChange((oldValue: Area, newValue: Area) => {
                  this.heightArr[index] = Number(newValue.height);
                });
              Text('')
                .offset({ x: -10, y: 8 })
                .backgroundColor(Color.Green)
                .width('20.00vp')
                .height('20.00vp')
                .borderRadius(40)
                .alignRules({
                  top: { anchor: `line${index}`, align: VerticalAlign.Top },
                  left: { anchor: `line${index}`, align: HorizontalAlign.Start },
                });
            }
            .height('auto')
            .margin({ left: 10, right: 10 });

          };
        });
      }
      .width('100%')
      .height('100%')
      .margin({ top: 10, left: 10 });
    };
  }
}
```

显示效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/J37349nCRry6o6u-1s8_ZQ/zh-cn_image_0000002658972599.png "点击放大")

## 常见FAQ

Q：RelativeContainer高度默认不是auto吗？

A：请参考[RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)说明中的第三点。
