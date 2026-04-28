---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-83
title: ArkTS是否支持反射调用类的静态成员函数和实例成员函数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持反射调用类的静态成员函数和实例成员函数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6cb8a1cfe85fa86de9eb435eebcd79eead0fac7cd5c5c594c0c3ed7b7fc54874
---

ArkTS 可以通过动态 import 实现反射功能，支持根据类名和方法名调用类中的静态成员函数和实例成员函数。示例如下：

在harlibrary中定义类及其成员函数和全局函数，并进行导出。

```
1. // harlibrary's src/main/ets/utils/Calc.ets
2. export class Calc {
3. public static staticAdd(a:number, b:number):number {
4. let c = a + b;
5. console.log('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
6. return c;
7. }
8. public instanceAdd(a:number, b:number):number {
9. let c = a + b;
10. console.log('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
11. return c;
12. }
13. }
14. export function addHarlibrary(a:number, b:number):number {
15. let c = a + b;
16. console.log('DynamicImport I am harlibrary in addHarlibrary, %d + %d = %d', a, b, c);
17. return c;
18. }
```

[Calc.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/harlibrary/src/main/ets/utils/Calc.ets#L22-L39)

```
1. // harlibrary's Index.ets
2. export { Calc, addHarlibrary } from './src/main/ets/utils/Calc'
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/harlibrary/Index.ets#L22-L23)

在HAP中添加对HARLibrary模块的依赖，动态导入HARLibrary模块，并调用其静态成员函数staticAdd()、实例成员函数instanceAdd()以及全局方法addHarlibrary()。

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "harlibrary": "file:../harlibrary"
4. },
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/oh-package.json5#L14-L17)

```
1. // HAP's Index.ets
2. import('harlibrary').then((ns:ESObject) => {
3. ns.Calc.staticAdd(8, 9);  // Call static member functions staticAdd()
4. let calc:ESObject = new ns.Calc();  // Instantiate class Calc
5. calc.instanceAdd(10, 11);  // Call member functions instanceAdd()
6. ns.addHarlibrary(6, 7);  // Call global methods addHarlibrary()

8. // Use string names of classes, member functions, and methods for reflection calls
9. let className = 'Calc';
10. let methodName = 'instanceAdd';
11. let staticMethod = 'staticAdd';
12. let functionName = 'addHarlibrary';
13. ns[className][staticMethod](12, 13);  // Call static member functions staticAdd()
14. let calc1:ESObject = new ns[className]();  // Instantiate class Calc
15. calc1[methodName](14, 15);  // Call member functions instanceAdd()
16. ns[functionName](16, 17);  // Call global methods addHarlibrary()
17. });
```

[HarlibraryIndex.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/HarlibraryIndex.ets#L22-L38)

具体可以参考：[业务扩展场景介绍](../harmonyos-guides/arkts-dynamic-import.md#业务扩展场景介绍)。
