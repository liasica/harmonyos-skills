---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unnecessary-boolean-literal-compare
title: "@typescript-eslint/no-unnecessary-boolean-literal-compare"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-boolean-literal-compare
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5e638b60f736c32eb21fb82fbc86d04b8a42b14ac603e30f8c5811ebf0ebcf8f
---

禁止将布尔值和布尔字面量直接进行比较。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-boolean-literal-compare": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-unnecessary-boolean-literal-compare选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-boolean-literal-compare/#options)。

## 正例

```ts
declare const someCondition: boolean;
if (someCondition) {
}

declare const someObjectBoolean: boolean | Record<string, object>;
if (someObjectBoolean === true) {
}

declare const someStringBoolean: boolean | string;
if (someStringBoolean === true) {
}
```

## 反例

```ts
declare const someCondition: boolean;
// 禁止将布尔变量和布尔字面量直接比较，直接使用someCondition判断即可
if (someCondition === true) {
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
