---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-floating-promises
title: "@typescript-eslint/no-floating-promises"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-floating-promises
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a3638937b8574a313f1facdfd065eea3c1b541d0dc91c0c7ac5790d47daea138
---

要求正确处理Promise表达式。

floating-promise是指在创建Promise时，没有使用任何代码来处理它可能引发的错误，这是一种不正确的使用方式。

## 规则配置

```screen
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

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
