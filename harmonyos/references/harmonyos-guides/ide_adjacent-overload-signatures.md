---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_adjacent-overload-signatures
title: "@typescript-eslint/adjacent-overload-signatures"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/adjacent-overload-signatures
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:af21da7a9e26e6e696ba12729cf0cb84813f8578e9456057bd3a294cbdd4eb6c
---

建议函数重载的签名保持连续。

## 规则配置

```json
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

```ts
export declare function bar(): void;
export declare function foo(a: string): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
```

## 反例

```ts
export declare function foo(a: string): void;
export declare function bar(): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
