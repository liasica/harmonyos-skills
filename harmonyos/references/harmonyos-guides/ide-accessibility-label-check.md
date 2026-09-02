---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-label-check
title: "@correctness/accessibility-label-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/accessibility-label-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fea01fab815c678160e6b87e8650758fad0c11a40083593e84fcb645b161b19a
---

在无障碍场景中，建议通过[accessibilityText](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitytext)为控件添加无障碍文本信息。

## 规则配置

```json5
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-label-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Entry
@Component
struct AccessibilityLabelPositive {
    build() {
        Column() {
            Text('文本')
                .width(60)
                .height(60)
                .accessibilityText('返回')
                .onClick(() => {})
        }
    }
}
```

## 反例

```ts
@Entry
@Component
struct AccessibilityLabelNegative {
    build() {
        Column() {
            Text()
                .width(60)
                .height(60)
                .backgroundColor(0xeaeaea)
                .onClick(() => {})
        }
    }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
