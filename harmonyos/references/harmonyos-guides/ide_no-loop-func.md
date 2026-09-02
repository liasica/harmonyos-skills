---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-loop-func
title: "@typescript-eslint/no-loop-func"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-loop-func
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b0b63ace4e82f2d0554628aeb7ebeb967bb878d44f8332b86ba253a7d0f8346f
---

禁止在循环语句内包含不安全引用的函数声明。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-loop-func": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const a = function(): void {
  console.info('hello');
};

for (let i = 10; i; i--) {
  a();
}

for (let i = 10; i; i--) {
  const b = function(): void {
    a();
  }; // OK, no references to variables in the outer scopes.
  b();
}
```

## 反例

```screen
const num = 10;
for (let i = num; i; i--) {
  // 变量i是不安全的引用
  (function(): number {
    return i;
  })();
}

let i1 = 0;
while (i1 < num) {
  // 变量i是不安全的引用
  const a = function(): number {
    return i1;
  };
  a();

  i1++;
}

let i2 = 0;
do {
  // 变量i是不安全的引用
  function a(): number {
    return i2;
  }
  a();

  i2++;
} while (i2 < num);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
