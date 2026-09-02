---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-assertion
title: "@typescript-eslint/no-non-null-assertion"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c9ac9bb48df5b0f5a8e7d36f93f2e11e3a569ca6fff6449a5d8428c76f2edba6
---

禁止以感叹号作为后缀的方式使用非空断言。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-non-null-assertion": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
interface Example {
  property?: string;
}

declare const example: Example;
export const includesBaz = example.property?.includes('baz') ?? false;
```

## 反例

```screen
interface Example {
  property?: string;
}

declare const example: Example;
// 禁止使用"example.property!"的方式来进行非空断言
export const includesBaz = example.property!.includes('baz');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
