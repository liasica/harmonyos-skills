---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-throw-literal
title: "@typescript-eslint/no-throw-literal"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-throw-literal
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7b7f0d95908dfb611db5495a2d508653e8b7ef7f005e332666d4a5ec0d736f76
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
