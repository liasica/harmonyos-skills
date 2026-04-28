---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-reduce-type-parameter
title: @typescript-eslint/prefer-reduce-type-parameter
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-reduce-type-parameter
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:079b847708df31d806f0be7aa80866bf02c56dcbd8d8008c569c124db651e5f2
---

调用“Array#reduce”时推荐使用类型参数而不是类型断言。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-reduce-type-parameter": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. ['1', '2', '3'].reduce<readonly string[]>((arr, text) => {
2. const newArr = [...arr];
3. newArr.push(text);
4. return newArr;
5. }, []);
```

## 反例

```
1. ['1', '2', '3'].reduce((arr, text) => {
2. const newArr = [...arr];
3. newArr.push(text);
4. return newArr;
5. }, [] as readonly string[]);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
