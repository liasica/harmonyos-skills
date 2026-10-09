---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-max-len
title: "@hw-stylistic/max-len"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/max-len
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3e9bac2af7c800596b0973b8c37d6fe692278b80d58b0d2690fa36b6c37fc58e
---

强制代码行最大长度为120个字符。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/max-len": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
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

```ts
// This line has a length of 135. Maximum allowed is 120.
export const longLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongName = 10;
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
