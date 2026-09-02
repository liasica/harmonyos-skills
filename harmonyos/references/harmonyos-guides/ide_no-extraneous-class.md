---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extraneous-class
title: "@typescript-eslint/no-extraneous-class"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extraneous-class
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0243686daa948da286947e6bd3e56271fa2d38c3127abe7272349db935e6a3a2
---

不允许将类用作命名空间，更多规则详情可参考[no-extraneous-class](https://typescript-eslint.nodejs.cn/rules/no-extraneous-class)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extraneous-class": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-extraneous-class选项](https://typescript-eslint.nodejs.cn/rules/no-extraneous-class/#options)。

## 正例

```screen
export const version = 42;

export function isProduction() {
  return version === 'production'.length;
}

export function logHelloWorld() {
  console.log('Hello, world!');
}
```

## 反例

```screen
export class StaticConstants {
  public static readonly version = 'development'.length;

  public static isProduction() {
    return StaticConstants.version === 'production'.length;
  }
}

export class HelloWorldLogger {
  public constructor() {
    console.log('Hello, world!');
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
