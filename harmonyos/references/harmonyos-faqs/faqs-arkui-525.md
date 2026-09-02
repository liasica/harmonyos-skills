---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-525
title: 关于绘制表格内容的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 关于绘制表格内容的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21bf29408a5dadce33295d04a2eb734debf19b9634afb897508c438133d3b7f3
---

## 问题现象

如何绘制单元格内容可能含有子表格的表格？表格需要有分隔线和圆角，不绘制子表格的外框线。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/HKRVADbXTJuCTxwjXW220A/zh-cn_image_0000002658790421.png "点击放大")

## 背景知识

* [Flex容器](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，可以通过设置FlexOptions的属性，设置容器内子组件的排列方向，单行列或多行列排列，主轴或交叉轴的对齐格式与间距等。
* 通用属性[border](../harmonyos-references/ts-universal-attributes-border.md#border)设置组件的边框样式，包括宽度、颜色、圆角半径、各边样式等。
* 通用属性[clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)设置是否对子组件超出容器范围的区域进行裁剪，以避免子组件内容超出容器范围。
* 通用属性[clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)可以将组件按指定的形状进行裁剪，指定形状时，可以通过position属性确定裁剪的位置信息。

## 解决方案

表格的实现可以使用Flex容器，设置为多行列排列；外层表格Flex容器和子组件按需要分别设置border边框样式，实现表格分隔线，且Flex容器设置clip属性，避免子组件内容超出范围；子表格可以使用clipShape属性裁去外框线。

外层表格数据源的类型调整为Array<Object>，或Object[]，使数组内可以插入混合类型的数据，包含Array数组；通过typeof判断元素的类型，并根据不同类型渲染表格的单元格内容。

具体实现如下：

1. 使用Flex容器横向排列，并设置为多行列排列与交叉轴方向拉伸填充，实现内容高度不一致时统一拉伸至当前行最大高度；由于表格同列宽度需保持一致，可以根据表格需要的列数为子组件设置宽度；通过border属性设置子组件边框样式，实现表格的分割线。

   ```screen
   Flex({
     direction: FlexDirection.Row,
     wrap: FlexWrap.Wrap,
     justifyContent: FlexAlign.Center,
     alignItems: ItemAlign.Stretch
   }) {
     ForEach(this.itemsArr, (item: ItemAttr) => {
       if (typeof item.content === 'string') {
         Text(item.content)
           .fontSize('16fp')
           .width(item.width)
           .padding(10)
           .textAlign(item.isHeader ? TextAlign.Center : TextAlign.Start)
           .backgroundColor(item.backgroundColor)
           .border({
             width: 1,
             color: '#eccc68'
           });
       } else if (typeof item.content === 'object') {
         MultiItem({ itemArr: item.content as string[] })
           .width(item.width)
           .padding(10)
           .border({
             width: 1,
             color: '#eccc68'
           });
       }
     });
   }
   .height('auto')
   .border({
     width: 1,
     color: '#eccc68',
     radius: 20
   })
   .clip(true);
   ```
2. Flex容器单独设置边框圆角borderRadius，且增加clip属性，使子组件超出容器的内容被裁剪，实现圆角表格。
3. 通过clipShape属性，指定裁剪形状为矩形，且裁剪位置从表格外框线内开始，通过调整裁剪的尺寸，将外框线裁去，实现无外框的表格。
4. 将数据源的类型调整为Array<Object>或Object[]，通过typeof判断元素的类型，并根据不同类型渲染表格的单元格内容。

完整示例参考如下：

```screen
import { RectShape } from '@kit.ArkUI';

const widthArr: Length[] = ['20%', '20%', '60%'];

class ItemAttr {
  content: Object = '';
  width: Length = 'auto';
  backgroundColor: ResourceColor = Color.White;
  isHeader: boolean = false;

  constructor(content: Object, width?: Length, bgColor?: ResourceColor, isHeader?: boolean) {
    this.content = content;
    this.width = width ?? 'auto';
    this.backgroundColor = bgColor ?? Color.White;
    this.isHeader = isHeader ?? false;
  }
}

@Entry
@Component
struct ContainerSheet {
  headerContentArr: string[] = ['title one', 'title two', 'title three'];
  itemContentArr: Object[] = ['Class A', 'Item One',
    'Introductory: This is an example of a table implementation using a Flex container.',
    'Class B', 'Item Two',
    ['item 1-1', 'item 1-2', 'item 1-3', 'item 2-1', 'item 2-2', 'item 2-3']
  ];
  headerArr: ItemAttr[] = [];
  @State itemsArr: ItemAttr[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < this.headerContentArr.length; i++) {
      this.headerArr.push(new ItemAttr(this.headerContentArr[i], widthArr[i], '#eccc68', true));
    }

    for (let i = 0; i < this.itemContentArr.length; i++) {
      let idx = i % this.headerContentArr.length;
      this.itemsArr.push(new ItemAttr(this.itemContentArr[i], widthArr[idx]));
    }

    this.itemsArr = this.headerArr.concat(this.itemsArr);
  }

  build() {
    Flex({
      direction: FlexDirection.Row,
      wrap: FlexWrap.Wrap,
      justifyContent: FlexAlign.Center,
      alignItems: ItemAlign.Stretch
    }) {
      ForEach(this.itemsArr, (item: ItemAttr) => {
        if (typeof item.content === 'string') {
          Text(item.content)
            .fontSize('16fp')
            .width(item.width)
            .padding(10)
            .textAlign(item.isHeader ? TextAlign.Center : TextAlign.Start)
            .backgroundColor(item.backgroundColor)
            .border({
              width: 1,
              color: '#eccc68'
            });
        } else if (typeof item.content === 'object') {
          MultiItem({ itemArr: item.content as string[] })
            .width(item.width)
            .padding(10)
            .border({
              width: 1,
              color: '#eccc68'
            });
        }
      });
    }
    .height('auto')
    .border({
      width: 1,
      color: '#eccc68',
      radius: 20
    })
    .clip(true);

  }
}

@Component
struct MultiItem {
  @State itemArr: string[] = [];
  @State containerHeight: number = 0;
  @State containerWidth: number = 0;

  build() {
    Column() {
      Flex({
        direction: FlexDirection.Row,
        wrap: FlexWrap.Wrap,
        justifyContent: FlexAlign.Center,
        alignItems: ItemAlign.Stretch
      }) {
        ForEach(this.itemArr, (item: string, index: number) => {
          Column() {
            Text(item)
              .fontSize('16fp')
              .width('100%')
              .textAlign(TextAlign.Center);
          }
          .width(index % 3 === 2 ? '40%' : '30%')
          .justifyContent(FlexAlign.Center)
          .border({
            width: 1,
            color: '#f1c40f'

          });
        });
      }
      .width('100%')
      .onAreaChange((oldValue, newValue) => {
        this.containerHeight = newValue.height as number;
        this.containerWidth = newValue.width as number;
      });
    }
    .alignItems(HorizontalAlign.Center)
    .clip(true)
    .clipShape(new RectShape({
      height: this.containerHeight - 2,
      width: this.containerWidth - 2
    }).position({ x: 1, y: 1 }));
  }
}
```

## 总结

* 表格样式可以通过Flex容器实现，不同的表格样式可以通过调整Flex容器及其子元素的属性实现。

  **说明** 

  **ItemAlign.Stretch只有在Flex容器的wrap设置为Wrap或WrapReverse时，元素才会拉伸到与当前行/列交叉轴长度最长的元素尺寸，其他情况下，无论元素尺寸是否设置均拉伸到容器尺寸。**
* Array<Object>允许数组内混合插入不同类型的数据，在某些特殊场景下可以通过此方式实现复杂数据的循环渲染。但一般情况下不建议使用混合类型数组，当数据的类型过于复杂，可能需要通过多重逻辑判断对不同类型的数据进行不同的渲染判断，代码丧失简洁性且最终结果可能会出现错误。
