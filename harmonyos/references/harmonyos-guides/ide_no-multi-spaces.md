---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-multi-spaces
title: "@hw-stylistic/no-multi-spaces"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/no-multi-spaces
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:05e347fca6cdc593f1fe9010c01c33f713ac944fc1d31446486e6f9542c5fc6a
---

不允许出现连续多个空格，除非是换行。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-multi-spaces": "error"
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
// Multiple spaces found before 'message'.
// Multiple spaces found before 'string'.
// Multiple spaces found before '='.
// Multiple spaces found before 'Hello World'.
export const   message:  string  =  'Hello World';
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
