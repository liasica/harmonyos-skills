---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-bracket-spacing
title: "@hw-stylistic/array-bracket-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/array-bracket-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7aa62e31e85886d8d4375f072c3276050718abd507d53de54609c12765ad3a24
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
