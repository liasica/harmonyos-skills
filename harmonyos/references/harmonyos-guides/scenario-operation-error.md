---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-operation-error
title: 网络连接中断播报
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 网络连接中断播报
category: harmonyos-guides
scraped_at: 2026-09-21T06:17:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:32aec237b82ad7d25d31e2eb60950cc11ee25c37dbef66c74377e2adc389f898
---

## 设计场景

比如网络连接错误，或者其他警告信息，不能仅仅以颜色区分，需要实时告诉用户错误提示和改进方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/CPjMtq60Txmsezo2-3IDRQ/zh-cn_image_0000002762992843.png)

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
