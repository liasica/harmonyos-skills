---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-automated-testing-frameworks
title: 自动化测试框架开发实践
breadcrumb: 最佳实践 > 测试框架 > 自动化测试框架开发实践
category: best-practices
scraped_at: 2026-04-28T08:23:12+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:dc83af324be166e4dc7ff5f76f76ed144a6d8ed428a2bc615f6b3b70763e88c5
---

## 概述

[自动化测试框架](../harmonyos-guides/arkxtest-guidelines.md)是一套面向多设备、全场景的端侧测试体系，基于DevEco Studio开发环境和hvigor构建系统，整合了UI测试（[@ohos.UiTest](../harmonyos-references/js-apis-uitest.md)）、单元测试（[@ohos/hypium](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fhypium)）等能力，通过标准化的工程结构、编码规范与执行流程，支撑开发者实现高效高质量验证。

该框架涵盖[单元测试框架](../harmonyos-guides/unittest-guidelines.md)、[UI测试框架](../harmonyos-guides/uitest-guidelines.md)和[白盒性能测试框架](../harmonyos-guides/perftest-guideline.md)。

* 单元测试框架：是自动化测试框架基础底座，UI测试脚本和性能测试脚本需基于单元测试框架进行开发，用于定义测试用例及验证执行结果。
* UI测试框架：调用[UiTest](../harmonyos-references/js-apis-uitest.md)接口进行UI界面查找和模拟操作。
* 白盒性能测试框架：调用[PerfTest](../harmonyos-references/js-apis-perftest.md)接口采集和度量测试应用内指定逻辑执行时的基础性能数据。

本文介绍了单元测试框架和UI测试框架的实现，旨在帮助开发者了解和掌握自动化测试框架的开发流程与实现细节。关键步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/5GMiT9VfSfqo4Ilhv36kaQ/zh-cn_image_0000002515546966.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=E25127A870415F80A14A6C8B6AF4A27B51F3BCE02924A50475AFA1146DCBEB7E "点击放大")

## 场景案例

### 场景描述

本节基于官网codelab[《从简单页面开始》](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_PageAndData01)介绍自动化测试框架的开发流程与实现细节，主要涵盖单元测试和UI测试两部分，开发者可根据具体业务场景对应用实施自动化测试。

### 实现原理

* **单元测试**

  使用单元测试框架通过Mock隔离被测代码与外部依赖，在无需启动完整应用的前提下，对应用逻辑（如工具函数、业务服务等）进行快速、隔离、可重复的验证。本文采用该框架的以下特性来实现单元测试：

  | 特性 | 使用说明 | 使用场景 |
  | --- | --- | --- |
  | [基础流程能力](../harmonyos-guides/unittest-guidelines.md#基础流程能力) | 通过基础流程能力如describe、it等接口定义测试套和测试用例。并对测试套和测试用例设置预置条件和清理条件。 | 定义测试套和测试用例，以及测试用例执行前需要预置条件和执行后需要清理条件的场景，如：设置定时器和清理定时器。 |
  | [断言能力](../harmonyos-guides/unittest-guidelines.md#断言能力) | 使用如assertEqual等断言接口判断检验实际值是否等于预期值。 | 检验函数功能是否正常。 |
  | [Mock能力](../harmonyos-guides/unittest-guidelines.md#mock能力) | 使用Mock能力，Mock自定义对象的函数。 | 函数依赖外部资源或复杂逻辑，如：依赖网络请求返回值。 |
  | [数据驱动](../harmonyos-guides/unittest-guidelines.md#数据驱动) | 使用数据驱动能力，对测试套或者测试用例执行若干次。 | 多个测试用例或测试套有相同类型参数，如：进行压力测试。 |

* **UI测试**

  通过[DevEco Testing](../harmonyos-guides/deveco-testing.md)的UIViewer获取屏幕坐标点信息，并使用UI测试框架接口对指定坐标点或指定控件注入模拟的输入事件（如点击、滑动等），实现界面交互和验证的自动化。本文针对不同UI测试场景提供如下实现方案：

  | 场景 | 实现方案 |
  | --- | --- |
  | 查找组件 | 创建[On](../harmonyos-references/js-apis-uitest.md#on9)对象，通过[id](../harmonyos-references/js-apis-uitest.md#id9)或[type](../harmonyos-references/js-apis-uitest.md#type9)描述目标控件，然后使用[findComponent()](../harmonyos-references/js-apis-uitest.md#findcomponent9)根据目标控件的属性要求查找该控件。 |
  | 模拟输入 | 通过[inputText()](../harmonyos-references/js-apis-uitest.md#inputtext9)模拟文本输入。 |
  | 模拟点击 | 通过[Component](../harmonyos-references/js-apis-uitest.md#component9)或[Driver](../harmonyos-references/js-apis-uitest.md#driver9)中的click属性模拟点击。 |
  | 模拟触摸屏手指滑动 | 通过[swipe()](../harmonyos-references/js-apis-uitest.md#swipe9)方法模拟对轮播图的滑动。 |
  | 等待页面加载 | 使用[waitForIdle()](../harmonyos-references/js-apis-uitest.md#waitforidle9)等待当前界面的所有控件空闲后，再进行下一步操作。 |

  UI测试流程图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/F2JstVZzSvueoZETv5fIig/zh-cn_image_0000002515387058.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=F28998454FDC032BB69858AB9B8BF233A2A155350C7FDF1A4DEFE0207D506720 "点击放大")

### 开发步骤

1. 搭建DevEco Studio环境

   测试脚本基于DevEco Studio编写，开发者需先下载[DevEco Studio](https://developer.huawei.com/consumer/cn/download/)并完成[环境准备](../harmonyos-guides/hdc.md#环境准备)。
2. 下载安装Hypium

   Hypium是OpenHarmony上的测试框架，提供测试用例的编写、执行及结果显示功能，用于OpenHarmony系统应用接口和应用界面的测试。使用DevEco Studio打开测试项目，并按以下方案进行配置。

   说明

   本示例使用的Hypium版本为@ohos/hypium(V1.0.24)，若开发者需使用最新版本，请查看[@ohos/hypium](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fhypium)。

   * 方案一：通过ohpm命令下载@ohos/hypium。

     ```
     1. ohpm install @ohos/hypium@1.0.24 --save-dev
     ```
   * 方案二：在应用工程的[oh-package.json5](../harmonyos-guides/ide-oh-package-json5.md)文件的devDependencies中配置版本号，然后点击编辑器窗口上方的“Sync Now”同步工程，即可使用对应版本的框架功能。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/KyyUbunDQNmbmpdy3o5q3w/zh-cn_image_0000002554811799.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=EFF6DFB3D185B5526F42B72C5D8DEF2F15F857177C326BE7091F785ECAADE961)
3. 新建测试脚本

   参考[创建ArkTS测试用例](../harmonyos-guides/ide-instrument-test.md#section36049271219)，导入所需的[单元测试框架能力](../harmonyos-guides/unittest-guidelines.md#单元测试框架能力使用说明)及其他测试脚本中依赖的接口，[编写单元测试脚本](../harmonyos-guides/unittest-guidelines.md#编写单元测试脚本)。

   启动被测试页面，检查设备显示的页面是否为预期页面。流程图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/yWBxx8WbRKWz5CcJTGDyow/zh-cn_image_0000002547066887.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=354B274E8B02DC125D5ACDF66083A897E19915B9CDDE1CD3EB274D7259070333 "点击放大")

   在自动化测试中，常用[基础流程能力](../harmonyos-guides/unittest-guidelines.md#基础流程能力)的it定义测试用例，其参数如下：

   | 参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | testCaseName | string | 是 | 测试用例的名称，用于标识该测试用例。 |
   | attribute | TestType | Size | Level | 是 | 测试类型，用于标记测试用例的类型。 |
   | func | Function | 是 | 异步函数（async），包含测试用例的具体逻辑。 |

   使用it创建测试用例后，通过[AbilityDelegatorRegistry](../harmonyos-references/js-apis-app-ability-abilitydelegatorregistry.md)获取应用包名，构造want启动对象、调用[startAbility()](../harmonyos-references/js-apis-inner-application-abilitydelegator.md#startability9)启动应用。在应用加载完成后，调用[getCurrentTopAbility()](../harmonyos-references/js-apis-inner-application-abilitydelegator.md#getcurrenttopability9)获取设备上前台显示页面，并使用[expect()](../harmonyos-guides/unittest-guidelines.md#基础流程能力)和[assertEqual()](../harmonyos-guides/unittest-guidelines.md#断言能力)断言当前页面是否为预期启动页面。

   ```
   1. const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

   3. export default function UITest() {
   4. describe('UITest', () => {

   6. /**
   7. * Start the application to be tested.
   8. */
   9. it('startApp', Level.LEVEL3, async (done: Function) => {
   10. hilog.info(0x0000, 'testTag', '%{public}s', "UITest: TestUiExample begin");
   11. // Initialize the Driver object.
   12. const driver = Driver.create();
   13. const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
   14. // Specify the bundle name and ability name of the application to be tested.
   15. const want: Want = {
   16. bundleName: bundleName,
   17. abilityName: 'EntryAbility'
   18. }
   19. // Start the application to be tested.
   20. await delegator.startAbility(want);
   21. // Wait until the application starts.
   22. await driver.waitForIdle(4000, 5000);
   23. const ability: UIAbility = await delegator.getCurrentTopAbility();
   24. hilog.info(0x0000, 'testTag', '%{public}s', "get top ability");
   25. // Ensure that the top ability of the application is the specified ability.
   26. expect(ability.context.abilityInfo.name).assertEqual('EntryAbility');
   27. done();
   28. })
   29. // ...
   30. })
   31. }
   ```

   [UITest.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/ui/UITest.test.ets#L22-L152)
4. 编写单元测试用例
   * [基础流程能力](../harmonyos-guides/unittest-guidelines.md#基础流程能力)

     使用基础流程能力[beforeAll()](../harmonyos-guides/unittest-guidelines.md#基础流程能力)定义预置条件，[afterAll()](../harmonyos-guides/unittest-guidelines.md#基础流程能力)定义清理条件。预置条件在所有测试用例开始前执行一次，清理条件在所有测试用例结束后执行一次。

     ```
     1. let success = -1;
     2. let timeout = 0;

     4. beforeAll(() => {
     5. // Preset increment action before all test cases of the test suite start.
     6. success++;
     7. // Set a timer before all test cases of the test suite start.
     8. timeout = setTimeout(() => {
     9. hilog.info(0x0000, 'testTag', '%{public}s', 'setTimeout');
     10. }, 1000);
     11. })

     13. beforeEach(() => {
     14. // Preset increment action before each test case of the test suite starts.
     15. success++;
     16. })

     18. afterEach(() => {
     19. hilog.info(0x0000, 'testTag', '%{public}s', `success: ${success}`);
     20. })

     22. afterAll(() => {
     23. hilog.info(0x0000, 'testTag', '%{public}s', 'AfterAll executed');
     24. hilog.info(0x0000, 'testTag', '%{public}s', `success: ${success}`);
     25. // Clear the timer After all test cases of the test suite end.
     26. clearTimeout(timeout);
     27. })
     ```

     [MainViewModel.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/unit/MainViewModel.test.ets#L41-L68)
   * [断言能力](../harmonyos-guides/unittest-guidelines.md#断言能力)

     通过[assertUndefined()](../harmonyos-guides/unittest-guidelines.md#断言能力)判断被检验的值是否为undefined，并使用[assertEqual()](../harmonyos-guides/unittest-guidelines.md#断言能力)检验实际值是否符合预期值。

     ```
     1. it('inputAccountLength', 0, () => {
     2. let inputAccountLength = CommonConstants.INPUT_ACCOUNT_LENGTH;
     3. // Check if INPUT_ACCOUNT_LENGTH is not undefined.
     4. expect(inputAccountLength).not().assertUndefined();
     5. expect(inputAccountLength).assertEqual(11);
     6. })
     ```

     [CommonConstants.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/unit/CommonConstants.test.ets#L44-L49)

     检验mainViewModel类中自定义函数返回值的长度及数据类型是否符合预期。

     ```
     1. it('getFirstGridData', 0, () => {
     2. const firstGridData = mainViewModel.getFirstGridData();
     3. // Verify if the return value of getFirstGridData is eight.
     4. expect(firstGridData.length).assertEqual(8);
     5. // Verify if the type of firstGridData[0] is 'ItemData'.
     6. expect(firstGridData[0] instanceof ItemData).assertTrue();
     7. })
     ```

     [MainViewModel.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/unit/MainViewModel.test.ets#L97-L105)
   * [Mock能力](../harmonyos-guides/unittest-guidelines.md#mock能力)

     对mainViewModel类中的getSwiperImages()函数进行Mock，并设置函数被Mock后的返回值。用例执行完毕后，恢复被Mock对象的实例。

     ```
     1. it('getSwiperImages', 0, () => {
     2. const swiperImages = mainViewModel.getSwiperImages();
     3. expect(swiperImages).assertInstanceOf('Array');
     4. expect(swiperImages.length).assertEqual(4);
     5. // Mock the getSwiperImages function of the mainViewModel class.
     6. let mocker = new MockKit();
     7. let getSwiperImages = mocker.mockFunc(mainViewModel, mainViewModel.getSwiperImages);
     8. // The result '[]' is returned when the function is called with any arguments passed in.
     9. when(getSwiperImages)(ArgumentMatchers.any).afterReturn([]);
     10. expect(mainViewModel.getSwiperImages()).assertInstanceOf('Array');
     11. expect(mainViewModel.getSwiperImages().length).assertEqual(0);
     12. // Restore the mocked object instances.
     13. mocker.clear(mainViewModel);
     14. // Verify if the mocked object instances is restored.
     15. expect(mainViewModel.getSwiperImages().length).assertEqual(4);
     16. })
     ```

     [MainViewModel.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/unit/MainViewModel.test.ets#L75-L90)
   * [数据驱动](../harmonyos-guides/unittest-guidelines.md#数据驱动)

     数据驱动需要使用Ability能力，可参考[自定义Ability和Resources](../harmonyos-guides/ide-instrument-test.md#section760061533)。文件内容示例可在[运行测试用例](../harmonyos-guides/ide-instrument-test.md#section14415226122419)后，在对应模块的build/{productName}/intermediates/src/ohosTest下查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/9PY39EHBSH6cfzMpQ1yYjA/zh-cn_image_0000002504491476.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=7D898166CD3E4051774B95C09736EFE3E22620A83DDF6FA4122C371C87C23BEA)

     定义Ability后需要在module.json5文件中补充配置字段mainElement、pages和abilities。关于字段的具体说明，请参考[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)。

     ```
     1. {
     2. "module": {
     3. "name": "entry_test",
     4. "type": "feature",
     5. "description": "$string:module_test_desc",
     6. "mainElement": "TestAbility",            // Corresponds to the ability name in the abilities section below.
     7. "deviceTypes": [
     8. "phone"
     9. ],
     10. "deliveryWithInstall": true,
     11. "installationFree": false,
     12. "pages": "$profile:test_pages",          // Corresponds to the test_pages.json file under resources > base > profile.
     13. "abilities": [                           // Configuration of the ability to add.
     14. {
     15. "name": "TestAbility",
     16. "srcEntry": "./ets/testability/TestAbility.ets",
     17. "description": "$string:TestAbility_desc",
     18. "icon": "$media:icon",
     19. "label": "$string:TestAbility_label",
     20. "exported": true,
     21. "startWindowIcon": "$media:icon",
     22. "startWindowBackground": "$color:start_window_background"
     23. }
     24. ]
     25. }
     26. }
     ```

     [module.json5](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/module.json5#L2-L27)

     说明

     build/{productName}/intermediates/src/ohosTest目录下的resources不包含icon图标，需开发者自行添加。

     数据驱动能力依据测试数据配置，驱动测试用例的执行次数及每次执行时的参数传递，使用时依赖data.json配置文件。

     ```
     1. {
     2. "suites": [
     3. {
     4. "describe": [
     5. "MainViewModelTest"
     6. ],
     7. "stress": 1,
     8. "items": [
     9. {
     10. "it": "testDataDriverAsync",
     11. "stress": 2,
     12. "params": [
     13. {
     14. "name": "tom",
     15. "value": 5
     16. },
     17. {
     18. "name": "jerry",
     19. "value": 4
     20. }
     21. ]
     22. },
     23. {
     24. "it": "testDataDriver",
     25. "stress": 3
     26. }
     27. ]
     28. }
     29. ]
     30. }
     ```

     Stage模型在测试工程中的TestAbility目录下TestAbility.ets文件中导入data.json，并在文件中的Hypium.hypiumTest()函数执行前设置参数数据。

     ```
     1. export default class TestAbility extends UIAbility {
     2. abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

     4. constructor() {
     5. super();
     6. this.abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
     7. }

     9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
     10. hilog.info(0x0000, 'testTag', '%{public}s', 'TestAbility onCreate');
     11. hilog.info(0x0000, 'testTag', '%{public}s', 'want param:' + JSON.stringify(want) ?? '');
     12. hilog.info(0x0000, 'testTag', '%{public}s', 'launchParam:' + JSON.stringify(launchParam) ?? '');
     13. let abilityDelegatorArguments: abilityDelegatorRegistry.AbilityDelegatorArgs;
     14. abilityDelegatorArguments = abilityDelegatorRegistry.getArguments();
     15. hilog.info(0x0000, 'testTag', '%{public}s', 'start run testcase!!!');
     16. // Set the data before Hypium.hypiumTest() is executed.
     17. Hypium.setData(data);
     18. Hypium.hypiumTest(this.abilityDelegator, abilityDelegatorArguments, testsuite);
     19. }

     21. // ...
     22. }
     ```

     [TestAbility.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/testability/TestAbility.ets#L27-L77)

     在data.json文件配置的测试套（MainViewModelTest）中定义测试用例，测试用例名称应与配置文件中items下的it名称一致。

     ```
     1. interface ParmObj {
     2. name: string,
     3. value: number
     4. }

     6. export default function MainViewModelTest() {
     7. describe('MainViewModelTest', () => {
     8. // ...
     9. it('testDataDriverAsync', 0, async (done: Function, data: ParmObj) => {
     10. // Use data object to receive parameters passed from data.json.
     11. hilog.info(0x0000, 'testTag', '%{public}s', `name: ${data.name}`);
     12. hilog.info(0x0000, 'testTag', '%{public}s', `value: ${data.value}`);
     13. // The name passed in data.json is either 'tom' or 'jerry'.
     14. expect(data.name === 'tom' || data.name === 'jerry').assertTrue();
     15. // Check if the actual value and the expected value '4' are within the allowable error range '1'.
     16. expect(data.value).assertClose(4, 1);
     17. done();
     18. });
     19. // ...
     20. })
     21. }
     ```

     [MainViewModel.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/unit/MainViewModel.test.ets#L33-L150)
5. 编写UI测试用例

   在UI测试中，开发者可以利用[UiTest](../harmonyos-references/js-apis-uitest.md)接口模拟点击、双击、长按、滑动等操作，以验证应用程序中的UI行为。

   * 模拟文本输入

     通过[On](../harmonyos-references/js-apis-uitest.md#on9)对象匹配目标控件，然后使用[inputText()](../harmonyos-references/js-apis-uitest.md#inputtext9)模拟文本输入。

     ```
     1. it('accountInputText', TestType.FUNCTION, async () => {
     2. let driver = Driver.create();
     3. // Match TextInput component by id.
     4. let on = ON.id('account');
     5. let accountInput = await driver.findComponent(on);
     6. await accountInput.inputText('123456');
     7. let account = await accountInput.getText();
     8. expect(account).assertEqual('123456');
     9. })
     ```

     [UITest.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/ui/UITest.test.ets#L56-L64)
   * 模拟触摸屏手指操作

     使用[click()](../harmonyos-references/js-apis-uitest.md#click9-1)模拟触摸屏手指操作以收起键盘，然后通过[findComponent()](../harmonyos-references/js-apis-uitest.md#findcomponent9)查找Button控件，点击该按钮进行登录操作。

     ```
     1. it('loginButton', TestType.FUNCTION, async () => {
     2. let driver = Driver.create();
     3. // Click the location of the confirm button in the input method to collapse the input method.
     4. await driver.click(1196, 2511);
     5. await driver.waitForIdle(2000, 3000);
     6. // Check if the button is displayed.
     7. let loginButton = await driver.findComponent(ON.type('Button'));
     8. await loginButton.click();
     9. // Wait the application for loading to the main page.
     10. await driver.waitForIdle(4000, 5000);
     11. })
     ```

     [UITest.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/ui/UITest.test.ets#L83-L93)

     等待Swiper控件加载完成后，使用[swipe()](../harmonyos-references/js-apis-uitest.md#swipe9)模拟触摸屏手指滑动。

     ```
     1. it('swiper', TestType.FUNCTION, async () => {
     2. let driver = Driver.create();
     3. // Wait the Swiper component for displaying in the current page.
     4. await driver.waitForComponent(ON.type('Swiper'), 2000);
     5. // Check if the Swiper component exists.
     6. await driver.assertComponentExist(ON.type('Swiper'));
     7. await driver.waitForIdle(1000, 2000);
     8. // Swipe the carousel from right to left.
     9. await driver.swipe(1100, 700, 100, 700, 3000);
     10. // Wait for the swipe operation to complete.
     11. await driver.waitForIdle(1000, 2000);
     12. await driver.swipe(1100, 700, 100, 700, 3000);
     13. await driver.waitForIdle(1000, 2000);
     14. })
     ```

     [UITest.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/ui/UITest.test.ets#L100-L113)
   * 页面加载等待

     使用[swipe()](../harmonyos-references/js-apis-uitest.md#swipe9)切换页面后，通过[waitForIdle()](../harmonyos-references/js-apis-uitest.md#waitforidle9)和[waitForComponent()](../harmonyos-references/js-apis-uitest.md#waitforcomponent9)等待Toggle控件出现来判断页面跳转是否完成。

     ```
     1. it('setting', TestType.FUNCTION, async () => {
     2. let driver = Driver.create();
     3. await driver.swipe(1100, 1500, 100, 1500, 3000);
     4. await driver.waitForIdle(1000, 2000);
     5. // Match the Toggle component in the ListItem component.
     6. let on = ON.type('Toggle').within(ON.type('ListItem'));
     7. await driver.waitForComponent(on, 2000);
     8. await driver.assertComponentExist(on);
     9. // ...
     10. })
     ```

     [UITest.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/ui/UITest.test.ets#L129-L147)
6. 执行测试脚本

   连接目标测试设备（如手机）或模拟器后，在DevEco Studio页面点击对应按钮，或通过命令行执行测试脚本。详细可参考[DevEco Studio执行测试脚本](../harmonyos-guides/unittest-guidelines.md#deveco-studio执行测试脚本)和[命令行执行测试脚本](../harmonyos-guides/unittest-guidelines.md#命令行执行测试脚本)。

### 实现效果

自动化测试实现效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Kl18HpQkQ0yqq5YO9hsKAg/zh-cn_image_0000002536291283.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=B44246D8865DC762585D18FD5E878FA0A3E6B15F08D34C906E16FEEF4A446A57 "点击放大")

## 常见问题

### 断言能力assertInstanceOf接口无法检验自定义类型

**问题现象**

使用[assertInstanceOf()](../harmonyos-guides/unittest-guidelines.md#断言能力)检验自定义数据类型，脚本运行时报错“Error in getFirstGridData, [object Object] is [object Object]not ItemData”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/OJM63T76TzGKqlH4LFxBMA/zh-cn_image_0000002536411247.png?HW-CC-KV=V1&HW-CC-Date=20260428T002309Z&HW-CC-Expire=86400&HW-CC-Sign=D8CFE62A8B98E04A34BD37DABEA972116E2F01370F9AE4FF2A601F7EA91070EB)

**可能原因**

[assertInstanceOf()](../harmonyos-guides/unittest-guidelines.md#断言能力)在进行类型判断时，会将对象转换为字符串进行比较。自定义数据类型转换后变为[Object Object]，导致与预期类型不符。

**解决方案**

在[expect()](../harmonyos-guides/unittest-guidelines.md#基础流程能力)中进行instanceof类型判断，并使用[assertTrue()](../harmonyos-guides/unittest-guidelines.md#断言能力)进行检验。修改后示例代码如下：

```
1. expect(firstGridData[0] instanceof ItemData).assertTrue();
```

[MainViewModel.test.ets](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest/blob/master/entry/src/ohosTest/ets/test/unit/MainViewModel.test.ets#L103-L103)

### UI测试时inputText接口无法输入字母和特殊字符

**问题现象**

使用[inputText()](../harmonyos-references/js-apis-uitest.md#inputtext9)对TextInput控件输入文本时，只能输入数字，无法输入字母和特殊字符。

**可能原因**

输入框类型为InputType.Number。纯数字输入模式的输入框，只能输入数字[0-9]。

**解决方案**

将输入框类型修改为InputType.USER\_NAME，开发者可根据业务场景[设置输入框类型](../harmonyos-guides/arkts-common-components-text-input.md#设置输入框类型)后再进行测试。

### UI测试时对控件首次操作无效

**问题现象**

使用[swipe()](../harmonyos-references/js-apis-uitest.md#swipe9)对Swiper控件滑动时，首次滑动无效，但后续多次滑动均能正常执行。

**可能原因**

调用UI操作接口时相关控件还未加载完成。

**解决方案**

使用[waitForComponent()](../harmonyos-references/js-apis-uitest.md#waitforcomponent9)等待控件加载完成后再进行UI操作。

## 总结

自动化测试框架是构建高效、稳定、可维护和可扩展测试体系的核心要素。使用该框架进行应用测试，测试用例可自动执行，无需开发者手动操作，有助于减少测试工作量。当测试用例执行失败时，通过DevEco Studio开发者能够快速发现并定位自动化测试中出现的问题，减少应用上架后的缺陷。

本文主要使用单元测试框架的基础流程、断言等能力，以及UI测试框架的UiTest接口来实现自动化测试，详细指导可参考[单元测试和UI测试](../harmonyos-guides/ut.md)。

若开发者需对应用逻辑进行性能测试，可参考[白盒性能测试框架使用指导](../harmonyos-guides/perftest-guideline.md)。

## 示例代码

* [基于自动化测试框架实现单元测试和UI测试](https://gitcode.com/HarmonyOS_Samples/ArkTSComponentsTest)
