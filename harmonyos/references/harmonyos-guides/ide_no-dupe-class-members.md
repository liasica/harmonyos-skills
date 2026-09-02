---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dupe-class-members
title: "@typescript-eslint/no-dupe-class-members"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-dupe-class-members
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:edb13706cf0cf05814d72e379c0c738c9e8c1dabaafabe72909fa56dbfb87fb1
---

不允许重复的类成员。如果类成员中有同名的声明，最后一个声明会覆盖其他声明，可能会导致意外行为。

编译器会自动校验该规则检查的代码问题，新建项目时可以不开启此规则。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-dupe-class-members": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
/*eslint no-dupe-class-members: "error"*/
export class A {
  public bar() {
    console.info('bar');
  }

  public qux() {
    console.info('qux');
  }
}

export class B {
  private name: string = 'bar';

  public get bar() {
    return this.name;
  }

  public set bar(value) {
    this.name = value;
  }
}

export class E {
  public static bar() {
    console.info('static bar');
  }

  public bar() {
    console.info('method bar');
  }
}
```

## 反例

```screen
/*eslint no-dupe-class-members: "error"*/
export class A {
  public bar() {
    console.info('bar');
  }

  public bar() {
    console.info('bar');
  }
}

export class B {
  private readonly name: string = 'bar';

  public get bar() {
    return this.name;
  }

  public bar() {
    return this.name;
  }
}

export class E {
  public static bar() {
    console.info('static bar');
  }

  public static bar() {
    console.info('static bar');
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
