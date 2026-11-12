---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-focus-redundancy-check
title: "@correctness/accessibility-focus-redundancy-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/accessibility-focus-redundancy-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:db6cd105cfebc5557608f4b811689fb0a4ae8bdf7e51df4d35a4d94f6347d6fb
---

在无障碍场景开发中，避免控件焦点冗余。

## 规则配置

```json5
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-focus-redundancy-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Entry
@Component
struct FocusRedundancyPositive {
    build() {
        Column() {
            Column() {
                Button('提交')
                    .onClick(() => {})
            }
            .accessibilityGroup(true)
            .onClick(() => {})
        }
    }
}
```

## 反例

```ts
@Entry
@Component
struct FocusRedundancyNegative {
    build() {
        Column() {
            Column() {
                Button('按钮1')
                    .accessibilityText('操作')
                    .onClick(() => {})

                Text('文本')
                    .accessibilityText('说明文字')

                Image($r('app.media.icon'))
                    .accessibilityText('图标')
                    .onClick(() => {}) 
            }
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
