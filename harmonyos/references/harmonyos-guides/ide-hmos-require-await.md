---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-require-await
title: "@typescript-eslint/require-await"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/require-await
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:767bfb50cc04069ecac88db6d5767d0097c95d4db825d4a856f2e51cf218e3b8
---

异步函数必须包含“await”。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-await": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  await doSomething();
}

export function baz() {
  doSomething().catch(() => {
    console.info('error');
  });
}
```

## 反例

```ts
async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  doSomething();
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
