---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-screen-reading
title: 标注屏幕朗读内容
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 标注屏幕朗读内容
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:46febed90c80e990ac5bfbbd28f815f220dcff5ee4b04b07cc9ac9d4d0c7d52e
---

## 设计场景

屏幕朗读提取信息进行朗读时无障碍文本的优先级大于显示文本，即当无障碍文本不为空时，会朗读无障碍文本，否则朗读显示文本。因此，在进行应用设计时，需要遵守如下规则：

* 对于文本类控件，尽量使用显示文本来表达信息，使视障用户和视力健全用户可以获取到相同的信息。
* 对于文本类控件，如果除显示文本外，还额外提供了颜色等视觉效果为视力健全用户提供了更多信息的场景，可采用无障碍文本为视障用户提供更多的信息用于朗读。
* 对于非文本类控件，可采用无障碍文本为视障用户提供朗读信息。

## 开发流程

以accessibilityText()设置无障碍文本为例，[accessibilityText](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitytext)设置无障碍文本。聚焦[Button](../harmonyos-references/ts-basic-components-button.md)时朗读效果为："Accessibility text，按钮"。

```typescript
@Entry
@Component
export struct Rule_2_1_1 {
  title: string = 'Rule 2.1.1';
  shortText: string = 'Button';
  longText: string = 'Accessibility text';

  build() {
    NavDestination() {
      Column() {
        Blank()
        Button(this.shortText)
          .accessibilityText(this.longText)
          .align(Alignment.Center)
          .fontSize(20)
        Blank()
      }
      .width('100%')
      .height('100%')
    }
    .title(this.title)
  }
}
```
