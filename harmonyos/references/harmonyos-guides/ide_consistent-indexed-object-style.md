---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-indexed-object-style
title: @typescript-eslint/consistent-indexed-object-style
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-indexed-object-style
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3da19ed01b1fb84d20c76667f2a9b3a3c3da94e47076fea77b4b48633d569d11
---

允许或禁止使用“Record”类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/consistent-indexed-object-style": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/consistent-indexed-object-style选项](https://typescript-eslint.nodejs.cn/rules/consistent-indexed-object-style/#options)。

## 正例

```
1. // 默认推荐使用Record 类型
2. export type Foo = Record<string, unknown>;
```

## 反例

```
1. export interface Foo1 {
2. // 默认推荐使用Record 类型
3. [key: string]: unknown;
4. }

6. export type Foo2 = {
7. // 默认推荐使用Record 类型
8. [key: string]: unknown;
9. };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
