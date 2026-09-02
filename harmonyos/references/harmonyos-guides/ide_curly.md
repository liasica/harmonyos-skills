---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_curly
title: "@hw-stylistic/curly"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/curly
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c80fd671508bdac2021b6b37c1dfbe89e4a799a6399ea0459686c40fe0ceccfe
---

条件语句和循环语句的逻辑代码必须写在大括号中。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/curly": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
