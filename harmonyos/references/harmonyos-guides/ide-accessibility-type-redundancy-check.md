---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-type-redundancy-check
title: "@correctness/accessibility-type-redundancy-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/accessibility-type-redundancy-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fc8dd4139ee9354b9328fe170b057b84a16c417d4faca88c5d4043a3cc77fe1e
---

在无障碍场景开发中，避免存在button、radio等冗余组件类型，否则可能导致冗余播放等问题。

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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
