---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-array-bracket-spacing
title: "@hw-stylistic/array-bracket-spacing"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/array-bracket-spacing
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:57a92a367fdf2eb280dcfcad597c22bc4e126381bf70bf4ed14f04318ebb335e
---

强制数组“[”之后和“]”之前加空格。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/array-bracket-spacing": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export const arr = ['a', 'b'];
```

## 反例

```ts
// There should be no space after '['.
// There should be no space before ']'.
export const arr = [ 'a', 'b' ];
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
