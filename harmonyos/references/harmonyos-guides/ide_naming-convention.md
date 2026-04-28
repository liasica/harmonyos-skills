---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_naming-convention
title: @typescript-eslint/naming-convention
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/naming-convention
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ff8e92885962bfb3a04252fc140213ce432dac0ab166bb2b6f5565564088a13d
---

强制标识符使用一致的命名风格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/naming-convention": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/naming-convention选项](https://typescript-eslint.nodejs.cn/rules/naming-convention/#options)。

## 正例

```
1. // 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
2. export class Bar {
3. public meth() {
4. console.info('method');
5. }
6. }

8. export function foo() {
9. console.info('function');
10. }
```

## 反例

```
1. // 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
2. export class bar {
3. public Meth() {
4. console.info('method');
5. }
6. }

8. export function Foo() {
9. console.info('function');
10. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
