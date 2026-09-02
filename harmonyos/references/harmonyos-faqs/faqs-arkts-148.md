---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-148
title: 应用通过对象字面量初始化class实例导致编译失败的原因和修改方案
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 应用通过对象字面量初始化class实例导致编译失败的原因和修改方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:22938a1622751211f16dc92d9b93099a48b15f2470389cb25fd5c6cdba63000c
---

**编译失败原因**

**复现方法**

1. 应用通过对象字面量初始化class的实例。
2. 该class在后续的版本中新增方法。

示例：

```ts
// SDK
declare class Base {
  // since 9
  getPropA(): number;
  // since 12 new method
  getPropB(): number;
}
// apply
let b: Base = {
  getPropA() {
    return 0;
  }
}
// Error message after upgrading to API 12.
// Property 'getPropB' is missing in type '{ getPropA(): number; }' but required in type 'Base'.
```

**报错原因**

ArkTS语言的类型检查要求类型和对象要匹配，Base有两个方法，但是赋值的对象只有一个，如果不在编译时检查报错，可能会在运行时出现异常。

**对象字面量初始化class实例**

**不推荐使用**

通过对象字面量初始化class实例是业界不推荐的用法。

会造成以下问题：

1. 篡改SDK提供的API，应用可覆盖SDK API，在后续的使用中有安全风险。

   ```ts
   // SDK API
   declare class Person1 {
     name: string;
     age: number;
     greet(): void;
   }
   // apply
   const p: Person1 = {
     name: 'Bob',
     age: 40,
     greet() {} // Tampering with system greet behavior.
   }
   ```
2. 运行时与该class无关，应用使用instanceof检查该对象与class的关系，返回false。

   ```ts
   // SDK API
   declare class Person2 {
     name: string;
     age: number;
     greet(): void;
   }
   // apply
   const p1: Person2 = {
     name: 'Bob',
     age: 40,
     greet() {}
   }
   console.log(`${p1 instanceof Person2}`); // return false
   ```

**业界使用罕见**

使用class的场景主要为：

1. 实例化，占比65%。

   ```ts
   // SDK API
   declare class Person3 {
     name: string;
     age: number;
     greet(): void;
   }
   const p2: Person3 = new Person3();
   ```
2. 子类继承，占比25%。

   ```ts
   // SDK API
   declare class Person4 {
     name: string;
     age: number;
     greet(): void;
   }

   class Student extends Person4 {
     study() {}
   }
   ```
3. 使用其静态方法，占比20%。

   ```ts
   // SDK API
   declare class Person5 {
     name: string;
     age: number;
     static greet(): void;
   }
   Person5.greet();
   ```
4. 其它用法，包括通过对象字面量初始化，占比小于0.01%。

   ```ts
   declare class Person6 {
     name: string;
     age: number;
     greet(): void;
   }

   const p3: Person2 = {
     name: 'Bob',
     age: 40,
     greet() {}
   }
   ```

扫描开源社区TypeScript官方代码，其.ts代码有80w行，其中通过对象字面量初始化class实例的代码为：生产代码，9行，占0.001%；测试代码，63行，占0.008%。

**系统演进**

操作系统的开放能力会持续演进，在class中新增方法是常见的演进行为，在HarmonyOS与业界其他操作系统中非常常见。

以程序框架UIAbilityContext为例，在API9、10、12版本中均有新增API：

```typescript
declare class UIAbilityContext {
  /**
   * @since 9
   */
  startAbility(): void;
  /**
   * @since 9
   */
  startAbilityForResult(): void;
  /**
   * @since 10
   */
  setMissionContinueState(): void;
  /**
   * @since 12
   */
  backToCallerAbilityWithResult(): Promise<void>;
}
```

**修改方案**

为保证操作系统开放能力的持续演进，开发者使用对象字面量的方式初始化class实例，若编译失败，需要修改。

应用不使用对象字面量的方式初始化class实例，修改为通过new的方式初始化。

```ts
// SDK
declare class Base2 {
  // since 9
  getPropA(): number;
  // since 12 new method
  getPropB(): number;
}

// Initialize an instance of a class using the new method.
let b2: Base2 = new Base2();
// Upgrading to API 12 SDK will not result in errors.
```
