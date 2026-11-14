---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-instrument-test
title: 仪器测试（Instrument Test）
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 开发自测试 > 仪器测试（Instrument Test）
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b0fe708b26b35dc475b4cfc202ff37ca95981cb360a134efcad63361a751bfbd
---

鸿蒙电脑DevEco Studio支持应用/元服务测试框架，提供测试用例执行能力，提供用例编写基础接口，输出测试结果，支持用户开发简洁易用的自动化测试脚本，支持代码覆盖率统计。当前支持Instrument Test，测试用例存放在ohosTest测试目录下，需要运行在设备上。Instrument Test支持ArkTS/JS语言。

**说明** 

覆盖率测试不支持开启混淆。

## 创建ArkTS测试用例

1. 手动在**ohosTest** > **ets** > **test**文件夹下创建测试文件，文件名以.test.ets结尾，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](arkxtest-guidelines.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/H9hkKqv5T7KYCwhnCIXcBQ/zh-cn_image_0000002781471280.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C5673D102FF53D0218849BFDD2F8564E5770A71AD570D63F9C6ED0E69AE9AD3 "点击放大")
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/SLwchV7SRmCLx9HJcudv5w/zh-cn_image_0000002810630815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=F830614B8CB3A4B39E959045BABBF8CA4BC097273C3D0E0D4F132726C7A43F11 "点击放大")
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/PBugHg31Q3ydq34FcHabbQ/zh-cn_image_0000002810750921.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=206D0CB33091922F349E995D583A12F4E2880C5E418309ADC6B901A5A0EF8AD7 "点击放大")
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-hmos-instrument-test.md#section1631610401035)后，点击DevEco Studio的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/lI7pwyCTThemGZ7Xgws6XA/zh-cn_image_0000002781471276.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=C91A12CC49FF203C8C6EBFC630AD5C00A36F88CE0CA5351C3DF6D0AADD596AC0 "点击放大")图标选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/XQwmgbegQP2OlOkP9SaWcw/zh-cn_image_0000002781471282.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB6E2D73CCAAE0BEE232CA4CD3706B405C26EE9EF141CAC6DFD3AF9FF7B33717 "点击放大")按钮执行Instrument Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/78TF2xnCQa-MXv01GpHshg/zh-cn_image_0000002810750939.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=802C301A57EDE454EE4DB3424A0F608611202BCCFBA9F1667C2588CC20AAC3EA "点击放大")

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/GMNCOsB3TRyE9iqRNQEJnQ/zh-cn_image_0000002781471260.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=66BE36155D3DE9D39959299529995186E706D530E4635E95EAA7BD8132E81134 "点击放大")

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 调试 '测试文件名称'**，以调试模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/M_IpQBwLSwOqxzheQxJKBQ/zh-cn_image_0000002810630809.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=71F3C1CEC508B5629EDB7361CAD323D12ADF258738253F43AA684A9AF6FEE673 "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/yjbJ5qtKRICsn_4z6625Fw/zh-cn_image_0000002781311348.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDDDB1381D192607EAFF028C135F73F45EF1C6B8498293FF2C7FA968D447C5B1)图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/0EUVpTjmTDKHHrO-BiwmaA/zh-cn_image_0000002810750919.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F73DAA297AD7FF7EF3699AD9A3D863626E2E2E71D2248DF061FD50D90F195CE)

在断点命中时，下方将出现调试器窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/wOymraUkQYWRrd3qVYixkw/zh-cn_image_0000002781311322.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD0C6E6BE5C37166C982D181D573BC700B4B47F70B1DA7E25BD7A99B240F6FF1 "点击放大")

断点命中时，在调试窗口中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/CUtiWiQmQL-UN1lCh1xuyw/zh-cn_image_0000002781471272.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AB7344BB53BEDF1CF89130D251A764CAE137399187A487D1885B8B35A8EB03D "点击放大")

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/CiY3mxUvSbO2QaHr-EcHdA/zh-cn_image_0000002781311332.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EB1ED741E5C6003D6D55467988CAEA0BB8725328342F66600C96402DD596810 "点击放大")

**说明** 

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-hmos-instrument-test.md#section386512457406)。

### 覆盖率统计模式

**说明** 

源码文件的命名不可为“test.ets”、“xx.test.ets”、“test.ts”和“xx.test.ts”，该命名的文件不会生成报告。

在Instrument Test运行的基础上支持代码覆盖率统计。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 使用覆盖率运行 '测试文件名称'** ，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/KdDTcJy0SwOQ5eDsWrsWsQ/zh-cn_image_0000002810750923.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=B127AE53D0424F7BA5F2D3A876B0CCE9F8E167D113C16FFA2E40AEFAF04BB764 "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/22v2OKItRV6jLjjEXd4-lQ/zh-cn_image_0000002781311346.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9670BA7D7B4765DFD00B37B7448C4DB042287952E281BB70F1C55971F21B9D9 "点击放大")图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/o37IKFzbReeQeD6lYtC1mA/zh-cn_image_0000002781311336.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=63A7E3CBE9D898852CC68EADD350EA1715114FE2D94959B054EB5EFA22D1A2C9)

启动测试后，进行编译构建，构建结束后自动拉起测试窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/vEH_FsTaREiUGybyEuX7Ag/zh-cn_image_0000002781311344.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AF85692CD257F54DF8B76093FDE2E9FFB502653BB69EA74E8042314467C4C88 "点击放大")

在本地找到报告后鼠标右键快速查看，打开报告，查看ArkTS代码覆盖率详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/1_ZPqGHBQjaAU9EU4gX4dQ/zh-cn_image_0000002781311334.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F80D5FFE4F1A9BB68C8EB6D729AED9AFDF9E876EA578F9A454428046821E2B7 "点击放大")

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 点击编辑器顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/IB4DnJ6NRKqJh7MDINiQFw/zh-cn_image_0000002810750915.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=E456B9E53F3360ED50014C60B536BF1C551D41D73871296927620845D9E8474F "点击放大")图标**，**选择**管理配置**进入配置管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/dY3o8A3NT5SNvmVP-njLTA/zh-cn_image_0000002781311338.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A3D82456D465331FC33E532AEC53FA1425641E8B37F6D16262149618EC47BD1 "点击放大")
2. 在**管理配置**界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/oH9dNytETgWhHGqeIuOvCA/zh-cn_image_0000002810630813.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC6F94CEC0169FA07D439948887B8FDBC77D5C6BBBF586F96CD06333AF4A172 "点击放大")按钮，在弹出的下拉菜单中，点击**Test**，输入名称后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/-9QoURsxSheAD_w5qgXepQ/zh-cn_image_0000002810750931.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=F68B2D0D4B1D9FA12445BE7D5DD9D6F47890B4B25EEDC68B63DA50889FDF2E1C)图标打开配置面板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/kvF57O7BQ0iz6kyWUPYCnA/zh-cn_image_0000002810630817.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E9F6E1AD948DF659FE476166E7183BE16698557486EC1A22E53E55AE2EDFC20 "点击放大")
3. 根据实际情况，配置Instrument Test的运行参数。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选**自动依赖**，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选**Only OhosTest Package**，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/sy_IA_NyR4-iUjPWK9FuVg/zh-cn_image_0000002810750927.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A7C3D5AC9D031D43FB2839E1DD6EDBBB6C9B9475144C71A14331F14A62E1D55 "点击放大")

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/9sZ97CzJRz222A3pW4Iw0A/zh-cn_image_0000002781311324.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA86135CCBBC5ABEFBE6A11927577C0B8A126968B081347BBAB0D9F2E9FCF9FA "点击放大")
2. 打开**运行/调试配置**窗口，在**Test Args**输入框中添加测试参数。例如将测试参数配置为level=1; size=medium。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LlxQQdFSSQeZahhbSvKYNA/zh-cn_image_0000002781471270.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=647F012850071C203BA98392F6FA3C11AF57FB739532935BD5444A793F20C19A "点击放大")

   **表1** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/y52BZkd0QA6uZ0st1RxWSQ/zh-cn_image_0000002810750917.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=B596F57F9EEC2C89F8074FF6FA7FD9E6FAC383A4E21C002027E07306048FE092 "点击放大")

### 设置调试代码类型

打开**测试配置**窗口，点击**调试器**页签，设置调试类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/dCYS3gIoSO2U8nu1i9-RNA/zh-cn_image_0000002810750925.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=E70DE7102D864304329535687A9F40F6A95E3836A537483BDF8B4106BCEAE499 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/KbeyCNJMRo6wcyD-DrWiVQ/zh-cn_image_0000002810630827.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=18D432835805F669442CFE3B3463394D4E71E51A7D4BFC31435E5170BEF781F9 "点击放大")
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/S2o2BEkNRR6dMqS41F9nbw/zh-cn_image_0000002810630821.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=27CF525D3D903F5569B4E8279AE0D54323D4A8F0738E2886166FAAEFFA35C54D "点击放大")
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/AcQsfArZQX2t50gk0F24yw/zh-cn_image_0000002781471284.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=C560751F3B6967F3B3A241CB53225945A51D921486517E3022F5B90BEB111D4E "点击放大")
