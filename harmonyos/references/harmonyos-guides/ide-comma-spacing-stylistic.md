---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-comma-spacing-stylistic
title: "@hw-stylistic/comma-spacing"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/comma-spacing
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7c6ec97e403bdd59c6493c1c6c5e198bba3b4aef4cbfaf983d4ade16163010fb
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
