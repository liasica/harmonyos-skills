---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-brace-style
title: "@typescript-eslint/brace-style"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/brace-style
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:67cd1f6edf8aadc07627a2b03f3380af04e3750c1e24d31c6d8408a09795fc80
---

对代码块强制执行一致的括号样式。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/brace-style": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/brace-style选项](https://eslint.nodejs.cn/docs/rules/brace-style#选项)。

## 正例

```ts
function foo(): boolean {
  return true;
}

class C {
  static {
    foo();
  }

  public meth() {
    foo();
  }
}

export { C };
```

## 反例

```ts
function foo(): boolean 
{
  return true;
}

class C {
  static 
  {
    foo();
  }

  public meth() 
  {
    foo();
  }
}

export { C };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
