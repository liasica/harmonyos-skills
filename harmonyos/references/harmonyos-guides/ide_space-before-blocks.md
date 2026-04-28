---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-before-blocks
title: @hw-stylistic/space-before-blocks
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/space-before-blocks
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:31+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:983aa74e6388305dde1c47414827aba71324ed8785f13ade5004bca4d668ec3e
---

强制在“{”之前加空格。该规则仅检查.ets文件类型。

例外：

* 函数的第一个参数或者数组中的第一个元素是对象，对象的“{”之前不用加空格。
* 模板代码中的“{”之前不用加空格。
* 行首的“{”之前不用加空格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/space-before-blocks": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export function a() {
2. // doSomething
3. }

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Column() {
11. Text('Hello World')
12. }
13. .width('100%')
14. }
15. .height('100%')
16. }
17. }
```

## 反例

```
1. // Missing space before opening brace.
2. export function a(){
3. // doSomething
4. }

6. @Entry
7. @Component
8. // Missing space before opening brace.
9. struct Index{
10. // Missing space before opening brace.
11. build(){
12. // Missing space before opening brace.
13. Row(){
14. // Missing space before opening brace.
15. Column(){
16. Text('Hello World')
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
