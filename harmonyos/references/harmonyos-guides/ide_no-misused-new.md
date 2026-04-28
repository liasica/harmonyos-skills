---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-new
title: @typescript-eslint/no-misused-new
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-misused-new
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:36+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3d15eb1312cff1bf6fb0d1659160fd2659335144a3376961cba94128deb2dece
---

要求正确地定义“new”和“constructor”。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-misused-new": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export declare class C {
2. public name: string;

4. public constructor();
5. }
```

## 反例

```
1. export declare class C {
2. // 应该定义为constructor(): C
3. public new(): C;
4. }

6. export interface I {
7. // 不应该定义constructor
8. constructor(): void;
9. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
