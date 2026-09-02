---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-550
title: 上下文内容显示不一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 上下文内容显示不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bec5f14ac4918d150c26868424eeab8a7da88ea364cf1f2b5690671adfec1727
---

## 问题现象

点击进入详情页面，标题和页面内的数据正好相反，问题现象如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Hv2YDJQ7RSmuLM29scLWRQ/zh-cn_image_0000002628391628.png "点击放大")

## 背景知识

[Text](../harmonyos-guides/ui-js-components-text.md)是文本组件，用于呈现一段文本信息。

## 问题定位

1. 使用DevEco Testing中的UIViewer工具，查看详情页面的布局，发现数据展示使用的是Text组件，并且同一个对象的数据分在了多个不同组件内展示，不涉及与H5页面的交互。
2. 对比发现标题和页面内数据展示相反，并且页面内问题数据与其他内容对不上，判断是页面内的数据传参有误。
3. 排查该Text组件的设置，用于展示问题数据的Text组件传参颠倒。

   ```ts
   Text(`标题：${this.PerList[0].nam} ${this.PerList[0].sum} : ${this.PerList[1].sum} ${this.PerList[1].nam}`)

   Column() {
     Row() {
       Text(this.PerList[1].nam)
       Text(this.PerList[1].sum.toString())
     }
     Row() {
       Text(this.PerList[0].nam)
       Text(this.PerList[0].sum.toString())
     }
   }
   ```

## 分析结论

页面内进行文本展示时，同一个对象的数据分在了多个不同组件内展示，传入Text组件时因过于分散导致错乱，从而造成页面内文本内容与标题不一致。

## 修改建议

对于同一个对象的数据，放在一起集中处理，避免因分散操作导致页面错乱等问题。示例代码如下：

```ts
@Entry
@Component
struct TextAlignment {
  @State PerList: Array<Per> = [new Per('PerA', 150), new Per('PerB', 130)];

  build() {
    Column({space: 30}) {
      Text(`标题：${this.PerList[0].nam} ${this.PerList[0].sum} : ${this.PerList[1].sum} ${this.PerList[1].nam}`)
        .fontSize(25)
        .fontWeight(FontWeight.Bold)
        .fontColor('#e6000000')

      Column() {
        ForEach(this.PerList, (item: Per) => {// 对于同一个对象的数据集中处理
          Row() {
            Text(item.nam)
              .fontSize(20)
              .fontWeight(FontWeight.Regular)
              .fontColor('#e6000000')
            Text(item.sum.toString())
              .fontSize(20)
              .fontWeight(FontWeight.Regular)
              .fontColor('#e6000000')
          }
          .width('100%')
          .height('10%')
          .justifyContent(FlexAlign.SpaceAround)
        })
      }
      .width('100%')
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

class Per {
  nam: string = '';
  sum: number = 0;
  constructor(nam: string, sum: number) {
    this.nam = nam;
    this.sum = sum;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/e5-0tET4Tz284rTv_DLXtw/zh-cn_image_0000002658910843.png "点击放大")
