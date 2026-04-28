---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_promise-function-async
title: @typescript-eslint/promise-function-async
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/promise-function-async
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2d16f52f1b3ad2df6a6b4127abb0f8ab56c30dc755bea6ac4d3324ee524df7c5
---

要求任何返回Promise的函数或方法标记为async。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/promise-function-async": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/promise-function-async选项](https://typescript-eslint.nodejs.cn/rules/promise-function-async/#options)。

## 正例

```
1. export const arrowFunctionReturnsPromise = async () => Promise.resolve('value');

3. export async function functionReturnsPromise() {
4. return Promise.resolve('value');
5. }

7. // An explicit return type that is not Promise means this function cannot be made async, so it is ignored by the rule
8. export function functionReturnsUnionWithPromiseExplicitly(
9. p: boolean
10. ): string | Promise<string> {
11. return p ? 'value' : Promise.resolve('value');
12. }

14. export async function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
15. return p ? 'value' : Promise.resolve('value');
16. }
```

## 反例

```
1. export const arrowFunctionReturnsPromise = () => Promise.resolve('value');

3. export function functionReturnsPromise() {
4. return Promise.resolve('value');
5. }

7. export function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
8. return p ? 'value' : Promise.resolve('value');
9. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
