---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed
title: @Computed装饰器：计算属性
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理数据对象的状态 > @Computed装饰器：计算属性
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:600a2eb7c927a71e0e79830b071afd8757f493ef446943ace3515c879ad10e43
---

当开发者使用相同的计算逻辑重复绑定在UI上时，为了防止重复计算，可以使用@Computed计算属性。计算属性中依赖的状态变量变化时，只会计算一次。这解决了UI多次重用该属性导致的重复计算和性能问题。如下面例子。

```
1. @Computed
2. get sum() {
3. return this.count1 + this.count2 + this.count3;
4. }
```

[ComputedProperty.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewComputed/entry/src/main/ets/pages/ComputedProperty.ets#L24-L29)

```
1. Text(`${this.count1 + this.count2 + this.count3}`) // 计算this.count1 + this.count2 + this.count3
2. Text(`${this.count1 + this.count2 + this.count3}`) // 重复计算this.count1 + this.count2 + this.count3
3. Text(`${this.sum}`) // 读取@Computed sum的缓存值，节省上述重复计算
4. Text(`${this.sum}`) // 读取@Computed sum的缓存值，节省上述重复计算
```

[ComputedProperty.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewComputed/entry/src/main/ets/pages/ComputedProperty.ets#L34-L39)

在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)，[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)，[@Local](arkts-new-local.md)。

说明

@Computed装饰器从API version 12开始支持。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Computed为方法装饰器，装饰getter方法。@Computed会检测被计算的属性变化，当被计算的属性变化时，@Computed只会被求解一次。不建议在@Computed中修改变量，错误的使用会导致数据无法被追踪或appfreeze等问题，详情见[使用限制](arkts-new-computed.md#使用限制)。

但需要注意，对于简单计算，不建议使用计算属性，因为计算属性本身也有开销。对于复杂的计算，@Computed能带来性能收益。

## 装饰器说明

@Computed语法：

```
1. @Computed
2. get varName(): T {
3. return value;
4. }
```

| @Computed方法装饰器 | 说明 |
| --- | --- |
| 支持类型 | getter访问器。 |
| 从父组件初始化 | 禁止。 |
| 可初始化子组件 | [@Param](arkts-new-param.md)。 |
| 被执行的时机 | @ComponentV2中的@Computed会在自定义组件创建的时候初始化，触发@Computed计算。  @ObservedV2装饰的类中的@Computed，会在@ObservedV2装饰的类实例创建后，异步初始化，触发@Computed计算。  在@Computed中计算的状态变量被改变时，计算属性会重新计算。 |
| 是否允许赋值 | @Computed装饰的属性是只读的，不允许赋值，详情见[使用限制](arkts-new-computed.md#使用限制)。 |

## 使用限制

* @Computed为方法装饰器，仅能装饰getter方法。

  ```
  1. @Computed
  2. get fullName() { // 正确用法
  3. return this.firstName + ' ' + this.lastName;
  4. }
  5. @Computed val: number = 0; // 错误用法，编译时报错
  6. @Computed
  7. func() { // 错误用法，编译时报错
  8. }
  ```
* @Computed装饰的方法只有在初始化，或者其被计算的状态变量改变时，才会发生重新计算。不建议开发者在@Computed装饰的getter方法中做除获取数据外其余的逻辑操作，如下面例子。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Page {
  4. @Local firstName: string = 'Hua';
  5. @Local lastName: string = 'Li';
  6. @Local showFullNameRequestCount: number = 0;
  7. private fullNameRequestCount: number = 0;

  9. @Computed
  10. get fullName() {
  11. console.info('fullName');
  12. // 不建议在@Computed的计算中做赋值逻辑，因为@Computed本质是一个getter访问器，用来节约重复计算
  13. // 在这个例子中，fullNameRequestCount仅代表@Computed计算次数，不能代表fullName被访问的次数
  14. this.fullNameRequestCount++;
  15. return this.firstName + ' ' + this.lastName;
  16. }

  18. build() {
  19. Column() {
  20. Text(`${this.fullName}`) // 获取一次fullName
  21. Text(`${this.fullName}`) // 获取一次fullName，累计获取两次fullName，但是fullName不会重新计算，读取缓存值

  23. // 点击Button，获取fullNameRequestCount次数
  24. Text(`count ${this.showFullNameRequestCount}`)
  25. Button('get fullName').onClick(() => {
  26. this.showFullNameRequestCount = this.fullNameRequestCount;
  27. })
  28. }
  29. }
  30. }
  ```
* 在@Computed装饰的getter方法中，不能改变参与计算的属性，以防止重复执行计算属性导致的appfreeze。

  在下面例子中，计算fullName1时触发了this.lastName的改变，this.lastName的改变，触发fullName2的计算，在fullName2的计算中，改变了this.firstName，再次触发fullName1的重新计算，从而导致循环计算，最终引起appfreeze。

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Page {
  4. @Local firstName: string = 'Hua';
  5. @Local lastName: string = 'Li';

  7. @Computed
  8. get fullName1() {
  9. console.info('fullName1');
  10. this.lastName += 'a'; // 错误，不能改变参与计算的属性
  11. return this.firstName + ' ' + this.lastName;
  12. }

  14. @Computed
  15. get fullName2() {
  16. console.info('fullName2');
  17. this.firstName += 'a'; // 错误，不能改变参与计算的属性
  18. return this.firstName + ' ' + this.lastName;
  19. }

  21. build() {
  22. Column() {
  23. Text(`${this.fullName1}`)
  24. Text(`${this.fullName2}`)
  25. }
  26. }
  27. }
  ```
* @Computed不能和[双向绑定!!](arkts-new-binding.md#概述)连用，@Computed装饰的是getter访问器，不会被子组件同步，也不能被赋值。开发者自己实现的计算属性的setter不生效，且产生编译时报错。

  ```
  1. @ComponentV2
  2. struct Child {
  3. @Param double: number = 100;
  4. @Event $double: (val: number) => void;

  6. build() {
  7. Button('ChildChange')
  8. .onClick(() => {
  9. this.$double(200);
  10. })
  11. }
  12. }

  14. @Entry
  15. @ComponentV2
  16. struct Index {
  17. @Local count: number = 100;

  19. @Computed
  20. get double() {
  21. return this.count * 2;
  22. }

  24. // @Computed装饰的属性是只读的，开发者自己实现的setter不生效，编译时报错。
  25. set double(newValue : number) {
  26. this.count = newValue / 2;
  27. }

  29. build() {
  30. Scroll() {
  31. Column({ space: 3 }) {
  32. Text(`${this.count}`)
  33. // 错误写法，@Computed装饰的属性是只读的，无法与双向绑定连用，编译时报错。
  34. Child({ double: this.double!! })
  35. }
  36. }
  37. }
  38. }
  ```
* @Computed为状态管理V2提供的能力，只能在@ComponentV2和@ObservedV2中使用。
* 多个@Computed一起使用时，警惕循环求解，以防止计算过程中的死循环。

  ```
  1. @Local a : number = 1;
  2. @Computed
  3. get b() {
  4. return this.a + ' ' + this.c;  // 错误写法，存在循环b -> c -> b
  5. }
  6. @Computed
  7. get c() {
  8. return this.a + ' ' + this.b; // 错误写法，存在循环c -> b -> c
  9. }
  ```

## 使用场景

### 当被计算的属性变化时，@Computed装饰的getter访问器只会被求解一次

1. 在自定义组件中使用计算属性。

   * 点击第一个Button改变lastName，触发@Computed fullName重新计算。
   * this.fullName被绑定在两个Text组件上，观察fullName日志，可以发现，计算只发生了一次。
   * 对于前两个Text组件，this.lastName + ' '+ this.firstName这段逻辑被求解了两次。
   * 如果UI中有多处需要使用this.lastName + ' '+ this.firstName这段计算逻辑，可以使用计算属性，减少计算次数。
   * 点击第二个Button，age自增，UI无变化。因为age非状态变量，只有被观察到的变化才会触发@Computed fullName重新计算。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = '[Sample_Textcomponent]';
   4. const DOMAIN = 0xF811;
   5. const BUNDLE = 'Textcomponent_';

   7. @Entry
   8. @ComponentV2
   9. struct CustomComponentUse {
   10. @Local firstName: string = 'Li';
   11. @Local lastName: string = 'Hua';
   12. age: number = 20; // 无法触发Computed

   14. @Computed
   15. get fullName() {
   16. hilog.info(DOMAIN, TAG, BUNDLE + '---------Computed----------');
   17. return this.firstName + ' ' + this.lastName + this.age;
   18. }

   20. build() {
   21. Column() {
   22. Text(this.lastName + ' ' + this.firstName)
   23. Text(this.lastName + ' ' + this.firstName)
   24. Divider()
   25. Text(this.fullName)
   26. Text(this.fullName)
   27. Button('changed lastName')
   28. .onClick(() => {
   29. this.lastName += 'a';
   30. })

   32. Button('changed age')
   33. .onClick(() => {
   34. this.age++;  // 无法触发Computed
   35. })
   36. }
   37. }
   38. }
   ```

   [CustomComponentUse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewComputed/entry/src/main/ets/pages/CustomComponentUse.ets#L15-L54)

   计算属性本身会带来性能开销，在实际应用开发中需要注意：

   * 对于简单的计算逻辑，可以不使用计算属性。
   * 如果计算逻辑在视图中仅使用一次，则不使用计算属性，直接求解。
2. 在@ObservedV2装饰的类中使用计算属性。

   点击Button改变lastName，触发@Computed fullName重新计算，且只被计算一次。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = '[Sample_Textcomponent]';
   4. const DOMAIN = 0xF811;
   5. const BUNDLE = 'Textcomponent_';

   7. @ObservedV2
   8. class Name {
   9. @Trace public firstName: string = 'Hua';
   10. @Trace public lastName: string = 'Li';

   12. @Computed
   13. get fullName() {
   14. hilog.info(DOMAIN, TAG, BUNDLE + '---------Computed----------');
   15. return this.firstName + ' ' + this.lastName;
   16. }
   17. }

   19. const name: Name = new Name();

   21. @Entry
   22. @ComponentV2
   23. struct ObservedV2ClassUser {
   24. name1: Name = name;

   26. build() {
   27. Column() {
   28. Text(this.name1.fullName)
   29. Text(this.name1.fullName)
   30. Button('changed lastName').onClick(() => {
   31. this.name1.lastName += 'a';
   32. })
   33. }
   34. }
   35. }
   ```

   [ObservedV2ClassUser.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewComputed/entry/src/main/ets/pages/ObservedV2ClassUser.ets#L15-L51)

### @Computed装饰的属性可以被@Monitor监听变化

如何使用计算属性求解fahrenheit和kelvin。示例如下：

* 点击“-”，celsius-- -> fahrenheit -> kelvin --> kelvin变化时调用onKelvinMonitor。
* 点击“+”，celsius++ -> fahrenheit -> kelvin --> kelvin变化时调用onKelvinMonitor。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. const TAG = '[Sample_Textcomponent]';
  4. const DOMAIN = 0xF811;
  5. const BUNDLE = 'Textcomponent_';

  7. @Entry
  8. @ComponentV2
  9. struct ComputedPropertyResolution {
  10. @Local celsius: number = 20;

  12. @Computed
  13. get fahrenheit(): number {
  14. return this.celsius * 9 / 5 + 32; // C -> F
  15. }

  17. @Computed
  18. get kelvin(): number {
  19. return (this.fahrenheit - 32) * 5 / 9 + 273.15; // F -> K
  20. }

  22. @Monitor('kelvin')
  23. onKelvinMonitor(mon: IMonitor) {
  24. hilog.info(DOMAIN, TAG, BUNDLE + 'kelvin changed from' + mon.value()?.before + ' to ' + mon.value()?.now);
  25. }

  27. build() {
  28. Column({ space: 20 }) {
  29. Row({ space: 20 }) {
  30. Button('-')
  31. .onClick(() => {
  32. this.celsius--;
  33. })

  35. Text(`Celsius ${this.celsius.toFixed(1)}`).fontSize(40)

  37. Button('+')
  38. .onClick(() => {
  39. this.celsius++;
  40. })
  41. }

  43. Text(`Fahrenheit ${this.fahrenheit.toFixed(2)}`).fontSize(40)
  44. Text(`Kelvin ${this.kelvin.toFixed(2)}`).fontSize(40)
  45. }
  46. .width('100%')
  47. }
  48. }
  ```

  [ComputingPropertyResolution.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewComputed/entry/src/main/ets/pages/ComputingPropertyResolution.ets#L15-L64)

### @Computed装饰的属性可以初始化@Param

下面的例子使用@Computed初始化@Param。

* 点击Button('-')和Button('+')改变商品数量，quantity是被@Trace装饰的，其改变时可以被观察到的。
* quantity的改变会触发total和qualifiesForDiscount重新计算，计算商品总价和是否可以享有优惠。
* total和qualifiesForDiscount的改变会触发子组件Child对应Text组件刷新。

  ```
  1. @ObservedV2
  2. class Article {
  3. @Trace public quantity: number = 0;
  4. public unitPrice: number = 0;

  6. constructor(quantity: number, unitPrice: number) {
  7. this.quantity = quantity;
  8. this.unitPrice = unitPrice;
  9. }
  10. }

  12. @Entry
  13. @ComponentV2
  14. struct ComputingInitParam {
  15. @Local shoppingBasket: Article[] = [new Article(1, 20), new Article(5, 2)];

  17. @Computed
  18. get total(): number {
  19. return this.shoppingBasket.reduce((acc: number, item: Article) => acc + (item.quantity * item.unitPrice), 0);
  20. }

  22. @Computed
  23. get qualifiesForDiscount(): boolean {
  24. return this.total >= 100;
  25. }

  27. build() {
  28. Column() {
  29. Text(`Shopping List: `)
  30. .fontSize(30)
  31. ForEach(this.shoppingBasket, (item: Article) => {
  32. Row() {
  33. Text(`unitPrice: ${item.unitPrice}`)
  34. Button('-')
  35. .onClick(() => {
  36. if (item.quantity > 0) {
  37. item.quantity--;
  38. }
  39. })
  40. Text(`quantity: ${item.quantity}`)
  41. Button('+')
  42. .onClick(() => {
  43. item.quantity++;
  44. })
  45. }

  47. Divider()
  48. })
  49. Child({ total: this.total, qualifiesForDiscount: this.qualifiesForDiscount })
  50. }.alignItems(HorizontalAlign.Start)
  51. }
  52. }

  54. @ComponentV2
  55. struct Child {
  56. @Param total: number = 0;
  57. @Param qualifiesForDiscount: boolean = false;

  59. build() {
  60. Row() {
  61. Text(`Total: ${this.total} `)
  62. .fontSize(30)
  63. Text(`Discount: ${this.qualifiesForDiscount} `)
  64. .fontSize(30)
  65. }
  66. }
  67. }
  ```

  [ComputedInitParam.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewComputed/entry/src/main/ets/pages/ComputedInitParam.ets#L16-L84)
