---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-ts-comment
title: "@typescript-eslint/ban-ts-comment"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-ts-comment
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3735e8da43c915ac8656d13942b0a75c872e82d283d73e7f6232e500833e304e
---

不允许使用`@ts-<directional>`格式的注释，或要求在注释后进行补充说明。

## 规则配置

```screen
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

```screen
console.log('hello');
```

## 反例

```screen
// @ts-expect-error
console.log('hello');

/* @ts-expect-error */
console.log('hello');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
