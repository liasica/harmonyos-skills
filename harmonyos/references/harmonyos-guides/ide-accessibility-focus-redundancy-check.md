---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-focus-redundancy-check
title: "@correctness/accessibility-focus-redundancy-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/accessibility-focus-redundancy-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:38bbc72472d70efe530f29f0f50189dc5c3e6926ec79086dbe9eac5bcd4774c8
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
