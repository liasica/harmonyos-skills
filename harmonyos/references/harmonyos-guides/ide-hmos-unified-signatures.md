---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-unified-signatures
title: "@typescript-eslint/unified-signatures"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/unified-signatures
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:690ea7aa69e194c5851a1b679e23d7218d5b45bf548c5ac23fa09b8142409454
---

如果两个重载函数可以用联合类型参数（|）、可选参数（?）或者剩余参数（...）来重构成一个函数，不允许使用重载。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/unified-signatures": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/unified-signatures选项](https://typescript-eslint.nodejs.cn/rules/unified-signatures/#options)。

## 正例

```ts
export declare function x(a: number | string): void;
export declare function y(...a: readonly number[]): void;
```

## 反例

```ts
export declare function x(a: number): void;
export declare function x(a: string): void;

export declare function y(): void;
export declare function y(...a: readonly number[]): void;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
