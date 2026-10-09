---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-non-null-asserted-optional-chain
title: "@typescript-eslint/no-non-null-asserted-optional-chain"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-non-null-asserted-optional-chain
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:355cbc126acb23a8f149301dca042ea0ae577562869619801b629a3edbfa5fc6
---

禁止在可选链表达式之后使用非空断言。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-non-null-asserted-optional-chain": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
class CC {
  public bar = 'hello';

  public foo(): void {
    console.info('foo');
  }
}
```

```ts
function getInstance(): CC | undefined {
  return new CC();
}

const instance = getInstance();
console.info(`${instance?.bar}`);
instance?.foo();
```

## 反例

```ts
class CC {
  public bar: string = 'hello';

  public foo() {
    console.info('foo');
  }
}

function getInstance(): CC | undefined {
  return new CC();
}

const instance = getInstance();
console.info(`${instance?.bar!}`);
instance?.foo()!;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
