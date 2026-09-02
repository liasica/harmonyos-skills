---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-call
title: "@typescript-eslint/no-unsafe-call"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-call
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44b357dc837d3563fd102fdcf2e9639918a96d6c6f3b1388fe78777af18a6f63
---

禁止调用“any”类型的表达式。

该规则仅支持对.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-call": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
