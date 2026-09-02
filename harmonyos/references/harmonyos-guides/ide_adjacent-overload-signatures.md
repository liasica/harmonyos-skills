---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_adjacent-overload-signatures
title: "@typescript-eslint/adjacent-overload-signatures"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/adjacent-overload-signatures
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6af7b25a71c24d87d9f6c8aa40eea21a5ed3791caae7f9525714ff0dcdc572ed
---

建议函数重载的签名保持连续。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/adjacent-overload-signatures": "error",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export declare function bar(): void;
export declare function foo(a: string): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
```

## 反例

```screen
export declare function foo(a: string): void;
export declare function bar(): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
