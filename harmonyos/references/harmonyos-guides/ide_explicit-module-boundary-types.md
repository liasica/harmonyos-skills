---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-module-boundary-types
title: @typescript-eslint/explicit-module-boundary-types
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/explicit-module-boundary-types
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:27+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8993f4521407254f53d013a0a185e08c9755254fa28f1a0b56ba806d3b97c305
---

导出到外部的函数和公共类方法，需要显式的定义返回类型和参数类型。

该规则仅支持对.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/explicit-module-boundary-types": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/explicit-module-boundary-types选项](https://typescript-eslint.nodejs.cn/rules/explicit-module-boundary-types/#options)。

## 正例

```
1. // A function with no return value (void)
2. export function test1(): void {
3. return;
4. }

6. // A return value of type string
7. export const arrowFn1 = (): string => 'test';

9. // All arguments should be typed
10. export const arrowFn2 = (arg: string): string => `test ${arg}`;

12. export class Test {
13. // A class method with no return value (void)
14. public method(): void {
15. return;
16. }
17. }

19. // The function does not apply because it is not an exported function.
20. function test2() {
21. return;
22. }

24. test2();
```

## 反例

```
1. // Should indicate that no value is returned (void)
2. export function test() {
3. return;
4. }

6. // Should indicate that a string is returned
7. export const arrowFn1 = () => 'test';

9. // All arguments should be typed
10. export const arrowFn2 = (arg): string => `test ${arg}`;
11. export const arrowFn3 = (arg: any): string => `test ${arg}`;

13. export class Test {
14. // Should indicate that no value is returned (void)
15. public method() {
16. return;
17. }
18. }
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
