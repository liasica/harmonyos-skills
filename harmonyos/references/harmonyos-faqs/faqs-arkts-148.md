---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-148
title: 应用通过对象字面量初始化class实例导致编译失败的原因和修改方案
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 应用通过对象字面量初始化class实例导致编译失败的原因和修改方案
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:945c92ea6c0e77c19423ca99b07dc6c3c2ede31a44fb897829edc291cdeb2756
---

**编译失败原因**

**复现方法**

1. 应用通过对象字面量初始化class的实例。
2. 该class在后续的版本中新增方法。

示例：

```
1. // SDK
2. declare class Base {
3. // since 9
4. getPropA(): number;
5. // since 12 new method
6. getPropB(): number;
7. }
8. // apply
9. let b: Base = {
10. getPropA() {
11. return 0;
12. }
13. }
14. // Error message after upgrading to API 12.
15. // Property 'getPropB' is missing in type '{ getPropA(): number; }' but required in type 'Base'.
```

[ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L21-L35)

**报错原因**

ArkTS语言的类型检查要求类型和对象要匹配，Base有两个方法，但是赋值的对象只有一个，如果不在编译时检查报错，可能会在运行时出现异常。

**对象字面量初始化class实例**

**不推荐使用**

通过对象字面量初始化class实例是业界不推荐的用法。

会造成以下问题：

1. 篡改SDK提供的API，应用可覆盖SDK API，在后续的使用中有安全风险。

   ```
   1. // SDK API
   2. declare class Person1 {
   3. name: string;
   4. age: number;
   5. greet(): void;
   6. }
   7. // apply
   8. const p: Person1 = {
   9. name: 'Bob',
   10. age: 40,
   11. greet() {} // Tampering with system greet behavior.
   12. }
   ```

   [ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L39-L50)
2. 运行时与该class无关，应用使用instanceof检查该对象与class的关系，返回false。

   ```
   1. // SDK API
   2. declare class Person2 {
   3. name: string;
   4. age: number;
   5. greet(): void;
   6. }
   7. // apply
   8. const p1: Person2 = {
   9. name: 'Bob',
   10. age: 40,
   11. greet() {}
   12. }
   13. console.log(`${p1 instanceof Person2}`); // return false
   ```

   [ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L54-L66)

**业界使用罕见**

使用class的场景主要为：

1. 实例化，占比65%。

   ```
   1. // SDK API
   2. declare class Person3 {
   3. name: string;
   4. age: number;
   5. greet(): void;
   6. }
   7. const p2: Person3 = new Person3();
   ```

   [ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L70-L76)
2. 子类继承，占比25%。

   ```
   1. // SDK API
   2. declare class Person4 {
   3. name: string;
   4. age: number;
   5. greet(): void;
   6. }

   8. class Student extends Person4 {
   9. study() {}
   10. }
   ```

   [ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L80-L89)
3. 使用其静态方法，占比20%。

   ```
   1. // SDK API
   2. declare class Person5 {
   3. name: string;
   4. age: number;
   5. static greet(): void;
   6. }
   7. Person5.greet();
   ```

   [ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L93-L99)
4. 其它用法，包括通过对象字面量初始化，占比小于0.01%。

   ```
   1. declare class Person6 {
   2. name: string;
   3. age: number;
   4. greet(): void;
   5. }

   7. const p3: Person2 = {
   8. name: 'Bob',
   9. age: 40,
   10. greet() {}
   11. }
   ```

   [ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L103-L113)

扫描开源社区TypeScript官方代码，其.ts代码有80w行，其中通过对象字面量初始化class实例的代码为：生产代码，9行，占0.001%；测试代码，63行，占0.008%。

**系统演进**

操作系统的开放能力会持续演进，在class中新增方法是常见的演进行为，在HarmonyOS与业界其他操作系统中非常常见。

以程序框架UIAbilityContext为例，在API9、10、12版本中均有新增API：

```
1. declare class UIAbilityContext {
2. /**
3. * @since 9
4. */
5. startAbility(): void;
6. /**
7. * @since 9
8. */
9. startAbilityForResult(): void;
10. /**
11. * @since 10
12. */
13. setMissionContinueState(): void;
14. /**
15. * @since 12
16. */
17. backToCallerAbilityWithResult(): Promise<void>;
18. }
```

**修改方案**

为保证操作系统开放能力的持续演进，开发者使用对象字面量的方式初始化class实例，若编译失败，需要修改。

应用不使用对象字面量的方式初始化class实例，修改为通过new的方式初始化。

```
1. // SDK
2. declare class Base2 {
3. // since 9
4. getPropA(): number;
5. // since 12 new method
6. getPropB(): number;
7. }

9. // Initialize an instance of a class using the new method.
10. let b2: Base2 = new Base2();
11. // Upgrading to API 12 SDK will not result in errors.
```

[ClassExample.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkUI/entry/src/main/ets/pages/ClassExample.ts#L117-L127)
