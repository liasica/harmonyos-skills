---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quotes-stylistic
title: "@hw-stylistic/quotes"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/quotes
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e071b592c1e83a2b35e6895a307ddd6ed8f58552ecb6e66be8410fe643a81c2c
---

强制字符串使用单引号。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/quotes": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export {a, b};

const a = 'hello';
const b = `hello`;
```

## 反例

```screen
// Strings must use single quotes.
export const a = "hello";
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
