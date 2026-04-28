---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-object-creation-check
title: @performance/object-creation-check（已下线）
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/object-creation-check（已下线）
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a04b9b6be04981b7846d3a12c262ec8ba139b35873160d70920f3bac2c8fa998
---

建议使用字面量进行对象创建。仅支持检查ts文件，暂不支持ets文件检查。该规则已于5.0.3.500版本下线。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/object-creation-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // Test.ts
2. // 创建一个array
3. let arr: number[] = [];
4. // 创建一个普通对象
5. let obj = {};
6. // 创建一个正则对象
7. let reg = /../;
```

## 反例

```
1. // Test.ts
2. // 创建一个array
3. let arr: number[] = new Array();
4. // 创建一个普通对象
5. let obj = new Object();
6. // 创建一个正则对象
7. let reg = new RegExp('..');
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
