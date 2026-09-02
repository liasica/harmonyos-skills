---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-use-before-define
title: "@typescript-eslint/no-use-before-define"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-use-before-define
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:04980ee9457409add548dae252ac5a8060befdfd5eb6e981ebe005ffa91d4270
---

禁止在变量声明之前使用变量。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-use-before-define": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-use-before-define选项](https://eslint.nodejs.cn/docs/rules/no-use-before-define#选项)。

## 正例

```screen
const a = '10';
console.info(a);

function ff(): void {
  console.info('function');
}
ff();

const foo = '1';
export { foo };
```

## 反例

```screen
console.info(a);
const a = '10';

ff();
function ff(): void {
  console.info('function');
}

export { foo };
const foo = '1';
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
