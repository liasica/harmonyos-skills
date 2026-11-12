---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-bracket-spacing
title: "@hw-stylistic/array-bracket-spacing"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/array-bracket-spacing
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d93a32c7a2a142b934dee23f106b833f879453d57c482b97687f57c6cc0f1377
---

强制数组“[”之后和“]”之前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/array-bracket-spacing": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export const arr = ['a', 'b'];
```

## 反例

```screen
// There should be no space after '['.
// There should be no space before ']'.
export const arr = [ 'a', 'b' ];
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
