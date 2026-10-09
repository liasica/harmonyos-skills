---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unnecessary-type-assertion
title: "@typescript-eslint/no-unnecessary-type-assertion"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-assertion
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c27590f1dbbe62060c3156073ecd56672431bfb5fe4e09e2b5bd8f4e27b467ab
---

禁止不必要的类型断言。

如果类型断言没有更改表达式的类型，也就没有必要使用。

## 规则配置

```json
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

```ts
const num = 3;
export const foo2 = num as number;
export const foo3 = 'foo' as string;
```

## 反例

```ts
const num = 3;
export const foo = num;
export const bar = foo!;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
