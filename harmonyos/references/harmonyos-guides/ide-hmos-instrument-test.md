---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-instrument-test
title: 仪器测试（Instrument Test）
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 开发自测试 > 仪器测试（Instrument Test）
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:56+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eddc5a4d29f86cdf27d1706ee0626a04cae5b4c2a40c0ba57c7c9b31957c2171
---

鸿蒙电脑DevEco Studio支持应用/元服务测试框架，提供测试用例执行能力，提供用例编写基础接口，输出测试结果，支持用户开发简洁易用的自动化测试脚本，支持代码覆盖率统计。当前支持Instrument Test，测试用例存放在ohosTest测试目录下，需要运行在设备上。Instrument Test支持ArkTS/JS语言。

**说明** 

覆盖率测试不支持开启混淆。

## 创建ArkTS测试用例

1. 手动在**ohosTest** > **ets** > **test**文件夹下创建测试文件，文件名以.test.ets结尾，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](arkxtest-guidelines.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/977RTLjxTba71XZtqMHqoQ/zh-cn_image_0000002792001162.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A7C7C5E579C2AFAE4DEE60A0341382A741793C95796021AE122891EBDA513C1 "点击放大")
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/fxFgNhVNRXaGUtxjFFcyug/zh-cn_image_0000002792001144.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=649169331556B9081F3745ADF73BC1466744ADEEF7F9F59F22A7EFCDB39B1D07 "点击放大")
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Z8OII7JzSxuf9bJ6rtqI7w/zh-cn_image_0000002792001154.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD23A21D948E010541371AE8852AEDB935BA68E45C2ECC64BB0C5F05537679CC "点击放大")
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-hmos-instrument-test.md#section1631610401035)后，点击DevEco Studio的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/cNjcH0W5SAGhx0gVoU13gA/zh-cn_image_0000002820721117.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA3CBDA775CE80B8FE1000465F56FE372B35923DF19871827072E045AA39B5E4 "点击放大")图标选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/5Llx4x_ETeCkvkB8EjSKRg/zh-cn_image_0000002820721129.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAB695AF76AC725D6B8E6E6C64327CCA85115CA460AF02EDA134C387E29B1734 "点击放大")按钮执行Instrument Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/gbpO0ZnjRf6m-ef9exK-8A/zh-cn_image_0000002792001148.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9FE9F16587E8AFD1D3A1DB0F551C77E239166305A75199BAA8473AAB4FA9EF0 "点击放大")

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/vRdjtkDSTsisMK0hiCgg3Q/zh-cn_image_0000002792001164.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=031D9A6112EA21D1FD8023F08879BC17CF6902B864D6287A5B3E12625F337685 "点击放大")

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 调试 '测试文件名称'**，以调试模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/YrEaajGaSY62WUH0kncE5w/zh-cn_image_0000002791841180.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=231722B6FAEA948190C56CEF4DBB904DF86500C978CAAB497E2A5B490CE5BEE2 "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vumyn1THROmDacS6RTXToA/zh-cn_image_0000002820681117.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=17DCB617187447C06298D5B493150CBA2996DD8929E9AC338063E1CF2A600892)图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/1c2IkT7FR3SIIFNEoZV8cA/zh-cn_image_0000002792001150.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=B09F120D7348506618547315845820A335805F9A40A8C7F665C735535BA52B08)

在断点命中时，下方将出现调试器窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/V2kOwbCSQZuYhdYl59JziA/zh-cn_image_0000002820721123.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F645DF956BE0F2F714DBA9A0C974FDEDCE1FF4F08B189572AEFDD151403D78E "点击放大")

断点命中时，在调试窗口中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Xs2ApYDTRdGtED5IB0eQ7Q/zh-cn_image_0000002820721119.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=A030477DC34057DE0DD5D58775D9A73CBE31DD43B5502FB2D50D865FDD76FE97 "点击放大")

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/FNGtarpJRGOzx66LiMZosQ/zh-cn_image_0000002820721111.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D26EC398F187BCDC2A06E2FE46AD31044285DBE7D416FBA3C8392BB1B204A4E "点击放大")

**说明** 

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-hmos-instrument-test.md#section386512457406)。

### 覆盖率统计模式

**说明** 

源码文件的命名不可为“test.ets”、“xx.test.ets”、“test.ts”和“xx.test.ts”，该命名的文件不会生成报告。

在Instrument Test运行的基础上支持代码覆盖率统计。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > 使用覆盖率运行 '测试文件名称'** ，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/TtF-G53dQ02g4xtBd2qvsw/zh-cn_image_0000002820721121.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C1027362CD8E2823FBE6F7634F4E2A8BE1928DFEFB9CBD786B987B6C99C7D29 "点击放大")
* 方式二：点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/0FzFrqD5Qz-JBDseZZKflA/zh-cn_image_0000002791841182.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=70602D4CA65AC42D4D785BCEDDB548F018C2E2FBC9698BDD1F236CCC258DFC39 "点击放大")图标执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/s-QjudIURjqAs5LOZdBFhA/zh-cn_image_0000002791841168.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=F04C19F88E605A148DE0008851A777989A467FE02BCACBCB58322485D2AA730A)

启动测试后，进行编译构建，构建结束后自动拉起测试窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/SEIRd2QvT82W36a9fZYI8g/zh-cn_image_0000002820681121.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A3D6E27B8F7B067F2A091C40D25F0CB11873A39D4F7F75A6F7BADA39D036031 "点击放大")

在本地找到报告后鼠标右键快速查看，打开报告，查看ArkTS代码覆盖率详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/c6m3QV2XQ2qbIztd7Sllig/zh-cn_image_0000002820721109.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=87152658AEDFE0AFC8B809428DF068CC10859338471EFCF30779B9683D8F82C7 "点击放大")

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 点击编辑器顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/H30A7dsGSgWRgnw2CvnUbw/zh-cn_image_0000002792001146.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=11D8E266C7FBD4CE58CA5C8D7DA316D57999D40B0CE7FF89AD9483512EC25459 "点击放大")图标**，**选择**管理配置**进入配置管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/eBjqD2OTSqyyYidV3u0kOg/zh-cn_image_0000002820681103.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=3270D0E8493FE82E5E584BBF37CB3482296E9CC428830B24C3B38C788FEB58BC "点击放大")
2. 在**管理配置**界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/-McEoHNTRPe7E4KlWAyF6A/zh-cn_image_0000002820721113.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=A460D49836D4E4FA62660EB131FDE63B144B7824EF1B41EFDFF5F77583D18A45 "点击放大")按钮，在弹出的下拉菜单中，点击**Test**，输入名称后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/D7WNUT7PQvSVUdIyLUHloA/zh-cn_image_0000002820721107.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA1CF120E61A5BEEBA2A9DEE21A1590E5E713C621C34EC34F689740692B49AD2)图标打开配置面板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/L4q4qE4bRK-INUc3LcYnRg/zh-cn_image_0000002792001142.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B2C48DC3E996BC147F3CD9A1ADA2CB9B214D522557A9842419A777CF2A30B6A "点击放大")
3. 根据实际情况，配置Instrument Test的运行参数。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选**保留应用数据**，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选**自动依赖**，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选**Only OhosTest Package**，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/K8tpDGkVSnSzPB0NG2Vu8w/zh-cn_image_0000002792001160.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=A089950F744550A734C85C7C5681356023CFA3E5C3CC69D479E41CD006357BB3 "点击放大")

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/MYcVAi4SRH6nqsn5H3oLwg/zh-cn_image_0000002792001156.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=23F90E6159B12048198A71F3B08EE337262A0B42533C23768297586383FC4949 "点击放大")
2. 打开**运行/调试配置**窗口，在**Test Args**输入框中添加测试参数。例如将测试参数配置为level=1; size=medium。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/6_-xusIGQ5aBAyjvpAFoNg/zh-cn_image_0000002792001152.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=66FCC7BC8948815B130498DC116AD07BA99DBF2AAEA5BDD315E7AC71258BB514 "点击放大")

   **表1** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/JinTyFqqRzuo7I7Bioaj7g/zh-cn_image_0000002820721115.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=909BAFAF2EF9BFF095D501F57CA0247447F599A7CF763412B9C6701470D89043 "点击放大")

### 设置调试代码类型

打开**测试配置**窗口，点击**调试器**页签，设置调试类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/-mie8BPmT-ysIYJkg46JmQ/zh-cn_image_0000002791841186.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA77AC8950029BF4B79CA6399822E193E390A77604F599ED730419A3CA3A5525 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/KLQN3WzrTeu29MIZ8gC0hg/zh-cn_image_0000002820681119.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6257ADF08C993F0E0BF5888B5FE5AB3374975C7F0AA5E4B731D9AD9D9E0101C "点击放大")
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/_1GoUM9LRa-gqVw5yab2tw/zh-cn_image_0000002820721127.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E2DF5530E7B232E140B7D642F2F8FAEFDB24D2B51952923E8458C3B13DEEDFF "点击放大")
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/g1Qx_mNITJWGF6bEU2OTLw/zh-cn_image_0000002820721131.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F499106EBEF24D41CA5BDB0B3F3FCACD96AC1997EAEC8C8A88B5C5CAAB3FB62 "点击放大")
