---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_max-len
title: "@hw-stylistic/max-len"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/max-len
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d484d8802c110681961755903c9fde4a09dada9ca1c848a62fe9c520c45c5f34
---

强制代码行最大长度为120个字符。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/max-len": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct Index {
  message: string = 'hello';

  build() {
    Text(this.message)
  }
}
```

## 反例

```screen
// This line has a length of 135. Maximum allowed is 120.
export const longLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongName = 10;
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
