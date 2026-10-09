---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ban-ts-comment
title: "@typescript-eslint/ban-ts-comment"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-ts-comment
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1513806cfa5e16bdedecdde8851384f11b78b7c121d6b9cbdeab2fe7f358659a
---

不允许使用`@ts-<directional>`格式的注释，或要求在注释后进行补充说明。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-ts-comment": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/ban-ts-comment选项](https://typescript-eslint.nodejs.cn/rules/ban-ts-comment/#options)。

## 正例

```ts
console.log('hello');
```

## 反例

```ts
// @ts-expect-error
console.log('hello');

/* @ts-expect-error */
console.log('hello');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
