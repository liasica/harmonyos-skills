---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-keyword-spacing-stylistic
title: @hw-stylistic/keyword-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/keyword-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:26+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9678a35a38b20473c6d1128ddcde94e628e075ef5e936ec79d6871c803ae5e45
---

在关键字前后强制加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/keyword-spacing": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export function test(a: number, b: number) {
2. if (a > b) {
3. console.info('doSomething');
4. } else if (a === b) {
5. console.info('doSomething');
6. } else {
7. console.info('doSomething');
8. }

10. for (const item of [a, b]) {
11. console.info(`${item}`);
12. }
13. }
```

## 反例

```
1. export function test(a: number, b: number) {
2. // Expected space after 'if'.
3. if(a > b) {
4. console.info('doSomething');
5. // Expected space before 'else'.
6. // Expected space after 'if'.
7. }else if(a === b) {
8. console.info('doSomething');
9. // Expected space before 'else'.
10. // Expected space after 'else'.
11. }else{
12. console.info('doSomething');
13. }

15. // Expected space after 'for'.
16. for(const item of [a, b]) {
17. console.info(`${item}`);
18. }
19. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
