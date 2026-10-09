---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-tabs
title: "@hw-stylistic/no-tabs"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/no-tabs
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1f297ad5361093151a28d665bd262a6f3b278000541da28f92cd77d76284f184
---

禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-tabs": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export const message: string = 'Hello World';
```

## 反例

```ts
export	const	message:	string = 'Hello World';
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
