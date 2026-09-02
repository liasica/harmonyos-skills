---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-boolean-literal-compare
title: "@typescript-eslint/no-unnecessary-boolean-literal-compare"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-boolean-literal-compare
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:04790c156d38a7bc1a3cd9d7f335e2fd1965a8a40d86aaeb0db072887aad26e7
---

禁止将布尔值和布尔字面量直接进行比较。

## 规则配置

```screen
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

```screen
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

```screen
declare const someCondition: boolean;
// 禁止将布尔变量和布尔字面量直接比较，直接使用someCondition判断即可
if (someCondition === true) {
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
