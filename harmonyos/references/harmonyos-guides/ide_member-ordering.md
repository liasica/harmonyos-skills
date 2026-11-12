---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_member-ordering
title: "@typescript-eslint/member-ordering"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/member-ordering
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d0c4a0283044d55cc471c956e48949658c0fbbecc66c5500c4c553b7411aed61
---

要求类、接口和类型字面量中成员的排序方式保持一致的风格。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/member-ordering": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/member-ordering选项](https://typescript-eslint.nodejs.cn/rules/member-ordering/#options)。

## 正例

```screen
// 默认排序规则：field-constructor-method
export class Foo2 {
  // -> field
  protected static e: string = '';

  public d: string = '';

  private readonly c: string = '';

  // -> constructor
  public constructor() {
    console.info('constructor');
  }

  // -> method
  public static a(): void {
    console.info('static method');
  }

  public b(): void {
    console.info(this.c);
  }
}
```

## 反例

```screen
// 默认排序规则：field-constructor-method
export class Foo2 {
  // -> method
  public static a(): void {
    console.info('static method');
  }

  public b(): void {
    console.info(this.c);
  }

  // -> field
  protected static e: string = '';

  private readonly c: string = '';

  public d: string = '';

  // -> constructor
  public constructor() {
    console.info('constructor');
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
