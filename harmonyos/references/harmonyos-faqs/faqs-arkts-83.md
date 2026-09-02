---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-83
title: ArkTS是否支持反射调用类的静态成员函数和实例成员函数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持反射调用类的静态成员函数和实例成员函数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3a26489da786d14c691e691388b15a4698a965a2ed7674516910979d17fe8948
---

ArkTS 可以通过动态 import 实现反射功能，支持根据类名和方法名调用类中的静态成员函数和实例成员函数。示例如下：

在harlibrary中定义类及其成员函数和全局函数，并进行导出。

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

在HAP中添加对HARLibrary模块的依赖，动态导入HARLibrary模块，并调用其静态成员函数staticAdd()、实例成员函数instanceAdd()以及全局方法addHarlibrary()。

```ts
// HAP's oh-package.json5
"dependencies": {
  "harlibrary": "file:../harlibrary"
},
```

```ts
// HAP's Index.ets
import('harlibrary').then((ns:ESObject) => {
  ns.Calc.staticAdd(8, 9);  // Call static member functions staticAdd()
  let calc:ESObject = new ns.Calc();  // Instantiate class Calc
  calc.instanceAdd(10, 11);  // Call member functions instanceAdd()
  ns.addHarlibrary(6, 7);  // Call global methods addHarlibrary()

  // Use string names of classes, member functions, and methods for reflection calls
  let className = 'Calc';
  let methodName = 'instanceAdd';
  let staticMethod = 'staticAdd';
  let functionName = 'addHarlibrary';
  ns[className][staticMethod](12, 13);  // Call static member functions staticAdd()
  let calc1:ESObject = new ns[className]();  // Instantiate class Calc
  calc1[methodName](14, 15);  // Call member functions instanceAdd()
  ns[functionName](16, 17);  // Call global methods addHarlibrary()
});
```

具体可以参考：[业务扩展场景介绍](../harmonyos-guides/arkts-dynamic-import.md#业务扩展场景介绍)。
