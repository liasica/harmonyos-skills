---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines
title: 单元测试框架使用指导
breadcrumb: 指南 > 应用测试 > 单元测试和UI测试 > 自动化测试框架使用指导 > 单元测试框架使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:52+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:14d93e2889519c81b3b887e0c89e8ff2b175250e6e4845e3661cffe0583afaa1
---

## 概述

单元测试框架（JsUnit），是自动化测试框架基础底座，提供测试脚本识别、调度、执行和结果汇总的能力。开发者可在测试脚本中调用UI测试框架和白盒性能测试框架接口编写测试用例。

本指南介绍单元测试框架的主要功能、实现原理和开发步骤。

## 框架能力全景

单元测试框架支持的功能特性如下。

| 特性 | 功能说明 |
| --- | --- |
| [基础流程能力](unittest-guidelines.md#基础流程能力) | 支持测试用例识别调度及异步执行测试用例。 |
| [断言能力](unittest-guidelines.md#断言能力) | 判断用例实际结果值与预期值是否相符。 |
| [Mock能力](unittest-guidelines.md#mock能力) | 支持函数级Mock能力，对定义的函数进行Mock并修改函数的行为，使其返回指定的值或者执行指定操作。 |
| [数据驱动能力](unittest-guidelines.md#数据驱动) | 提供数据驱动能力，支持复用同一个测试脚本，使用不同输入数据驱动测试脚本执行。 |
| [专项能力](unittest-guidelines.md#命令行执行测试脚本) | 支持测试套与用例筛选、随机执行、压力测试、超时设置、遇错即停模式和跳过执行模式。 |

**图1.单元测试框架主要功能**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/6kBtbrVlQx6EE9Tn80YCqQ/zh-cn_image_0000002581217681.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=8CF8CDD9D61FF7B80B45B57ACA072CFC4365EE68643C9F9EC6AE886BC276B52E)

## 单元测试框架发布方式

单元测试框架以ohpm包独立发布，版本信息详见[服务组件官网](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fhypium)。开发者下载DevEco Studio后，在应用工程中的[oh-package.json5](ide-oh-package-json5.md)文件中devDependencies节点中配置版本号即可使用对应版本框架功能。

**配置示例**

```
1. "devDependencies": {
2. "@ohos/hypium": "1.0.25"
3. }
```

## 基于ArkTS编写和执行测试脚本

### 搭建环境

测试脚本基于DevEco Studio编写，请下载[DevEco Studio](https://developer.huawei.com/consumer/cn/download/)并完成[hdc配置](hdc.md#环境准备)。

### 新建测试脚本

参考[DevEco Studio指导](ide-instrument-test.md#section36049271219)创建ArkTS测试用例。

### 编写单元测试脚本

一个完整的测试脚本需要包含以下基本元素：

1. 依赖导包，以便使用单元测试框架提供的接口，以及其他测试脚本中需要依赖使用的接口。
2. 测试代码编写，编写测试用例的相关测试逻辑。
3. 断言接口调用，设置测试代码中的检查点，用于检查用例是否符合预期。

下面提供一个简单示例，测试场景：启动被测试页面，检查设备当前显示的页面是否为预期启动的页面。

```
1. import { describe, expect, it, Level, Size, TestType } from '@ohos/hypium';
2. import { abilityDelegatorRegistry } from '@kit.TestKit';
3. import { UIAbility, Want } from '@kit.AbilityKit';

5. const delegator = abilityDelegatorRegistry.getAbilityDelegator();

7. function sleep(time: number) {
8. return new Promise<void>((resolve: Function) => setTimeout(resolve, time));
9. }

11. export default function abilityTest() {
12. describe('ActsAbilityTest', () => {
13. // 测试套名称为ActsAbilityTest
14. // 可根据此处设置的用例类型、用例规模、用例级别进行用例筛选
15. it('testExample', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL1, async (done: Function) => {
16. // 测试用例名称为testExample
17. await sleep(500);
18. const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
19. // 启动被测试Ability
20. const want: Want = {
21. bundleName: bundleName,
22. abilityName: 'EntryAbility'
23. }
24. await delegator.startAbility(want);
25. await sleep(500);
26. // 获取设备上前台显示的页面并断言检查
27. const ability: UIAbility = await delegator.getCurrentTopAbility();
28. expect(ability.context.abilityInfo.name).assertEqual('EntryAbility');
29. done();
30. })
31. })
32. }
```

### DevEco Studio执行测试脚本

连接目标测试设备（如手机），在DevEco Studio页面点击对应按钮执行测试脚本，当前支持以下四种方式：

1. 测试包级别执行，即执行测试包内的全部用例。
2. 测试类级别执行，即执行\*.ets文件里的所有测试用例。
3. 测试套级别执行，即执行describe接口中定义的全部测试用例。
4. 测试用例级别执行，即执行指定it接口也就是单条测试用例。

下面给出测试类级别即测试文件执行示例，其他请参考[运行模式](ide-instrument-test.md#section1574003717165)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/dbxiE2wrSymGulvpkNDlMA/zh-cn_image_0000002550777586.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=374C31D8CE4F2C9261F1CAEA6A403AD1ABEDBBB8E2E0717AC4F10CEF16F3E4CE)

* 查看测试结果

测试执行后可直接在DevEco Studio中查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/S2Rhpp8lTE2tTr4uCHnPxQ/zh-cn_image_0000002581377645.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=66AF126AF449B55CDD90F81A844F6D1CAA05AAEB4F8D57FF57FB4C13D0633A50)

* 查看测试用例覆盖率

执行测试用例后可以查看测试用例覆盖率，具体操作请参考[覆盖率统计模式](ide-instrument-test.md#section1989615417457)章节内的内容。

### 命令行执行测试脚本

脚本执行需连接硬件设备，开发者安装测试包到连接设备上，在命令行窗口中通过执行aa test命令并设置执行参数，触发执行测试用例。

* aa test工具命令列表

以下是单元测试过程中的常用命令，其他aa test命令及含义说明参考[命令指南说明](aa-tool.md)。

| 参数 | 参数说明 | 示例 |
| --- | --- | --- |
| --bundleName/-b | 指定应用Bundle名称。 | - b com.test.example |
| --packageName/-p | 指定应用模块名，适用于FA模型应用。 | - p com.test.example.entry |
| --moduleName/-m | 指定应用模块名，适用于Stage模型应用。 | -m entry |
| -s | 特定参数，以<key, value>键值对方式传入。框架支持通过-s参数键值配置多种用例执行方式，-s的参数及对应含义参见下表。 | - s unittest /ets/testrunner/OpenHarmonyTestRunner |

| 参数 | 参数含义及取值 | 示例 |
| --- | --- | --- |
| unittest | 用例执行所使用OpenHarmonyTestRunner对象，取值可为OpenHarmonyTestRunner或用户自定义runner名称。 | -s unittest OpenHarmonyTestRunner |
| class | 筛选执行方式，即指定要执行的测试套或测试用例。取值为describeName，describeName#itName，其中describeName为测试套名称、itName为测试用例名称。 | -s class attributeTest#testAttributeIt |
| notClass | 排除执行方式，即指定不需要执行的测试套或测试用例。取值为describeName，describeName#itName，其中describeName为测试套名称、itName为测试用例名称。 | -s notClass attributeTest#testAttributeIt |
| itName | 筛选执行方式， 指定要执行的测试用例。取值为itName。 | -s itName testAttributeIt |
| timeout | 设置测试用例执行的超时时间。取值为正整数（单位ms），默认值：5000。 | -s timeout 15000 |
| breakOnError | 遇错即停方式，设置是否在用例失败时立即停止测试。取值为true（停止）/false（继续），默认为false。  **说明**：从@ohos/hypium 1.0.6版本开始支持。 | -s breakOnError true |
| random | 随机执行方式，设置为true时随机顺序执行测试用例。取值为true（设置）/false（不设置），默认为false。  **说明**：从@ohos/hypium 1.0.3版本开始支持。 | -s random true |
| testType | 筛选执行方式，指定筛选执行的用例类型。取值为function，performance，power，reliability，security，global，compatibility，user，standard，safety，resilience。 | -s testType function |
| level | 筛选执行方式，指定筛选执行的用例级别。取值为0，1，2，3，4。 | -s level 0 |
| size | 筛选执行方式，指定筛选执行的用例规模。取值为small，medium，large。 | -s size small |
| stress | 压力执行方式，指定执行用例的执行次数，设置后框架按照设置次数重复执行。取值为正整数。  **说明**：从@ohos/hypium 1.0.5版本开始支持。 | -s stress 1000 |
| skipMessage | 控制显示待执行的测试用例信息全集中，是否包含被设置跳过执行的测试套和用例的信息。取值为true（不显示相关信息）/false（显示相关信息），默认为false。  **说明**：从@ohos/hypium 1.0.17版本开始支持。 | -s skipMessage true |
| runSkipped | 跳过执行方式，指定要执行的跳过测试套&跳过用例。取值为all，skipped，describeName#itName。  **说明**：从@ohos/hypium 1.0.17版本开始支持。 | -s runSkipped all |

* 执行测试脚本

说明

下文参数配置和命令示例均基于Stage模型。

执行命令参数需基于@ohos/hypium框架发布版本，且测试应用包需集成该版本，否则命令参数无法响应，具体配置方式参考[发布方式](unittest-guidelines.md#单元测试框架发布方式)。

**示例代码1**：执行所有测试用例

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner
```

**示例代码2**：执行指定的describe测试套用例，指定多个需用逗号隔开

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s class s1,s2
```

**示例代码3**：执行指定测试套中指定的用例，指定多个需用逗号隔开

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s class testStop#stop_1,testStop1#stop_0
```

**示例代码4**：执行除指定配置外的所有用例，设置不执行多个测试套需用逗号隔开

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s notClass testStop
```

**示例代码5**：执行指定it名称的所有用例，指定多个需用逗号隔开

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s itName stop_0
```

**示例代码6**：用例执行超时时长配置

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s timeout 15000
```

**示例代码7**：用例以遇错即停模式执行用例

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s breakOnError true
```

**示例代码8**：执行测试类型匹配的测试用例

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s testType function
```

**示例代码9**：执行测试级别匹配的测试用例

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s level 0
```

**示例代码10**：执行测试规模匹配的测试用例

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s size small
```

**示例代码11**：执行测试用例指定次数

```
1. hdc shell aa test -b xxx -m xxx -s unittest OpenHarmonyTestRunner -s stress 1000
```

* 查看测试结果

1. 在命令行模式执行过程中，框架会打印如下日志信息。

   ```
   1. OHOS_REPORT_STATUS: class=ActsAbilityTest
   2. OHOS_REPORT_STATUS: current=1
   3. OHOS_REPORT_STATUS: id=JS
   4. OHOS_REPORT_STATUS: numtests=447
   5. OHOS_REPORT_STATUS: stream=
   6. OHOS_REPORT_STATUS: test=testExample
   7. OHOS_REPORT_STATUS_CODE: 1

   9. OHOS_REPORT_STATUS: class=ActsAbilityTest
   10. OHOS_REPORT_STATUS: current=1
   11. OHOS_REPORT_STATUS: id=JS
   12. OHOS_REPORT_STATUS: numtests=447
   13. OHOS_REPORT_STATUS: stream=
   14. OHOS_REPORT_STATUS: test=testExample
   15. OHOS_REPORT_STATUS_CODE: 0
   16. OHOS_REPORT_STATUS: consuming=4
   ```

   | 日志输出字段 | 日志输出字段含义 |
   | --- | --- |
   | OHOS\_REPORT\_SUM | 当前执行的测试套中用例总数。 |
   | OHOS\_REPORT\_STATUS: class | 当前执行用例所属测试套名称。 |
   | OHOS\_REPORT\_STATUS: id | 当前用例执行语言，默认JS。 |
   | OHOS\_REPORT\_STATUS: numtests | 当前测试包中测试用例总数。 |
   | OHOS\_REPORT\_STATUS: stream | 当前用例发生错误时，记录错误信息。 |
   | OHOS\_REPORT\_STATUS: test | 当前用例执行的it name。 |
   | OHOS\_REPORT\_STATUS\_CODE | 当前用例执行状态。1表示用例开始执行，0表示用例执行通过，-1表示用例执行报错，-2表示用例执行失败。 |
   | OHOS\_REPORT\_STATUS: consuming | 当前用例执行消耗的时长（ms）。 |
2. 命令行执行完成后，框架会打印如下相关日志信息。

   ```
   1. OHOS_REPORT_RESULT: stream=Tests run: 447, Failure: 0, Error: 1, Pass: 201, Ignore: 245
   2. OHOS_REPORT_CODE: 0

   4. OHOS_REPORT_RESULT: breakOnError model, Stopping whole test suite if one specific test case failed or error
   5. OHOS_REPORT_STATUS: taskconsuming=16029
   ```

   | 日志输出字段 | 日志输出字段含义 |
   | --- | --- |
   | run | 当前测试包用例总数。 |
   | Failure | 当前测试失败用例数量。 |
   | Error | 当前执行用例发生错误用例数量。 |
   | Pass | 当前执行用例通过用例数量。 |
   | Ignore | 当前未执行用例数量。 |
   | taskconsuming | 执行当前测试用例总耗时（ms）。 |

   说明

   当按照遇错即停方式执行时，用例发生错误时，注意查看Ignore字段以及错误中断时的提示信息。

## 单元测试框架能力使用说明

### 基础流程能力

单元测试框架提供执行测试脚本所需的基础流程接口，开发者需要实现相关接口，框架侧在运行时通过基础流程接口识别测试用例，调度执行并汇总测试结果。当前支持的基础流程接口如下表所示：

| 接口名 | 功能说明 |
| --- | --- |
| describe | 定义一个测试套，测试套中可以定义多个测试用例函数，但不支持异步函数。 |
| it | 定义一条测试用例。 |
| beforeAll | 在测试套内定义一个预置条件，在所有测试用例开始前执行且仅执行一次。 |
| beforeEach | 在测试套内定义一个预置条件，在每条测试用例开始前执行，执行次数与it定义的测试用例数一致。 |
| beforeEachIt | 在测试套内定义一个单元预置条件，在每条测试用例开始前执行。  外层测试套定义的beforeEachIt会在内部测试套中的测试用例执行前执行。  **说明**：从@ohos/hypium 1.0.25版本开始支持。 |
| afterEach | 在测试套内定义一个单元清理条件，在每条测试用例结束后执行，执行次数与it定义的测试用例数一致。 |
| afterEachIt | 在测试套内定义一个单元预置条件，在每条测试用例结束后执行。  外层测试套定义的afterEachIt会在内部测试套中的测试用例执行结束后执行。  **说明**：从@ohos/hypium 1.0.25版本开始支持。 |
| afterAll | 在测试套内定义一个清理条件，在所有测试用例结束后执行且仅执行一次。 |
| beforeItSpecified | 在测试套内定义一个单元预置条件，仅在指定测试用例开始前执行。  **说明**：从@ohos/hypium 1.0.15版本开始支持。 |
| afterItSpecified | 在测试套内定义一个单元清理条件，仅在指定测试用例结束后执行。  **说明**：从@ohos/hypium 1.0.15版本开始支持。 |
| expect | 支持bool类型判断等多种断言能力。 |
| xdescribe | 定义一个跳过的测试套，测试套中可以定义多个测试用例函数，但不支持异步函数。  **说明**：从@ohos/hypium 1.0.17版本开始支持。 |
| xit | 定义一条跳过的测试用例。  **说明**：从@ohos/hypium 1.0.17版本开始支持。 |

**示例代码1**：beforeAll/beforeEach/afterEach/afterAll使用示例

```
1. import { afterAll, afterEach, beforeAll, beforeEach, describe, expect, it, Level } from '@ohos/hypium';

3. export default function exampleTest() {

5. describe('order1_sample', () => {
6. let testNumA: number = 1;
7. let testNumB: number = 1;

9. beforeAll(() => {
10. testNumA++;
11. })

13. beforeEach(() => {
14. testNumA++;
15. testNumB++;
16. })

18. afterEach(() => {
19. testNumA++;
20. })

22. afterAll(() => {
23. let expectValue: number = 5;
24. expect(testNumA).assertEqual(expectValue);
25. })

27. it('testExampleA', Level.LEVEL1, async (done: Function) => {
28. let expectA: number = 3;
29. let expectB: number = 2;
30. expect(testNumA).assertEqual(expectA);
31. expect(testNumB).assertEqual(expectB);
32. done();
33. })

35. it('testExampleB', Level.LEVEL1, async (done: Function) => {
36. let expectA: number = 5;
37. let expectB: number = 3;
38. expect(testNumA).assertEqual(expectA);
39. expect(testNumB).assertEqual(expectB);
40. done();
41. })
42. })
43. }
```

**示例代码2**：beforeItSpecified/afterItSpecified使用示例，从1.0.15版本开始支持

```
1. import { afterItSpecified, beforeItSpecified, describe, expect, it, Level } from '@ohos/hypium';

3. export default function exampleTest() {

5. describe('order2_sample', () => {
6. let testNumA: number = 1;
7. let testNumB: number = 1;

9. beforeItSpecified(['testExampleB'], () => {
10. testNumB++;
11. })
12. afterItSpecified(['testExampleA'], () => {
13. testNumA++;
14. })

16. it('testExampleA', Level.LEVEL1, async (done: Function) => {
17. expect(testNumA).assertEqual(1);
18. expect(testNumB).assertEqual(1);
19. done();
20. })

22. it('testExampleB', Level.LEVEL1, async (done: Function) => {
23. expect(testNumA).assertEqual(2);
24. expect(testNumB).assertEqual(2);
25. done();
26. })
27. })
28. }
```

**示例代码3**：xit使用示例，从1.0.17版本开始支持

```
1. import { describe, it, Level, xit } from '@ohos/hypium';

3. export default function describeExampleTest() {

5. describe('order3_sample', () => {
6. xit('testExampleA', Level.LEVEL1, async (done: Function) => {
7. done();
8. })

10. it('testExampleB', Level.LEVEL1, async (done: Function) => {
11. done();
12. })
13. })
14. }
```

**示例代码4**：beforeEachIt/afterEachIt使用示例，从1.0.25版本开始支持

```
1. import { describe, beforeEach, afterEach, beforeEachIt, afterEachIt, it, expect } from '@ohos/hypium';
2. let str = "";
3. export default function test() {
4. describe('test0', () => {
5. beforeEach(async () => {
6. str += "A"
7. })
8. beforeEachIt(async () => {
9. str += "B"
10. })
11. afterEach(async () => {
12. str += "C"
13. })
14. afterEachIt(async () => {
15. str += "D"
16. })
17. it('test0000', 0, () => {
18. expect(str).assertEqual("BA");
19. })
20. describe('test1', () => {
21. beforeEach(async () => {
22. str += "E"
23. })
24. beforeEachIt(async () => {
25. str += "F"
26. })
27. it('test1111', 0, async () => {
28. expect(str).assertEqual("BACDBFE");
29. })
30. })
31. })
32. }
```

### 断言能力

单元测试框架提供了丰富的断言接口，供开发者在不同测试场景下使用，详细接口可查看下表。

| 接口名 | 功能说明 |
| --- | --- |
| assertClose | 检验实际值和预期值之间的数值差异是否在指定的允许误差范围内。 |
| assertContain | 检验实际值中是否包含预期值。 |
| assertEqual | 检验实际值是否等于预期值。 |
| assertFail | 抛出一个错误。 |
| assertFalse | 检验实际值是否是false。 |
| assertTrue | 检验实际值是否是true。 |
| assertInstanceOf | 检验实际值是否是预期类型，支持基础类型。 |
| assertLarger | 检验实际值是否大于预期值。 |
| assertLargerOrEqual | 检验实际值是否大于或等于预期值。 |
| assertLess | 检验实际值是否小于预期值。 |
| assertLessOrEqual | 检验实际值是否小于或等于预期值。 |
| assertNull | 检验实际值是否是null。 |
| assertThrowError | 检验实际值抛出Error内容是否为预期的异常类型。 |
| assertUndefined | 检验实际值是否是undefined。 |
| assertNaN | 检验实际值是否是NaN。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertNegUnlimited | 检验实际值是否等于Number.NEGATIVE\_INFINITY。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPosUnlimited | 检验实际值是否等于Number.POSITIVE\_INFINITY。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertDeepEquals | 检验实际值和预期值是否完全相等。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPromiseIsPending | 检验Promise是否处于Pending状态。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPromiseIsRejected | 检验Promise是否处于Rejected状态。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPromiseIsRejectedWith | 检验Promise是否处于Rejected状态，并且比较执行的结果值。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPromiseIsRejectedWithError | 检验Promise是否处于Rejected状态并包含异常，比较异常类型和异常信息。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPromiseIsResolved | 检验Promise是否处于Resolved状态。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| assertPromiseIsResolvedWith | 检验Promise是否处于Resolved状态并比较结果值。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |
| not | 断言取反，支持上述所有断言功能。  **说明**：从@ohos/hypium 1.0.4版本开始支持。 |

**示例代码**：

```
1. import { describe, expect, it, Level } from '@ohos/hypium';

3. export default function exampleTest() {
4. describe('ExampleTest', () => {
5. it('assertCloseTest', Level.LEVEL1, () => {
6. let a: number = 100;
7. let b: number = 0.1;
8. let c: number = 99;
9. expect(a).assertClose(c, b);
10. })

12. it('assertContain_1', Level.LEVEL1, () => {
13. let a = 'abc';
14. expect(a).assertContain('b');
15. })

17. it('assertContain_2', Level.LEVEL1, () => {
18. let a = [1, 2, 3];
19. expect(a).assertContain(1);
20. })

22. it('assertEqualTest', Level.LEVEL1, () => {
23. expect(3).assertEqual(3);
24. })

26. it('assertFailTest', Level.LEVEL1, () => {
27. expect().assertFail(); // 用例失败
28. })

30. it('assertFalseTest', Level.LEVEL1, () => {
31. expect(false).assertFalse();
32. })

34. it('assertTrueTest', Level.LEVEL1, () => {
35. expect(true).assertTrue();
36. })

38. it('assertInstanceOfTest', Level.LEVEL1, () => {
39. let a: string = 'strTest';
40. expect(a).assertInstanceOf('String');
41. })

43. it('assertLargerTest', Level.LEVEL1, () => {
44. expect(3).assertLarger(2);
45. })

47. it('assertLessTest', Level.LEVEL1, () => {
48. expect(2).assertLess(3);
49. })

51. it('assertNullTest', Level.LEVEL1, () => {
52. expect(null).assertNull();
53. })

55. it('assertThrowErrorTest', Level.LEVEL1, () => {
56. expect(() => {
57. throw new Error('test');
58. }).assertThrowError('test');
59. })

61. it('assertUndefinedTest', Level.LEVEL1, () => {
62. expect(undefined).assertUndefined();
63. })

65. it('assertLargerOrEqualTest', Level.LEVEL1, () => {
66. expect(3).assertLargerOrEqual(3);
67. })

69. it('assertLessOrEqualTest', Level.LEVEL1, () => {
70. expect(3).assertLessOrEqual(3);
71. })

73. it('assertNaNTest', Level.LEVEL1, () => {
74. expect(Number.NaN).assertNaN(); // true
75. })

77. it('assertNegUnlimitedTest', Level.LEVEL1, () => {
78. expect(Number.NEGATIVE_INFINITY).assertNegUnlimited(); // true
79. })

81. it('assertPosUnlimitedTest', Level.LEVEL1, () => {
82. expect(Number.POSITIVE_INFINITY).assertPosUnlimited(); // true
83. })

85. it('deepEquals_null_true', Level.LEVEL1, () => {
86. expect(null).assertDeepEquals(null);
87. })

89. it('deepEquals_array_not_have_true', Level.LEVEL1, () => {
90. const a: Array<number> = [];
91. const b: Array<number> = [];
92. expect(a).assertDeepEquals(b);
93. })

95. it('deepEquals_map_equal_length_success', Level.LEVEL1, () => {
96. const a: Map<number, number> = new Map();
97. const b: Map<number, number> = new Map();
98. a.set(1, 100);
99. a.set(2, 200);
100. b.set(1, 100);
101. b.set(2, 200);
102. expect(a).assertDeepEquals(b);
103. })

105. it('deepEquals_obj_success_1', Level.LEVEL1, () => {
106. const a: SampleTest = { x: 1 };
107. const b: SampleTest = { x: 1 };
108. expect(a).assertDeepEquals(b);
109. })

111. it('deepEquals_regExp_success_0', Level.LEVEL1, () => {
112. const a: RegExp = new RegExp('/test/');
113. const b: RegExp = new RegExp('/test/');
114. expect(a).assertDeepEquals(b);
115. })

117. it('assertPromiseIsPendingTest', Level.LEVEL1, async () => {
118. let p: Promise<void> = new Promise<void>(() => {
119. });
120. await expect(p).assertPromiseIsPending();
121. })

123. it('assertPromiseIsRejectedTest', Level.LEVEL1, async () => {
124. let info: PromiseInfo = { res: 'no' };
125. let p: Promise<PromiseInfo> = Promise.reject(info);
126. await expect(p).assertPromiseIsRejected();
127. })

129. it('assertPromiseIsRejectedWithTest', Level.LEVEL1, async () => {
130. let info: PromiseInfo = { res: 'reject value' };
131. let p: Promise<PromiseInfo> = Promise.reject(info);
132. await expect(p).assertPromiseIsRejectedWith(info);
133. })

135. it('assertPromiseIsRejectedWithErrorTest', Level.LEVEL1, async () => {
136. let p1: Promise<TypeError> = Promise.reject(new TypeError('number'));
137. await expect(p1).assertPromiseIsRejectedWithError(TypeError);
138. })

140. it('assertPromiseIsResolvedTest', Level.LEVEL1, async () => {
141. let info: PromiseInfo = { res: 'result value' };
142. let p: Promise<PromiseInfo> = Promise.resolve(info);
143. await expect(p).assertPromiseIsResolved();
144. })

146. it('assertPromiseIsResolvedWithTest', Level.LEVEL1, async () => {
147. let info: PromiseInfo = { res: 'result value' };
148. let p: Promise<PromiseInfo> = Promise.resolve(info);
149. await expect(p).assertPromiseIsResolvedWith(info);
150. })

152. it('test_message', Level.LEVEL1, () => {
153. expect(1).message('1 is not equal 2!').assertEqual(2); // fail
154. })
155. })
156. }

158. interface SampleTest {
159. x: number;
160. }

162. interface PromiseInfo {
163. res: string;
164. }
```

### Mock能力

从@ohos/hypium 1.0.1版本开始，单元测试框架支持Mock能力。配置方式参考上文[发布方式](unittest-guidelines.md#单元测试框架发布方式)。

说明

仅支持Mock应用工程中自定义对象，不支持Mock系统API对象。如需Mock系统API，请参考[系统模块Mock指南](ide-test-mock.md#section8353132513310)。

**基础类**

MockKit是Mock的基础类，用于指定需要Mock的实例和函数。

| 接口名 | 功能说明 |
| --- | --- |
| mockFunc | Mock某个类实例中的函数，支持使用异步函数。 |
| mockPrivateFunc | Mock某个类的实例上的私有方法。  **说明**：从@ohos/hypium 1.0.25版本开始支持。 |
| mockProperty | Mock某个类的实例上的属性。  **说明**：从@ohos/hypium 1.0.25版本开始支持。 |
| verify | 验证函数在对应参数下的执行行为是否符合预期，返回一个VerificationMode类。 |
| ignoreMock | 使用ignoreMock可以还原实例中被Mock后的函数，对被Mock后的函数有效。 |
| clear | 用例执行完毕后，对被Mock对象实例进行还原处理（还原之后对象恢复被Mock之前的功能）。 |
| clearAll | 用例执行完毕后，进行数据和内存清理，不会还原实例中被Mock后的函数。 |

**VerificationMode**

VerificationMode用于验证被Mock函数的被调用次数，需同verify函数结合使用。

| 接口名 | 功能说明 |
| --- | --- |
| times | 验证函数被调用过的次数符合预期。 |
| once | 验证函数被调用过一次。 |
| atLeast | 验证函数最少被调用的次数符合预期。 |
| atMost | 验证函数最多被调用的次数符合预期。 |
| never | 验证函数从未被调用过。 |

**when**

when是一个函数，用于设置函数期望被Mock的值。

| 接口名 | 功能说明 |
| --- | --- |
| when | 对传入后函数做检查，检查是否被Mock并标记过，返回一个内置函数，函数执行后返回一个类用于设置Mock值。 |

使用when函数之后，需使用如下函数设置函数被Mock后的返回值。

| 接口名 | 功能说明 |
| --- | --- |
| afterReturn | 设定一个自定义的期望返回值，比如某个字符串或者一个Promise。 |
| afterReturnNothing | 设定预期没有返回值，即undefined。 |
| afterAction | 设定预期返回一个函数执行的操作。 |
| afterThrow | 设定预期抛出异常，并指定异常描述信息。 |

**ArgumentMatchers相关接口**

ArgumentMatchers用于用户自定义函数参数，当开发者想基于某类规则设定预期返回值时，可以使用。它以枚举值或函数的形式提供给开发者使用。

| 枚举名 | 功能说明 |
| --- | --- |
| any | 设定用户传任何类型参数（undefined和null除外），执行的结果返回所设置的预期值，使用ArgumentMatchers.any方式调用。 |
| anyString | 设定用户传任何字符串参数，执行的结果都是预期的值，使用ArgumentMatchers.anyString方式调用。 |
| anyBoolean | 设定用户传任何boolean类型参数，执行的结果都是预期的值，使用ArgumentMatchers.anyBoolean方式调用。 |
| anyFunction | 设定用户传任何function类型参数，执行的结果都是预期的值，使用ArgumentMatchers.anyFunction方式调用。 |
| anyNumber | 设定用户传任何数字类型参数，执行的结果都是预期的值，使用ArgumentMatchers.anyNumber方式调用。 |
| anyObj | 设定用户传任何对象类型参数，执行的结果都是预期的值，使用ArgumentMatchers.anyObj方式调用。 |

| 接口名 | 功能说明 |
| --- | --- |
| matchRegexs | 设定用户传任何符合正则表达式验证的参数，执行的结果都是预期的值，使用ArgumentMatchers.matchRegexs(Regex)方式调用。 |

说明

使用Mock能力时必须导入Mock能力模块： MockKit，when，开发者可根据实际需求导入对应模块。

例如：import { describe, expect, it, MockKit, when} from '@ohos/hypium'

**示例代码1**：使用afterReturn/afterReturnNothing设置预期返回值

```
1. import { describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(arg: string) {
8. return '888888';
9. }
10. }

12. export default function afterReturnTest() {
13. describe('afterReturn_sample', () => {
14. it('afterReturnTest', 0, () => {
15. // 创建一个Mock能力的对象MockKit
16. let mocker: MockKit = new MockKit();
17. // 初始化ClassName的对象claser，作为被Mock的对象实例
18. let claser: ClassName = new ClassName();
19. // 进行Mock操作，对ClassName类的method_1函数进行Mock
20. let mockfunc: Function = mocker.mockFunc(claser, claser.method_1);
21. // 期望claser.method_1函数被Mock后, 以'testA'为入参时调用函数返回结果'1',以'testB''为入参时调用函数返回结果undefined
22. when(mockfunc)('testA').afterReturn('1');
23. when(mockfunc)('testB').afterReturnNothing();
24. // 对Mock后的函数进行断言，看是否符合预期。分别传入参数'testA'和'testB'时，应该返回自定义的预期结果1和undefined
25. expect(claser.method_1('testA')).assertEqual('1'); // 断言执行通过
26. expect(claser.method_1('testB')).assertUndefined(); // 断言执行通过
27. })
28. })
29. }
```

**示例代码2**：使用ArgumentMatchers设定参数类型为any即接受任何参数（undefined和null除外）

```
1. import { ArgumentMatchers, describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(arg: string) {
8. return '888888';
9. }
10. }

12. export default function argumentMatchersAnyTest() {
13. describe('argumentMatchersForAny_sample', () => {
14. it('testMockfunc', 0, () => {
15. // 创建一个Mock能力的对象MockKit
16. let mocker: MockKit = new MockKit();
17. // 初始化ClassName的对象claser
18. let claser: ClassName = new ClassName();
19. // 进行Mock操作，对ClassName类的method_1函数进行Mock
20. let mockfunc: Function = mocker.mockFunc(claser, claser.method_1);
21. // 期望claser.method_1函数被Mock后, 参数为任一类型在被调用时均返回结果'1'
22. when(mockfunc)(ArgumentMatchers.any).afterReturn('1');
23. // 传入不同参数验证是否符合预期
24. expect(claser.method_1('test')).assertEqual('1'); // 断言执行通过
25. expect(claser.method_1('123')).assertEqual('1'); // 断言执行通过
26. expect(claser.method_1('true')).assertEqual('1'); // 断言执行通过
27. })
28. })
29. }
```

**示例代码3**：使用ArgumentMatchers设定参数类型为String

```
1. import { ArgumentMatchers, describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(arg: string) {
8. return '888888';
9. }
10. }

12. export default function argumentMatchersTest() {
13. describe('argumentMatchersForString_sample', () => {
14. it('testMockfunc', 0, () => {
15. // 创建一个Mock能力的对象MockKit
16. let mocker: MockKit = new MockKit();
17. // 初始化ClassName的对象claser
18. let claser: ClassName = new ClassName();
19. // 进行Mock操作,对ClassName类的method_1函数进行Mock
20. let mockfunc: Function = mocker.mockFunc(claser, claser.method_1);
21. // 期望claser.method_1函数被Mock后, 以任何string类型为参数调用函数时返回结果'1'
22. when(mockfunc)(ArgumentMatchers.anyString).afterReturn('1');
23. // 传入不同string类型参数，验证是否符合预期
24. expect(claser.method_1('test')).assertEqual('1'); // 断言执行通过
25. expect(claser.method_1('abc')).assertEqual('1'); // 断言执行通过
26. })
27. })
28. }
```

**示例代码4**：使用ArgumentMatchers设定参数类型为matchRegexs（Regex）即正则表达式

```
1. import { ArgumentMatchers, describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(arg: string) {
8. return '888888';
9. }
10. }

12. export default function matchRegexsTest() {
13. describe('argumentMatchersForRegex_sample', () => {
14. it('testMockfunc', 0, () => {
15. // 创建一个Mock能力的对象MockKit
16. let mocker: MockKit = new MockKit();
17. // 初始化ClassName的对象claser
18. let claser: ClassName = new ClassName();
19. // 进行Mock操作，对ClassName类的method_1函数进行Mock
20. let mockfunc: Function = mocker.mockFunc(claser, claser.method_1);
21. // 期望claser.method_1函数被Mock后, 以"test"为入参调用函数时返回结果'1'
22. when(mockfunc)(ArgumentMatchers.matchRegexs(new RegExp("test"))).afterReturn('1');
23. // 传入test参数后验证是否符合预期
24. expect(claser.method_1('test')).assertEqual('1'); // 断言执行通过
25. })
26. })
27. }
```

**示例代码5**：使用verify函数验证被Mock函数在对应参数下的执行行为是否符合预期

```
1. import { describe, it, MockKit } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(...arg: string[]) {
8. return '888888';
9. }

11. method_2(...arg: string[]) {
12. return '999999';
13. }
14. }

16. export default function verifyTest() {
17. describe('verify_sample', () => {
18. it('testMockfunc', 0, () => {
19. // 创建一个Mock能力的对象MockKit
20. let mocker: MockKit = new MockKit();
21. // 初始化ClassName的对象claser
22. let claser: ClassName = new ClassName();
23. // 进行Mock操作，对ClassName类的method_1和method_2两个函数进行Mock
24. mocker.mockFunc(claser, claser.method_1);
25. mocker.mockFunc(claser, claser.method_2);
26. // 函数调用
27. claser.method_1('abc', 'ppp');
28. claser.method_1('abc');
29. claser.method_1('xyz');
30. claser.method_1();
31. claser.method_1('abc', 'xxx', 'yyy');
32. claser.method_1();
33. claser.method_2('111');
34. claser.method_2('111', '222');
35. // 对Mock后的两个函数进行验证，验证method_2,参数仅为'111'时执行过一次
36. mocker.verify('method_2', ['111']).once(); // 断言执行通过
37. })
38. })
39. }
```

**示例代码6**：使用ignoreMock函数还原指定被Mock函数实现

```
1. import { ArgumentMatchers, describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(...arg: number[]) {
8. return '888888';
9. }

11. method_2(...arg: number[]) {
12. return '999999';
13. }
14. }

16. export default function ignoreMockTest() {
17. describe('ignoreMock_sample', () => {
18. it('testMockfunc', 0, () => {
19. // 创建一个Mock能力的对象MockKit
20. let mocker: MockKit = new MockKit();
21. // 初始化ClassName的对象claser
22. let claser: ClassName = new ClassName();
23. // 进行Mock操作，对ClassName类的method_1和method_2两个函数进行Mock
24. let func_1: Function = mocker.mockFunc(claser, claser.method_1);
25. let func_2: Function = mocker.mockFunc(claser, claser.method_2);
26. // 期望claser.method_1函数被Mock后, 以number类型为入参时调用函数返回结果'4'
27. when(func_1)(ArgumentMatchers.anyNumber).afterReturn('4');
28. // 期望claser.method_2函数被Mock后, 以number类型为入参时调用函数返回结果'5'
29. when(func_2)(ArgumentMatchers.anyNumber).afterReturn('5');
30. // 函数调用
31. expect(claser.method_1(123)).assertEqual("4");
32. expect(claser.method_2(456)).assertEqual("5");
33. // 现在对Mock后的两个函数的其中一个函数method_1进行还原处理
34. mocker.ignoreMock(claser, claser.method_1);
35. // 调用claser.method_1函数
36. expect(claser.method_1(123)).assertEqual('888888'); // 断言执行通过
37. })
38. })
39. }
```

**示例代码7**：使用clear函数还原类中所有被Mock函数原有实现

```
1. import { ArgumentMatchers, describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(...arg: number[]) {
8. return '888888';
9. }

11. method_2(...arg: number[]) {
12. return '999999';
13. }
14. }

16. export default function clearTest() {
17. describe('clearMock_sample', () => {
18. it('testMockfunc', 0, () => {
19. // 创建一个Mock能力的对象MockKit
20. let mocker: MockKit = new MockKit();
21. // 初始化ClassName的对象claser
22. let claser: ClassName = new ClassName();
23. // 进行Mock操作，对ClassName类的method_1和method_2两个函数进行Mock
24. let func_1: Function = mocker.mockFunc(claser, claser.method_1);
25. let func_2: Function = mocker.mockFunc(claser, claser.method_2);
26. // 期望claser.method_1函数被Mock后, 以任何number类型为参数调用函数时返回结果'4'
27. when(func_1)(ArgumentMatchers.anyNumber).afterReturn('4');
28. // 期望claser.method_2函数被Mock后, 以任何number类型为参数调用函数时返回结果'5'
29. when(func_2)(ArgumentMatchers.anyNumber).afterReturn('5');
30. // 函数调用
31. expect(claser.method_1(123)).assertEqual('4');
32. expect(claser.method_2(123)).assertEqual('5');
33. // 还原obj上所有的Mock能力
34. mocker.clear(claser);
35. // 调用claser.method_1,claser.method_2函数，测试结果
36. expect(claser.method_1(123)).assertEqual('888888'); // 断言执行通过
37. expect(claser.method_2(123)).assertEqual('999999'); // 断言执行通过
38. })
39. })
40. }
```

**示例代码8**：使用afterThrow函数抛出指定异常信息

```
1. import { describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(arg: string) {
8. return '888888';
9. }
10. }

12. export default function afterThrowTest() {
13. describe('afterThrow_sample', () => {
14. it('testMockfunc', 0, () => {
15. // 创建一个Mock能力的对象MockKit
16. let mocker: MockKit = new MockKit();
17. // 初始化ClassName的对象claser
18. let claser: ClassName = new ClassName();
19. // 进行Mock操作,对ClassName类的method_1函数进行Mock
20. let mockfunc: Function = mocker.mockFunc(claser, claser.method_1);
21. // 期望claser.method_1函数被Mock后, 以'test'为参数调用函数时抛出error xxx异常
22. when(mockfunc)('test').afterThrow('error xxx');
23. // 执行Mock后的函数，捕捉异常并使用assertEqual对比msg否符合预期
24. try {
25. claser.method_1('test');
26. } catch (e) {
27. expect(e).assertEqual('error xxx'); // 断言执行通过
28. }
29. })
30. })
31. }
```

**示例代码9**：Mock异步返回Promise对象

```
1. import { describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. async method_1(arg: string) {
8. return new Promise<string>((resolve: Function, reject: Function) => {
9. setTimeout(() => {
10. resolve('Data conversion');
11. }, 2000);
12. });
13. }
14. }

16. export default function mockPromiseTest() {
17. describe('returnPromise_sample', () => {
18. it('testMockfunc', 0, async (done: Function) => {
19. // 创建一个Mock能力的对象MockKit
20. let mocker: MockKit = new MockKit();
21. // 初始化ClassName的对象claser
22. let claser: ClassName = new ClassName();
23. // 进行Mock操作对ClassName类的method_1函数进行Mock
24. let mockfunc: Function = mocker.mockFunc(claser, claser.method_1);
25. // 期望claser.method_1函数被Mock后, 以'test'为参数调用函数时返回一个Promise对象
26. when(mockfunc)('test').afterReturn(new Promise<string>((resolve: Function, reject: Function) => {
27. resolve('success something');
28. }));
29. // 执行Mock后的函数，即对定义的Promise进行后续执行
30. let result = await claser.method_1('test');
31. expect(result).assertEqual('success something'); // 断言执行通过
32. done();
33. })
34. })
35. }
```

**示例代码10**：使用times/atLeast函数验证被Mock函数调用次数

```
1. import { describe, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. method_1(...arg: string[]) {
8. return '888888';
9. }
10. }

12. export default function verifyTimesTest() {
13. describe('verifyTimes_sample', () => {
14. it('test_verify_times', 0, () => {
15. // 创建一个Mock能力的对象MockKit
16. let mocker: MockKit = new MockKit();
17. // 初始化ClassName的对象claser
18. let claser: ClassName = new ClassName();
19. // 进行Mock操作对ClassName类的method_1函数进行Mock
20. let func_1: Function = mocker.mockFunc(claser, claser.method_1);
21. // 期望被Mock后的函数返回结果'4'
22. when(func_1)('123').afterReturn('4');
23. // 函数调用
24. claser.method_1('123', 'ppp');
25. claser.method_1('abc');
26. claser.method_1('xyz');
27. claser.method_1();
28. claser.method_1('abc', 'xxx', 'yyy');
29. claser.method_1('abc');
30. claser.method_1();
31. // 验证函数method_1且参数为'abc'时，执行过的次数是否为2
32. mocker.verify('method_1', ['abc']).times(2); // 断言执行通过
33. // 验证函数method_1且参数为空时，是否至少执行过2次
34. mocker.verify('method_1', []).atLeast(2); // 断言执行通过
35. })
36. })
37. }
```

**示例代码11**：Mock静态函数（从@ohos/hypium 1.0.16版本开始支持）

```
1. import { ArgumentMatchers, describe, expect, it, MockKit, when } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }

7. static method_1() {
8. return 'ClassName_method_1_call';
9. }
10. }

12. export default function staticTest() {
13. describe('mockStatic_sample', () => {
14. it('staticTest_001', 0, () => {
15. let really_result = ClassName.method_1();
16. expect(really_result).assertEqual('ClassName_method_1_call');
17. // 创建MockKit对象
18. let mocker: MockKit = new MockKit();
19. // Mock类ClassName对象的某个函数method_1
20. let func_1: Function = mocker.mockFunc(ClassName, ClassName.method_1);
21. // 期望被mock后的函数返回结果'mock_data'
22. when(func_1)(ArgumentMatchers.any).afterReturn('mock_data');
23. let mock_result = ClassName.method_1();
24. expect(mock_result).assertEqual('mock_data'); // 断言执行通过
25. // 清除Mock能力
26. mocker.clear(ClassName);
27. let really_result1 = ClassName.method_1();
28. expect(really_result1).assertEqual('ClassName_method_1_call'); // 断言执行通过
29. })
30. })
31. }
```

**示例代码12**：Mock私有函数（从@ohos/hypium 1.0.25版本开始支持）

```
1. import { describe, it, expect, MockKit, when, ArgumentMatchers } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }
6. method(arg: number):number {
7. return this.method_1(arg);
8. }
9. private method_1(arg: number) {
10. return arg;
11. }
12. }

14. export default function staticTest() {
15. describe('privateTest', () => {
16. it('private_001', 0, () => {
17. let claser: ClassName = new ClassName();
18. let really_result = claser.method(123);
19. expect(really_result).assertEqual(123);
20. // 1.创建MockKit对象
21. let mocker: MockKit = new MockKit();
22. // 2.Mock类ClassName对象的私有方法，比如method_1
23. let func_1: Function = mocker.mockPrivateFunc(claser, "method_1");
24. // 3.期望被Mock后的函数返回结果为456
25. when(func_1)(ArgumentMatchers.any).afterReturn(456);
26. let mock_result = claser.method(123);
27. expect(mock_result).assertEqual(456);
28. // 清除Mock能力
29. mocker.clear(claser);
30. let really_result1 = claser.method(123);
31. expect(really_result1).assertEqual(123);
32. })
33. })
34. }
```

**示例代码13**：Mock成员变量（从@ohos/hypium 1.0.25版本开始支持）

```
1. import { describe, it, expect, MockKit, when, ArgumentMatchers } from '@ohos/hypium';

3. class ClassName {
4. constructor() {
5. }
6. data = 1;
7. private priData = 2;
8. method() {
9. return this.priData;
10. }
11. }

13. export default function staticTest() {
14. describe('propertyTest', () => {
15. it('property_001', 0, () => {
16. let claser: ClassName = new ClassName();
17. let data = claser.data;
18. expect(data).assertEqual(1);
19. let priData = claser.method();
20. expect(priData).assertEqual(2);
21. // 1.创建MockKit对象
22. let mocker: MockKit = new MockKit();
23. // 2.Mock类ClassName对象的成员变量data
24. mocker.mockProperty(claser, "data", 3);
25. mocker.mockProperty(claser, "priData", 4);
26. // 3.期望被Mock后的成员和私有成员的值分别为3，4
27. let mock_result = claser.data;
28. let mock_private_result = claser.method();
29. expect(mock_result).assertEqual(3);
30. expect(mock_private_result).assertEqual(4);
31. // 清除Mock能力
32. mocker.ignoreMock(claser, "data");
33. mocker.ignoreMock(claser, "priData");
34. let really_result = claser.data;
35. expect(really_result).assertEqual(1);
36. let really_private_result = claser.method();
37. expect(really_private_result).assertEqual(2);
38. })
39. })
40. }
```

### 数据驱动

单元测试框架的数据驱动能力从[@ohos/hypium 1.0.2版本](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fhypium)开始支持。开发者可以复用测试用例代码，通过数据配置文件配置输入数据和预期结果数据，在用例实现中获取数据进行相应实现和断言处理，减少冗余测试代码。

数据驱动能力可以根据测试数据配置来驱动测试用例的执行次数和每次执行时传入的参数，使用时依赖data.json配置文件，文件内容如下：

说明

data.json与测试用例\*.test.js或\*.test.ets文件同目录。

data.json文件中的参数配置名称需同测试用例中定义参数名称保持一致。

```
1. {
2. "suites": [{
3. "describe": ["paramExampleTest"],
4. "stress": 4,
5. "params": {
6. "suiteParams1": "suiteParams001",
7. "suiteParams2": "suiteParams002"
8. },
9. "items": [{
10. "it": "testDataDriverAsync"
11. },
12. {
13. "it": "testDataDriverParam",
14. "stress": 2,
15. "params":[
16. {
17. "ts1": "ts1",
18. "ts2": "ts2"
19. }
20. ]
21. }]
22. }]
23. }
```

配置参数说明：

| 配置项名称 | 功能 | 必填 |
| --- | --- | --- |
| "suite" | 测试套配置。 | 是 |
| "describe" | 测试套名称。 | 是 |
| "items" | 测试用例。 | 是 |
| "it" | 测试用例名称。 | 是 |
| "params" | 测试套/测试用例可传入使用的参数。 | 否 |
| "stress" | 测试套/测试用例指定执行次数。 | 否 |

**示例代码**

Stage模型在测试工程中的TestAbility目录下TestAbility.ets文件中导入data.json（FA模型在测试工程中的TestAbility目录下的app.js或app.ets文件中导入data.json），并在文件中的Hypium.hypiumTest()函数执行前设置参数数据，参考下面示例代码。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { abilityDelegatorRegistry } from '@kit.TestKit';
3. import { Hypium } from '@ohos/hypium';
4. import testsuite from '../test/List.test';
5. import data from '../test/data.json';
6. import Logger from '../util/Logger';
7. import { window } from '@kit.ArkUI';

9. const TAG = 'testTag';

11. export default class TestAbility extends UIAbility {
12. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
13. Logger.info(TAG, 'TestAbility onCreate');
14. Logger.info(TAG, 'want param:' + JSON.stringify(want));
15. Logger.info(TAG, 'launchParam:' + JSON.stringify(launchParam));
16. let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
17. let abilityDelegatorArguments = abilityDelegatorRegistry.getArguments();
18. Logger.info(TAG, 'start run testcase!!!');
19. // 设置数据
20. Hypium.setData(data);
21. Hypium.hypiumTest(abilityDelegator, abilityDelegatorArguments, testsuite);
22. }
```

```
1. import { describe, it } from '@ohos/hypium';

3. export default function abilityTest() {
4. describe('AbilityTest', () => {
5. it('testDataDriverAsync', 0, async (done: Function, data: ParamObj) => {
6. done();
7. });

9. it('testDataDriver', 0, () => {
10. });
11. })
12. }

14. interface ParamObj {
15. name: string,
16. value: string
17. }
```

说明

若要使用数据驱动传入参数功能，测试用例it的func必须传入两个参数：done和data，且入参顺序不可调整。若不使用数据驱动传入参数功能，func可以不传参或仅传入done。

### 专项能力

专项能力提供脚本执行配置能力，包括筛选执行、压力执行、随机执行等，通过命令行方式执行，具体用法请参考[命令行执行测试脚本](unittest-guidelines.md#命令行执行测试脚本)章节介绍。

## 单元测试框架常见问题

**用例中增加的打印日志在用例结果之后才打印**

**问题描述**

用例中新增的日志打印信息未在执行过程中出现，而是在执行结束之后才显示。

**可能原因**

此类情况仅在用例调用异步接口时出现。为确保日志正确捕获执行过程，用例中所有日志信息必须在用例执行结束前打印。

**解决方法**

当被调用的异步接口数量超过两个时，建议将接口调用封装成Promise方式调用。

**执行用例时报用例超时错误**

**问题描述**

用例执行结束，控制台提示execute time XXms错误，即用例执行超时。

**可能原因**

1. 用例执行异步接口时，如果未调用done函数，会导致用例无法正常结束，最终超时。
2. 用例调用函数耗时过长，超过用例执行设置的超时时间（默认5000ms）。
3. 用例调用函数时断言失败抛出异常，导致用例执行超时终止。

**解决方法**

1. 检查用例代码逻辑，确保断言失败时能走到done函数，完成用例执行。
2. 可在DevEco Studio的Run/Debug Configurations中修改用例执行超时参数，避免执行超时。
3. 检查用例代码逻辑，确保断言通过。

## 完整示例

[测试框架](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/Test/jsunit)
