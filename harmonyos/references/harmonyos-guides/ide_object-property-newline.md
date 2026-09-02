---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_object-property-newline
title: "@hw-stylistic/object-property-newline"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/object-property-newline
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d9a17c7bd7923d1300bd51ee9faa50d2a3f637ace224c821573b6a9a3a60798
---

强制对象属性换行。该规则仅检查.ets文件类型。

对象属性不超过4个时，允许在同一行，也可以每个属性都换行。对象属性超过4个时，每个属性必须换行。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/object-property-newline": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
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
  p3: 'p3',
  p4: 'p4',
  p5: 'p5'
};

const b: II = { p1: 'p1', p2: 'p2', p3: 'p3', p4: 'p4' };
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
