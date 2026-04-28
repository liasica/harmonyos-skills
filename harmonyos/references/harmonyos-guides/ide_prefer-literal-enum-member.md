---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-literal-enum-member
title: @typescript-eslint/prefer-literal-enum-member
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-literal-enum-member
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6f3f2541fbf81dfc966fbe9e5659c973623b083b790d136799a28b85da57ea73
---

要求所有枚举成员都定义为字面量值。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-literal-enum-member": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/prefer-literal-enum-member选项](https://typescript-eslint.nodejs.cn/rules/prefer-literal-enum-member/#options)。

## 正例

```
1. export enum Valid {
2. a = 'hello',
3. b = 'TestStr' // A regular string
4. }
```

## 反例

```
1. const str = 'Test';
2. export enum Invalid {
3. a = str, // Variable assignment
4. b = {}, // Object assignment
5. c = `A template literal string`, // Template literal
6. d = new Set(1, 2, 3), // Constructor in assignment
7. e = 2 + 2 // Expression assignment
8. }
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
