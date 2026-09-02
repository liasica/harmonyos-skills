---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-70
title: 是否支持模块的动态加载？如何实现
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 是否支持模块的动态加载？如何实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:539cb28c47a3586650366c03a4def27647cd068747439e64bd1ab3ecfeef8b78
---

当前不支持动态加载设备侧的二进制包。可以使用动态import进行异步加载，以实现类似Class.forName()的反射效果。

示例如下，hap动态导入harlibrary，并调用静态成员函数staticAdd()、实例成员函数instanceAdd()和全局方法addHarlibrary()。

```ts
// harlibrary's src/main/ets/utils/Calc.ets
export class Calc {
  public static staticAdd(a:number, b:number):number {
    let c = a + b;
    console.log('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
    return c;
  }
  public instanceAdd(a:number, b:number):number {
    let c = a + b;
    console.log('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
    return c;
  }
}
export function addHarlibrary(a:number, b:number):number {
  let c = a + b;
  console.log('DynamicImport I am harlibrary in addHarlibrary, %d + %d = %d', a, b, c);
  return c;
}
```

```ts
// harlibrary's Index.ets
export { Calc, addHarlibrary } from './src/main/ets/utils/Calc'
```
