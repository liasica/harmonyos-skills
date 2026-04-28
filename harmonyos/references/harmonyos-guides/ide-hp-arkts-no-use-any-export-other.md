---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkts-no-use-any-export-other
title: @performance/hp-arkts-no-use-any-export-other
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkts-no-use-any-export-other
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:05+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:ab0a3cb83e80db560676103f7c47e707f8d33f1f54d20162b76d9849dddd732b
---

避免使用export \* 导出其他模块中定义的类型和数据。

冷启动完成时延场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkts-no-use-any-export-other": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 当前文件 User.ets
2. // 从 Product.ets 文件中导出Product成员
3. export { Product } from './Product';
4. class User {
5. id?: number;
6. name?: string;
7. }
```

## 反例

```
1. // 当前文件 User.ets
2. // 从 Product.ets 文件中导出所有可导出的成员
3. export * from './Product';
4. // 从 Product.ets 文件中导出所有可导出的成员
5. export * as XX from './Product';
6. class User {
7. id?: number;
8. name?: string;
9. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
