---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_strict-boolean-expressions
title: @typescript-eslint/strict-boolean-expressions
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/strict-boolean-expressions
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:328022258fa6cde46780c9dc266aff149f16db4d9c107fd7a4411a2fc15445f1
---

不允许在布尔表达式中使用非布尔类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/strict-boolean-expressions": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/strict-boolean-expressions选项](https://typescript-eslint.nodejs.cn/rules/strict-boolean-expressions/#options)。

## 正例

```
1. // nullable values should be checked explicitly against null or undefined
2. function getNum(): number | undefined {
3. return undefined;
4. }

6. const num: number | undefined = getNum();
7. if (num !== undefined) {
8. console.log('num is defined');
9. }

11. function getStr(): string | null {
12. return 'null';
13. }

15. const str: string | null = getStr();
16. if (str !== null) {
17. console.log('str is not empty');
18. }
```

## 反例

```
1. // nullable values should be checked explicitly against null or undefined
2. function getNum(): number | undefined {
3. return undefined;
4. }

6. const num: number | undefined = getNum();
7. if (num) {
8. console.log('num is defined');
9. }

11. function getStr(): string | null {
12. return 'null';
13. }

15. const str: string | null = getStr();
16. if (str) {
17. console.log('str is not empty');
18. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
