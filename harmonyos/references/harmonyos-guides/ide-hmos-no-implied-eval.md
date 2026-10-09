---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-implied-eval
title: "@typescript-eslint/no-implied-eval"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-implied-eval
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1599f1a3158fe098fe4893660a204169bd14f12936b5e5e2a1ce476aa2cc427b
---

禁止使用类似“eval()”的方法。

setTimeout()、setInterval()、setImmediate()或者execScript()这些函数可以接受一个字符串作为其第一个参数，比如

```screen
setTimeout('alert(`Hi!`);', 100);
```

这种行为被认为是隐式“eval()”，不推荐使用。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-implied-eval": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
function alert(arg: string) {
  console.log(arg);
}

const time = 100;

setTimeout(() => {
  alert('Hi!');
}, time);

setInterval(() => {
  alert('Hi!');
}, time);

const fn = () => {
  console.info('fn');
};
setTimeout(fn, time);

class Foo {
  public static fn = () => {
    console.info('static');
  };

  public meth() {
    console.info('method');
  }
}

setTimeout(Foo.fn, time);
```

## 反例

```ts
const time = 100;
setTimeout('alert(`Hi!`);', time);

setInterval('alert(`Hi!`);', time);

const fn1 = '() = {}';
setTimeout(fn1, time);

const fn2 = () => {
  return 'x = 10';
};
setTimeout(fn2(), time);

export const fn3 = new Function('a', 'b', 'return a + b');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
