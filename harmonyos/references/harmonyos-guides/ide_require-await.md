---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-await
title: "@typescript-eslint/require-await"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/require-await
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a8fa6800f35730224f5ba4dfa97fbce6ef14f02dcbde5049443ab204c7e53b7d
---

异步函数必须包含“await”。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-await": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
