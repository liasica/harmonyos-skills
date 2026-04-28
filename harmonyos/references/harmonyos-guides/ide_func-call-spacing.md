---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_func-call-spacing
title: @typescript-eslint/func-call-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/func-call-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:27+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:034a618ed9166088865cf2a9358a817b2d8b12f7858735d554239d7b437ce4f8
---

禁止或者要求函数名与函数名后面的括号之间加空格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/func-call-spacing": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/func-call-spacing选项](https://eslint.nodejs.cn/docs/rules/func-call-spacing#选项)。

## 正例

```
1. function fn() {
2. console.log('hello');
3. }

5. // 默认不允许函数名称和左括号之间有空格。
6. fn();
```

## 反例

```
1. function fn() {
2. console.log('hello');
3. }

5. // 默认不允许函数名称和左括号之间有空格。
6. fn ();

8. fn
9. ();
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
