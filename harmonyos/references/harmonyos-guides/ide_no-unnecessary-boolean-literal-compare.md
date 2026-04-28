---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-boolean-literal-compare
title: @typescript-eslint/no-unnecessary-boolean-literal-compare
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-boolean-literal-compare
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2d486b92523429fc090e9b19d22b69179336a3111e667d71ace1a489fe78b7b4
---

禁止将布尔值和布尔字面量直接进行比较。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unnecessary-boolean-literal-compare": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-unnecessary-boolean-literal-compare选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-boolean-literal-compare/#options)。

## 正例

```
1. declare const someCondition: boolean;
2. if (someCondition) {
3. }

5. declare const someObjectBoolean: boolean | Record<string, object>;
6. if (someObjectBoolean === true) {
7. }

9. declare const someStringBoolean: boolean | string;
10. if (someStringBoolean === true) {
11. }
```

## 反例

```
1. declare const someCondition: boolean;
2. // 禁止将布尔变量和布尔字面量直接比较，直接使用someCondition判断即可
3. if (someCondition === true) {
4. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
