---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-object-property-newline
title: "@hw-stylistic/object-property-newline"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/object-property-newline
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fca2f9f0d7e9c9e1e45fabeaedc076996d9b38df88d262da6aa355b6a40a3a96
---

强制对象属性换行。该规则仅检查.ets文件类型。

对象属性不超过4个时，允许在同一行，也可以每个属性都换行。对象属性超过4个时，每个属性必须都换行。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/object-property-newline": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export {a, b};

interface II {
  p1: string;
  p2: string;
  p3: string;
  p4: string;
  p5?: string;
}

const a: II = {
  p1: 'p1',
  p2: 'p2',
  p3: 'pe',
  p4: 'p4',
  p5: 'p5'
};

const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4' };
```

## 反例

```ts
export {a, b};

interface II {
  p1: string;
  p2: string;
  p3: string;
  p4: string;
  p5?: string;
}

// Object properties must go on a new line.
const a: II = { p1: 'p1', p2: 'p2',
  p3: 'p3', p4: 'p4' };

// Object properties must go on a new line.
const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4', p5: 'p5' };
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
