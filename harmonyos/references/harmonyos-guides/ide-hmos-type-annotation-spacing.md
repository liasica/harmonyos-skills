---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-type-annotation-spacing
title: "@typescript-eslint/type-annotation-spacing"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/type-annotation-spacing
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8fdd5bf3fb3990b47896d5f517f535ecbee8c113c77b1b94e4874175e82def11
---

类型注释前后需要一致的空格风格。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/type-annotation-spacing": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/type-annotation-spacing选项](https://typescript-eslint.nodejs.cn/rules/type-annotation-spacing/#options)。

## 正例

```ts
// 默认冒号前无空格，冒号后有空格
export const foo1: string = 'bar';

export declare function foo2(): string;

export class Foo3 {
  public name: string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = () => void;
```

## 反例

```ts
// 默认冒号前无空格，冒号后有空格
export const foo1 :string = 'bar';

export declare function foo2() :string;

export class Foo3 {
  public name :string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = ()=>void;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
