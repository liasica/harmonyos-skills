---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-comma-spacing-stylistic
title: "@hw-stylistic/comma-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/comma-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e5763c10cb9e8867191c0e45e3420f838cc7bb8a919d444b7469cf207a082d8d
---

强制数组元素和函数中多个参数之间的逗号后面加空格，逗号前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/comma-spacing": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export {bar, arr};

function bar(param1: string, param2: string) {
  return [param1, param2];
}
const arr = ['s1', 's2', 's3', 's4'];
```

## 反例

```screen
export {arr};
// A space is required after ','.
// There should be no space before ','.
const arr = ['s1' ,'s2' ,'s3'];
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
