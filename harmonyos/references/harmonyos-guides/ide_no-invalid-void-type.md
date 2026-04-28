---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-invalid-void-type
title: @typescript-eslint/no-invalid-void-type
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-invalid-void-type
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:dadeb51680e4acc53de1beaf5e950bf62bcadf28c8ce391abb9ba6014ab7a4d1
---

禁止在返回类型或者泛型类型之外使用void。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-invalid-void-type": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-invalid-void-type选项](https://typescript-eslint.nodejs.cn/rules/no-invalid-void-type/#options)。

## 正例

```
1. export type NoOp = () => void;
2. export function noop(): void {
3. console.info('noop');
4. }
5. export const trulyUndefined = void Number.MAX_VALUE;
6. export async function promiseMeSomething(): Promise<void> {
7. return Promise.reject('value').catch(() => {
8. console.error('error');
9. });
10. }
11. export type StillVoid = void | never;
```

## 反例

```
1. // 不允许使用void作为类型
2. export type PossibleValues = string | number | void;
3. // 不允许使用void作为类型
4. export type MorePossibleValues = string | (string | void);

6. // 不允许使用void作为类型
7. export function logSomething(thing: void) {
8. return thing;
9. }
10. export function printArg<T = void>(arg: T) {
11. return arg;
12. }

14. export interface Interface {
15. lambda: () => void;
16. // 不允许使用void作为类型
17. prop: void;
18. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
