---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-readonly-parameter-types
title: @typescript-eslint/prefer-readonly-parameter-types
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-readonly-parameter-types
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6d364c672b27464d4872aa241ecfd53b826867dbdd68d2122ad4c37e9b95df14
---

要求将函数参数解析为“只读”类型，以防止参数被修改而产生一些副作用，更多规则详情请参考[prefer-readonly-parameter-types](https://typescript-eslint.nodejs.cn/rules/prefer-readonly-parameter-types)。

该规则校验比较严格，由开发者自主判断是否需要修复告警。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-readonly-parameter-types": "warn"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/prefer-readonly-parameter-types选项](https://typescript-eslint.nodejs.cn/rules/prefer-readonly-parameter-types/#options)。

## 正例

```
1. const index = 0;
2. export function array1(arg: readonly string[]): void {
3. console.info(`${arg[index]}`);
4. }

6. export function array2(arg: readonly (readonly string[])[]): void {
7. console.info(`${arg[index][index]}`);
8. }
9. export function array3(arg: readonly [string, number]): void {
10. console.info(`${arg[index][index]}`);
11. }

13. export function array4(arg: readonly [readonly string[], number]): void {
14. console.info(`${arg[index][index]}`);
15. }

17. export function primitive1(arg: string): void {
18. console.info(`${arg}`);
19. }

21. export function primitive2(arg: number): void {
22. console.info(`${arg}`);
23. }

25. export function primitive3(arg: boolean): void {
26. console.info(`${arg}`);
27. }

29. export function primitive5(arg: null): void {
30. console.info(`${arg}`);
31. }

33. export function primitive6(arg: undefined): void {
34. console.info(`${arg}`);
35. }
```

## 反例

```
1. const index = 0;
2. export function array1(arg: string[]): void {
3. console.info(`${arg[index]}`);
4. }

6. export function array2(arg: (string[])[]): void {
7. console.info(`${arg[index][index]}`);
8. }
9. export function array3(arg: [string, number]): void {
10. console.info(`${arg[index][index]}`);
11. }

13. export function array4(arg: [string[], number]): void {
14. console.info(`${arg[index][index]}`);
15. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
