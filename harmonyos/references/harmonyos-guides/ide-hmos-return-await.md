---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-return-await
title: "@typescript-eslint/return-await"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/return-await
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b96296c6c93fcef351674698170368fba2620e07420e8dce1b4e8f97fb9daf7f
---

要求异步函数返回“await”。

## 规则配置

```json
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

```ts
export async function validInTryCatch1() {
  try {
    return await Promise.resolve('try');
  } catch (e) {
    return await Promise.resolve('catch');
  }
}
```

## 反例

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
