---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-multidimensional-nesting
title: 多维信息整体朗读
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 多维信息整体朗读
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5fad0470a37b2487a385917f496d9c600d11e77afd0c37cc00906431411421ba
---

## 设计场景

如果应用展示的是多维信息，还可能出现“嵌套组”的情况。在嵌套组中，应避免两个可获焦对象的功能或朗读内容产生重复。比如下图的天气卡片，时间和地点信息获取到焦点时，都是朗读的时间信息；不同焦点的重复朗读会额外增加用户的操作步骤，焦点控制杂乱，这些对同一个信息结构的完整描述应该统一标注在这几个子控件的父控件上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/D43JQw9sSbOT1-sxaoW3sw/zh-cn_image_0000002736312163.png)

## 开发流程

```typescript
@Entry
@Component
export struct Rule_2_1_3 {
  title: string = 'Rule 2.1.3';

  build() {
    NavDestination() {
      Column() {
        Text('Incorrect behavior:') // 播报 "Time Group 12:05 Beijing" + "12:05" + "Beijing"。
          // 继续下滑焦点可聚焦至子控件文本重复了两次，这是不正确的。
          .width('100%')
          .fontSize(12)
          .fontColor(Color.Black)
          .margin({bottom: 12})
        Row(){
          Text('12:05') // time information.
            .fontSize(32)
            .fontColor(Color.Red)
            .fontWeight(FontWeight.Bold)
            .textAlign(TextAlign.Center)
            .margin({right: 20})

          Text('Beijing') // location information.
            .fontSize(20)
            .fontColor(Color.Green)
            .fontWeight(FontWeight.Bold)
            .textAlign(TextAlign.Center)
        }
        .accessibilityText('Time Group') // 时间信息、位置信息和此可访问性文本在获得焦点时被朗读。
        // 带有时间信息的文本组件可聚焦并朗读。
        // 具有位置信息的文本组件可聚焦并朗读。
        .height(50)
        .margin({bottom: 150})

        Text('Correct behavior:') // 只朗读 "07:05 Moscow"，不重复文本，是正确的。
          .width('100%')
          .fontSize(12)
          .fontColor(Color.Black)
          .margin({bottom: 12})
        Row(){
          Text('07:05') // time information.
            .fontSize(32)
            .fontColor(Color.Red)
            .fontWeight(FontWeight.Bold)
            .textAlign(TextAlign.Center)
            .margin({right: 20})

          Text('Moscow') // location information.
            .fontSize(20)
            .fontColor(Color.Green)
            .fontWeight(FontWeight.Bold)
            .textAlign(TextAlign.Center)
        }
        .height(50)
        .accessibilityGroup(true) // 获取焦点时朗读时间和位置信息。
        // 带有时间信息的文本组件无法聚焦和朗读。
        // 具有位置信息的文本组件无法获得焦点并朗读。
      }
      .alignItems(HorizontalAlign.Start)
      .padding(10)
    }
    .title(this.title)
  }
}
```
