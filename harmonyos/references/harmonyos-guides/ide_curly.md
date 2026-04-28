---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_curly
title: @hw-stylistic/curly
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/curly
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:798534bca47a209f323e631c03f217de8d161a4db3b48be44ce2627b85120a06
---

条件语句和循环语句的逻辑代码必须写在大括号中。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/curly": "error"
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

10. while (a > b) {
11. a--;
12. console.info('doSomething');
13. }

15. console.info('doSomething');
16. }
```

## 反例

```
1. export function test(a: number, b: number) {
2. if (a > b)
3. // Expected { after 'if' condition.
4. console.info('doSomething');
5. else if (a === b)
6. // Expected { after 'if' condition.
7. console.info('doSomething');
8. else
9. // Expected { after 'else'.
10. console.info('doSomething');
11. console.info('doSomething');
12. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
