---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_promise-function-async
title: "@typescript-eslint/promise-function-async"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/promise-function-async
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8927aaba80aa81bf628854116f3ed3d28e542aceca1203672487fcf26cd0cdb4
---

要求任何返回Promise的函数或方法标记为async。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/promise-function-async": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/promise-function-async选项](https://typescript-eslint.nodejs.cn/rules/promise-function-async/#options)。

## 正例

```screen
export const arrowFunctionReturnsPromise = async () => Promise.resolve('value');

export async function functionReturnsPromise() {
  return Promise.resolve('value');
}

// An explicit return type that is not Promise means this function cannot be made async, so it is ignored by the rule
export function functionReturnsUnionWithPromiseExplicitly(
  p: boolean
): string | Promise<string> {
  return p ? 'value' : Promise.resolve('value');
}

export async function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
```

## 反例

```screen
export const arrowFunctionReturnsPromise = () => Promise.resolve('value');

export function functionReturnsPromise() {
  return Promise.resolve('value');
}

export function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
