---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-type-redundancy-check
title: "@correctness/accessibility-type-redundancy-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/accessibility-type-redundancy-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6f66a1db00df927efb91caf0b4c6725767135d5ce3d5b1c03e053f5a52e90b18
---

在无障碍场景开发中，避免存在冗余的button、radio等组件类型，否则可能导致冗余播放等问题。

## 规则配置

```json5
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-type-redundancy-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Entry
@Component
struct AccessibilityTypeRedundancyPositive {
    build() {
        Column() {
            Button('提交')
                .accessibilityText('提交表单')
                .onClick(() => {})
        }
    }
}
```

## 反例

```screen
@Entry
@Component
struct AccessibilityTypeRedundancyNegative {
    build() {
        Column() {
            Button()
                .accessibilityText('提交按钮')
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
