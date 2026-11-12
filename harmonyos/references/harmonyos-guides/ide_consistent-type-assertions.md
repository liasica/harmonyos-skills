---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-assertions
title: "@typescript-eslint/consistent-type-assertions"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-assertions
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:62bed91e4dc131d695a09b0a436c65a4537d9230a2f782713863990beb0864dc
---

强制使用一致的类型断言。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/consistent-type-assertions": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/consistent-type-assertions选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-assertions/#options)。

## 正例

```screen
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
// 默认推荐使用 value as Type：优先选择const x = value as Type; 而不是const x = <Type>value;
export const y = x as object;
```

## 反例

```screen
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
// 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = <Type>value;
export const y = <object>x;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
