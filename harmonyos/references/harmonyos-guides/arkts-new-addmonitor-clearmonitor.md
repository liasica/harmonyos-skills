---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-addmonitor-clearmonitor
title: addMonitor/clearMonitor接口：动态添加/取消监听
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 辅助接口 > addMonitor/clearMonitor接口：动态添加/取消监听
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:24+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1d7cfc6fa3dcaf4a223908af2aa3905708fe88b1ce57ddce6076dd367979f877
---

为了动态添加或删除状态管理V2的状态变量的监听函数，开发者可以使用[addMonitor](../harmonyos-references/js-apis-statemanagement.md#addmonitor20)或[clearMonitor](../harmonyos-references/js-apis-statemanagement.md#clearmonitor20)。

在阅读本文档前，建议提前阅读：[@ObservedV2/@Trace](arkts-new-observedv2-and-trace.md)、[@Monitor](arkts-new-monitor.md)。

说明

从API version 20开始，开发者可以使用UIUtils中的addMonitor/clearMonitor接口动态给状态管理V2的状态变量添加或删除监听函数。

## 概述

装饰器[@Monitor](arkts-new-monitor.md)如果声明在[@ObservedV2](arkts-new-observedv2-and-trace.md)和[@ComponentV2](arkts-create-custom-components.md#componentv2)中，会使得开发者构造出的所有的@ObservedV2和@ComponentV2的实例，都默认有同样的@Monitor的监听回调，且无法取消或删除对应的监听回调。

如果开发者希望动态给@ObservedV2和@ComponentV2实例添加或者删除监听函数，则可以使用[addMonitor](../harmonyos-references/js-apis-statemanagement.md#addmonitor20)和[clearMonitor](../harmonyos-references/js-apis-statemanagement.md#clearmonitor20)接口。

* 使用addMonitor/clearMonitor接口需要导入UIUtils工具。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  ```
* 仅支持监听状态管理V2的状态变量的变化。
* clearMonitor仅可以删除addMonitor添加的监听函数，无法删除@Monitor的监听函数。

## 使用规则

* addMonitor/clearMonitor可以传入数组一次性给多个状态变量添加或删除回调函数。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 0;
6. @Trace name: string = 'Jack';

8. onChange1(mon: IMonitor) {
9. mon.dirty.forEach((path: string) => {
10. console.info(`onChange1: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
11. });
12. }

14. constructor() {
15. UIUtils.addMonitor(this, ['age', 'name'], this.onChange1);
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Page {
22. user: User = new User();

24. build() {
25. Column() {
26. Text(`User name ${this.user.name}`)
27. .fontSize(20)
28. .onClick(() => {
29. // 改变name，回调onChange1监听函数
30. this.user.name += '!';
31. })
32. Text(`User age ${this.user.age}`)
33. .fontSize(20)
34. .onClick(() => {
35. // age自增，回调onChange1监听函数
36. this.user.age++;
37. })
38. Button('clear name and age monitor fun')
39. .onClick(() => {
40. // 删除age和name的onChange1监听函数
41. // 再次点击Text组件改变name和age，无监听函数回调
42. UIUtils.clearMonitor(this.user, ['age', 'name'], this.user.onChange1);
43. })
44. }
45. }
46. }
```

* addMonitor可以给path对应的状态变量添加多个监听函数，但是需要注意，如果开发者添加同名的监听函数，则会添加失败，打印错误日志。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 0;

7. onChange1(mon: IMonitor) {
8. mon.dirty.forEach((path: string) => {
9. console.info(`onChange1: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
10. });
11. }

13. onChange2(mon: IMonitor) {
14. mon.dirty.forEach((path: string) => {
15. console.info(`onChange2: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
16. });
17. }

19. constructor() {
20. // 正确用法，给age注册监听函数onChange1
21. UIUtils.addMonitor(this, 'age', this.onChange1);
22. // 正确用法，给age注册监听函数onChange2
23. UIUtils.addMonitor(this, 'age', this.onChange2);
24. }
25. }

27. @Entry
28. @ComponentV2
29. struct Page {
30. user: User = new User();

32. onChange1(mon: IMonitor) {
33. mon.dirty.forEach((path: string) => {
34. console.info(`onChange1 in View: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
35. });
36. }

38. aboutToAppear(): void {
39. // 错误用法，已经给age注册过方法名为onChange1的函数，无法重复注册相同函数名的监听函数
40. // 打印错误日志提示添加失败：FIX THIS APPLICATION ERROR: AddMonitor 'onChange1' owned by 'User' path: 'age' - failed when adding duplicate path
41. UIUtils.addMonitor(this.user, 'age', this.onChange1);
42. }

44. build() {
45. Column() {
46. Text(`User age ${this.user.age}`)
47. .fontSize(20)
48. .onClick(() => {
49. // age自增，回调User中的onChange1和onChange2方法
50. this.user.age++;
51. })
52. }
53. }
54. }
```

* addMonitor设置[isSynchronous](../harmonyos-references/js-apis-statemanagement.md#monitoroptions20)仅第一次有效，即其不能被更改，如果开发者更改isSynchronous，则会打印错误日志。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 0;

7. onChange1(mon: IMonitor) {
8. mon.dirty.forEach((path: string) => {
9. console.info(`onChange1: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
10. });
11. }

13. constructor() {
14. // 正确用法，给a注册监听函数onChange1，没有设置options默认为异步监听回调
15. UIUtils.addMonitor(this, 'age', this.onChange1);
16. // 错误用法，不能改变this.onChange1的监听回调的方式
17. // 打印错误日志提示： FIX THIS APPLICATION ERROR: addMonitor failed, current function onChange1 has already register as async, cannot change to sync anymore
18. UIUtils.addMonitor(this, 'age', this.onChange1, { isSynchronous: true });
19. }
20. }

22. @Entry
23. @ComponentV2
24. struct Page {
25. user: User = new User();

27. build() {
28. Column() {
29. Text(`User age ${this.user.age}`)
30. .fontSize(20)
31. .onClick(() => {
32. // age自增，回调onChange1，回调方式为异步回调
33. // 监听回调的日志：onChange1: User property age change from 0 to 2
34. this.user.age++;
35. this.user.age++;
36. })
37. }
38. }
39. }
```

* clearMonitor可以删除path对应的状态变量的监听函数，开发者可以通过传入监听回调函数来指定删除具体的监听函数，也可以不指定具体的监听函数，删除当前path对应状态变量的所有监听回调函数。

  需要注意：当调用clearMonitor时，如果发现当前回调函数没有在path对应的状态变量上注册过，或者当前状态变量没有任何监听函数，都会打印告警日志提示开发者删除失败。

  监听函数被删除后，状态变量的改变不会再回调对应的监听函数。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 0;
6. @Trace name: string = 'Jack';

8. onChange1(mon: IMonitor) {
9. mon.dirty.forEach((path: string) => {
10. console.info(`onChange1: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
11. });
12. }

14. onChange2(mon: IMonitor) {
15. mon.dirty.forEach((path: string) => {
16. console.info(`onChange2: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
17. });
18. }

20. onChange3(mon: IMonitor) {
21. mon.dirty.forEach((path: string) => {
22. console.info(`onChange3: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
23. });
24. }

26. constructor() {
27. UIUtils.addMonitor(this, 'age', this.onChange1);
28. UIUtils.addMonitor(this, 'age', this.onChange2);
29. UIUtils.addMonitor(this, 'age', this.onChange3);
30. }
31. }

33. @Entry
34. @ComponentV2
35. struct Page {
36. user: User = new User();

38. build() {
39. Column() {
40. Text(`User age ${this.user.age}`)
41. .fontSize(20)
42. .onClick(() => {
43. // step1：点击age，回调onChange1，onChange2，onChange3
44. this.user.age++;
45. })
46. Button('clear age onChange1').onClick(() => {
47. // step2：第一次点击该Button。删除onChange1，删除成功。此时点击User age，仅会回调onChange2，onChange3
48. // step3：再次点击该Button。再次删除onChange1，onChange1已经被删除，此次删除失败
49. // 打印错误日志：FIX THIS APPLICATION ERROR: cannot clear path age for onChange1 because it was never registered with addMonitor
50. UIUtils.clearMonitor(this.user, 'age', this.user.onChange1);
51. })
52. Button('clear age monitors').onClick(() => {
53. // step4：删除age所有添加的监听函数。再次点击User age，无监听函数回调
54. UIUtils.clearMonitor(this.user, 'age');
55. })
56. Button('clear name monitors').onClick(() => {
57. // step5：删除name添加的监听方法。因为name无任何监听回调，删除失败
58. // 打印错误日志：FIX THIS APPLICATION ERROR: cannot clear path name for current target User because no Monitor function for this path was registered
59. UIUtils.clearMonitor(this.user, 'name');
60. })
61. }
62. }
63. }
```

## 限制条件

* addMonitor/clearMonitor仅支持对@ComponentV2和@ObservedV2装饰（至少有一个@Trace装饰的变量）的实例添加/取消回调，否则会有运行时报错，错误码为130000。

  下面为addMonitor的例子，clearMonitor同理。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @ObservedV2
  4. class A {
  5. @Trace a: number = 0;

  7. onChange(mon: IMonitor) {
  8. mon.dirty.forEach((path: string) => {
  9. console.info(`A property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
  10. });
  11. }

  13. constructor() {
  14. // 正确用法
  15. UIUtils.addMonitor(this, 'a', this.onChange);
  16. }
  17. }

  19. @Observed
  20. class B {
  21. @Track b: number = 0;

  23. onChange(mon: IMonitor) {
  24. mon.dirty.forEach((path: string) => {
  25. console.info(`B property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
  26. });
  27. }

  29. constructor() {
  30. // 目标对象非法入参，当前this为@Observed装饰的对象
  31. // Error code: 130000
  32. UIUtils.addMonitor(this, 'b', this.onChange);
  33. }
  34. }

  36. class C {
  37. @Track c: number = 0;

  39. onChange(mon: IMonitor) {
  40. mon.dirty.forEach((path: string) => {
  41. console.info(`C property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
  42. });
  43. }

  45. constructor() {
  46. // 错误用法：目标对象非法入参，当前this为普通class
  47. // Error code: 130000
  48. UIUtils.addMonitor(this, 'c', this.onChange);
  49. // 错误用法：目标对象非法入参undefined
  50. // Error code: 130000
  51. UIUtils.addMonitor(undefined, 'c', this.onChange);
  52. }
  53. }

  55. let a: A = new A();
  56. let b: B = new B();
  57. let c: C = new C();
  ```
* addMonitor/clearMonitor观察路径必须为string或者为数组，如果开发者传入不支持的类型，则会有运行时报错，错误码为130001。

  下面为addMonitor的例子，clearMonitor同理。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @ObservedV2
  4. class A {
  5. @Trace a: number = 0;
  6. @Trace b: number = 0;
  7. invalidPath: number | string = 0;

  9. onChange(mon: IMonitor) {
  10. mon.dirty.forEach((path: string) => {
  11. console.info(`A property ${path} change from ${mon.value(path)?.before} to   ${mon.value(path)?.now}`);
  12. });
  13. }

  15. constructor() {
  16. // 正确用法
  17. UIUtils.addMonitor(this, 'a', this.onChange);
  18. // 正确用法
  19. UIUtils.addMonitor(this, ['a', 'b'], this.onChange);
  20. // 错误用法，path必须为string或数组，会发生运行时校验，错误码为130001
  21. UIUtils.addMonitor(this, this.invalidPath as string, this.onChange);
  22. // 错误用法，path必须为string或数组，会发生运行时校验，错误码为130001
  23. UIUtils.addMonitor(this, undefined, this.onChange);
  24. }
  25. }

  27. let a: A = new A();
  ```
* addMonitor的回调函数必须存在，类型必须为方法类型，且不能为匿名函数，如果开发者传入不支持的类型，则会有运行时报错，错误码为130002。

  clearMonitor开发者可以不设置回调函数，如果设置了，其类型必须为function类型，且不能为匿名函数。

  ```
  1. import { UIUtils } from '@kit.ArkUI';

  3. @ObservedV2
  4. class A {
  5. @Trace a: number = 0;
  6. @Trace b: number = 0;
  7. invalidFunc: Function | number = 0;

  9. onChange1(mon: IMonitor) {
  10. mon.dirty.forEach((path: string) => {
  11. console.info(`A property ${path} change from ${mon.value(path)?.before} to   ${mon.value(path)?.now}`);
  12. });
  13. }

  15. onChange2(mon: IMonitor) {
  16. mon.dirty.forEach((path: string) => {
  17. console.info(`A property ${path} change from ${mon.value(path)?.before} to   ${mon.value(path)?.now}`);
  18. });
  19. }

  21. constructor() {
  22. // 正确用法，给变量a添加函数onChange1
  23. UIUtils.addMonitor(this, 'a', this.onChange1);
  24. // 正确用法，给变量a添加函数onChange2
  25. UIUtils.addMonitor(this, 'a', this.onChange2);
  26. // 正确用法，给变量b添加函数onChange1
  27. UIUtils.addMonitor(this, 'b', this.onChange1);
  28. // 错误用法。传入的回调函数为非function类型，错误码130002
  29. UIUtils.addMonitor(this, 'a', undefined);
  30. // 错误用法，传入的回调函数为匿名函数，错误码130002
  31. UIUtils.addMonitor(this, 'a', (mon: IMonitor) => {});
  32. // 错误用法，绕过编译器检查，传入的回调函数为非Function类型，错误码130002
  33. UIUtils.addMonitor(this, 'a', this.invalidFunc as (mon: IMonitor) => void);
  34. }
  35. }

  37. let a: A = new A();
  38. // 正确用法，删除a注册的监听函数onChange1
  39. UIUtils.clearMonitor(a, 'a', a.onChange1);
  40. // 正确用法，删除a所有的监听函数
  41. UIUtils.clearMonitor(a, 'a');
  42. // 正确用法。等于不传参数，删除b所有的监听函数
  43. UIUtils.clearMonitor(a, 'a', undefined);
  44. // 错误用法，传入的回调函数为匿名函数，错误码130002
  45. UIUtils.clearMonitor(a, 'a', (mon: IMonitor) => {});
  ```

## addMonitor监听变化的规则

addMonitor和装饰器[@Monitor](arkts-new-monitor.md)监听变化的主要规则大体保持一致，对比如下表：

| 场景 | addMonitor | @Monitor |
| --- | --- | --- |
| [监听@ObservedV2类中@Trace修饰属性的变化](arkts-new-addmonitor-clearmonitor.md#监听observedv2类中trace修饰属性和componentv2组件中状态变量的变化) | 支持 | 支持 |
| [监听@ComponentV2组件中状态变量的变化](arkts-new-addmonitor-clearmonitor.md#监听observedv2类中trace修饰属性和componentv2组件中状态变量的变化) | 支持 | 支持 |
| [监听数组类型状态变量的下标和length的变化](arkts-new-addmonitor-clearmonitor.md#监听数组类型状态变量的下标和length的变化) | 支持 | 支持 |
| 监听Map、Set、Date类型状态变量变化 | 不支持 | 不支持 |
| [独立监听path变化](arkts-new-addmonitor-clearmonitor.md#独立监听path) | 支持 | 不支持 |
| [监听变量从可访问到不访问和从不可访问到可访问](arkts-new-addmonitor-clearmonitor.md#监听变量从可访问到不访问和从不可访问到可访问) | 支持 | 不支持 |
| [配置同步监听函数](arkts-new-addmonitor-clearmonitor.md#配置同步监听函数) | 支持 | 不支持 |
| [监听构造函数中同步修改的状态变量的变化](arkts-new-addmonitor-clearmonitor.md#监听构造函数中同步修改的状态变量的变化) | 支持 | 不支持 |
| [动态取消@ObservedV2/@ComponentV2实例的监听](arkts-new-addmonitor-clearmonitor.md#动态取消observedv2componentv2实例的监听) | 支持 | 不支持 |

## 使用场景

### 监听@ObservedV2类中@Trace修饰属性和@ComponentV2组件中状态变量的变化

在下面的例子中：

* 在User的构造函数中添加对age和name的监听函数onChange。
* 在自定义组件Page的aboutToAppear的生命周期中，添加对user的监听函数onChangeInView。
* 点击Text(`User name ${this.user.name}`)，改变name的值，触发onChange方法。
* 点击Text(`User age ${this.user.age}`)，改变age的值，触发onChange方法。
* 点击Text(`reset User`)，对user整体赋值，触发onChangeInView方法。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 0;
6. @Trace name: string = 'Jack';

8. onChange(mon: IMonitor) {
9. mon.dirty.forEach((path: string) => {
10. console.info(`onChange: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
11. });
12. }

14. constructor() {
15. UIUtils.addMonitor(this, ['age', 'name'], this.onChange);
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Page {
22. @Local user: User = new User();

24. onChangeInView(mon: IMonitor) {
25. mon.dirty.forEach((path: string) => {
26. console.info(`onChange in View: View property ${path} change from ${JSON.stringify(mon.value(path)?.before)} to ${JSON.stringify(mon.value(path)?.now)}`);
27. });
28. }

30. aboutToAppear(): void {
31. UIUtils.addMonitor(this, 'user', this.onChangeInView);
32. }

34. build() {
35. Column() {
36. Text(`User name ${this.user.name}`)
37. .fontSize(20)
38. .onClick(() => {
39. // 改变name，回调onChange监听函数
40. this.user.name += '!';
41. })
42. Text(`User age ${this.user.age}`)
43. .fontSize(20)
44. .onClick(() => {
45. // age自增，回调onChange监听函数
46. this.user.age++;
47. })
48. Text(`reset User`)
49. .fontSize(20)
50. .onClick(() => {
51. // user整体赋值，回调onChangeInView监听函数
52. this.user = new User();
53. })
54. }
55. }
56. }
```

### 监听数组类型状态变量的下标和length的变化

下面的例子展示了对Array数组下标和length的监听。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct Page {
6. @Local arr: string[] = ['a', 'b', 'c']

8. onChange(mon: IMonitor) {
9. mon.dirty.forEach((path: string) => {
10. console.info(`onChange: View property ${path} change from ${JSON.stringify(mon.value(path)?.before)} to ${JSON.stringify(mon.value(path)?.now)}`);
11. });
12. }

14. aboutToAppear(): void {
15. // 添加对数组index为0,1,2和数组length的监听回调onChange
16. UIUtils.addMonitor(this, ['arr.0', 'arr.1', 'arr.2', 'arr.length'], this.onChange);
17. }

19. build() {
20. Column() {
21. Text(`len ${this.arr.length}`).fontSize(20)
22. Text(`${this.arr[0]}`).fontSize(20).onClick(() => {
23. // 改变数组index为0的数组项
24. // onChange回调：onChange: View property arr.0 change from "a" to "az"
25. this.arr[0] += 'z';
26. })
27. Text(`${this.arr[1]}`).fontSize(20).onClick(() => {
28. // 改变数组index为1的数组项
29. // onChange回调：onChange: View property arr.1 change from "b" to "bz"
30. this.arr[1] += 'z';
31. })
32. Text(`${this.arr[2]}`).fontSize(20).onClick(() => {
33. // 改变数组index为2的数组项
34. // onChange回调：onChange: View property arr.2 change from "c" to "cz"
35. this.arr[2] += 'z';
36. })
37. Text(`push`).fontSize(20).onClick(() => {
38. // 在数组末尾push新数组项'd'，其index为4，index为4没有被监听
39. // 数组长度改变，length被监听
40. // onChange回调：onChange: View property arr.length change from 3 to 4
41. this.arr.push('d');
42. })
43. Text(`shift`).fontSize(20).onClick(() => {
44. // 删除数组第一个元素
45. // 0: az -> bz
46. // 1: bz -> cz
47. // 2: cz -> d
48. // length: 4 -> 3
49. // onChange回调：
50. // onChange: View property arr.0 change from "az" to "bz"
51. // onChange: View property arr.1 change from "bz" to "cz"
52. // onChange: View property arr.2 change from "cz" to "d"
53. // onChange: View property arr.length change from 4 to 3
54. this.arr.shift();
55. })
56. }
57. }
58. }
```

### 独立监听Path

@Monitor没有对path独立监听，所以需要依赖开发者正确传入@Monitor入参，[传入非状态变量时会造成被连带监听的情况](arkts-new-monitor.md#正确设置monitor入参)。

对于addMonitor，对不同path采取了独立监听的机制，如下面的例子，点击Button('change age&name')，会输出以下日志：

```
1. property path:age change from 24 to 25
```

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class Info {
5. name: string = 'John';
6. @Trace age: number = 24;

8. onPropertyChange(monitor: IMonitor) {
9. monitor.dirty.forEach((path: string) => {
10. console.info(`property path:${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
11. });
12. }

14. constructor() {
15. UIUtils.addMonitor(this, ['age', 'name'], this.onPropertyChange);
16. }
17. }

19. @Entry
20. @ComponentV2
21. struct Index {
22. info: Info = new Info();
23. build() {
24. Column() {
25. Button('change age&name')
26. .onClick(() => {
27. this.info.age = 25; // 同时改变状态变量age和非状态变量name
28. this.info.name = 'Johny';
29. })
30. }
31. }
32. }
```

### 监听变量从可访问到不访问和从不可访问到可访问

[@Monitor不会记录状态变量不可访问时的状态](arkts-new-monitor.md#无法监听变量从可访问变为不可访问和从不可访问变为可访问)，所以其无法监听变量从可访问到不访问和从不可访问到可访问。

addMonitor会记录变量不可访问的状态，所以可以监听变量从可访问到不访问和从不可访问到可访问。例子如下。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 10;
6. }

8. @Entry
9. @ComponentV2
10. struct Page {
11. @Local user: User | undefined | null = new User();

13. onChange(mon: IMonitor) {
14. mon.dirty.forEach((path: string) => {
15. console.info(`onChange: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
16. });
17. }

19. aboutToAppear() {
20. UIUtils.addMonitor(this, ['user.age'], this.onChange);
21. }

23. build() {
24. Column() {
25. Text(`User age ${this.user?.age}`).fontSize(20)
26. Button('set user to undefined').onClick(() => {
27. // age可访问->不可访问
28. // 触发onChange监听回调：onChange: User property user.age change from 10 to undefined
29. this.user = undefined;
30. })
31. Button('set user to User').onClick(() => {
32. // age不可访问->可访问
33. // 触发onChange监听回调：onChange: User property user.age change from undefined to 10
34. this.user = new User();
35. })
36. Button('set user to null').onClick(() => {
37. // age可访问->不可访问
38. // 触发onChange监听回调：onChange: User property user.age change from 10 to undefined
39. this.user = null;
40. })
41. }
42. }
43. }
```

### 配置同步监听函数

和@Monitor仅支持异步监听不同，addMonitor可支持配置成同步监听函数，在下面的例子中，点击Text(`User age ${this.user.age}`)，触发两次age的自增，回调两次onChange函数，日志打印如下：

```
1. onChange: User property user.age change from 10 to 11
2. onChange: User property user.age change from 11 to 12
```

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 10;
6. }

8. @Entry
9. @ComponentV2
10. struct Page {
11. @Local user: User = new User();

13. onChange(mon: IMonitor) {
14. mon.dirty.forEach((path: string) => {
15. console.info(`onChange: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
16. });
17. }

19. aboutToAppear(): void {
20. // addMonitor支持配置成同步监听函数
21. UIUtils.addMonitor(this, 'user.age', this.onChange, { isSynchronous: true })
22. }

24. build() {
25. Column() {
26. Text(`User age ${this.user.age}`).fontSize(20).onClick(() => {
27. this.user.age++;
28. this.user.age++;
29. })
30. }
31. }
32. }
```

如果将上面的例子改成@Monitor，仅会打印一次回调，日志如下：

```
1. onChange: User property user.age change from 10 to 12
```

```
1. @ObservedV2
2. class User {
3. @Trace age: number = 10;
4. }

6. @Entry
7. @ComponentV2
8. struct Page {
9. @Local user: User = new User();

11. // @Monitor仅支持异步监听
12. @Monitor('user.age')
13. onChange(mon: IMonitor) {
14. mon.dirty.forEach((path: string) => {
15. console.info(`onChange: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
16. });
17. }

19. build() {
20. Column() {
21. Text(`User age ${this.user.age}`).fontSize(20).onClick(() => {
22. this.user.age++;
23. this.user.age++;
24. })
25. }
26. }
27. }
```

### 监听构造函数中同步修改的状态变量的变化

和[@Monitor异步构造](arkts-new-monitor.md#类中monitor对变量监听的生效及失效时间)不同，addMonitor是同步构造的，所以在开发者调用完UIUtils.addMonitor(this, 'message', this.onMessageChange);后就完成了对message添加监听函数this.onMessageChange。在下面的例子中：

* 拉起页面，构造Info的实例，回调onMessageChange监听函数。
* 点击Button('change message')，回调onMessageChange监听函数。

日志输出如下：

```
1. message change from not initialized to initialized
2. message change from initialized to Index aboutToAppear
3. message change from Index aboutToAppear to Index click to change message
```

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class Info {
5. @Trace message: string = 'not initialized';

7. constructor() {
8. // addMonitor可以监听构造函数中message的变化
9. UIUtils.addMonitor(this, 'message', this.onMessageChange);
10. this.message = 'initialized';
11. }
12. onMessageChange(monitor: IMonitor) {
13. console.info(`message change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct Page {
20. info: Info = new Info();

22. aboutToAppear(): void {
23. this.info.message = 'Index aboutToAppear';
24. }

26. build() {
27. Column() {
28. Button('change message')
29. .onClick(() => {
30. this.info.message = 'Index click to change message';
31. })
32. }
33. }
34. }
```

### 动态取消@ObservedV2/@ComponentV2实例的监听

和@Monitor不同，addMonitor/clearMonitor可以对不同的@ObservedV2/@ComponentV2实例动态添加监听函数。例子如下。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class User {
5. @Trace age: number = 10;

7. onChange(mon: IMonitor) {
8. mon.dirty.forEach((path: string) => {
9. console.info(`onChange: User property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
10. });
11. }

13. constructor(needMonitor: boolean) {
14. if (needMonitor) {
15. UIUtils.addMonitor(this, 'age', this.onChange);
16. }
17. }
18. }

20. @Entry
21. @ComponentV2
22. struct Page {
23. @Local user1: User = new User(true);
24. @Local user2: User = new User(false);
25. @Local count: number = 10;

27. build() {
28. Column() {
29. Text(`user1 age ${this.user1.age}`).fontSize(20).onClick(() => {
30. // 有Monitor回调
31. this.user1.age++;
32. })
33. Text(`user2 age ${this.user2.age}`).fontSize(20).onClick(() => {
34. // 无Monitor回调
35. this.user2.age++;
36. })
37. Button(`remove user1 monitor`).onClick(() => {
38. UIUtils.clearMonitor(this.user1, 'age', this.user1.onChange);
39. })

41. Button(`change count`).onClick(() => {
42. this.count++;
43. })

45. Child({ needMonitor: true, count: this.count })
46. Child({ needMonitor: false, count: this.count })
47. }
48. }
49. }

51. @ComponentV2
52. struct Child {
53. @Param needMonitor: boolean = false;
54. @Param count: number = 0;

56. onChange(mon: IMonitor) {
57. mon.dirty.forEach((path: string) => {
58. console.info(`Child needMonitor ${this.needMonitor} onChange: property ${path} change from ${mon.value(path)?.before} to ${mon.value(path)?.now}`);
59. });
60. }

62. aboutToAppear(): void {
63. if (this.needMonitor) {
64. UIUtils.addMonitor(this, 'count', this.onChange);
65. }
66. }

68. build() {
69. Column() {
70. Text(`${this.count}`).fontSize(20)
71. }
72. }
73. }
```
