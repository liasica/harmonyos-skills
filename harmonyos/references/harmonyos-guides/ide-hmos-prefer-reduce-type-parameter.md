---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-reduce-type-parameter
title: "@typescript-eslint/prefer-reduce-type-parameter"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-reduce-type-parameter
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c006c34246a55950aec4b4c8f49d976f22a3520aef86cee9b722f1979cc5d6ca
---

调用“Array#reduce”时推荐使用类型参数而不是强制转换类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-reduce-type-parameter": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
['1', '2', '3'].reduce<readonly string[]>((arr, text) => {
  const newArr = [...arr];
  newArr.push(text);
  return newArr;
}, []);
```

## 反例

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
