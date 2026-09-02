---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-throw-literal
title: "@typescript-eslint/no-throw-literal"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-throw-literal
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3caec03b65e5cecb2b37fb3c9822e1140b1e14255574c4e4ea5a55ff5a3692a3
---

禁止将字面量作为异常抛出。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-throw-literal": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-throw-literal选项](https://typescript-eslint.nodejs.cn/rules/no-throw-literal#options)。

## 正例

```screen
// 抛出Error对象
throw new Error();

const e = new Error('error');
throw e;

const err1 = new Error();
throw err1;

function err2() {
  return new Error();
}
throw err2();

class CustomError extends Error {
  // ...
}
throw new CustomError();
```

## 反例

```screen
throw 'error';

throw 0;

throw undefined;

throw null;

const err1 = new Error();
throw 'an ' + err1;

const err2 = new Error();
throw `${err2}`;

const err3 = '';
throw err3;

function err() {
  return '';
}
throw err();
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
