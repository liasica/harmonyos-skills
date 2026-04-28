---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-invalid-this
title: @typescript-eslint/no-invalid-this
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-invalid-this
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:880c923317f8e664eb76d370e65bdc6cb51eb6bc6e85ecdfb530b430b5b4dd97
---

禁止在this值为undefined的上下文中使用this。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-invalid-this": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-invalid-this选项](https://eslint.nodejs.cn/docs/rules/no-invalid-this#选项)。

## 正例

```
1. // ts代码文件中需要添加"use strict"
2. function baz(arg0: () => object) {
3. return arg0;
4. }

6. export class Bar {
7. public a: number;

9. public constructor() {
10. this.a = 0;
11. baz(() => this);
12. }
13. }
```

## 反例

```
1. // ts代码文件中需要添加"use strict"
2. function baz(arg0: () => object) {
3. return arg0;
4. }

6. export function foo1() {
7. this.a = 0;
8. baz(() => this);
9. }

11. export const foo2 = () => {
12. this.a = 0;
13. baz(() => this);
14. };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
