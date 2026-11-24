---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test
title: 仪器测试（Instrument Test）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > 仪器测试（Instrument Test）
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0a71ee29448b23a89f7ad0357ea256c29cca255444ad78a49ac555524d77ff35
---

## 创建ArkTS测试用例

### 创建默认测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Instrument Test**或快捷键**Alt+Enter** **（macOS为Option+Enter）> Create Instrument Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/J6ScWwPaQre5FFzhO2He1g/zh-cn_image_0000002808886859.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=31A9FCEF24B11D7216B54B8B3AD2539FA7AF570EA307A24BC5E64EFC688990E2)
2. 在弹出的Create Instrument Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit，JS语言默认为DECC-JSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/zsGQGo5JSOKd0uyayA4-rg/zh-cn_image_0000002808766767.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BD2AEDDF61A262D21950549AF1CACAF7D14BA5D6FC81F046A1F795BD61FAADC)
3. DevEco Studio在ohosTest/ets/test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](arkxtest-guidelines.md)。

   **说明** 

   * 您也可以手动在ohosTest > ets > test文件夹下创建测试文件，手动创建后，需要在List.test.ets文件中添加创建的用例类。手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾，否则将在运行时弹窗提示“Error: Test files must end with '.test.ets'.”请点击**Fix**按钮，DevEco Studio将自动对ohosTest > ets > test目录下的文件名进行修改。
   * 首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UITest测试能力。

### 自定义Ability和Resources

从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。

**说明** 

如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。

**表1** **新旧版本ohosTest目录对比**

|  |  |
| --- | --- |
| **新版本** | **历史版本** |
|  |  |

1. 创建以下目录或文件，文件内容示例可在[运行Instrument Test测试用例](ide-instrument-test.md#section1574003717165)后，在对应模块的.test/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1及以上版本）或build/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1以下版本）下查看，其中productName是当前生效的product，可以通过点击DevEco Studio右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/U1QmDGS8SaOlJSLH_HP9Lw/zh-cn_image_0000002808766775.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8834A5132F561BC66F8FC677712A1DD67B9D2A0DB3BB494C36D002F5AB00D5BE)图标进行查看。
   * testability目录 > TestAbility.ets文件
   * testability目录 > pages目录 > Index.ets文件
   * testrunner目录 > OpenHarmonyTestRunner.ets文件
   * resources目录 > base目录 > element目录 > color.json文件
   * resources目录 > base目录 > element目录 > string.json文件
   * resources目录 > base目录 > profile目录 > test\_pages.json文件
2. 在module.json5文件中补充ability配置字段mainElement、pages、abilities，关于字段的具体说明请参考[module.json5配置文件](module-configuration-file.md)。

   ```json5
   {
     "module": {
       "name": "entry_test",
       "type": "feature",
       "description": "$string:module_test_desc",
       "mainElement": "TestAbility",                                   // 对应下方abilities中的ability name。
       "deviceTypes": [
         "phone",
         "tablet",
         "2in1"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:test_pages",                                 // 对应resources目录 > base目录 > profile目录 > test_pages.json文件。
       "abilities": [                                                  // 添加的ability的配置信息。
         {
           "name": "TestAbility",
           "srcEntry": "./ets/testability/TestAbility.ets",
           "description": "$string:TestAbility_desc",
           "icon": "$media:icon",    // 确保引用的资源都存在
           "label": "$string:TestAbility_label",
           "exported": true,
           "startWindowIcon": "$media:icon",
           "startWindowBackground": "$color:start_window_background"
         }
       ]
     }
   }
   ```

## 运行测试用例

### 运行模式

使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考[使用本地真机运行应用](ide-run-device.md)或[使用模拟器运行应用](ide-run-emulator.md)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：

* 在工程目录中，单击**右键 > Run '测试文件名称'**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/hlkVYc9ASvKO1W1wFPwqFg/zh-cn_image_0000002779407222.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=68A8270B23E397E60D589DF4F5942C7134B4AD6B5367F668B44F7BA80EDAB826)
* 打开测试文件，单击测试套件左侧按钮。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/u-66vzV6R3O6tKC2dVHSPg/zh-cn_image_0000002779567182.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3385DBCD16DD6B57B05252874D746EAB58570107C5DC459675AD3FCA888F35D4)
* 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](ide-instrument-test.md#section65264166107)后，通过如下方式的其中之一，执行Instrument Test：
  + 在工具栏主菜单单击**Run > Run '测试名称'**。
  + 在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Y3XTa7TJTJ2_4R9Qkskf9w/zh-cn_image_0000002808766757.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA6A8EE7EA58BDFAECD349B45013842907AC1F5CAC1C36EE8A6074A3E3E01F14)按钮，执行Instrument Test。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/UQ6IV53TTI-mJh5nF-CaDA/zh-cn_image_0000002808766783.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5685C0DE7C275846B91048CCDCACEE5030D8F6CBD71F37846DD75D6BA680E261)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/XxxFj78_TLu2OGsj4dmmIQ/zh-cn_image_0000002808766779.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A803C85FF570AC339D16510275906CD378AF90331247141D8A23ABC96B3F5241)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug '测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/itni1UCbSQiftb8cG3tZ9w/zh-cn_image_0000002808766777.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D9106046A6272E97831FBF03B7DEB6A9F60DCDCF5D002CE40A97C54C09F86C1)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/bn8OIB8cSUWQTLxyxC-INg/zh-cn_image_0000002779407204.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC6BBC3D06AF6F880390E97751E3F2073BF90A0A37B26677502554751D155D25)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Z_1PQ4vNQmqETv-HfS-fww/zh-cn_image_0000002779567208.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A3EACA6021E0B154629619EDA42387096128C76A2101EADA70EC74CB6091319)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/6JHMNVPBR5y_upgK-VHN7Q/zh-cn_image_0000002808766793.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=994686D65B9C67DA7E0448A2A685426291979C4D1A73CFA8564F1DB3E828D387)

**说明** 

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](ide-instrument-test.md#section0164586312)。

### 覆盖率统计模式

在Instrument Test运行的基础上支持代码覆盖率统计。

开发者可以自定义参与覆盖率测试的本地文件或远程源码har包，具体配置方法请参考[配置覆盖率过滤文件](ide-ui-test.md#section13756446154)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/cj_s-CNuSIqhClEMoHqR0A/zh-cn_image_0000002808886841.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AFD4A843E59FCE9D84FE2E6394A73042AD8DA5581C4A42D5209150BBF3FE881)
* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Z7a9ogyCS_mbcLZmOdUjZQ/zh-cn_image_0000002808766785.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DBD0D52F59F0EBAF2E9A87D01AAA2BC0740637F824842FAF4C1EF39C2924DB4)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/3VglCFIyTH-PSVVJ79lzSQ/zh-cn_image_0000002779407232.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=098A36FFC33C97B7387763A105A34C718B995FB375E562720340015E666D3B17)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/AljcHK7mTw-fPCjVrCbEnw/zh-cn_image_0000002779407202.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7A08DC65BD48ABE02E56A2F22D1C38D0DDBE7CE57A4E195DC47FEC06A30CA95)

点击链接可打开报告，查看ArkTS代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ck6zeayNRNyCXoubWq-t6g/zh-cn_image_0000002808886855.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=85FF87494B8FAA01EEDBE25A8A4D2FDA91C55B715DBD6ACF0E1A354C7692E218)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Og3ScJolSRmWchnT5HuI4A/zh-cn_image_0000002808886839.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=97EF85248194A7BB6BEC68518DA74A9F733532E5B409288CA7F281A125EB84C7)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run** > **Edit Configurations**进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击+按钮，在弹出的下拉菜单中，单击Instrument Test。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/FhPgNSsJRR2VEXTk0KcsUg/zh-cn_image_0000002779407212.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9D627D0F8B554FFEAA3DF49FCF80EC4AD2ACFE9F9924384B23CD2AD1DFA3945)
3. 根据实际情况，配置Instrument Test的运行参数。然后单击**OK**，完成配置。
   * 如果模块依赖共享包，请提前设置HAP安装方式，勾选“**Keep Application Data**”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
   * 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块），在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选“**Auto Dependencies**”，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
   * 如果不涉及UI测试，勾选“**Only OhosTest Package**”，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/zDSiK7x5TFe96zDTFSNQaw/zh-cn_image_0000002779407236.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DF85E5DBAC46F9FBD0C541D83D75E84E8035D8F1334A7567A876AB71FBDF1F1)

### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/qKmJ9L3WQxeFhgsWX7cnEg/zh-cn_image_0000002808766769.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCEC0FAB0EF76C99D4EB4A4822304C71F0697B43C5C6380C1FABCA408A16F668)
2. 打开**Run/Debug Configurations**窗口，点击Test Args![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/s84A75qvS1iBGnXD5y2eIA/zh-cn_image_0000002808766787.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=64B63590E9A411A6E20280C086F2B4BB05726AD09688A3BE13CAC05FD5146D86)，打开**Test Args**界面，添加测试参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/vYjWGV90TZKs2MUUiCDD9Q/zh-cn_image_0000002779567192.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEAE7BADB89860C15B184C3D49312A3F1996FD16A4DB8723DC55D032E5163793)

   例如将测试参数配置为level=1, size=medium

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/VkMJHCcITM6UucP5ydg9bQ/zh-cn_image_0000002779567190.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=45F176A2915FC94DFCD43F8DA64A7E0A2E9E3C8DD742D5313E5F16906DFDAA0D)

   **表2** 参数规则参考

   | Key | 含义说明 | Value取值范围 |
   | --- | --- | --- |
   | level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |
   | size | 用例粒度 | "small","medium","large", 例如：-s size small |
   | testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |
3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/y6uF6vayTwCNEORj9WmF2A/zh-cn_image_0000002779407226.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=28DD38F535671A49AD59DD54CFECE3C16DA497171AA13FB3C9A489789A10E5EA)

### 设置调试代码类型

点击**Run > Edit Configurations**，打开**Run/Debug Configurations**窗口，选择Instrument Test，点击**Debugger**页签，设置Debug type。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Vim-_R2LQmuTDlZNeGSDmQ/zh-cn_image_0000002779407230.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=12B96594ED6054953C2DBC300C2E7E2FDF199667E162D6A23974E879D9D0514E)

调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：

| 调试类型 | 调试代码 |
| --- | --- |
| Detect Automatically | 自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。  如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。 |
| ArkTS/JS | 只调试ArkTS/JS，只出现PandaDebugger调试窗口。 |
| Native | 单独调试C++，只出现Native调试窗口。 |
| Dual(ArkTS/JS + Native) | 支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。 |

**说明** 

调试C++代码时，当前模块及所有依赖的HSP模块的[Address Sanitizer配置](ide-instrument-test.md#section8352185341915)要保持一致，若不一致，可能无法进入C++代码的断点处。

### ASan检测

Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](ide-asan.md)，当前不支持JS语言。

1. 在运行/调试配置窗口，选择对应的Instrument Test，点击**Diagnostics**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/dLuYLLtqRd-JJ_CCVqNs4Q/zh-cn_image_0000002808886873.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1DABE81BDA4A0D88CEB5DBF1E2C024A7542BDA91B2237A058EBAD36086D7EEE)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/vWZwWwznROuXkmV8Jyk1Sg/zh-cn_image_0000002779567210.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4C11FBE9043EF0C95377B967B7B7F31927ABC0ADD244B338D8CE9EA6D3B7880)
3. 运行测试用例。
4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/jEO8-Tc_Rq2-kTG6z6LmPg/zh-cn_image_0000002808886875.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=56EE782797878891AB397492161331CAE553B1136C3AC404B17437EE6E5F9723)

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

   **说明** 

   DevEco Studio生成的cpp测试目录中不包含C++测试框架，需要开发者自行选择开源测试框架使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/EpceAzcsQZOsYGTzDH7HyA/zh-cn_image_0000002779407206.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD03937E4DEA8EF89F0A48F0B9572413D2ECE34380A0D42D7CADA700BB981A3E)
2. 通过ArkTS测试用例拉起C++测试，示例如下。

   ```ts
   // ArkTS测试文件Ability.test.ets
   import entryTest from 'libentry_test.so';
   export default function abilityTest() {
     describe('ActsAbilityTest', () => {
       // ...
       it('testNative', 0, () => {
         hilog.info(0x0000, 'testTag', '%{public}s', 'testNative it begin');
         let result = entryTest.runNativeTest();
         hilog.info(0x0000, 'testTag', '%{public}s', result)
         expect(result).assertContain("ended");
       })
     })
   }
   ```
3. 运行testNative测试用例，查看测试结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/JyI7ViiiRJuh_B_90ChBbg/zh-cn_image_0000002808886861.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B502763713A1041D12B30D0D59D9D1BCF156C92C8404C09465DAADB1C76FFB6D)

### 收集代码覆盖率

DevEco Studio默认不收集C++代码覆盖率，需要通过以下方式开启。

1. 在测试目录下的CMakeLists.txt中添加以下代码，开启覆盖率编译插桩能力。

   ```txt
   // DevEco Studio 6.0.2 Beta1之前版本
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")

   // DevEco Studio 6.0.2 Beta1及以上版本，OHOS_TEST_COVERAGE在覆盖率模式下为true，在调试/运行模式下为false
   if(OHOS_TEST_COVERAGE)
     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
     set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
   endif()
   ```
2. 在napi\_init.cpp文件的RunNativeTest方法中，调用\_\_llvm\_profile\_write\_file方法，将覆盖率数据保存到设备的/data/storage/el2/base路径下的c++\_coverage.profraw文件中，该路径和文件名不可修改，示例代码如下。

   ```cpp
   extern "C" {
       void __llvm_profile_set_filename(char *);
       int __llvm_profile_write_file(void);
   }

   static napi_value RunNativeTest(napi_env env, napi_callback_info info)
   {
       char filename[256];
       snprintf(filename, sizeof(filename), "/data/storage/el2/base/c++_coverage.profraw"); // 覆盖率报告文件路径和文件名，不可修改
       __llvm_profile_set_filename(filename);
       // 开启测试
       // ...
       // 结束测试，保存数据
        __llvm_profile_write_file();
       // ...
   }
   ```
3. 运行覆盖率测试，选中ArkTS测试文件，单击**右键 >** **Run '测试文件名称' with Coverage**，执行测试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/-DOdjQIeQRWvsmrrNffY1g/zh-cn_image_0000002808886865.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=141968BD6D79ED6CA881AA16374BC533729EED5AEF99FD9B3E22DC9B87CF54FF)

   启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/hWHo-loNTM2Ft7GCzaIXYQ/zh-cn_image_0000002779567194.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=18AAA479C5C7DC7702790D917FA68013296E14A81E890AD477E930D0F2F073B5)

   点击链接可打开报告，查看C++代码覆盖率详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/rNe3QOoNSxKptV49Dk0SjA/zh-cn_image_0000002808886857.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AEAF2CE9F1C168021D765941325B95A4775097428CD02730ABC65FFBF17B05F)

## 使用命令行执行测试

通过命令行方式执行Instrument Test，在工程根目录下执行命令：

```bash
hvigorw onDeviceTest -p module={moduleName} -p coverage={true|false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false} -p patch={patchPath} -p device={SN}
```

* module：执行测试的模块，缺省默认是执行所有模块的用例。
* coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/ohosTest/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

  如果开启了C++代码覆盖率测试，会生成C++代码的覆盖率报告，路径：<module-path>/.test/default/outputs/ohosTest/cpp\_reports/index.html
* scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
* ohos-debug-asan：是否启用ASan检测，缺省默认是false。从DevEco Studio 5.1.1 Beta1版本开始支持。

  ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage\_data
* patch：可选参数，指定代码补丁文件路径，用于统计增量代码覆盖率。仅支持绝对路径，后缀必须为.patch或.diff，可以通过git diff等命令生成。从26.0.0版本开始支持。
* device：可选参数，用于连接多个设备时指定某个设备进行测试。设备的SN号可以通过命令hdc list targets获取。缺省时会使用hdc list targets命令返回的第一个设备。从26.0.1版本开始支持。

**说明** 

* 通过命令行执行测试时，不支持配置product，默认为default。
* 多个module和scope之间用逗号隔开。

测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt
