---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-reduce-type-parameter
title: "@typescript-eslint/prefer-reduce-type-parameter"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-reduce-type-parameter
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6c8708636270cf962a1905f0cfb9f64bc692ebb4677bfe4574e240448c420b6e
---

调用“Array#reduce”时推荐使用类型参数而不是类型断言。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-reduce-type-parameter": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
['1', '2', '3'].reduce<readonly string[]>((arr, text) => {
  const newArr = [...arr];
  newArr.push(text);
  return newArr;
}, []);
```

## 反例

```screen
['1', '2', '3'].reduce((arr, text) => {
  const newArr = [...arr];
  newArr.push(text);
  return newArr;
}, [] as readonly string[]);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
