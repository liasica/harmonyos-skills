---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_return-await
title: "@typescript-eslint/return-await"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/return-await
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:caa8ab260e8c087fbe2da24de60d440691cfad8b94fd1fbfaf4867fea44e42a3
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
