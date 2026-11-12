---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_return-await
title: "@typescript-eslint/return-await"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/return-await
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6755e40092c184aa5dc7311fe3ed7a90e852f25c8ab11a56af7250b47f294a5f
---

要求异步函数返回“await”。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/return-await": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/return-await选项](https://typescript-eslint.nodejs.cn/rules/return-await/#options)。

## 正例

```screen
export async function validInTryCatch1() {
  try {
    return await Promise.resolve('try');
  } catch (e) {
    return await Promise.resolve('catch');
  }
}
```

## 反例

```screen
export async function validInTryCatch1() {
  try {
    return Promise.resolve('try');
  } catch (e) {
    return Promise.resolve('catch');
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
