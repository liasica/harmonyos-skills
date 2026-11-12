---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-status-missing-check
title: "@correctness/accessibility-status-missing-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/accessibility-status-missing-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1d55bbde043bd0faba9931e212a3729f5c9d7388eb9a9afe5df73eafc6ff1284
---

在无障碍场景开发中，须通过[accessibilityRole](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityrole18)声明组件的类型标识，如“按钮”、“编辑框”。

## 规则配置

```json5
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-status-missing-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Entry
@Component
struct AccessibilityStatusMissingPositive {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
                .accessibilityRole(AccessibilityRoleType.BUTTON)
                .onClick(() => {})
		}
	}
}
```

## 反例

```screen
@Entry
@Component
struct AccessibilityStatusMissingNegative {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
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
