---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-object-creation-check
title: "@performance/object-creation-check（已下线）"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/object-creation-check（已下线）
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:65a8d4096e3ae84dff0f58d3bd405f8fd43b4e34ecc6f7b1efa7240c37edcb4a
---

建议使用字面量进行对象创建。仅支持检查ts文件，暂不支持ets文件检查。该规则已于5.0.3.500版本下线。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/object-creation-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// Test.ts
// 创建一个array
let arr: number[] = [];
// 创建一个普通对象
let obj = {};          
// 创建一个正则对象
let reg = /../;
```

## 反例

```screen
// Test.ts
// 创建一个array
let arr: number[] = new Array(); 
// 创建一个普通对象
let obj = new Object();          
// 创建一个正则对象
let reg = new RegExp('..');
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
