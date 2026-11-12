---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-tabs
title: "@hw-stylistic/no-tabs"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/no-tabs
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4839c4056cd482340f528dcede85720fdefb11b14f6af0048b614cd0bef97e24
---

禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-tabs": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export const message: string = 'Hello World';
```

## 反例

```screen
export	const	message:	string = 'Hello World';
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
