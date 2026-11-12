---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-optional-chain
title: "@typescript-eslint/prefer-optional-chain"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-optional-chain
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7db9ca2323d4dc1f77c3c000f0d4f97ab9c2ef3b37e21c8e5e6f98f5b7a41576
---

强制使用链式可选表达式，而不是链式逻辑与、否定逻辑或、以及空对象。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-optional-chain": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/prefer-optional-chain选项](https://typescript-eslint.nodejs.cn/rules/prefer-optional-chain/#options)。

## 正例

```screen
class Foo {
  public a?: Foo = new Foo();

  public b?: Foo = new Foo();

  public c?: Foo = new Foo();

  public method?(): void {
    console.info('method');
  }
}

const foo = new Foo();
export const c = foo.a?.b?.c;
foo.a?.b?.method?.();
```

## 反例

```screen
class Foo {
  public a?: Foo = new Foo();

  public b?: Foo = new Foo();

  public c?: Foo = new Foo();

  public method?(): void {
    console.info('method');
  }
}

const foo = new Foo();
let c = foo.a;
c = c && c.b;
c = c && c.c;
export { c };
if (foo.a && foo.a.b && foo.a.b.method) {
  foo.a.b.method();
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
