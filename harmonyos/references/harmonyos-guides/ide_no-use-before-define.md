---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-use-before-define
title: "@typescript-eslint/no-use-before-define"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-use-before-define
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2b125e1a0ade140c1c06bfa3e11d0b6cceb62c909bb1cb2cee79cf7e1cd0f1ea
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
