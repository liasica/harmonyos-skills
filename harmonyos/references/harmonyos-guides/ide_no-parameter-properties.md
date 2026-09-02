---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-parameter-properties
title: "@typescript-eslint/no-parameter-properties"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-parameter-properties
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:025f8d53b2b421a4aafc3109702c864b5c4d888bdf6cfa91a856a5f91c91477d
---

禁止在类构造函数中使用参数属性。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-parameter-properties": "error"
  }
}
```

## 选项

默认禁止在构造函数中使用任何参数属性，如果想要使用某些属性，可以配置额外选项。

allows：接受一个字符串数组，数组中的属性可以使用。字符串支持以下值：

* readonly
* private
* protected
* public
* private readonly
* protected readonly
* public readonly

示例：

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-parameter-properties": ["error", {"allows": ["readonly"]}]
  }
}
```

## 正例

```screen
export class Foo {
  public name: string;

  public constructor(name: string) {
    this.name = name;
  }
}
```

## 反例

```screen
export class Foo {
  // 默认配置下，参数不允许使用readonly
  public constructor(public readonly name: string) {}
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
