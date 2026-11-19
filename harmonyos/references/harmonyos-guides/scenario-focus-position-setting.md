---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-focus-position-setting
title: 重新设置新焦点位置
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 重新设置新焦点位置
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:28+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:616d8cabfb06ca7a6546a8b2d93a428437f508675009fdf39e9f7937d4bef9f8
---

## 设计场景

当前焦点所在的控件消失或者隐藏后，需要重新设置新的焦点位置。一般情况下，新焦点应该在原控件位置的下一个控件上，不应该跳变到前面的控件。应用可以调用主动聚焦的接口对想要聚焦的组件进行主动聚焦。

主动聚焦接口相关参数说明

**表1** **[EventInfo](../harmonyos-references/js-apis-accessibility.md#eventinfo) 说明**

| 属性 | 类型 | 说明 | 例 |
| --- | --- | --- | --- |
| type | EventType | 主动聚焦事件类型 | requestFocusForAccessibility |
| bundleName | string | 目标应用名 | 当前应用包名 |
| triggerAction | Action | 触发事件的Action | common |
| customId | string | 组件id | button1 |

## 开发流程

```typescript
import { accessibility } from '@kit.AccessibilityKit'

@Entry
@Component
export struct Rule_2_1_12 {
  title: string = 'Rule 2.1.12';
  eventInfo: accessibility.EventInfo = ({
    type: 'requestFocusForAccessibility',
    bundleName: 'com.samples.uiextensionandaccessibility',
    triggerAction: 'common',
    customId: 'button1'
  });

  build() {
    NavDestination() {
      Column() {
        Blank()
        Button('button1')
          .accessibilityText('点击聚焦到button2')
          .align(Alignment.Center)
          .fontSize(20)
          .id('button1')
          .onClick(() => {
            this.eventInfo.customId = 'button2';
            accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
              console.info(`Succeeded in send event, eventInfo is: ${JSON.stringify(this.eventInfo)}`);
            }).catch((error: BusinessError) => {
              // 捕获事件发送失败（rejected）的异常。
              console.error(`Failed to send event, code: ${error.code}, message: ${error.message}.`);
            });
          })
        Blank()
          .height(10)
        Button('button2')
          .accessibilityText('点击聚焦到button1')
          .align(Alignment.Center)
          .fontSize(20)
          .id('button2')
          .onClick(() => {
            this.eventInfo.customId = 'button1';
            accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
              console.info(`Succeeded in send event, eventInfo is: ${JSON.stringify(this.eventInfo)}`);
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
