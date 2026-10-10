---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-operation-error
title: 网络连接中断播报
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 网络连接中断播报
category: harmonyos-guides
scraped_at: 2026-10-11T07:20:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f11af63d7ebf1e9b192265ea99da4bfa15f09616d753b8be4b8939f0e13f54f6
---

## 设计场景

比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/xU70E8WxQ0OZDAsUnkWS6g/zh-cn_image_0000002755182766.png)

## 开发流程

如下是一个将连接中断播报出来的例子。

```typescript
@Entry
@Component
export struct Rule_2_1_9 {
  title: string = 'Rule 2.1.9';

  build() {
    NavDestination() {
      Column() {
        Flex({
          direction: FlexDirection.Column,
          alignItems: ItemAlign.Center,
          justifyContent: FlexAlign.Center,
        }) {
          Row() {
            Text('Connection state').fontSize(30)
          }
          Row() {
            Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)
              .radioStyle({
                checkedBackgroundColor: Color.Red
              })
              .height(50)
              .width(50)
              .onChange((isChecked: boolean) => {
                console.info('Radio1 status is: ', isChecked);
              })
            Text('Connection interrupted').fontColor(Color.Red)
          }
          .width('80%')
          .accessibilityGroup(true) // 将单选和文本合并到单个对象中。
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
      }
    }.title(this.title)
  }
}
```
