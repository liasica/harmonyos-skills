---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-restricted-syntax
title: @typescript-eslint/no-restricted-syntax
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-restricted-syntax
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2a9557f4c3258fab0bc978a99dbd520240ba226d4c5da0e52daf4c4b75cf557b
---

不允许使用指定的（即用户在规则中定义的）语法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-restricted-syntax": [
5. "error",
6. {
7. "selector": "FunctionExpression",
8. "message": "Function expressions are not allowed."
9. },
10. {
11. "selector": "CallExpression[callee.name='setTimeout'][arguments.length!=2]",
12. "message": "setTimeout must always be invoked with two arguments."
13. }
14. ]
15. }
16. }
```

## 选项

详情请参考[@typescript-eslint/no-restricted-syntax选项](https://eslint.nodejs.cn/docs/latest/rules/no-restricted-syntax#选项)。

## 正例

```
1. /* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
2. export function doSomething() {
3. console.info('doSomething');
4. }
```

## 反例

```
1. /* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
2. export class CC {
3. public name: string;

5. public constructor(name: string) {
6. this.name = name;
7. }
8. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
