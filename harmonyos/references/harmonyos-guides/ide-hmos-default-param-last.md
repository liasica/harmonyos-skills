---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-default-param-last
title: "@typescript-eslint/default-param-last"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/default-param-last
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a643d6c22b5bb31ca922cc05a8d47e03a750ab2b1cb0f7083857507f8b4f2cbc
---

强制默认参数位于参数列表的最后一个。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/default-param-last": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
const defaultValue = 0;
export function f1(a = defaultValue) {
  return a;
}
export function f2(a: number, b = defaultValue) {
  return a + b;
}
export function f3(a: number, b?: number) {
  return b !== undefined ? a + b : a;
}
export function f4(a: number, b?: number, c = defaultValue) {
  return b !== undefined ? a + b + c : a + c;
}
export function f5(a: number, b = defaultValue, c?: number) {
  return c !== undefined ? a + c : a + b;
}
```

## 反例

```ts
const defaultValue = 0;
export function f2(b = defaultValue, a: number) {
  return a + b;
}
export function f3(b?: number, a: number) {
  return b !== undefined ? a + b : a;
}
export function f4(b?: number, a: number, c = defaultValue) {
  return b !== undefined ? a + b + c : a + c;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
