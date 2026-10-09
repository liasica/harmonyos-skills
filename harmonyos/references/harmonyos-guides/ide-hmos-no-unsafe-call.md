---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unsafe-call
title: "@typescript-eslint/no-unsafe-call"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-call
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e05cf66737b38d7741df71d3646b3f6ccde73ebf9387551e7a1a3fad3c9d54d5
---

禁止调用“any”类型的表达式。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-call": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
declare const typedVar: () => void;
declare const typedNested: { prop: { a: () => void } };

typedVar();
typedNested.prop.a();

((): void => {
  console.info('hello');
})();

new Map();

export const raw = String.raw`foo`;
```

## 反例

```ts
declare const anyVar: any;
declare const nestedAny: { prop: any };
// anyVar为any类型，禁止调用
anyVar();
anyVar.a.b();
// nestedAny中的prop属性为any类型，禁止调用
nestedAny.prop();
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
