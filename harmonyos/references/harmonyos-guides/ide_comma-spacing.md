---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-spacing
title: "@typescript-eslint/comma-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/comma-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:83b05f9c5d226f474795c291f84c92c2411af3f8fac9fc50d51101cb68e9184d
---

强制逗号前后的空格风格保持一致。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-spacing": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/comma-spacing选项](https://eslint.nodejs.cn/docs/rules/comma-spacing#选项)。

## 正例

```screen
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr1 = ['1', '2'];
export const arr2 = ['1',, '3'];

function qur(a: string, b: string) {
  return `${a}${b}`;
}
qur('1', '2');
```

## 反例

```screen
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr = ['1' , '2'];

function qur(a: string ,b: string) {
  return `${a}${b}`;
}
qur('1' ,'2');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
