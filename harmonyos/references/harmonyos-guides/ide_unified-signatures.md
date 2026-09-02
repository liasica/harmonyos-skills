---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_unified-signatures
title: "@typescript-eslint/unified-signatures"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/unified-signatures
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:11095b7c6156857517d345f61b0a81a1df5e1d78ac53415f2237de77661be9ca
---

如果两个重载函数可以用联合类型参数（|）、可选参数（?）或者剩余参数（...）来重构为一个函数，不允许使用重载。

## 规则配置

```screen
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

```screen
export declare function x(a: number | string): void;
export declare function y(...a: readonly number[]): void;
```

## 反例

```screen
export declare function x(a: number): void;
export declare function x(a: string): void;

export declare function y(): void;
export declare function y(...a: readonly number[]): void;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
