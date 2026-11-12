---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-row-column-to-replace-flex
title: "@performance/hp-arkui-use-row-column-to-replace-flex"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-row-column-to-replace-flex
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:61ce6d24247b073b808fd954aef67e12eda2c2efb09e63c1849a04eff5b48ed1
---

建议使用Column/Row替代Flex。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-row-column-to-replace-flex": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct MyComponent {
  build() {
    // Replace Flex with Column/Row
    Column() {
      Text('Replace Flex with Column/Row')
        .fontSize(12)
        .height('16')
        .margin({
          top: 5,
          bottom: 10
        })
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
    }.height(200)
  }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  build() {
    // Flex Nesting
    Flex({ direction: FlexDirection.Column }) {
      Text('Replace Flex with Column/Row')
        .fontSize(12)
        .height('16')
        .margin({
          top: 5,
          bottom: 10
        })
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
    }.height(200)
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
