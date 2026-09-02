---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1143
title: 设置ListItem子组件的文字水平居中
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 设置ListItem子组件的文字水平居中
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:08a5c2ccb6c638b3dc8e3bdbe53cd558ebfa9a351854997bcb1eeab82d705eb3
---

## 问题现象

如何实现每列Item的文字水平居中？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Ko8JwUFcTjCuMQea50UcOA/zh-cn_image_0000002658928925.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/XacPWIQ_R7q2A91k7k9Dxw/zh-cn_image_0000002658808971.gif "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：列表包含一系列相同宽度的列表项。仅支持ListItem、ListItemGroup子组件。
* [listDirection](../harmonyos-references/ts-container-list.md#listdirection)：设置List组件排列方向。
* [lanes](../harmonyos-references/ts-container-list.md#lanes9)：设置List组件的布局列数或行数。gutter为列间距，当列数大于1时生效。

## 解决方案

当List组件设置listDirection(Axis.Horizontal)和lanes(2)时，内部的ListItem自身会均匀分配父List的高度，只可以设置每个ListItem垂直方向的位置；而此时ListItem宽度由自适应撑开，故无法设置每列Item的水平居中，因此需要给ListItem一个固定宽度，在每个ListItem同宽的情况下设置子组件的水平方向位置。

```screen
@Entry
@Component
export struct TwoLine {
  @State array?: Array<string> = new Array;

  aboutToAppear(): void {
    this.array?.push('一个栏目');
    this.array?.push('测试');
    this.array?.push('哈哈哈哈哈');
    this.array?.push('对对');
    this.array?.push('好吧好');
    this.array?.push('行行行行行');
    this.array?.push('对对对');
    this.array?.push('是吗');
    this.array?.push('栏目编辑');
  }

  build() {
    Column() {
      List({ space: 10 }) {
        ForEach(this.array, (item: string) => {
          ListItem() {
            Column() {
              Text(item)
                .height(20)
                .backgroundColor(Color.White)
                .textAlign(TextAlign.Center)
                .align(Alignment.Center)
                .alignSelf(ItemAlign.Center)
                .constraintSize({ minWidth: 30 })
            }
            .width("24%") // 设置width固定时可以实现水平居中，不设置时listItem宽度由内容撑开，无法设置居中。
            .height('100%')
            .justifyContent(FlexAlign.Center)
            .backgroundColor(Color.Blue)
          }
          .margin({ bottom: 10 })
        });
      }
      .width('100%')
      .height(70)
      .lanes(2)
      .listDirection(Axis.Horizontal)
      .backgroundColor('#87ceeb')
      .alignListItem(ListItemAlign.Center)

      Text('如何实现每列文字的水平居中？')
        .margin({ top: 100 })
        .fontSize(20)
    }
    .padding(10)
  }
}
```
