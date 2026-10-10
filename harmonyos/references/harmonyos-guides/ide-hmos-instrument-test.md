---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-instrument-test
title: 仪器测试（Instrument Test）
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 开发自测试 > 仪器测试（Instrument Test）
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8366e71e654bc56b608f2c42d0f1e8c39391c62cd22cc495bd0256330d9b66fa
---

鸿蒙电脑DevEco Studio支持应用/元服务测试框架，提供测试用例执行能力，提供用例编写基础接口，输出测试结果，支持用户开发简洁易用的自动化测试脚本，支持代码覆盖率统计。当前支持Instrument Test，测试用例存放在ohosTest测试目录下，需要运行在设备上。Instrument Test支持ArkTS/JS语言。

**说明** 

覆盖率测试不支持开启混淆。

## 创建ArkTS测试用例

1. 手动在**ohosTest** > **ets** > **test**文件夹下创建测试文件，文件名以.test.ets结尾，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](arkxtest-guidelines.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/zyuyIdiWRNufJ1Odg6m97A/zh-cn_image_0000002750169796.jpg "点击放大")
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/a3w6vnykTlawk2gleFChFw/zh-cn_image_0000002750009890.png "点击放大")
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/GN07a0uvSoS-EyOQL-xfHg/zh-cn_image_0000002750169784.png "点击放大")
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-hmos-instrument-test.md#section1631610401035)后，点击DevEco Studio的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/rZbOuX1LR0Osd5qkgPbxHQ/zh-cn_image_0000002750009900.jpg "点击放大")图标选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/s6pvifP4QJKDJipgz6-3HQ/zh-cn_image_0000002779728965.jpg "点击放大")按钮执行Instrument Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/hj-DMzMIRBuF2Ge1Lc09sA/zh-cn_image_0000002779728963.png "点击放大")

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/KUJlbU9nSnGFLcpSkCM9_A/zh-cn_image_0000002779728951.png "点击放大")

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 调试 '测试文件名称'**，以调试模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/lzia1fgxRyaksC4yTKz66Q/zh-cn_image_0000002779608803.png "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/EO1zV9j_Rxmx-TOrfLtqfA/zh-cn_image_0000002779608819.png)图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/M7e-674hTU2gKiNr_PS3aQ/zh-cn_image_0000002750009888.png)

在断点命中时，下方将出现调试器窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/x4r9b0NYRUyIybv4fuGv4A/zh-cn_image_0000002750009886.jpg "点击放大")

断点命中时，在调试窗口中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/D4n6ZJuRTo6nggmSpp52-w/zh-cn_image_0000002779728961.jpg "点击放大")

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/mp1GajjwT8-Ze0eUqsR2Tw/zh-cn_image_0000002750169788.png "点击放大")

**说明** 

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-hmos-instrument-test.md#section386512457406)。

### 覆盖率统计模式

**说明** 

源码文件的命名不可为“test.ets”、“xx.test.ets”、“test.ts”和“xx.test.ts”，该命名的文件不会生成报告。

在Instrument Test运行的基础上支持代码覆盖率统计。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 使用覆盖率运行 '测试文件名称'** ，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/AqnBEduPTF6GGx_I7MDfgw/zh-cn_image_0000002779608807.png "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/dvzAfekHQfq06-X1GxkSNw/zh-cn_image_0000002750009902.jpg "点击放大")图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/TusMAND0QXmJmslixnOvPg/zh-cn_image_0000002750009898.png)

启动测试后，进行编译构建，构建结束后自动拉起测试窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/dIFuQ0ntTmiOT2XGCwNYQA/zh-cn_image_0000002779608817.png "点击放大")

在本地找到报告后鼠标右键快速查看，打开报告，查看ArkTS代码覆盖率详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/8S-yxvW_RSS58JFeKZymyQ/zh-cn_image_0000002779728959.png "点击放大")

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 点击编辑器顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/eLZyf2viSjeQDsBc89BQCQ/zh-cn_image_0000002750169780.jpg "点击放大")图标**，**选择**管理配置**进入配置管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/5RC34LgOQkCFcs-1PI9NkQ/zh-cn_image_0000002779608815.png "点击放大")
2. 在**管理配置**界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/sztk9eSkTLOaa4eMakAT6w/zh-cn_image_0000002779608805.jpg "点击放大")按钮，在弹出的下拉菜单中，点击**Test**，输入名称后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/wqS_mBz0Q7WeOuY9f_4faA/zh-cn_image_0000002779608813.png)图标打开配置面板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/HFHa1LtzTS2kLuUYUbee1w/zh-cn_image_0000002750009892.jpg "点击放大")
3. 根据实际情况，配置Instrument Test的运行参数。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选**自动依赖**，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选**Only OhosTest Package**，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Gt1-0RQsTXuylJz-Dpa7Og/zh-cn_image_0000002779608811.png "点击放大")

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/yL_QoJ8NTPG6yMZllyhekQ/zh-cn_image_0000002750169782.png "点击放大")
2. 打开**运行/调试配置**窗口，在**Test Args**输入框中添加测试参数。例如将测试参数配置为level=1; size=medium。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/BNWfVu36SJG6uJvTuL1vTA/zh-cn_image_0000002750169792.png "点击放大")

   **表1** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/OXtv8QJrRASw5lWnzPwKLw/zh-cn_image_0000002779728949.png "点击放大")

### 设置调试代码类型

打开**测试配置**窗口，点击**调试器**页签，设置调试类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/qYchpUYiRQau67vwqQyJmA/zh-cn_image_0000002779608809.png "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/owcZpcRfQci53nipWa8lZw/zh-cn_image_0000002750169794.png "点击放大")
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/WthFgsiZQ7irtNtV9N0bcg/zh-cn_image_0000002750009896.png "点击放大")
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/3EL8P7oRQdONAnnCiNUpOg/zh-cn_image_0000002750169798.png "点击放大")
