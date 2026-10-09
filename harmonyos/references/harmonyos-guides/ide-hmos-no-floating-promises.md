---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-floating-promises
title: "@typescript-eslint/no-floating-promises"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-floating-promises
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b6ed0d62b6d9f6452f508af835e913aea2a885424d7ec85cbf363a8af5cc9c04
---

要求正确处理Promise表达式。

floating-promise是指在创建Promise时，没有使用任何代码来处理它可能引发的错误，这是一种不正确的使用方式。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-floating-promises": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-floating-promises选项](https://typescript-eslint.nodejs.cn/rules/no-floating-promises/#options)。

## 正例

```ts
export async function bar() {
  const promise = new Promise<string>(resolve => {
    resolve('value');
    return 'finish';
  });
  await promise;

  Promise.reject('value').catch(() => {
    console.error('error');
  });

  await Promise.reject('value').finally(() => {
    console.info('finally');
  });

  await Promise.all(['1', '2', '3'].map(x => x + '1'));
}
```

## 反例

```ts
export async function bar() {
  const promise = new Promise<string>(resolve => {
    resolve('value');
    return 'finish';
  });
  promise;

  Promise.reject('value').catch();

  await Promise.reject('value').finally();

  ['1', '2', '3'].map(async x => x + '1');
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
