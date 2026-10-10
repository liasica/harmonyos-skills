---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-iude-no-unnecessary-type-arguments
title: "@typescript-eslint/no-unnecessary-type-arguments"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-type-arguments
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:17+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:8f7240a213843fab3f1a257f6add8bb467b9e174480be98b213567807ec06312
---

当类型参数和默认值相同时，不允许显式使用。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-arguments": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
function f<T = number>(para: T): void {
  console.info(`${para as number}`);
}
f(Number.MAX_VALUE);
f<string>('hello');

function g<T = number, U = string>(para1: T, para2?: U) {
  if (para2 !== undefined) {
    console.info(`${para2 as string}`);
  }
  console.info(`${para1 as number}`);
}
g<string>('para1', 'para2');
g<number, number>(Number.MAX_VALUE);

class C<T = number> {
  public name: T;

  public constructor(name: T) {
    this.name = name;
  }
}
new C(Number.MAX_VALUE);
new C<string>('hello');
```

## 反例

```ts
function f<T = number>(para: T): void {
  console.info(`${para as number}`);
}
// 参数类型默认是number，直接使用f()即可
f<number>(Number.MAX_VALUE);

function g<T = number, U = string>(para1: T, para2?: U) {
  if (para2 !== undefined) {
    console.info(`${para2 as string}`);
  }
  console.info(`${para1 as number}`);
}
// 第二个参数类型默认是string，直接使用g<string>()即可
g<string, string>('hello');

class C<T = number> {
  public meth(para: T): void {
    console.info(`${para as number}`);
  }
}
// 参数类型默认是number，直接使用new C()即可
new C<number>();
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
