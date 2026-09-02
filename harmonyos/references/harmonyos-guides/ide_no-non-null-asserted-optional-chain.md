---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-asserted-optional-chain
title: "@typescript-eslint/no-non-null-asserted-optional-chain"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-non-null-asserted-optional-chain
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d12caf6feef4ef0c7bbf166e55abceb157d3512e71327fccd80d59841d0fe6fc
---

禁止在可选链表达式之后使用非空断言。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-non-null-asserted-optional-chain": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
class CC {
  public bar = 'hello';

  public foo(): void {
    console.info('foo');
  }
}
function getInstance(): CC | undefined {
  return new CC();
}

const instance = getInstance();
console.info(`${instance?.bar}`);
instance?.foo();
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
