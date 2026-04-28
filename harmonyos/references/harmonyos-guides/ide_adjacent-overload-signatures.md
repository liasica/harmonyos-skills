---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_adjacent-overload-signatures
title: @typescript-eslint/adjacent-overload-signatures
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/adjacent-overload-signatures
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f50217ca4cbea73f96b1e021a2a9e5186c4c8118d70b694ea02cc36b849650a9
---

建议函数重载的签名保持连续。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/adjacent-overload-signatures": "error",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export declare function bar(): void;
2. export declare function foo(a: string): void;
3. export declare function foo(a: number, b: number): void;
4. export declare function foo(a: number, b: string, c?: string): void;
```

## 反例

```
1. export declare function foo(a: string): void;
2. export declare function bar(): void;
3. export declare function foo(a: number, b: number): void;
4. export declare function foo(a: number, b: string, c?: string): void;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
