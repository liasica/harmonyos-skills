---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-curly
title: "@hw-stylistic/curly"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/curly
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:37+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:b0a8e586dcb1feaf2e750d5cf8fc6efd2bc400b801b04dc354d67d4b8fd532d4
---

条件语句和循环语句的逻辑代码必须写在大括号中。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/curly": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export function test(a: number, b: number) {
  if (a > b) {
    console.info('doSomething');
  } else if (a === b) {
    console.info('doSomething');
  } else {
    console.info('doSomething');
  }

  while (a > b) {
    a--;
    console.info('doSomething');
  }

  console.info('doSomething');
}
```

## 反例

```ts
export function test(a: number, b: number) {
  if (a > b)
  // Expected { after 'if' condition.
    console.info('doSomething');
  else if (a === b)
  // Expected { after 'if' condition.
    console.info('doSomething');
  else
  // Expected { after 'else'.
    console.info('doSomething');
  console.info('doSomething');
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
