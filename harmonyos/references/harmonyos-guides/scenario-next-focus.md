---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-next-focus
title: 自定义控件走焦顺序
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 自定义控件走焦顺序
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9ec5a82ecfdba49d4cc0b64644396f0a420a4f2f07bf126164a15396f53a9dec
---

## 设计场景

从API版本18开始，开启屏幕朗读后用户可以通过单指左右滑动实现聚焦的焦点切换，当前焦点默认切换顺序为按照节点树顺序走焦，如果默认走焦顺序不满足开发者需要实现的功能场景时，需要开发者通过自定义设置下一个焦点的方式重新定义走焦顺序。

[accessibilityNextFocusId](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)属性用于指定焦点移动过程中下一个被聚焦组件的id。建议开发者将聚焦顺序按照画面显示的自上而下、自左向右方向设置。

从API版本26.0.0开始，新增参数nextFocusParams，可以设置焦点搜索是否应考虑目标元素后代中的可聚焦节点。

## 参数说明

**表1** [接口入参说明](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| nextId | string | 指定下个接口id |
| nextFocusParams | AccessibilityNextFocusParams | 详细参数 |

**表2** [AccessibilityNextFocusParams](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)说明

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isConsiderDescendants | boolean | 焦点搜索是否应考虑目标元素后代中的可聚焦节点（默认false） |

## 开发流程

本实例中组件的视觉呈现顺序为“A->B->C->D->E”，在设置[accessibilityNextFocusId](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)参数后最终走焦顺序为“A->C->D->E”。

```typescript
@Entry
@Component
export struct NextFocusIdBasic {
  title: string = 'NextFocusIdBasic';

  build() {
    NavDestination() {
      Column({ space: 10 }) {
        Button('按钮A, Next为column')
          .onClick(() => {
          }).fontSize(20).width('80%')
          .accessibilityNextFocusId('next_column')

        Button('按钮B')
          .onClick(() => {
          }).fontSize(20).width('80%')

        Column() {
          Button('按钮C')
            .onClick(() => {
            }).fontSize(20).width('80%')

          Button('按钮D')
            .onClick(() => {
            }).fontSize(20).width('80%')
        }
        .id('next_column')
        .backgroundColor(Color.Green)

        Button('按钮E')
          .id('btn_e')
          .onClick(() => {
          }).fontSize(20).width('80%')
      }
      .width('100%')
      .height('100%')
    }
    .title(this.title)
  }
}
```
