---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-useless-constructor
title: "@typescript-eslint/no-useless-constructor"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-useless-constructor
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9d28c00fc67922958cf3a3f8a64ee13c0bc57a17b544a2dedff6587e5a6f1216
---

禁止不必要的构造函数。

不必要的构造函数包括：空的构造函数，或者构造函数中直接执行父类构造函数的逻辑。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-useless-constructor": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
class A {
  public name: string = 'hello';
}

export class B {
  public name: string = 'name';

  public constructor() {
    console.info('hello');
  }
}

export class C extends A {
  public constructor() {
    super();
    console.info('hello');
  }
}
```

## 反例

```screen
class A {
  public name: string = 'name';

  constructor() {

  }
}

export class B extends A {
  public name: string = 'name';

  constructor() {
    super();
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
