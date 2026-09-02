---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-assertion
title: "@typescript-eslint/no-unnecessary-type-assertion"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-assertion
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fff19fd3bd44e172f64484a5c4e09dc9c2ca87668dcd9caf4ba213d907e80dc7
---

禁止不必要的类型断言。

如果类型断言没有更改表达式的类型，也就没有必要使用。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-assertion": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-unnecessary-type-assertion选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-type-assertion/#options)。

## 正例

```screen
const num = 3;
export const foo2 = num as number;
export const foo3 = 'foo' as string;
```

## 反例

```screen
const num = 3;
export const foo = num;
export const bar = foo!;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
