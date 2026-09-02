---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-disable-screen-reading-focus
title: 禁用屏幕朗读焦点
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 禁用屏幕朗读焦点
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:40642906aaca431393df31b20bf27027b17388665408f24b7557999daedc4d5e
---

## 设计场景

装饰性的控件一般为分隔符、占位符和美化图标等，这类图形元素仅仅起到调整页面布局或装饰性效果，并不会向用户传达有效的信息或提供交互功能，删除后不影响指引用户体验。可以设置控件的无障碍组[accessibilityGroup](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitygroup)、无障碍重要性[accessibilityLevel](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitylevel)、组件可见性[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)等属性将其设置为无障碍不可聚焦，这样在屏幕朗读模式下控件就不会获取焦点和朗读。

通过以下无障碍属性可以改变控件可聚焦属性：

* accessibilityGroup(true) 用于多个组件的组合，拼接所有子组件text文本并设置到无障碍组节点，除非子组件设置了[accessibilityLevel](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitylevel)为yes，否则子组件默认一定都不可聚焦。
* accessibilityLevel("no")用于组件设置不可聚焦，忽略当前组件的文本属性和点击属性。
* accessibilityLevel("no-hide-descendants")用于组件及其所有子组件设置不可聚焦，忽略当前组件及其所有子组件的文本属性和点击属性。

## 开发流程

以下代码同时显示“Broadcast”和“No broadcast”消息，但当ScreenReader处于“打开”状态时，message可被聚焦，但message1将不被聚焦。

```typescript
@Entry
@Component
export struct Rule_2_1_2 {
  title: string = 'Rule 2.1.2'
  @State message: string = 'Broadcast';
  @State message1: string = 'No broadcast';

  build() {
    NavDestination() {
      Column() {
        Row() {
          Text(this.message)
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
            .fontColor(Color.Blue)
            .margin({
              left: 40
            })
        }
        .width('100%')
        .height('50%')
        Row() {
          Text(this.message1)
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
            .fontColor(Color.Grey)
            .margin({
              left: 40
            })
            .accessibilityLevel("no") // use for component
        }
        // .accessibilityGroup(true)
        // .accessibilityLevel("no-hide-descendants")
        // 可以使用这两行代替28行的accessibilityLevel("no")。
        .width('100%')
        .height('50%')
      }
      .height('100%')
    }
    .title(this.title)
  }
}
```
