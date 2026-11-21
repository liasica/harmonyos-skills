---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-component-relocation
title: 控件位置调整
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 控件位置调整
category: harmonyos-guides
scraped_at: 2026-11-21T09:10:54+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:d51215b5d89d9bee9abe46647fa292ff8dbd24fdeb5a99aef723734aa5d39d67
---

## 设计场景

移动过程中需要实时播报即将移动到的位置，新位置的播报会打断老位置的播报，放置到确定位置后，需要再播报已经放置的位置信息，尽量保证视障用户耳朵听到的信息和我们通过眼睛看到的信息是一致的。

## 开发流程

例如，当前展示的网页书签被托起时，会播报”华为专区已托起”，移动的过程中，根据即将放置的位置播报“移动到华为手机服务|华为官网上面”。应用可调用主动播报的接口来进行主动播报。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/zEjExZs6S5-4SNeU9Kx9Sg/zh-cn_image_0000002821756053.png?HW-CC-KV=V1&HW-CC-Date=20261121T010931Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCF2A4D33F098C15B61BB1E04BD45921DEF3956E8CA1BC61EA23D2BEAC4A51AF)

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
