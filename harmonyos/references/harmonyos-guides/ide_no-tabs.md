---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-tabs
title: @hw-stylistic/no-tabs
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f4ebf39462b438af955e69242679093c3cac581b01a239812fdcfafdd401274d
---

禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/no-tabs": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const message: string = 'Hello World';
```

## 反例

```
1. export    const    message:    string = 'Hello World';
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
