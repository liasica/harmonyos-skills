---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-assertions
title: @typescript-eslint/consistent-type-assertions
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-assertions
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1ee5a0e2a3ebcd8726241f745cbaf0cb3ad4264c37466f7cce066c783a2a1980
---

强制使用一致的类型断言。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/consistent-type-assertions": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/consistent-type-assertions选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-assertions/#options)。

## 正例

```
1. interface MyType {
2. name: string;
3. }
4. export const x: MyType = {
5. name: 'hello'
6. };
7. // 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = <Type>value;
8. export const y = x as object;
```

## 反例

```
1. interface MyType {
2. name: string;
3. }
4. export const x: MyType = {
5. name: 'hello'
6. };
7. // 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = <Type>value;
8. export const y = <object>x;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
