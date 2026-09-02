---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-optional-chain
title: "@typescript-eslint/prefer-optional-chain"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-optional-chain
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-06-24
content_hash: sha256:bd40815df48cdee47eadf924580043ed229a81923c9a5034a355bd8235d76f6f
---

强制使用链式可选表达式，而不是链式逻辑与、否定逻辑或、或空对象。

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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
