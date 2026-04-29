---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test
title: Instrument Test
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > Instrument Test
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3638d5b920fc7d7280e94e836417daf69d7dafe47f18ba45c8f83b146a55b97
---

## 创建ArkTS测试用例

### 创建默认测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Instrument Test**或快捷键**Alt+Enter** **（macOS为Option+Enter）> Create Instrument Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/V8ccGOKbTVeRYOFxWS13Ow/zh-cn_image_0000002561753237.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=39078BFBFB0B2D25042AF57F7649D50933D8AC1327E5A7CD07DF48A3C3323F40)
2. 在弹出的Create Instrument Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit，JS语言默认为DECC-JSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/eyc60ZQWREW99mogGuIH3w/zh-cn_image_0000002561833197.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=637184F3D073796E125042F46E03A98F7531C2B485B4B13CEF428DEB981AE6A5)
3. DevEco Studio在ohosTest/ets/test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](arkxtest-guidelines.md)。

   说明

   * 您也可以手动在ohosTest > ets > test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾，否则将在运行时弹窗提示“Error: Test files must end with '.test.ets'.”请点击**Fix**按钮，DevEco Studio将自动对ohosTest > ets > test目录下的文件名进行修改。
   * 首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UiTest测试能力。

### 自定义Ability和Resources

从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。

说明

如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。

**表1** **新旧版本ohosTest目录对比**

|  |  |
| --- | --- |
| **新版本** | **历史版本** |
|  |  |

1. 创建以下目录或文件，文件内容示例可在[运行Instrument Test测试用例](ide-instrument-test.md#section1574003717165)后，在对应模块的.test/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1及以上版本）或build/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1以下版本）下查看，其中productName是当前生效的product，可以通过点击DevEco Studio右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/V2WTSIfBT8O3W1Q-_HMS_Q/zh-cn_image_0000002561753229.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=9C0CCB6C628979B4DFB4EDE92A3930F26E7FC3AE4B0996D03687F4A4C6C86CB2)图标进行查看。
   * testability目录 > TestAbility.ets文件
   * testability目录 > pages目录 > Index.ets文件
   * testrunner目录 > OpenHarmonyTestRunner.ets文件
   * resources目录 > base目录 > element目录 > color.json文件
   * resources目录 > base目录 > element目录 > string.json文件
   * resources目录 > base目录 > profile目录 > test\_pages.json文件
2. 在module.json5文件中补充ability配置字段mainElement、pages、abilities，关于字段的具体说明请参考[module.json5配置文件](module-configuration-file.md)。

   ```
   1. {
   2. "module": {
   3. "name": "entry_test",
   4. "type": "feature",
   5. "description": "$string:module_test_desc",
   6. "mainElement": "TestAbility",                                   // 对应下方abilities中的ability name。
   7. "deviceTypes": [
   8. "phone",
   9. "tablet",
   10. "2in1"
   11. ],
   12. "deliveryWithInstall": true,
   13. "installationFree": false,
   14. "pages": "$profile:test_pages",                                 // 对应resources目录 > base目录 > profile目录 > test_pages.json文件。
   15. "abilities": [                                                  // 添加的ability的配置信息。
   16. {
   17. "name": "TestAbility",
   18. "srcEntry": "./ets/testability/TestAbility.ets",
   19. "description": "$string:TestAbility_desc",
   20. "icon": "$media:icon",    // 确保引用的资源都存在
   21. "label": "$string:TestAbility_label",
   22. "exported": true,
   23. "startWindowIcon": "$media:icon",
   24. "startWindowBackground": "$color:start_window_background"
   25. }
   26. ]
   27. }
   28. }
   ```

## 运行测试用例

### 运行模式

使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考[使用本地真机运行应用](ide-run-device.md)或[使用模拟器运行应用](ide-run-emulator.md)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：

* 在工程目录中，单击**右键 > Run'测试文件名称'**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/dTifN1D_TiSmNk5Zw7AFUQ/zh-cn_image_0000002561753243.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=82C38A33E0AA358294B22E9F6CA10A849BC31F54DF33A2A6527B02A96DF1889F)
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/nirvPpS1SHSv7rb50_fWmQ/zh-cn_image_0000002561833189.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=C58156C04D41F28D5C0E74A7A44931EB664F9217A204E2738EE3D63F8D68E594)
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-instrument-test.md#section65264166107)后，通过如下方式的其中之一，执行Instrument Test：
  + 在工具栏主菜单单击**Run > Run'测试名称'**。
  + 在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Skw6wyrfSmuZ9yNOS1LCPA/zh-cn_image_0000002561833183.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=96492197575A45108435D8B9A88C7D649FF0BE4EC2235951226BCB696E08B8DD)按钮，执行Instrument Test。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/AkesYuarTMumhxLHT9s4GA/zh-cn_image_0000002530913302.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=A107FB13F87CC06061ED0F0E8B3EF001E89C6F9D151CBD5E13A30348CCA21FEC)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/I11e8iYiTWe_BLTeyueWPw/zh-cn_image_0000002530913296.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=95613DB78A174728953C7D743BD65A3845923B47262987C178A657693C973050)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/K9dtO0N2Qh2g-OenW-KEDQ/zh-cn_image_0000002530753298.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=7D5BD8063DFD3F5A526D1BDC03FBE3D4301B2D61D5A7F3342C7BB65E973207DD)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/oToPJuuHSPycGTe6nGVF8A/zh-cn_image_0000002561833191.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=524438FEBCE993D37D6AA5C0539572D98674C1B528E0D393BA18E8519F265AA6)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/zofwtpaXRjqLzYRtaMZawg/zh-cn_image_0000002530753322.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=56B95A975D3BFD2CCDED2A01D3AFE54BFBFD682F4D0B1B1DFA2A36BA0BAA09C9)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/fbKvUMY_TV2tZxp1FT3yLw/zh-cn_image_0000002561833251.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=A418772DF1B57982DC53B4CB4B334806C2C95748FB3242BE210B506C16446C7D)

说明

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-instrument-test.md#section0164586312)。

### 覆盖率统计模式

在Instrument Test运行的基础上支持代码覆盖率统计。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](ide-ui-test.md#section13756446154)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/mg4QTHRmTBipmtmO1v62iw/zh-cn_image_0000002561833187.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=6C16691FE115F2714CB8D1979B258084E149B4BFAE809B74AFF8C8092CB8A5BE)
* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/CCg_KLGQRLaRtOCKex972g/zh-cn_image_0000002561753249.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=E0583C2D17D53A8155872D4472B626EC6FFF77BEB4ACE5EA77EBE182C75B951B)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Gee9lvZ0RQKfkPC1bI19VQ/zh-cn_image_0000002530753328.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=CBDEF84B9AA9588BC356C166590FE7EF4331C894845CC0429B3AC4A49DAB7851)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/kJUhDTNqS52oiCkUih49jg/zh-cn_image_0000002530913262.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=BA1B492D01841B0915C011769C2A91CE9A26064143CB01B3F4271CC604792F14)

点击链接可打开报告，查看ArkTS代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/cXoj8L8HQZmAdIsQt2VlkA/zh-cn_image_0000002561833207.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=772C0FAAE30C0AA138DB801600E846A966ABD7A5017C8C1F4A003FB4E8066CFC)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/AR0i9_VTSzmbkhbzEAWvtA/zh-cn_image_0000002530913260.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=8A933582663CADD64A8FAB33DC080C231D34135A198CDAC9E6C3BC1DEB8A2A76)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run** > **Edit Configurations**进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击+按钮，在弹出的下拉菜单中，单击Instrument Test。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/xD73cLWsSJqADWGgA0e7MA/zh-cn_image_0000002561833203.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=D7F6394014276BCCE92E6847A27B9D427C411B4FD7A9AA11937D4BEA6564023C)
3. 根据实际情况，配置Instrument Test的运行参数。然后单击**OK**，完成配置。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选“**Keep Application Data**”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选“**Auto Dependencies**”，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选“**Only OhosTest Package**”，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/2ObF-0cxRUi0L5H54rrdWg/zh-cn_image_0000002561753275.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=073C18208114C0F1D89D5E7AC61C757C10816566B04793202CA20D568D97D9DF)

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/2zKhnYoeR5OB7Z6YhnXx-w/zh-cn_image_0000002561833199.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=C15385124BCEE70C85048D128222CBDBAD73E199A0A47BFCD4556FEE21A5FD95)
2. 打开**Run/Debug Configurations**窗口，点击Test Args![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/YqhFV4VJSIi0BCmnjQxNRg/zh-cn_image_0000002530753318.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=52F10ECECBBE2B1135C0C691207A4F52C89BFEDA2394A02D2D98383F0B412FEB)，打开**Test Args**界面，添加命令行参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/8G0avxnoRtamA_YcS142Jw/zh-cn_image_0000002530753288.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=9482EC7AB25EB3CA6629232A32C7474907C74109ADAFB368E2BF7E48D90A4EB1)

   例如将测试参数配置为level=1, size=medium

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IMAMGCUTSs6iAf2Fo5vj2A/zh-cn_image_0000002530913276.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=81D0186ED4751B568CB6837D2389E3885562C589A4926D1C4BC4837465A8593D)

   **表2** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/dhLrI8goQnCz3zj73klTkg/zh-cn_image_0000002530753314.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=CF1BF9296223C90BDB88BEFAB132F3CB7DFAC5B07AD963D333D65596CED53779)

### 设置调试代码类型

点击**Run > Edit Configurations**，打开**Run/Debug Configurations**窗口，选择Instrument Test，点击**Debugger**页签，设置Debug type。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Ge_YZQUqQBKHT0Ne7PLEdg/zh-cn_image_0000002530913318.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=C9A54911F217A5158DF06A425BBB7C62D402FF624DD8244F97EE4D30CFCE05F9)

调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：

| 调试类型 | 调试代码 |
| --- | --- |
| Detect Automatically | 自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。  如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。 |
| ArkTS/JS | 只调试ArkTS/JS，只出现PandaDebugger调试窗口。 |
| Native | 单独调试C++，只出现Native调试窗口。 |
| Dual(ArkTS/JS + Native) | 支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。 |

说明

调试C++代码时，当前模块及所有依赖的HSP模块的[Address Sanitizer配置](ide-instrument-test.md#section8352185341915)要保持一致，若不一致，可能无法进入C++代码的断点处。

### ASan检测

Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](ide-asan.md)，当前不支持JS语言。

1. 在运行/调试配置窗口，选择对应的Instrument Test，点击**Diagnostics**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/1aQCu1LpSjKk9oHrWGAy1Q/zh-cn_image_0000002561753267.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=E0CB22CEE7CBA74988E51A283A7153982B02C6B86ADB52D31D926C137E5E3572)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Afk7RIFYRtKKrgzsyJVuHQ/zh-cn_image_0000002530913320.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=E4740F31B00E0EEDC6821D320B20056629A9E2596A5D2D76E06DCE7DEFA6D142)
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/iSu88a_wSgG7Fzvn6Q_0kg/zh-cn_image_0000002561753273.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=1CB2520DDF958C55ABE1519A116A47E9DEA26EF2D0C72F3EB91C38F76EEA5A4A)

## 测试C++代码

从DevEco Studio 6.0.0 Beta5版本开始，支持对C++代码进行测试，包括运行/调试C++测试代码、对C++代码进行覆盖率统计。

由于C++的测试so无法直接在设备上运行，需要通过Node-API的方式拉起，即通过ArkTS/JS语言拉起C/C++测试用例。

### 运行C++测试代码

1. 创建cpp测试目录，鼠标右键单击ohosTest目录，选择**New > C/C++ File(Napi)**，在ohosTest下生成cpp测试目录，以entry模块为例，目录结构如下。
   * **src > ohosTest > cpp > types**：用于存放C++的API接口描述文件。
   * **src > ohosTest > cpp > types** **> libentry\_test > index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。
   * **src > ohosTest > cpp > types** **> libentry\_test > oh-package.json5**：配置.so三方包声明文件的入口及包名。
   * **src > ohosTest > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
   * **src > ohosTest > cpp > napi\_init.cpp：**定义C++ API接口的文件**。**

   说明

   DevEco Studio生成的cpp测试目录中不包含C++测试框架，需要开发者自行选择开源测试框架使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/MyXXprD0RGyplAhPijJXvA/zh-cn_image_0000002561753213.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=9286F7BF65C6586F7FFE8EE360D7DA27FA11A803828172BF36E8233A7C9AF674)
2. 通过ArkTS测试用例拉起C++测试，示例如下。

   ```
   1. // ArkTS测试文件Ability.test.ets
   2. import entryTest from 'libentry_test.so';
   3. export default function abilityTest() {
   4. describe('ActsAbilityTest', () => {
   5. ...
   6. it('testNative', 0, () => {
   7. hilog.info(0x0000, 'testTag', '%{public}s', 'testNative it begin');
   8. let result = entryTest.runNativeTest();
   9. hilog.info(0x0000, 'testTag', '%{public}s', result)
   10. expect(result).assertContain("ended");
   11. })
   12. })
   13. }
   ```
3. 运行testNative测试用例，查看测试结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Lz4GdlvCSxCsJ79U8lL6_w/zh-cn_image_0000002530753304.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=E03A6DCF34208C4159005B410565F9832029B585D4890F33D809877E85D5330C)

### 收集代码覆盖率

DevEco Studio默认不收集C++代码覆盖率，需要通过以下方式开启。

1. 在测试目录下的CMakeLists.txt中添加以下代码，开启覆盖率编译插桩能力。

   ```
   1. // DevEco Studio 6.0.2 Beta1之前版本
   2. set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   3. set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")

   5. // DevEco Studio 6.0.2 Beta1及以上版本，OHOS_TEST_COVERAGE在覆盖率模式下为true，在调试/运行模式下为false
   6. if(OHOS_TEST_COVERAGE)
   7. set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   8. set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   9. endif()
   ```
2. 在napi\_init.cpp文件的RunNativeTest方法中，调用\_\_llvm\_profile\_write\_file方法，将覆盖率数据保存到设备的/data/storage/el2/base路径下的c++\_coverage.profraw文件中，该路径和文件名不可修改，示例代码如下。

   ```
   1. extern "C" {
   2. void __llvm_profile_set_filename(char *);
   3. int __llvm_profile_write_file(void);
   4. }

   6. static napi_value RunNativeTest(napi_env env, napi_callback_info info)
   7. {
   8. char filename[256];
   9. snprintf(filename, sizeof(filename), "/data/storage/el2/base/c++_coverage.profraw"); // 覆盖率报告文件路径和文件名，不可修改
   10. __llvm_profile_set_filename(filename);
   11. // 开启测试
   12. ...
   13. // 结束测试，保存数据
   14. __llvm_profile_write_file();
   15. ...
   16. }
   ```
3. 运行覆盖率测试，选中ArkTS测试文件，单击**右键 >** **Run '测试文件名称' with Coverage**，执行测试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/h_seHO06TKOYvEa2cnw6tg/zh-cn_image_0000002530753310.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=548DC426A5BB042EF394EC55BBA649CB14BAA9A2EDFE216FBDB89E163EC5790F)

   启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/tBp2tVXoSH-l2JHIHsiq6g/zh-cn_image_0000002530753290.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=FD887CB9CAD015A868968C3E637FA511CE5E86FB39C2D6EDB46AF62D48F9546B)

   点击链接可打开报告，查看C++代码覆盖率详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/U4T-q9RxQJiFxRoFxCJ4zg/zh-cn_image_0000002561833213.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=F407F523B361B5DC500BA9EFE11D0DBDB472C46748DAA3B9D3030A3DECF84FDE)

## 使用命令行执行测试Instrument Test

通过命令行方式执行Instrument Test，在工程根目录下执行命令：

```
1. hvigorw onDeviceTest -p module={moduleName} -p coverage={true|false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false}
```

* module：执行测试的模块，缺省默认是执行所有模块的用例。
* coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/ohosTest/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

  如果开启了C++代码覆盖率测试，会生成C++代码的覆盖率报告，路径：<module-path>/.test/default/outputs/ohosTest/cpp\_reports/index.html
* scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
* ohos-debug-asan：是否启用ASan检测，缺省默认是false。从DevEco Studio 5.1.1 Beta1版本开始支持。

  ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage\_data

说明

* 通过命令行执行测试时，不支持配置product，默认为default。
* 多个module和scope之间用逗号隔开。

测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt
