---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-adjacent-overload-signatures
title: "@typescript-eslint/adjacent-overload-signatures"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/adjacent-overload-signatures
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8b7335742d7dce0ee80d9e95b1295548fb8f3a5f46b41ffbd10aaf79042e3228
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

该规则无需配置额外选项。

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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
