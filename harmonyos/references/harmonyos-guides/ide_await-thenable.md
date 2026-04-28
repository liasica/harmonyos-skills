---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_await-thenable
title: @typescript-eslint/await-thenable
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/await-thenable
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a85eaff486948c5e4f408443e9c68ee5721066198de280becca7253b06d7774c
---

不允许对不是“Thenable”对象的值使用await关键字（“Thenable”表示某个对象拥有“then”方法，比如Promise）。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/await-thenable": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. async function test() {
2. await Promise.resolve('value');
3. }

5. export { test };
```

## 反例

```
1. async function test() {
2. await 'value';
3. }

5. export { test };
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
