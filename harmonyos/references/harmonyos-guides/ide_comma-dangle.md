---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-dangle
title: @typescript-eslint/comma-dangle
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/comma-dangle
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:24+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b0827864f679bdd761c9c0cb2e72e62c6383d4c016d6173565b2447c9e9a2ea3
---

允许或禁止使用尾随逗号。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/comma-dangle": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/comma-dangle选项](https://eslint.nodejs.cn/docs/rules/comma-dangle#选项)。

## 正例

```
1. // 默认不允许尾随逗号
2. interface MyType {
3. bar: string;
4. qux: string;
5. }

7. const foo: MyType = {
8. bar: 'baz',
9. qux: 'qux'
10. };

12. const arr = ['1', '2'];

14. export { foo, arr };
```

## 反例

```
1. interface MyType {
2. bar: string;
3. qux: string;
4. }

6. const foo: MyType = {
7. bar: 'baz',
8. qux: 'qux',
9. };

11. const arr = ['1', '2',];

13. export { foo, arr, };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
