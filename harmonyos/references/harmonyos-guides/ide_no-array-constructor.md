---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-array-constructor
title: @typescript-eslint/no-array-constructor
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-array-constructor
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9eeb8e971647b91c23e3943c2bf72fc7fb3e830455e456e746e25c6f9d5f0be4
---

不允许使用“Array”构造函数。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-array-constructor": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const length = 500;
2. Array(length);

4. export const newArr: number[] = new Array(['1'].length);

6. export const arr = ['0', '1', '2'];

8. export const createArray = (array: string) => new Array(array.length);
```

## 反例

```
1. Array();

3. Array('0', '1', '2');

5. new Array('0', '1', '2');
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
