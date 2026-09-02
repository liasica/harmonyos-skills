---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilitystatedescription
title: 自定义控件播报状态
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 自定义控件播报状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:902e0dd517d4aa46650f7a470a8350047c1f69beb9bc5141027eb879122e70ae
---

## 场景介绍

可切换状态的控件可以处于“已选中”或“未选中”状态，屏幕朗读功能可以从控件的语义属性中推导出默认状态说明标签。在某些情况下，推导出的默认状态说明标签不能完全适用于应用场景，此时可以通过[accessibilityStateDescription](../harmonyos-references/ts-universal-attributes-accessibility.md)指定状态说明标签进行判断。屏幕朗读模式下，若指定了可点击控件的状态说明标签，当用户聚焦控件或执行双击操作后，屏幕朗读会播报指定的状态说明标签。

## accessibilityStateDescription说明

* [description](../harmonyos-references/ts-universal-attributes-accessibility.md)：指定组件的状态说明标签，支持string类型和Resource类型，默认值为空。

## 开发流程

如下示例实现一个收藏按钮，点击可切换状态，播报指定的状态说明标签：

```typescript
@Entry
@Component
export struct Rule_2_1_14 {
  title: string = 'Rule 2.1.14';
  // 收藏按钮状态，表示是否被选中。
  @State private isSelected: boolean = false;

  build() {
    NavDestination() {
      Column() {
        Button() {
          // 根据状态显示不同的图标。
          Image(this.isSelected ? $r('app.media.favorIcon') : $r('app.media.unfavorIcon'))
            .width(30)
            .height(30)
        }
        // 指定按钮的状态说明标签，"已收藏"或"未收藏"。
        .accessibilityStateDescription(this.isSelected ? "已收藏" : "未收藏")
        // 设置按钮的选中状态。
        .accessibilitySelected(this.isSelected)
        // 按钮点击事件处理程序，切换选中状态。
        .onClick(() => {
          this.isSelected = !this.isSelected;
        })
      }
      .width('100%')
      .height('100%')
    }
    .title(this.title)
  }
}
```
