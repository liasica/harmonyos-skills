---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-redeclare
title: @typescript-eslint/no-redeclare
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-redeclare
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d95bd659761206b635c5fc6a1e46672e1488a045d6b7d9e807bf73bc04d2f6c6
---

禁止变量重复声明。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-redeclare": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-redeclare选项](https://eslint.nodejs.cn/docs/rules/no-redeclare#选项)。

## 正例

```
1. let a = '3';
2. a = '10';
3. console.info(a);

5. export class C {
6. static {
7. let c = '3';
8. c = '10';
9. console.info(c);
10. }

12. public foo() {
13. let b = '3';
14. b = '10';
15. console.info(b);
16. }
17. }
```

## 反例

```
1. // 不允许重复声明变量a
2. const a = '3';
3. const a = '10';

5. export class C {
6. static {
7. // 不允许重复声明变量c
8. const c = '3';
9. const c = '10';
10. }

12. public foo() {
13. // 不允许重复声明变量b
14. const b = '3';
15. const b = '10';
16. }
17. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
