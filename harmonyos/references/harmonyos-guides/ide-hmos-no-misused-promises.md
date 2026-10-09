---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-misused-promises
title: "@typescript-eslint/no-misused-promises"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-misused-promises
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:77753c7d127870f5caf29e1c658375c44058f8109ef0d9f1f7f07dc06ce26971
---

禁止在不正确的位置使用Promise。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-misused-promises": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-misused-promises选项](https://typescript-eslint.nodejs.cn/rules/no-misused-promises/#options)。

## 正例

```ts
export async function func(): void {
  const promise = Promise.resolve('value');

  // Always `await` the Promise in a conditional
  if (await promise) {
    // Do something
  }

  const val = await promise ? '123' : '456';
  console.log(`${val}`);

  while (await promise) {
    // Do something
  }
}
```

## 反例

```ts
export async function func(): void {
  const promise = Promise.resolve('value');
  // 默认条件语句中需要使用await Promise
  if (promise) {
    // Do something
  }

  // 默认条件语句中需要使用await Promise
  const val = promise ? '123' : '456';
  console.log(`${val}`);

  // 默认条件语句中需要使用await Promise
  while (promise) {
    // Do something
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
