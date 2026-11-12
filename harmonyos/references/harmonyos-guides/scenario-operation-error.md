---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-operation-error
title: 网络连接中断播报
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 网络连接中断播报
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bd1b2b2563bcc120c8d7abaf5da670995483d3f3e79ffae569142f833628714c
---

## 设计场景

比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/YvGholxAT5Si5uq3cOFqng/zh-cn_image_0000002786518368.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=B33CB676C11426E7ED2ABA123FB7679EE07A5DC13BD0E0C5281955785BA04173)

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
