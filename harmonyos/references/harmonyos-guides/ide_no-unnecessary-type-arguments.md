---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-arguments
title: @typescript-eslint/no-unnecessary-type-arguments
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-arguments
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:40+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b6760e5ba40caba077fed2b867ece82cdf6d1fde5ea9f5c18347546a55b2ee39
---

当类型参数和默认值相同时，不允许显式使用。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unnecessary-type-arguments": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. function f<T = number>(para: T): void {
2. console.info(`${para as number}`);
3. }
4. f(Number.MAX_VALUE);
5. f<string>('hello');

7. function g<T = number, U = string>(para1: T, para2?: U) {
8. if (para2 !== undefined) {
9. console.info(`${para2 as string}`);
10. }
11. console.info(`${para1 as number}`);
12. }
13. g<string>('para1', 'para2');
14. g<number, number>(Number.MAX_VALUE);

16. class C<T = number> {
17. public name: T;

19. public constructor(name: T) {
20. this.name = name;
21. }
22. }
23. new C(Number.MAX_VALUE);
24. new C<string>('hello');
```

## 反例

```
1. function f<T = number>(para: T): void {
2. console.info(`${para as number}`);
3. }
4. // 参数类型默认是number，直接使用f()即可
5. f<number>(Number.MAX_VALUE);

7. function g<T = number, U = string>(para1: T, para2?: U) {
8. if (para2 !== undefined) {
9. console.info(`${para2 as string}`);
10. }
11. console.info(`${para1 as number}`);
12. }
13. // 第二个参数类型默认是string，直接使用g<string>()即可
14. g<string, string>('hello');

16. class C<T = number> {
17. public meth(para: T): void {
18. console.info(`${para as number}`);
19. }
20. }
21. // 参数类型默认是number，直接使用new C()即可
22. new C<number>();
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
