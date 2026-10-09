---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-method-signature-style
title: "@typescript-eslint/method-signature-style"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/method-signature-style
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:34a85ed6909ee37120673f60640b5732bef6e3d70417bf96eebee578592c0e6b
---

定义函数类型的属性时，强制使用特定的风格。

有两种方式定义对象/接口中函数类型的属性，一种是定义为属性，属性签名是函数，另一种是直接定义为方法。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/method-signature-style": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/method-signature-style选项](https://typescript-eslint.nodejs.cn/rules/method-signature-style/#options)。

## 正例

```ts
// 默认要求定义为属性
export interface T1 {
  func: (arg: string) => number;
}
```

## 反例

```ts
// 默认要求定义为属性
export interface T1 {
  func(arg: string): number;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
