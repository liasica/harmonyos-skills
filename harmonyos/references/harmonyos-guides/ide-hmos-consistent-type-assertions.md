---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-consistent-type-assertions
title: "@typescript-eslint/consistent-type-assertions"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-assertions
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c8b900360a36248c1fc016557509693004e323ab2b57e59b5ac53f12d8e88c84
---

强制使用一致的类型断言。

## 规则配置

```json
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

```ts
// 默认推荐使用 ... as foo， 始终优先选择 const x = { ... } as T; 而不是const x: T = { ... };
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
export const y = x as object;
```

## 反例

```ts
// 默认推荐使用 ... as foo， 始终优先选择 const x = { ... } as T; 而不是const x: T = { ... };
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
export const y = <object>x;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
