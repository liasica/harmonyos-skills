---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_operator-linebreak
title: "@hw-stylistic/operator-linebreak"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/operator-linebreak
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7b209f41cd1e97739ff1ddbdab837d75f7ff7cf0a0fac4b0160f95f46b4610c9
---

强制运算符位于代码行末。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/operator-linebreak": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export function test(n1: number, n2: number): void {
  if (n1 > n2) {
    console.info('hello');
  }

  if (n1 >
    n2) {
    console.info('hello');
  }
}
```

## 反例

```screen
export function test(n1: number, n2: number, n3: number): void {
  if (n1 > n2
    // '||' should be placed at the end of the line.
    || n1 < n3) {
    console.info('hello');
  }
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
