---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-dynamic-content-change
title: 内容动态变化
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 内容动态变化
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec0c2e252233f9f2927ea194d7b7490ba68943d255f725a3e01afad08b640621
---

## 设计场景

界面上重要内容在动态变化后，需要实时发送变化后的朗读内容。具体地，当界面上内容发生动态变化且其内容对用户具有必要的提示/告知/指导作用，则其发生变化后需对其变化内容进行播报，可调用无障碍提供的主动播报接口进行播报。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/fKFdaEF-SnmNhGR-6V-9Kw/zh-cn_image_0000002712243298.png)

主动播报接口相关参数说明：

**表1** [EventInfo](../harmonyos-references/js-apis-accessibility.md#eventinfo) 说明

| 属性 | 类型 | 说明 | 例 |
| --- | --- | --- | --- |
| type | EventType | 主动播报事件类型 | announceForAccessibility |
| bundleName | string | 目标应用名 | 当前应用包名 |
| triggerAction | Action | 触发事件的Action | click或其他都不会有任何影响 |
| textAnnouncedForAccessibility | string | 主动播报的内容 | test123 text |

## 开发流程

```typescript
import { accessibility } from '@kit.AccessibilityKit'

@Entry
@Component
export struct Rule_2_1_7 {
  title: string = 'Rule 2.1.7';
  shortText: string = 'Button';
  longText: string = 'sendAccessibilityEvent';
  eventInfo: accessibility.EventInfo = ({
    type: 'announceForAccessibility',
    bundleName: 'com.samples.uiextensionandaccessibility',
    triggerAction: 'common',
    textAnnouncedForAccessibility: 'test123 text'
  });

  build() {
    NavDestination() {
      Column() {
        Blank()
        Button(this.shortText)
          .accessibilityText(this.longText)
          .align(Alignment.Center)
          .fontSize(20)
          .onClick(() => {
            accessibility.sendAccessibilityEvent(this.eventInfo).then(() => {
              console.info(`test123 Succeeded in send event, eventInfo is: ${JSON.stringify(this.eventInfo)}`);
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
