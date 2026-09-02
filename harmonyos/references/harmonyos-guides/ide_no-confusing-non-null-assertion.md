---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-non-null-assertion
title: "@typescript-eslint/no-confusing-non-null-assertion"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-confusing-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9ee7a97f4deed12d18d73e76c02cc485b9a7be519b6a9bcab7575e5f645748d0
---

不允许在可能产生混淆的位置使用非空断言。

在赋值或者等于旁边使用非空断言（!）会产生混淆，看起来类似于不等于，不建议这种写法。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-confusing-non-null-assertion": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
interface Foo {
  bar?: string;
  num?: number;
}

function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX_VALUE
  };
}
const foo: Foo = getFoo();
export const isEqualsBar = foo.bar === 'hello';
const num = 2;
export const isEqualsNum = num + (foo.num!) === num;
```

## 反例

```screen
interface Foo {
  bar?: string;
  num?: number;
}

function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX_VALUE
  };
}
const foo: Foo = getFoo();
// 可能会产生混淆，误以为是不等于
export const isEqualsBar = foo.bar! === 'hello';
// 可能会产生混淆，误以为是不等于
const num = 2;
export const isEqualsNum = num + foo.num! === num;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
