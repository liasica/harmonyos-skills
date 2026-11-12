---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-multi-spaces
title: "@hw-stylistic/no-multi-spaces"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/no-multi-spaces
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:27b4c9b63999c1ea2c57d96e1d3a1abc4e0d5f89e5fa2441a65c0b0996354df7
---

不允许出现连续多个空格，除非是换行。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-multi-spaces": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export const message: string = 'Hello World';
```

## 反例

```screen
// Multiple spaces found before 'message'.
// Multiple spaces found before 'string'.
// Multiple spaces found before '='.
// Multiple spaces found before 'Hello World'.
export const   message:  string  =  'Hello World';
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
