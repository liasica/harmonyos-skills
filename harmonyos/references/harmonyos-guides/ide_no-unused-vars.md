---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-vars
title: "@typescript-eslint/no-unused-vars"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unused-vars
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ebf2c11b97ec5526e183fb2612d8f50816cd711bfb5dadd7f53c00b7ec87f512
---

禁止定义未使用的变量。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unused-vars": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-unused-vars选项](https://eslint.nodejs.cn/docs/rules/no-unused-vars#选项)。

## 正例

```screen
const x = 10;
console.info(`${x}`);

((foo) => {
  return foo;
})();

const num = 50;
let myFunc1: () => number = () => num;
myFunc1 = () => setTimeout(() => {
  // myFunc is considered used
  myFunc1();
}, num);
```

## 反例

```screen
const x = 10;

((foo) => {
  return 'hello';
})();

const num = 50;
const myFunc1: () => number = () => num;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
