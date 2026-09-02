---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-shadow
title: "@typescript-eslint/no-shadow"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-shadow
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d7fa59091038edf9436d6e7dd6363630a00fd2ba97a306462b640c40ae905523
---

禁止声明与外部作用域变量同名的变量。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-shadow": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-shadow选项](https://typescript-eslint.nodejs.cn/rules/no-shadow/#options)。

## 正例

```screen
/*eslint no-shadow: "error"*/
const a = '1';
export function b() {
  const a1 = '10';
  console.info(a1);
}

export const c = () => {
  const a1 = '10';
  console.info(a1);
};

console.info(a);
```

## 反例

```screen
/*eslint no-shadow: "error"*/
const a = '3';
export function b() {
  const a = '10';
  console.info(a);
}

export const c = () => {
  const a = '10';
  console.info(a);
};

console.info(a);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
