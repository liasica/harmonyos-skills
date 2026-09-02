---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-promises
title: "@typescript-eslint/no-misused-promises"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-misused-promises
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8820c2450af367983b341b991defaacb5de4a270918222b96394ea96d597563a
---

禁止在不正确的位置使用Promise。

## 规则配置

```screen
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

```screen
export async function func(): Promise<void>{
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

```screen
export async function func(): Promise<void>{
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
