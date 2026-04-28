---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-semi
title: @typescript-eslint/no-extra-semi
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-semi
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:33+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7791b82a77bb644926b59f6c2ba17f5bcd08e020a898f503a230cc6135173f68
---

禁止使用不必要的分号。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-extra-semi": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export const x = 5;

3. export function foo() {
4. // code
5. }

7. export const bar = () => {
8. // code
9. };

11. export class C {
12. public field: string = 'field';

14. static {
15. // code
16. }

18. public method() {
19. // code
20. }
21. }
```

## 反例

```
1. export const x = 5;;

3. export function foo() {
4. // code
5. };

7. export const bar = () => {
8. // code
9. };;

11. export class C {
12. public field: string = 'field';;

14. static {
15. // code
16. };

18. public method() {
19. // code
20. };
21. };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
