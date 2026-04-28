---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-condition
title: @typescript-eslint/no-unnecessary-condition
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-condition
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3abb7f3244c4414f9bd8b747658034441940b9e9bade7d2cb8a302cf6e7594e5
---

不允许使用类型始终为真或始终为假的表达式作为判断条件。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unnecessary-condition": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-unnecessary-condition选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-condition/#options)。

## 正例

```
1. const index = 0;
2. export function head(items: readonly string[]): string {
3. // Necessary, since items.length might be 0
4. if (items.length) {
5. return items[index].toUpperCase();
6. } else {
7. return '';
8. }
9. }

11. export function foo(arg: string): void {
12. // Necessary, since foo might be ''.
13. if (arg) {
14. }
15. }

17. export function bar(arg?: string | null) {
18. // Necessary, since arg might be nullish
19. return arg?.length;
20. }
```

## 反例

```
1. const index = 0;
2. export function head(items: readonly string[]) {
3. // items can never be nullable, so this is unnecessary
4. if (items) {
5. return items[index].toUpperCase();
6. } else {
7. return '';
8. }
9. }

11. export function foo(arg: 'bar' | 'baz') {
12. // arg is never nullable or empty string, so this is unnecessary
13. if (arg) {
14. }
15. }

17. export function bar(arg: string) {
18. // arg can never be nullish, so ?. is unnecessary
19. return arg?.length;
20. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
