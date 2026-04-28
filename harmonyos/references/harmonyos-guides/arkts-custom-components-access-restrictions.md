---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-access-restrictions
title: 自定义组件成员属性访问限定符使用限制
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件成员属性访问限定符使用限制
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6fbed4b7e161ce5516d175cb1b41a8240b4032161b8b19a72f5968c07eb05876
---

在状态管理V1版本中，完成自定义组件封装后，调用方难以明确知晓应传入哪些变量作为组件的输入参数。当组件开发者不希望状态变量被外部初始化时，可以使用private限定符来限制当前变量不允许被外部初始化。外部初始化也需要遵循装饰器自身的规则，具体规则见[使用限制](arkts-custom-components-access-restrictions.md#使用限制)。

ArkTS会对自定义组件的成员变量使用的访问限定符private/public/protected进行校验，当不按规范使用访问限定符private/public/protected时，会产生对应的日志信息。

在阅读本文档前，建议提前阅读：[状态管理概述](arkts-state-management-overview.md)。

说明

从API version 12开始，支持自定义组件成员属性访问限定符使用限制的规则。

## 使用限制

* [@State](arkts-state.md)/[@Prop](arkts-prop.md)/[@Provide](arkts-provide-and-consume.md)/[@BuilderParam](arkts-builderparam.md)/常规成员变量(不涉及更新的普通变量)的初始化规则为可以被外部初始化，也可以使用本地值进行初始化。当组件开发者不希望当前变量被外部初始化时，可以使用private进行修饰，在这种情况下，错误进行外部初始化会有编译告警日志提示。
* [@StorageLink](arkts-appstorage.md#storagelink)/[@StorageProp](arkts-appstorage.md#storageprop)/[@LocalStorageLink](arkts-localstorage.md#localstoragelink)/[@LocalStorageProp](arkts-localstorage.md#localstorageprop)/[@Consume](arkts-provide-and-consume.md)变量的初始化规则为不可以被外部初始化，当组件开发者希望当前变量被外部初始化而使用public修饰时，与装饰器本身的初始化规则不符，会有编译告警日志提示。
* [@Link](arkts-link.md)/[@ObjectLink](arkts-observed-and-objectlink.md)变量的初始化规则为必须被外部初始化，禁止本地初始化。当组件开发者使用private对变量进行修饰时，与装饰器本身的初始化规则不符，会有编译告警日志提示。
* 由于struct没有继承能力，上述所有的这些变量使用protected修饰时，会有编译告警日志提示。
* [@Require](arkts-require.md)含义是当前被@Require装饰的变量必须被外部初始化，当@Require和private同时装饰[@State](arkts-state.md)/[@Prop](arkts-prop.md)/[@Provide](arkts-provide-and-consume.md)/[@BuilderParam](arkts-builderparam.md)/常规成员变量(不涉及更新的普通变量)时，它们的含义是自相矛盾的，会有编译告警日志提示。

## 使用场景

1. 当成员变量被private访问限定符和@State/@Prop/@Provide/@BuilderParam装饰器同时修饰，并且通过父组件进行初始化赋值，ArkTS会进行校验并产生告警日志。

   【反例】

   ```
   1. @Entry
   2. @Component
   3. struct LinkErrorAccessRestrictions {
   4. @Builder
   5. buildTest() {
   6. Text('Parent builder')
   7. }

   9. build() {
   10. Column() {
   11. LinkErrorComponentChild({
   12. stateValue: 'Hello',
   13. propValue: 'Hello',
   14. provideValue: 'Hello',
   15. builderValue: this.buildTest,
   16. regularValue: 'Hello'
   17. })
   18. }
   19. .width('100%')
   20. }
   21. }

   23. @Component
   24. struct LinkErrorComponentChild {
   25. // 此处使用private修饰符时会出现告警日志
   26. @State private stateValue: string = 'Hello';
   27. // 此处使用private修饰符时会出现告警日志
   28. @Prop private propValue: string = 'Hello';
   29. // 此处使用private修饰符时会出现告警日志
   30. @Provide private provideValue: string = 'Hello';
   31. // 此处使用private修饰符时会出现告警日志
   32. @BuilderParam private builderValue: () => void = this.buildTest;
   33. // 此处使用private修饰符时会出现告警日志
   34. private regularValue: string = 'Hello';

   36. @Builder
   37. buildTest() {
   38. Text('Child builder')
   39. }

   41. build() {
   42. Column() {
   43. Text('Hello')
   44. .fontSize(50)
   45. .fontWeight(FontWeight.Bold)
   46. }
   47. }
   48. }
   ```

   [LlinkWithPrivateErrorCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/linkWithPrivate/LlinkWithPrivateErrorCase.ets#L16-L66)

   编译告警日志如下：

   ```
   1. Property 'stateValue' is private and can not be initialized through the component constructor.
   2. Property 'propValue' is private and can not be initialized through the component constructor.
   3. Property 'provideValue' is private and can not be initialized through the component constructor.
   4. Property 'builderValue' is private and can not be initialized through the component constructor.
   5. Property 'regularValue' is private and can not be initialized through the component constructor.
   ```

   【正例】

   ```
   1. @Entry
   2. @Component
   3. struct LinkAccessRestrictions {
   4. @Builder
   5. buildTest() {
   6. Text('Parent builder')
   7. }

   9. build() {
   10. Column() {
   11. LinkComponentChild({
   12. stateValue: 'Hello',
   13. propValue: 'Hello',
   14. provideValue: 'Hello',
   15. builderValue: this.buildTest,
   16. regularValue: 'Hello'
   17. })
   18. }
   19. .width('100%')
   20. }
   21. }

   23. @Component
   24. struct LinkComponentChild {
   25. @State stateValue: string = 'Hello';
   26. @Prop propValue: string = 'Hello';
   27. @Provide provideValue: string = 'Hello';
   28. @BuilderParam builderValue: () => void = this.buildTest;
   29. regularValue: string = 'Hello';

   31. @Builder
   32. buildTest() {
   33. Text('Child builder')
   34. }

   36. build() {
   37. Column() {
   38. Text('Hello')
   39. .fontSize(50)
   40. .fontWeight(FontWeight.Bold)
   41. }
   42. }
   43. }
   ```

   [LlinkWithPrivateCorrectCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/linkWithPrivate/LlinkWithPrivateCorrectCase.ets#L16-L61)
2. 当成员变量被public访问限定符和@StorageLink/@StorageProp/@LocalStorageLink/@LocalStorageProp/@Consume装饰器同时修饰，并且通过父组件进行初始化赋值，ArkTS会进行校验并产生告警日志。

   【反例】

   ```
   1. @Entry
   2. @Component
   3. struct PublicErrorAccessRestrictions {
   4. @Provide consumeValue: string = 'Hello';

   6. build() {
   7. Column() {
   8. PublicErrorComponentChild()
   9. }
   10. .width('100%')
   11. }
   12. }

   14. @Component
   15. struct PublicErrorComponentChild {
   16. // 此处使用public修饰符时会出现告警日志
   17. @LocalStorageProp('sessionLocalProp') public localPropValue: string = 'Hello';
   18. // 此处使用public修饰符时会出现告警日志
   19. @LocalStorageLink('sessionLocalLink') public localLinkValue: string = 'Hello';
   20. // 此处使用public修饰符时会出现告警日志
   21. @StorageProp('sessionProp') public storagePropValue: string = 'Hello';
   22. // 此处使用public修饰符时会出现告警日志
   23. @StorageLink('sessionLink') public storageLinkValue: string = 'Hello';
   24. // 此处使用public修饰符时会出现告警日志
   25. @Consume public consumeValue: string;

   27. build() {
   28. Column() {
   29. Text('Hello')
   30. .fontSize(50)
   31. .fontWeight(FontWeight.Bold)
   32. }
   33. }
   34. }
   ```

   [PublicWithStoragePropErrorCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/publicWithStorageProp/PublicWithStoragePropErrorCase.ets#L16-L52)

   编译告警日志如下：

   ```
   1. Property 'localPropValue' can not be decorated with both '@LocalStorageProp' and public.
   2. Property 'localLinkValue' can not be decorated with both '@LocalStorageLink' and public.
   3. Property 'storagePropValue' can not be decorated with both '@StorageProp' and public.
   4. Property 'storageLinkValue' can not be decorated with both '@StorageLink' and public.
   5. Property 'consumeValue' can not be decorated with both '@Consume' and public.
   ```

   【正例】

   ```
   1. @Entry
   2. @Component
   3. struct PublicCorrectAccessRestrictions {
   4. @Provide consumeValue: string = 'Hello';

   6. build() {
   7. Column() {
   8. PublicCorrectComponentChild()
   9. }
   10. .width('100%')
   11. }
   12. }

   14. @Component
   15. struct PublicCorrectComponentChild {
   16. @LocalStorageProp('sessionLocalProp') localPropValue: string = 'Hello';
   17. @LocalStorageLink('sessionLocalLink') localLinkValue: string = 'Hello';
   18. @StorageProp('sessionProp') storagePropValue: string = 'Hello';
   19. @StorageLink('sessionLink') storageLinkValue: string = 'Hello';
   20. @Consume consumeValue: string;

   22. build() {
   23. Column() {
   24. Text('Hello')
   25. .fontSize(50)
   26. .fontWeight(FontWeight.Bold)
   27. }
   28. }
   29. }
   ```

   [PublicWithStoragePropCorrectCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/publicWithStorageProp/PublicWithStoragePropCorrectCase.ets#L16-L47)
3. 当成员变量被private访问限定符和@Link/@ObjectLink装饰器同时修饰，并且通过父组件进行初始化赋值，ArkTS会进行校验并产生告警日志。

   【反例】

   ```
   1. @Entry
   2. @Component
   3. struct PrivateWithLinkErrorAccessRestrictions {
   4. @State linkValue: string = 'Hello';
   5. @State objectLinkValue: PrivateErrorComponentObj = new PrivateErrorComponentObj();

   7. build() {
   8. Column() {
   9. PrivateWithLinkErrorComponentChild({ linkValue: this.linkValue, objectLinkValue: this.objectLinkValue })
   10. }
   11. .width('100%')
   12. }
   13. }

   15. @Observed
   16. class PrivateErrorComponentObj {
   17. public count: number = 0;
   18. }

   20. @Component
   21. struct PrivateWithLinkErrorComponentChild {
   22. // 此处使用private修饰符时会出现告警日志
   23. @Link private linkValue: string;
   24. // 此处使用private修饰符时会出现告警日志
   25. @ObjectLink private objectLinkValue: PrivateErrorComponentObj;

   27. build() {
   28. Column() {
   29. Text('Hello')
   30. .fontSize(50)
   31. .fontWeight(FontWeight.Bold)
   32. }
   33. }
   34. }
   ```

   [PrivateWithLinkEerrorCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/privateWithLink/PrivateWithLinkEerrorCase.ets#L16-L52)

   编译告警日志如下：

   ```
   1. Property 'linkValue' can not be decorated with both '@Link' and private.
   2. Property 'objectLinkValue' can not be decorated with both '@ObjectLink' and private.
   ```

   【正例】

   ```
   1. @Entry
   2. @Component
   3. struct PrivateWithLinkAccessRestrictions {
   4. @State linkValue: string = 'Hello';
   5. @State objectLinkValue: PrivateComponentObj = new PrivateComponentObj();

   7. build() {
   8. Column() {
   9. PrivateWithLinkComponentChild({ linkValue: this.linkValue, objectLinkValue: this.objectLinkValue })
   10. }
   11. .width('100%')
   12. }
   13. }

   15. @Observed
   16. class PrivateComponentObj {
   17. public count: number = 0;
   18. }

   20. @Component
   21. struct PrivateWithLinkComponentChild {
   22. @Link linkValue: string;
   23. @ObjectLink objectLinkValue: PrivateComponentObj;

   25. build() {
   26. Column() {
   27. Text('Hello')
   28. .fontSize(50)
   29. .fontWeight(FontWeight.Bold)
   30. }
   31. }
   32. }
   ```

   [PrivateWithLinkCorrectCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/privateWithLink/PrivateWithLinkCorrectCase.ets#L16-L50)
4. 当成员变量被protected访问限定符修饰，并且通过父组件进行初始化赋值，ArkTS会进行校验并产生告警日志。

   【反例】

   ```
   1. @Entry
   2. @Component
   3. struct ProtectedErrorAccessRestrictions {
   4. build() {
   5. Column() {
   6. ProtectedErrorComponentChild({ regularValue: 'Hello' })
   7. }
   8. .width('100%')
   9. }
   10. }

   12. @Component
   13. struct ProtectedErrorComponentChild {
   14. // 此处使用protected修饰符时会出现告警日志
   15. protected regularValue: string = 'Hello';

   17. build() {
   18. Column() {
   19. Text('Hello')
   20. .fontSize(50)
   21. .fontWeight(FontWeight.Bold)
   22. }
   23. }
   24. }
   ```

   [ProtectedInStructErrorCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/protectedInStruct/ProtectedInStructErrorCase.ets#L16-L42)

   编译告警日志如下：

   ```
   1. The member attributes of a struct can not be protected.
   ```

   【正例】

   ```
   1. @Entry
   2. @Component
   3. struct ProtectedCorrectAccessRestrictions {
   4. build() {
   5. Column() {
   6. ProtectedCorrectComponentChild({ regularValue: 'Hello' })
   7. }
   8. .width('100%')
   9. }
   10. }

   12. @Component
   13. struct ProtectedCorrectComponentChild {
   14. regularValue: string = 'Hello';

   16. build() {
   17. Column() {
   18. Text('Hello')
   19. .fontSize(50)
   20. .fontWeight(FontWeight.Bold)
   21. }
   22. }
   23. }
   ```

   [ProtectedInStructCorrectCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/protectedInStruct/ProtectedInStructCorrectCase.ets#L16-L41)
5. 当成员变量被private访问限定符、@Require和@State/@Prop/@Provide/@BuilderParam装饰器同时修饰，并且通过父组件初始化赋值时，ArkTS会进行校验并产生告警日志。

   【反例】

   ```
   1. @Entry
   2. @Component
   3. struct PrivateErrorAccessRestrictions {
   4. build() {
   5. Column() {
   6. PrivateErrorComponentChild({ propValue: 'Hello' })
   7. }
   8. .width('100%')
   9. }
   10. }

   12. @Component
   13. struct PrivateErrorComponentChild {
   14. // 此处使用private修饰符时会出现告警日志
   15. @Require @Prop private propValue: string = 'Hello';

   17. build() {
   18. Column() {
   19. Text('Hello')
   20. .fontSize(50)
   21. .fontWeight(FontWeight.Bold)
   22. }
   23. }
   24. }
   ```

   [PrivateWithRequireErrorCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/privateWithRequire/PrivateWithRequireErrorCase.ets#L16-L42)

   编译告警日志如下：

   ```
   1. Property 'propValue' can not be decorated with both '@Require' and private.
   2. Property 'propValue' is private and can not be initialized through the component constructor.
   ```

   【正例】

   ```
   1. @Entry
   2. @Component
   3. struct PrivateCorrectAccessRestrictions {
   4. build() {
   5. Column() {
   6. PrivateCorrectComponentChild({ propValue: 'Hello' })
   7. }
   8. .width('100%')
   9. }
   10. }

   12. @Component
   13. struct PrivateCorrectComponentChild {
   14. @Require @Prop propValue: string = 'Hello';

   16. build() {
   17. Column() {
   18. Text('Hello')
   19. .fontSize(50)
   20. .fontWeight(FontWeight.Bold)
   21. }
   22. }
   23. }
   ```

   [PrivateWithRequireCorrectCase.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Restrictions/entry/src/main/ets/pages/privateWithRequire/PrivateWithRequireCorrectCase.ets#L16-L41)
