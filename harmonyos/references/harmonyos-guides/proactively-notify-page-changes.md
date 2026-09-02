---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/proactively-notify-page-changes
title: 主动通知页面变化
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 主动通知页面变化
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce5030119334a8d41e8660fac9a628a2f39cc00d653ca1ec4ba4d2ea271b14f8
---

## 设计场景

应用自定义的页面可以通过堆叠的方式覆盖在原页面上，实现页面切换的效果，但是系统无法自动识别到这种场景，可能会导致焦点丢失。此时，应用可以调用主动通知页面变化的接口，通知屏幕朗读在新页面上寻找节点聚焦。该接口支持指定新页面的根节点，如果指定了有效的根节点，则从该根节点开始找首焦点聚焦，如果未指定，则默认从当前窗口根节点开始找首焦点聚焦。

## 主动通知页面变化接口相关参数说明：

**表1** [EventInfo](../harmonyos-references/js-apis-accessibility.md#eventinfo) 说明

| 属性 | 类型 | 说明 | 例 |
| --- | --- | --- | --- |
| type | EventType | 主动通知页面变化事件类型。 | pageActive |
| bundleName | string | 目标应用名。 | 'com.example.accessibilityinfo' |
| triggerAction | Action | 触发事件的Action。 | common |
| customId | string | 自定义页面根节点id。 | 'abc345' |

## 开发流程

如下示例实现一个自定义页面切换，通过改变[Stack](../harmonyos-references/ts-container-stack.md)子组件Z序的方式实现切换页面的效果：

```typescript
import { accessibility } from '@kit.AccessibilityKit'

@Entry
@Component
export struct Rule_2_1_16 {
  title: string = 'Rule 2.1.16';
  // 定义状态变量，用于控制顶层显示的层数。
  @State topLayer: number = 0;

  // 定义自定义页面。
  @Builder
  Layer(text: string, index: number) {
    Column() {
      Column() {
        Text(text)
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .margin({ bottom: 20 })
        Text(`${text} 测试节点1`)
        Text(`${text} 测试节点2`)
        Text(`${text} 测试节点3`)
        // 创建按钮用于切换页面。
        Button(`页面切换${index}`)
          .onClick(() => {
            // 判断当前顶层，在0与1之间切换。
            if (this.topLayer === 0) {
              this.topLayer = 1;
            } else {
              this.topLayer = 0;
            }
            // 定义事件信息描述，事件类型为pageActive，页面根节点id为`Layer_${this.topLayer}`。
            const eventInfo: accessibility.EventInfo = ({
              type: 'pageActive',
              bundleName: 'com.samples.uiextensionandaccessibility',
              triggerAction: 'common',
              customId: `Layer_${this.topLayer}`
            });
            // 发送主动通知页面变化的事件。
            accessibility.sendAccessibilityEvent(eventInfo).then(() => {
              console.info(`pageActive event send Successed, customId=Layer_${this.topLayer}.`); // 发送成功日志。
            });
          })
      }
      // 指定自定义节点id，用于标识页面根节点。
      .id('Layer_' + index)
    }
    .height('100%')
    .width('100%')
    .backgroundColor(index === 0 ? Color.Red : Color.Green)
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .borderRadius(16)
    .padding(20)
    // 修改页面Z序，用于实现页面切换效果。
    .zIndex(this.topLayer === index ? 1 : 0)
    // 根据当前页面是否顶层显示，指定自定义页面节点是否无障碍可识别，若否，则设置为不可识别。
    .accessibilityLevel(this.topLayer === index ? 'no' : 'no-hide-descendants')
  }

  build() {
    NavDestination() {
      Column() {
        Stack() {
          this.Layer('页面0', 0)
          this.Layer('页面1', 1)
        }
      }
    }
  }
}
```
