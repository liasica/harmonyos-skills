---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-class
title: 数据对象状态变量迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 数据对象状态变量迁移
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e0937d4cb66d3c11f27ac18f1537096d7579bbfd6232f2aab16cab94a13c80eb
---

本文档主要介绍数据对象内的状态变量的迁移场景，包含以下场景：

| V1装饰器名 | V2装饰器名 |
| --- | --- |
| [@ObjectLink](arkts-observed-and-objectlink.md)/[@Observed](arkts-observed-and-objectlink.md) /[@Track](arkts-track.md) | [@ObservedV2](arkts-new-observedv2-and-trace.md)/[@Trace](arkts-new-observedv2-and-trace.md) |

## 各装饰器迁移示例

### @ObjectLink/@Observed/@Track -> @ObservedV2/@Trace

**迁移规则**

在V1中，@Observed与@ObjectLink装饰器用于观察类对象及其嵌套属性的变化，但V1只能观察对象的第一层属性。嵌套对象的属性需要通过自定义组件和@ObjectLink观察。此外，V1中提供了@Track装饰器实现对属性级别变化的精确控制。

在V2中，结合使用@ObservedV2和@Trace，可以高效实现类对象及其嵌套属性的深度观察，省去对自定义组件的依赖，简化开发流程。同时，@Trace装饰器具备精确更新能力，替代V1中的@Track，实现更高效的UI刷新控制。根据不同场景，有以下迁移策略：

* 嵌套对象的属性观察：V1中需要通过自定义组件和@ObjectLink观察嵌套属性，V2中则可以使用@ObservedV2和@Trace直接观察嵌套对象，简化了代码结构。
* 类属性的精确更新：V1中的@Track可以用V2中的@Trace取代，@Trace可以同时观察和精确更新属性变化，使代码更简洁高效。

**示例**

**嵌套对象属性观察方法**

在V1中，无法直接观察嵌套对象的属性变化，只能观察到第一层属性的变化。必须通过创建自定义组件并使用@ObjectLink来实现对嵌套属性的观察。V2中使用@ObservedV2和@Trace，可以直接对嵌套对象的属性进行深度观察，减少复杂度。

V1实现：

```
1. @Observed
2. class Address {
3. public city: string;

5. constructor(city: string) {
6. this.city = city;
7. }
8. }

10. @Observed
11. class User {
12. public name: string;
13. public address: Address;

15. constructor(name: string, address: Address) {
16. this.name = name;
17. this.address = address;
18. }
19. }

21. @Component
22. struct AddressView {
23. // 子组件中@ObjectLink装饰的address从父组件初始化，接收被@Observed装饰的Address实例
24. @ObjectLink address: Address;

26. build() {
27. Column() {
28. Text(`City: ${this.address.city}`)
29. Button('city +a')
30. .onClick(() => {
31. this.address.city += 'a';
32. })
33. }
34. }
35. }

37. @Entry
38. @Component
39. struct UserProfile {
40. @State user: User = new User('Alice', new Address('New York'));

42. build() {
43. Column() {
44. Text(`Name: ${this.user.name}`)
45. // 无法直接观察嵌套对象的属性变化，例如this.user.address.city
46. // 只能观察到对象第一层属性变化，所以需要将嵌套的对象Address抽取到自定义组件AddressView
47. AddressView({ address: this.user.address })
48. }
49. }
50. }
```

[MigrationNestedObjectPropertiesV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/migrationDataObjectVariables/MigrationNestedObjectPropertiesV1.ets#L29-L80)

V2迁移策略：使用@ObservedV2和@Trace。

```
1. @ObservedV2
2. class Address {
3. @Trace public city: string;

5. constructor(city: string) {
6. this.city = city;
7. }
8. }

10. @ObservedV2
11. class User {
12. @Trace public name: string;
13. @Trace public address: Address;

15. constructor(name: string, address: Address) {
16. this.name = name;
17. this.address = address;
18. }
19. }

21. @Entry
22. @ComponentV2
23. struct UserProfile {
24. @Local user: User = new User('Alice', new Address('New York'));

26. build() {
27. Column() {
28. Text(`Name: ${this.user.name}`)
29. // 通过@ObservedV2和@Trace可以直接观察嵌套属性
30. Text(`City: ${this.user.address.city}`)
31. Button('city +a')
32. .onClick(() => {
33. this.user.address.city += 'a';
34. })
35. }
36. }
37. }
```

[MigrationNestedObjectPropertiesV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/migrationDataObjectVariables/MigrationNestedObjectPropertiesV2.ets#L29-L67)

**类属性变化观测**

在V1中，@Observed用于观察类实例及其属性的变化，@Track用于类对象的属性级的观察。在V2中，@Trace实现了观察和更新属性级别变化的能力，搭配@ObservedV2实现高效的UI更新。

V1实现：

```
1. @Observed
2. class User {
3. @Track public name: string;
4. @Track public age: number;

6. constructor(name: string, age: number) {
7. this.name = name;
8. this.age = age;
9. }
10. }

12. @Entry
13. @Component
14. struct UserProfile {
15. @State user: User = new User('Alice', 30);

17. build() {
18. Column() {
19. Text(`Name: ${this.user.name}`)
20. Text(`Age: ${this.user.age}`)
21. // 点击Button更新user.age，触发UI刷新
22. Button('increase age')
23. .onClick(() => {
24. this.user.age++;
25. })
26. }
27. }
28. }
```

[MigrationClassAttributeV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/migrationDataObjectVariables/MigrationClassAttributeV1.ets#L29-L57)

V2迁移策略：使用@ObservedV2和@Trace。

```
1. // V2使用@ObservedV2代替V1的@Observed
2. @ObservedV2
3. class User {
4. // V2使用@Trace代替V1的@Track
5. @Trace public name: string;
6. @Trace public age: number;

8. constructor(name: string, age: number) {
9. this.name = name;
10. this.age = age;
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct UserProfile {
17. @Local user: User = new User('Alice', 30);

19. build() {
20. Column() {
21. Text(`Name: ${this.user.name}`)
22. Text(`Age: ${this.user.age}`)
23. Button('Increase age')
24. .onClick(() => {
25. this.user.age++;
26. })
27. }
28. }
29. }
```

[MigrationClassAttributeV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/migrationDataObjectVariables/MigrationClassAttributeV2.ets#L29-L57)
