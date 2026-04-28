---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-bracket-spacing
title: @hw-stylistic/array-bracket-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/array-bracket-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:24+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b9e902430d2d35e37442d5fa9e8a89ba39cfe34dcb0675b78ff85e59356e40bd
---

强制数组“[”之后和“]”之前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/array-bracket-spacing": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const arr = ['a', 'b'];
```

## 反例

```
1. // There should be no space after '['.
2. // There should be no space before ']'.
3. export const arr = [ 'a', 'b' ];
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
