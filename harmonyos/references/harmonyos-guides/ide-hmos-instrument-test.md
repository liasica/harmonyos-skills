---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-instrument-test
title: 仪器测试（Instrument Test）
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 开发自测试 > 仪器测试（Instrument Test）
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d388f869bdf6e27f2dba66eea12374d5287136e3fe746cef377b5cff79c05f68
---

鸿蒙电脑DevEco Studio支持应用/元服务测试框架，提供测试用例执行能力，提供用例编写基础接口，输出测试结果，支持用户开发简洁易用的自动化测试脚本，支持代码覆盖率统计。当前支持Instrument Test，测试用例存放在ohosTest测试目录下，需要运行在设备上。Instrument Test支持ArkTS/JS语言。

**说明** 

覆盖率测试不支持开启混淆。

## 创建ArkTS测试用例

1. 手动在**ohosTest** > **ets** > **test**文件夹下创建测试文件，文件名以.test.ets结尾，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](arkxtest-guidelines.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/CjGIrT5pT1WJF4NSW1Nz3A/zh-cn_image_0000002792001162.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD62D6364C2AE394772935DD4673101CC6F060999213E9F96DF4C4AD4301AB15 "点击放大")
2. 在List.test.ets文件中添加创建的用例类，例如用例类abilityTest。

   ```ts
   import abilityTest from './Ability.test';

   export default function testsuite() {
     abilityTest();
   }
   ```

   **说明** 

   * 手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾。
   * 测试文件名称应保持唯一性，并且不能使用逗号、横线、空格以及\ / : \* ? “”< > | （）&等特殊字符。
   * 首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UITest测试能力。

## 运行测试用例

### 运行模式

使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备上运行，具体请参考[应用/元服务运行](ide-hmos-run-device.md)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：

* 在工程目录中，单击**右键 > 运行 '测试文件名称'**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/XJ8vCST4SZO88BjzttR0Fw/zh-cn_image_0000002792001144.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D862A778EE0BC32ED9F0DF56A8A1C1A643DC5ADC55833488FA571F1CE25A09B5 "点击放大")
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/_xcXxh4hS_ORXU17z0n8Tw/zh-cn_image_0000002792001154.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=63EAEBF2D1DD15C59BFAF61826CD15E80592FEBC3E239A25AF2DCF3DF6D6DFBD "点击放大")
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-hmos-instrument-test.md#section1631610401035)后，点击DevEco Studio的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/xBeyY-GUTtKsTMUIS450Wg/zh-cn_image_0000002820721117.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=46A8E8AFADE03B1CD29D4CCA7698F27EA25631FE992A3E1210491DD677856838 "点击放大")图标选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/-7-eAbzWRou-L2DoOJru4w/zh-cn_image_0000002820721129.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E09163C5396397100AFAD003A30935E127E24B1EE5E3F59655C1F4FF3A461728 "点击放大")按钮执行Instrument Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/gF_UcE6WQU2dqlsJ3rH2-A/zh-cn_image_0000002792001148.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=579B3A016C80029DC283F0D72AD426FA9DE644080B0580B87DBCBEB63FCE6D69 "点击放大")

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/jGrjJ92xTY-GeyBOJMAwow/zh-cn_image_0000002792001164.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=531FDF93E1769A0E2B08A14E482660F5719E707E532CBCFC09982BEC99FE0572 "点击放大")

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 调试 '测试文件名称'**，以调试模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/O4tkNU7hQvC8w3hy2-_7tQ/zh-cn_image_0000002791841180.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBBF6FEDBAF43CC9E1A0596234E2C98B4111FF8CA82F264E51EA501030742C39 "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/8knxT7U6RtOVVNzHSTyrLw/zh-cn_image_0000002820681117.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C3C94DABC03ED723032113668823B108822CF02C91A50AFAF7858435D6FFEF7)图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/q-6vKmvLS7OYmvpauPoUcA/zh-cn_image_0000002792001150.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F96E3EA9BD07748AF9A3F00738C191327D0C4BBF5BD1DEA25FCD50FA52D1E47C)

在断点命中时，下方将出现调试器窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/UJLpEebAQmu-J0ziLGnwGg/zh-cn_image_0000002820721123.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=258C2AF2392B6818A131F9B3D8166B22632AFAF7D82C1D4A0C04D81627AC0D29 "点击放大")

断点命中时，在调试窗口中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/O6-sS0QyReGFrsx8ZLOrfQ/zh-cn_image_0000002820721119.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB07B7B11EEB468326886DE1E36E29FD971F0B5F5BFC31054A99EF5BB2BC383E "点击放大")

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/rWd47J1gScCw4HnWHsgDzg/zh-cn_image_0000002820721111.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFC01E6653C0B035A082BCEB561EE390295444929F31C66DE2538AFF8876C35F "点击放大")

**说明** 

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-hmos-instrument-test.md#section386512457406)。

### 覆盖率统计模式

**说明** 

源码文件的命名不可为“test.ets”、“xx.test.ets”、“test.ts”和“xx.test.ts”，该命名的文件不会生成报告。

在Instrument Test运行的基础上支持代码覆盖率统计。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 使用覆盖率运行 '测试文件名称'** ，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/rd28lqBBSmGL5NLpbEn2DA/zh-cn_image_0000002820721121.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=5836BF2CC529A222A32D09D5CEA7A198104A893AD5265C9E62F4793D79DADC5B "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/z0gtJ8LtR-yTeyTw2vAVfA/zh-cn_image_0000002791841182.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3F83A364E666AEAE9D8EAD9918CCD25A60CD9B3D34698169CD8F1E647687A47 "点击放大")图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/A4Y2wlVfQm6Rl7lqtJzsWw/zh-cn_image_0000002791841168.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=C92B3FDBE8506E10AB4B78B12163D1EA87C3A34FA7DD28F6AC6C3B1CACD507DA)

启动测试后，进行编译构建，构建结束后自动拉起测试窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/QmIcnmWQSXysmYhrq0xV0g/zh-cn_image_0000002820681121.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A504384F0628C8CDB19A85E107D8BC46CD72FDBAC97D2BF77E1637278E52A76 "点击放大")

在本地找到报告后鼠标右键快速查看，打开报告，查看ArkTS代码覆盖率详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/7jUctmVwQACQPAQYV_kJmw/zh-cn_image_0000002820721109.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=45FF69BC5A1D4560A56928F22DE8BE66A1CBE85153BD37118564F452A5614462 "点击放大")

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 点击编辑器顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/6i3J1W55TI-GSc5WaPNgUQ/zh-cn_image_0000002792001146.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8229EC997F0955AB7EB7803536CBFB5E316D3E8161C23E9A2FA7BE4B8A8A48F5 "点击放大")图标**，**选择**管理配置**进入配置管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/zVNbEhbqQte9f9M5FPLFYQ/zh-cn_image_0000002820681103.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=3383DD787CA7F12B35B7E23DA0D65A847B3EA02F43D73A3D11F412CB8D8374FD "点击放大")
2. 在**管理配置**界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/JhE6UK6YTu2HVfuT0YvtwQ/zh-cn_image_0000002820721113.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FCCB05B17ECF6EBDD09F48F3653375F34FF3537FF01AC3EE0B4D3425FCD2FA5 "点击放大")按钮，在弹出的下拉菜单中，点击**Test**，输入名称后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/4hnAvWDGTgOBoQPuiJVXyw/zh-cn_image_0000002820721107.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABBCD8AFC1606D3E2849A785C67D86867571791BDA57FFC1982A6373EA45BEEC)图标打开配置面板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/10R0e5lOTz2iAtFJJh0nxQ/zh-cn_image_0000002792001142.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5203937654B72B7671216D9147038C67C9B0CF4B2A8DE374CCC988C94320906 "点击放大")
3. 根据实际情况，配置Instrument Test的运行参数。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选**自动依赖**，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选**Only OhosTest Package**，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/KfYHfVSaQKyZ5-eYLeA1HA/zh-cn_image_0000002792001160.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=467A4104A50351491B4E022A9A9F9CB2092903BC215BE75589ED852291B0A577 "点击放大")

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/XuCgN9_9RZihQY3duzvoVw/zh-cn_image_0000002792001156.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=958145C5FD99AC9E45F76F9C209565BB1280AAD98F5C7478FAF49529CBA25DB5 "点击放大")
2. 打开**运行/调试配置**窗口，在**Test Args**输入框中添加测试参数。例如将测试参数配置为level=1; size=medium。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/COpEoN5PSRyHPzFnnr6NSA/zh-cn_image_0000002792001152.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F627507C3849F6FC773FCA8EE092DF20AC0018DAB8CA7AA21972411888B9735 "点击放大")

   **表1** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/yjluhnM_QheHI1gRzV9YaQ/zh-cn_image_0000002820721115.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEF46E4E4ABA4DF73E37AC2E3A0DF7D8252F51C556C8A111884AFEBF7D68844A "点击放大")

### 设置调试代码类型

打开**测试配置**窗口，点击**调试器**页签，设置调试类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UdkPwe9rSO2_cVEZwJEkJQ/zh-cn_image_0000002791841186.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=04BE179D987BB13926204B9C0244E6255A8C0A117295F669FDF99824F4A4708D "点击放大")

调试类型默认为Detect Automatically，关于各调试类型的说明如下表所示：

| 调试类型 | 调试代码 |
| --- | --- |
| **Detect Automatically** | 新建工程默认调试器选项。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 |
| **ArkTS/JS** | * 调试ArkTS代码 * 调试JS代码 |
| **Native** | 仅调试C/C++代码 |
| **Dual(ArkTS/JS + Native)** | 调试C/C++工程的ArkTS/JS和C/C++代码 |

**说明** 

调试C++代码时，当前模块及所有依赖的HSP模块的[Address Sanitizer配置](ide-hmos-instrument-test.md#section8352185341915)要保持一致，若不一致，可能无法进入C++代码的断点处。

### ASan检测

Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](ide-hmos-asan.md)，当前不支持JS语言。

1. 在运行/调试配置窗口，选择对应的Instrument Test，点击**诊断**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/WN4XELo2T7iT3CMBz5hmbA/zh-cn_image_0000002820681119.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D19D31A684280C5618BB3175DAFDD2799AADF2D005144757F691B2C7816E7B5 "点击放大")
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/lk3vD-z6SeCpJkPS35Fn8Q/zh-cn_image_0000002820721127.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D9A808692B1E8AC8042E06A9D5EC71EB41FC81771BBEFB802E01F83678D991D "点击放大")
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ygHoXNlFSrKjfuGc6NtBQQ/zh-cn_image_0000002820721131.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAF2314115E98C7686A8E4C0E866A065E1928B66CB866CE7A7BA42220DC89726 "点击放大")
