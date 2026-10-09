---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-space-infix-ops-stylistic
title: "@hw-stylistic/space-infix-ops"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:57119c705865d74b12d90c0c6c6f000069c604561ee1a90d7ffe5411ad675f6f
---

强制运算符前后都加空格。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/space-infix-ops": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export function test(size: number) {
  for (let i = 0; i < size; i++) {
    console.info(`${i}`);
  }
}

export function test1(a: boolean, b: boolean, c: boolean) {
  return a || (b && c)
}
```

## 反例

```ts
export function test(size: number) {
  // Operator '=' must be spaced.
  // Operator '<' must be spaced.
  for (let i=0; i<size; i++) {
    console.info(`${i}`);
  }
}

export function test1(a: boolean, b: boolean, c: boolean) {
  // Operator '||' must be spaced.
  // Operator '&&' must be spaced.
  return a||b&&c;
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
