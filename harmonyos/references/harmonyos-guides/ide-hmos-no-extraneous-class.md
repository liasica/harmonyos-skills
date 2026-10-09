---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-extraneous-class
title: "@typescript-eslint/no-extraneous-class"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extraneous-class
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1edd3d8db7c3910fbabe38ff269d6d13451dc26d40bf3d8b4b9f1c1f080f936c
---

不允许将类用作命名空间。

## 规则配置

```json
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

```ts
export const version = 42;

export function isProduction() {
  return version === 'production'.length;
}

export function logHelloWorld() {
  console.log('Hello, world!');
}
```

## 反例

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
