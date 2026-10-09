---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-useless-constructor
title: "@typescript-eslint/no-useless-constructor"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-useless-constructor
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fb646a87e08a649f3b86035d9383e18825f6db271e764f23fc029c0ec96ddb25
---

禁止不必要的构造函数。

不必要的构造函数包括：空的构造函数，或者构造函数中直接执行父类构造函数的逻辑。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-useless-constructor": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
