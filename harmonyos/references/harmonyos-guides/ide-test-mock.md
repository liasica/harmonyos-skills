---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-test-mock
title: Mock能力
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > Mock能力
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a5f10c613ad65635c679df511fb0801e8d3417888d8d99278ac16da1d2d2150
---

在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用Mock能力，对这些接口或对象进行模拟。当前Instrument Test和Local Test均支持对模块进行Mock，对于调用系统模块API或外部依赖模块，使用import mock，对于本地模块，使用hamock/hypium插件包的mock接口或者import mock。

说明

仅API 11及以上版本的Stage模型工程支持。

## 系统模块/依赖模块Mock

通过import mock对系统模块API或依赖模块的方法进行Mock，在mock-config.json5配置文件中定义目标模块和Mock实现代码文件的映射关系，运行时import目标模块都将指向Mock实现代码。以系统API bluetoothManager为例，具体实现如下。

1. 在src/mock目录下新建一个ArkTS文件，例如bluetooth\_manager.mock.ets，在这个文件内定义目标模块的Mock实现。

   ```
   1. // src/mock/bluetooth_manager.mock.ets
   2. enum BluetoothState {
   3. /** Indicates the local Bluetooth is off */
   4. STATE_OFF = 0,
   5. /** Indicates the local Bluetooth is turning on */
   6. STATE_TURNING_ON = 1,
   7. /** Indicates the local Bluetooth is on, and ready for use */
   8. STATE_ON = 2,
   9. /** Indicates the local Bluetooth is turning off */
   10. STATE_TURNING_OFF = 3,
   11. /** Indicates the local Bluetooth is turning LE mode on */
   12. STATE_BLE_TURNING_ON = 4,
   13. /** Indicates the local Bluetooth is in LE only mode */
   14. STATE_BLE_ON = 5,
   15. /** Indicates the local Bluetooth is turning off LE only mode */
   16. STATE_BLE_TURNING_OFF = 6
   17. }
   18. interface BluetoothInfo {
   19. state: number
   20. }
   21. const MockBluetoothManager: Record<string, Object> = {
   22. 'getBluetoothInfo': () => {
   23. return { state : BluetoothState.STATE_BLE_TURNING_ON } as BluetoothInfo;
   24. },
   25. };
   26. export default MockBluetoothManager;
   ```
2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的映射关系。

   ```
   1. "@ohos.enterprise.bluetoothManager": {  // 待替换的模块名
   2. "source": "src/mock/bluetooth_manager.mock.ets"  // Mock代码的路径，相对于模块根目录
   3. }
   ```
3. 在测试文件中编写如下代码。

   ```
   1. // bluetoothManager.test.ets
   2. import { describe, it, expect } from '@ohos/hypium';
   3. import { bluetoothManager } from '@kit.MDMKit';

   5. export default function mock_system_api() {
   6. describe('mock_system_api', () => {
   7. /* mock系统API */
   8. it('mock_system_api', 0, () => {
   9. let bluetoothInfo = bluetoothManager.getBluetoothInfo({
   10. bundleName: "com.example.myapplication"
   11. })
   12. expect(bluetoothInfo.state).assertEqual(4)
   13. });
   14. });
   15. }
   ```
4. 如果测试文件是手动创建的，需要将用例类mock\_system\_api添加到List.test.ets文件中。

   ```
   1. import mock_system_api from './bluetoothManager.test';

   3. export default function testsuite() {
   4. mock_system_api();
   5. }
   ```
5. 执行测试，用例通过。

## 本地模块Mock

有两种方式可以对本地模块进行Mock，一是使用hamock/hypium插件包的mock接口，二是使用import mock。

### 使用hamock/hypium插件包的mock接口

以下例子通过mock接口模拟本地模块的某个方法，关于Mock的更多说明可以参考[mock能力](https://gitcode.com/openharmony/testfwk_arkxtest#mock能力)。

1. 在src/main/ets目录下新建一个ArkTS文件，例如ClassForMock.ets，并在其中导出一个类。

   ```
   1. export class ClassForMock {
   2. constructor() {
   3. }
   4. method_1(arg: string) {
   5. return '888888';
   6. }
   7. method_2(arg: string) {
   8. return '999999';
   9. }
   10. }
   ```
2. 在测试文件中编写如下代码。

   ```
   1. // afterReturnTest.test.ets
   2. import { describe, expect, it, MockKit, when } from '@ohos/hypium';
   3. import { ClassForMock } from '../../../main/ets/ClassForMock';

   5. export default function afterReturnTest() {
   6. describe('afterReturnTest', () => {
   7. it('afterReturnTest', 0, () => {
   8. console.info("it begin");
   9. // 1.创建一个mock能力的对象MockKit
   10. let mocker: MockKit = new MockKit();
   11. // 2.定义类ClassForMock，里面两个函数，然后创建一个对象classForMock
   12. let classForMock: ClassForMock = new ClassForMock();
   13. // 3.进行mock操作,比如需要对ClassForMock类的method_1函数进行mock
   14. let mockFunc: Function = mocker.mockFunc(classForMock, classForMock.method_1);
   15. // 4.期望classForMock.method_1函数被mock后, 以'test'为入参时调用函数返回结果'1'
   16. when(mockFunc)('test').afterReturn('1');
   17. // 5.对mock后的函数进行断言，看是否符合预期
   18. // 执行成功案例，参数为'test'
   19. expect(classForMock.method_1('test')).assertEqual('1'); // 执行通过
   20. })
   21. })
   22. }
   ```
3. 如果测试文件是手动创建的，需要将用例类afterReturnTest添加到List.test.ets文件中。

   ```
   1. import afterReturnTest from './afterReturnTest.test';

   3. export default function testsuite() {
   4. afterReturnTest();
   5. }
   ```
4. 执行测试，用例通过。

### 使用import mock

使用import mock对本地模块进行Mock，操作步骤和系统模块/依赖模块的Mock类似，在mock-config.json5配置文件中定义目标模块和Mock实现代码文件的映射关系，运行时import目标模块都将指向Mock实现代码。以下例子对本地模块entry/src/main/ets/common/calc.ets中的sum函数进行Mock。

1. 在src/mock目录下新建一个common目录并创建一个ArkTS文件，例如calc.mock.ets，在这个文件内定义目标模块的Mock实现。

   ```
   1. // src/mock/common/calc.mock.ets
   2. export function sum() {
   3. return "this is mock sum";
   4. }
   ```

   calc.ets的原始实现如下：

   ```
   1. // src/main/ets/common/calc.ets
   2. export function sum() {
   3. return 1;
   4. }
   ```
2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的映射关系。

   ```
   1. {
   2. "common/calc.ets": { // 本地模块只支持ets/xxx的相对路径，并需明确文件后缀
   3. "source": "src/mock/common/calc.mock.ets"  // Mock代码的路径，相对于模块根目录
   4. },
   5. }
   ```
3. 在测试文件中编写如下代码。

   ```
   1. // test_mock_local_method.test.ets
   2. import { describe, it, expect } from '@ohos/hypium'
   3. import { sum } from '../../../main/ets/common/calc';

   5. export default function test_mock_local_method() {
   6. describe('test_mock_local_method', () => {
   7. it("test_mock_local_method", 0, () => {
   8. expect(sum()).assertEqual("this is mock sum")
   9. })
   10. })
   11. }
   ```
4. 如果测试文件是手动创建的，需要将用例类test\_mock\_local\_method添加到List.test.ets文件中。

   ```
   1. import test_mock_local_method from './test_mock_local_method.test';

   3. export default function testsuite() {
   4. test_mock_local_method();
   5. }
   ```
5. 执行测试，用例通过。
