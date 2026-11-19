---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-component-relocation
title: 控件位置调整
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 控件位置调整
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:28+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:f0ee0e31dad4150ece942f4ae759247441ce6b5451f092cacd240be4e21e1598
---

## 设计场景

移动过程中需要实时播报即将移动到的位置，新位置的播报会打断老位置的播报，放置到确定位置后，需要再播报已经放置的位置信息，尽量保证视障用户耳朵听到的信息和我们通过眼睛看到的信息是一致的。

## 开发流程

例如，当前展示的网页书签被托起时，会播报”华为专区已托起”，移动的过程中，根据即将放置的位置播报“移动到华为手机服务|华为官网上面”。应用可调用主动播报的接口来进行主动播报。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/MskH71BDTBi3whFkhXnKdQ/zh-cn_image_0000002791564498.png?HW-CC-KV=V1&HW-CC-Date=20261119T014728Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC7376D9F4A6559CE5BEAE72AB585C69E01371DBAC0313411166BC2323002C89)

```typescript
import { accessibility } from '@kit.AccessibilityKit'

@Entry
@Component
export struct Rule_2_1_11 {
  title: string = 'Rule 2.1.11';
  eventInfo: accessibility.EventInfo = ({
    type: 'announceForAccessibility',
    bundleName: 'com.samples.uiextensionandaccessibility',
    triggerAction: 'common',
    textAnnouncedForAccessibility: '移动到华为手机服务|华为官网上面'
  });

  build() {
    NavDestination() {
      Column() {
        Blank()
        Button('button')
          .accessibilityText('主动播报')
          .align(Alignment.Center)
          .fontSize(20)
          .id('button1')
          .onClick(() => {
            accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
              console.info(`Succeeded in send event, eventInfo is ${JSON.stringify(this.eventInfo)}`);
            }).catch((error: BusinessError) => {
              // 捕获事件发送失败（rejected）的异常。
              console.error(`Failed to send event, code: ${error.code}, message: ${error.message}.`);
            });
          })
        Blank()
      }
      .width('100%')
      .height('100%')
    }
    .title(this.title)
  }
}
```
