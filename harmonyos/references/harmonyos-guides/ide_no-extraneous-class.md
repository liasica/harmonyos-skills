---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extraneous-class
title: "@typescript-eslint/no-extraneous-class"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extraneous-class
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8e295414ca1991b97688673711d31e239458c2b318b6c94c668c9b1093c502d8
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
