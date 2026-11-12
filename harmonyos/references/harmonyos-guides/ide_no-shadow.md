---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-shadow
title: "@typescript-eslint/no-shadow"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-shadow
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:188055a9091dac7564c707b94dfc3d3908a08d37da960aca858b0a8607f73f04
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
