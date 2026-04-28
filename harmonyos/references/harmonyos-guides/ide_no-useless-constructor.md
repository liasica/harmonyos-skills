---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-useless-constructor
title: @typescript-eslint/no-useless-constructor
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-useless-constructor
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:43+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b50abcc4ebfdc5ba09d1b811a4234fddf73842cc60d5b86a14efa62e15637709
---

禁止不必要的构造函数。

不必要的构造函数包括：空的构造函数，或者构造函数中直接执行父类构造函数的逻辑。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-useless-constructor": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class A {
2. public name: string = 'hello';
3. }

5. export class B {
6. public name: string = 'name';

8. public constructor() {
9. console.info('hello');
10. }
11. }

13. export class C extends A {
14. public constructor() {
15. super();
16. console.info('hello');
17. }
18. }
```

## 反例

```
1. class A {
2. public name: string = 'name';

4. constructor() {

6. }
7. }

9. export class B extends A {
10. public name: string = 'name';

12. constructor() {
13. super();
14. }
15. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
