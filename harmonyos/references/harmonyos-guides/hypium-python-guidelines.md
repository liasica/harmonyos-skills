---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines
title: 应用UI测试（基于Python）
breadcrumb: 指南 > 应用测试 > 单元测试和UI测试 > 应用UI测试（基于Python）
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9cc5426659794883a0626ac92bfa9a19815115196301a070fc542d8b035d0a62
---

## 框架概述

DevEco Testing Hypium （以下简称Hypium）是HarmonyOS平台的UI自动化测试框架，支持用户使用Python语言为应用编写UI自动化测试脚本，主要包含以下特性：

1. Hypium提供了控件、图像和比例坐标等**多种控件定位能力**，支持多窗口操作以及触摸屏/鼠标/键盘等**多种模拟输入功能**，支持**多设备**并行操作，能够覆盖各类场景和多种形态设备上的自动化用例编写需求，可支持鸿蒙手机、平板、PC等设备。
2. Hypium提供了在PyCharm中使用的**用例编写辅助插件**，支持控件查看/投屏操作等多种用例开发辅助功能，提升用例开发体验和效率。
3. Hypium能够为执行的用例生成详细的**用例执行报告**，并且自动记录设备日志以及执行步骤截图，为用户提供高效和专业的测试用例执行和结果分析体验。

## 安装向导

**1.安装Python**

推荐从[Python官网](https://www.python.org/)安装Python3.10版本。

**2.安装PyCharm**

推荐从[PyCharm官网](https://www.jetbrains.com.cn/en-us/pycharm/)安装2022.3以后的社区版本。

说明

项目创建功能只支持2022.3至2025.1的PyCharm版本。2024.3版本由于pycharm自身原因，只能选择单设备模板进行创建。

**3.安装hdc**

请参考[调试工具-hdc](hdc.md)中环境准备章节来安装和配置hdc环境。

**4.安装****Hypium**

* **方式一：****PyPI在线安装(推荐)**

在命令行中执行以下命令安装最新版本hypium

```
1. pip install hypium -U
```

* **方式二：安装包离线安装**

访问华为开发者联盟官网[下载DevEco Testing Hypium安装包](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)。下载后解压该安装包，找到其中的hypium-6.0.6.210.zip（此版本仅作为示例，请以实际版本号为准）。再次解压hypium-6.0.6.210.zip，进入解压后的文件目录执行以下命令，按照顺序安装4个安装包（命令中版本号仅做示例，请以实际版本号为准）。

```
1. python -m pip install xdevice-6.0.6.210.tar.gz
2. python -m pip install xdevice-devicetest-6.0.6.210.tar.gz
3. python -m pip install xdevice-ohos-6.0.6.210.tar.gz
4. python -m pip install hypium-6.0.6.210.tar.gz

6. # 此版本仅作为示例，实际请根据项目使用的版本选择
```

**5.DevEco Testing Hypium插件安装及使用方法**

注意

Mac系统使用UiViewer功能时，需在设置面板中手动指定hdc路径，详情可见 **本小节中 · 插件功能 Ⅳ.设置面板区域-hdc路径**。

若设备ROM版本和hypium都为6.1及以上版本，则UiViewer版本也需要升级至6.1及以上版本，否则在用例执行过程中，UiViewer会出现断连现象。

* **插件安装**

Ⅰ. 访问华为开发者联盟官网[下载页面](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)下载DevEco Testing Hypium安装包，下载后解压该安装包，找到其中的hypium-pycharm-plugin-6.0.6.210.zip（该版本号仅做示例，请以实际版本号为准），此文件为插件的安装包，无需再进行解压。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/SQFImOjLS_Kh9F_A_QwJGw/zh-cn_image_0000002524503481.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=09DDCE4F74181092246483E83B88199130684E1771F7458B9078BC1DA114AA8B "点击放大")

Ⅱ. 打开PyCharm后，点击File -> Settings -> Plugin -> 齿轮图标 -> Install Plugin from Disk。在弹出的文件选择器中，选择第一步下载的hypium-pycharm-plugin-6.0.6.210.zip（该版本号仅做示例，请以实际版本号为准）离线安装包，完成安装。安装完成后，重启PyCharm即可使用新安装的Deveco Testing Hypium插件。

说明

在6.0及以后的版本中，DevEco Testing Hypium插件在下载包中的名称由“DevEcoTesting-Hypium”修改为“hypium-pycharm-plugin”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5zEC26LfSf6dPm3brU61OA/zh-cn_image_0000002524503499.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=85CDBEEFD34DFCD0EF06EF0F537605D13B90799B8F3924828D76F28906661586 "点击放大")

安装完成后在Plugins界面可以看到DevEcoTesting-Hypium插件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Kljl_O1WQ8yvNWWps8_A-g/zh-cn_image_0000002492503710.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=E871555A67CF332D5124F632BC94DB058F2DADDE4DA496EC4233B83E7B0D7AD3)

* **插件功能**

PyCharm有三个主要的开发功能区，如下图所示。DevEco Testing Hypium插件在不同的开发功能区提供了对应的用例开发辅助功能，在PyCharm的设置面板中提供了插件的设置功能，在PyCharm的工程新建面板中提供了用例工程模板创建功能，下文分区域介绍这些功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/gH70QFnwRhmAVht_4si_fQ/zh-cn_image_0000002524623423.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=8F01236966E7F8E8B117E8042035AB86C19F180916E19935F7EAB749AA41A208 "点击放大")

**Ⅰ. 项目文件区域**

在项目文件区域右键点击项目目录或者文件，选择 DevEco Testing Hypium，弹出对应的功能菜单。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/rJWn3xbySD-6xSfNAkFbPQ/zh-cn_image_0000002524623427.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=31CE9BC2FD892E3685F64EFE2E51F64EB7E7C7246D2B5A4FF5464AC24C34578A)

功能菜单根据选择的目录和文件不同存在区别，详细参见下表：

| 序号 | 功能 | 图片 | 说明 | 注意 |
| --- | --- | --- | --- | --- |
| 1 | 执行当前目录 |  | 执行当前目录中的所有测试用例。 | 此功能仅右键选中文件夹时可用。 |
| 2 | 一键执行当前用例 |  | 执行当前选中的测试用例文件。 | 此功能仅右键选中测试用例对应Python或JSON文件时可用。 |
| 3 | 生成Hypium模板用例 |  | 在当前选中的目录下生成测试用例模板文件。 |  |
| 4 | 生成Hypium模板测试套 | 在当前选中的目录下生成测试套模板文件。 |  |
| 5 | 生成测试服务包 |  | 该功能支持生成“回归测试”和“场景化性能”两种类型的测试服务包模板，用户可根据实际需求填写配置项，完成设置后即可生成对应的测试服务包。 | 1. 该功能仅在右键点击项目根目录时可用，选中其他目录无法触发此功能。 2. 项目根目录下需要包含 testcases 文件夹。 3. 项目根目录下需存在 setup-sceneperf.py 或 setup-regression.py 文件之一，以支持相应测试服务包的生成。 |

**Ⅱ. 代码编辑区域**

| 序号 | 功能 | 图片 | 说明 | 注意 |
| --- | --- | --- | --- | --- |
| 1 | 一键执行当前用例 |  | 执行当前文件对应的测试用例。 | 此功能仅在当前项目根目录下存在config文件夹时可用。 |
| 2 | 一键调试当前用例 | 以调试模式执行当前文件对应的测试用例 | 此功能仅在当前项目根目录下存在config文件夹时可用。 |
| 3 | 选区快速执行 | 快速执行选中的代码片段，无需运行整个用例。 | 1. 此功能仅在正常连接被测设备时可用。  2. 此功能仅在当前项目根目录下存在config文件夹时可用。 |
| 4 | 选区快速调试 | 以调试模式快速执行选中的代码片段。 | 1. 此功能仅在正常连接被测设备时可用。  2. 此功能仅在当前项目根目录下存在config文件夹时可用。 |
| 5 | 生成Hypium模板代码 |  | 快速生成内置的模板操作代码。 |  |
| 6 | 函数快速执行 |  | 快速执行测试用例中的指定生命周期函数。 | 1. 此功能仅在正常连接被测设备时可用。  2. 此功能仅在当前项目根目录下存在config文件夹时可用。  3. 此功能仅在当前编辑的文件为Hypium测试用例Python文件时可用。 |

**Ⅲ. ToolWindow区域**

**UiViewer功能**

DevEco Testing Hypium插件会在PyCharm界面右边缘的ToolWindow区域生成UiViewer标签，点击后会展开UiViewer功能面板。UiViewer功能目前分为4个界面：设备选择界面 、单设备控件查看界面 、单设备投屏界面 、双设备投屏界面。

注意

UiViewer插件当前仅支持USB连接本地设备调测和本地模拟器进行调测，但是由于模拟器性能资源管理策略，当模拟器处于后台或被其他页面遮挡时，将不会进行画面渲染绘制。此时在投屏时会出现黑屏闪烁现象，如需规避，需要使模拟器处于前台显示。

**设备选择界面**

设备选择界面如下图所示， 若首次进入该界面，或设备状态发生变化，需点击“刷新”按钮以更新设备列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/vqJuXh1dQDWnrgSfZ5vICQ/zh-cn_image_0000002558763237.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=AF7F2ACA2A420211C34F0317A900FFC6B77CD3F0AE7BD36F26A645B02FF73C11)

设备信息说明见下表：

| 序号 | 参数名称 | 说明 | 图片 |
| --- | --- | --- | --- |
| 1 | SN（Serial Number）号 | 该参数为已连接设备的序列号（SN号），用于区分不同设备。 |  |
| 2 | 设备类型 | 该参数为设备连接通道类型，仅支持hdc连接，对应设备类型显示为HDC。 |  |
| 3 | 设备状态 | 该参数显示当前设备是否支持使用 UiViewer 工具：“OK” 表示该设备可用；“NOT\_SUPPORT” 表示设备不可用。 |  |
| 4 | 设备编号 | 该参数用于在多设备同时投屏时配置各设备的显示位置，用户可手动进行调整。  在双设备投屏界面中，默认情况下，设备编号为 dev1 的设备显示在左侧，设备编号为 dev2 的设备显示在右侧。 |  |
| 5 | 添加远程设备 | 点击后会弹出远程设备IP添加面板，可以在此填入远程设备所在电脑的IP和hdc端口，以此来发现远程电脑上所连接的hdc设备。 |  |
| 6 | 删除远程设备 | 在管理远程设备面板中，可以在之前添加的远程IP对象上右键，点击删除按钮进行删除 |  |

设备选择界面最多支持同时选择两个设备进行投屏。

* 若仅勾选一个设备并点击“确定”按钮，则进入单设备投屏界面。
* 若勾选了两个设备并点击“确定”按钮，将进入双设备投屏界面；其中，设备编号为 “dev1” 的设备显示在左侧，设备编号为 “dev2”的设备显示在右侧，用户可以通过设备编号的下拉选项框自定义配置设备编号，控制双设备投屏。

**单设备投屏界面**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/b0Nq5Z3tRKiQ2yb4OS0MBw/zh-cn_image_0000002492343770.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=4C3CF87097E84401647B5EB232734380C597301FE22F1CA6F3604DFB17EC74BA "点击放大")

**功能说明：**

* **设备切换按钮：**点击后返回设备选择界面，可重新选择要投屏的设备。
* **设备屏幕显示区域：**显示当前设备的实时屏幕画面。在投屏模式下，可通过鼠标点击或滑动该界面来操作设备。
* **工具区：**位于设备屏幕显示区域右侧，从上至下分为以下三个子工具区。

**工具区1：**

该工具区提供控件查看功能。进入控件查看模式后，设备画面将保持静止，不再实时更新。若需获取当前页面的最新控件信息，需手动点击“控件刷新”按钮以重新抓取页面结构和控件数据。

| 序号 | 图标 | 功能 | 说明 |
| --- | --- | --- | --- |
| 1 |  | 查看控件 | 点击该按钮进入控件查看模式，插件会读取设备当前的控件树和屏幕截图，并显示到界面上（此过程需要一定时间，在鼠标光标处于转圈状态时，请勿点击其他按钮，以免操作冲突或导致异常）。在控件查看模式下再次点击该按钮，可退出当前模式，返回实时投屏模式。 |
| 2 |  | 进入高级控件查看模式 | 点击该按钮进入高级控件查看模式，系统会根据鼠标移动实时高亮对应控件，并持续展示其控件信息。点击某一控件信息后，将自动切换到普通控件查看模式，并定位显示该控件在控件树中的详细信息。  处于高级控件查看模式时，再次点击该按钮，可退出当前模式，则返回实时投屏模式。 |
| 3 |  | 录制Hypium测试用例脚本 | 点击该按钮进入操作录制模式，在此模式下，用户点击或操作投屏画面中的控件时，系统将自动识别操作行为，并在编辑器当前光标位置生成对应的 Hypium 自动化测试脚本代码。  处于操作录制模式时，再次点击该按钮可退出当前模式，返回实时投屏模式。 |
| 4 |  | 刷新控件 | 如果设备界面发生变动，可点击此按钮重新获取当前页面的最新控件信息。 |

**工具区2：**

此工具区提供一系列常用的设备操作功能，便于在投屏过程中快速执行基本控制与调试操作，当前支持的功能见下表：

| 序号 | 图标 | 功能 | 说明 |
| --- | --- | --- | --- |
| 1 |  | 提高音量 | 点击后对设备进行音量加操作。 |
| 2 |  | 降低音量 | 点击后对设备进行音量减操作。 |
| 3 |  | 触发电源键 | 点击后模拟按下设备电源键。 |
| 4 |  | 执行重启操作 | 点击后重启设备。 |
| 5 |  | 触发返回键 | 点击后模拟返回键操作。 |
| 6 |  | 触发返回桌面操作 | 点击后模拟返回桌面操作。 |

**工具区3：**

此工具区提供系统管理相关功能，当前支持的功能见下表：

| 序号 | 图标 | 功能 | 说明 |
| --- | --- | --- | --- |
| 1 |  | 查看设备信息 | 点击后在“设备信息展示区”显示当前设备的信息。 |
| 2 |  | 执行全屏截图 | 点击后会将当前屏幕画面保存至当前项目的“resource”文件夹下的“Hypium”目录下。 |
| 3 |  | 执行区域截图 | 点击该按钮后，设备显示界面将进入区域截图状态。此时，在设备画面中按住鼠标左键并拖动，可自由框选需要截图的区域。松开鼠标后，系统将对选定区域进行截图，并自动保存至当前项目的 resource/Hypium/ 目录下。 |
| 4 |  | 切换竖屏 | 将设备屏幕方向设置为竖屏（Portrait）状态。点击该按钮后，设备将旋转显示方向至竖屏模式。此操作会向设备发送系统指令，实际效果取决于当前应用是否支持方向控制。 |
| 5 |  | 切换横屏 | 将设备屏幕方向设置为横屏（Landscape）状态。点击该按钮后，设备将旋转显示方向至横屏模式。此操作会向设备发送系统指令，实际效果取决于当前应用是否支持方向控制。 |
| 6 |  | 安装应用 | 点击该按钮后，用户可以从本地计算机选择一个HAP文件安装到连接的设备中。 |
| 7 |  | 卸载应用 | 用户可对当前连接设备上已安装的应用程序进行卸载操作。点击该按钮后，系统将获取设备上已安装应用列表，用户可从中选择目标应用并执行卸载。 |
| 8 |  | 发送文件 | 用户可以从电脑本地选择单个文件或整个目录，通过此功能将其发送至设备端指定的存储路径。 |
| 9 |  | 管理应用 | 点击该按钮后将打开一个独立的应用管理界面，用户可以在应用管理界面安装和卸载应用。 |
| 10 |  | 录制文本输入 | 此按钮在进入录制状态后才能够使用。点击此按钮后将进入录制输入状态，此时点击界面上要进行输入的文本框控件后，会弹出一个输出框；用户在输入框中输入要插入的文本后点击确定，此时工具便会在代码编辑区光标处生成录制出的文本输入语句，同时设备侧也会自动输入文本。 |

**双设备投屏界面**

该界面支持同时对两个设备进行投屏与操作，双设备投屏时，每个设备的显示区域功能与单设备投屏一致，支持独立触摸控制、截图、旋转等操作。

当需要对某一设备进行控件查看时，插件将自动退出双设备投屏模式，切换至单设备控件查看界面，以确保控件信息的准确展示与操作体验。完成控件查看后，用户可手动返回双设备投屏视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/8CU7myJrQom48oRLySVANQ/zh-cn_image_0000002492503742.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=15895FF1DDB55460E42EA1A3B93104CB0AF399D3BEE75D6ED142BD328FACC545 "点击放大")

**执行结果报告展示功能**

使用“一键执行当前用例”功能完成测试用例执行后，插件将在控制台旁边自动生成执行结果标签。点击该标签，即可查看本次用例执行过程中各步骤的截图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/gbz6L6WJRxaYnlRG58rsJA/zh-cn_image_0000002524623411.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=E42FDE0EB6DE2E1503A245651715ED6A3CBBE4C30195A1D71B5376F3FC6DEDEB "点击放大")

**Ⅳ. 设置面板区**

打开PyCharm设置面板，选中左侧的DevEco Testing Hypium选项，可以进入DevEco Testing Hypium的设置面板，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/6L8gGujWTm-QA9oqEjgF1w/zh-cn_image_0000002524623405.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=59D18AABA83F694D59B4965DAB3D92E2696731063375409966ABA2A5F32E91E0)

各个配置项的详细说明见下表：

| 序号 | 功能 | 说明 | 注意 |
| --- | --- | --- | --- |
| 1 | 配置文件路径 | 配置一键执行/调试功能所使用的配置文件路径，如不设置，默认使用当前项目下的config文件夹作为配置文件路径。 | - |
| 2 | 测试用例路径 | 配置一键执行/调试功能所使用的测试文件路径，如不设置，则默认使用当前项目下的testcases文件夹作为测试用例路径。 | - |
| 3 | 额外执行参数 | 配置运行用例一键执行/调试功能时，额外传递给Hypium测试框架的命令行参数。例如用户需要开启Hypium框架的用例单步骤截图功能，可以将额外执行参数设置为“-ta screenshot:true”。 | - |
| 4 | 是否以bin模式执行 | 配置是否以bin模式执行用例时，通过该模式执行时，可避免投屏和用例执行冲突。 | **正常使用时该选项无需配置。**  该设置项在DevEco Testing Hypium 6.0.5.200以及更新的版本中不再需要，已移除。 |
| 5 | hdc路径 | 配置UiViewer所使用的hdc路径。 | - |
| 6 | 高级控件查看模式自动刷新间隔 | 配置UiViewer功能中的高级控件查看模式的刷新间隔，默认60秒自动重新获取一次界面的布局，最小时间可以设为30秒，最大时间300秒。 | - |
| 7 | 录制步骤是否生成性能脚本 | 操作录制模式默认生成功能测试脚本，通过该选项可以配置生成性能测试步骤脚本。注意执行性能测试脚本需要首先安装hypium-perf性能测试插件。 | 该功能仅DevEco Testing Hypium 6.0.5.200以及更新的版本支持。 |
| 8 | 是否使用视频流投屏模式 | 配置是否使用视频流模式投屏。当投屏异常时，可尝试将此选项改为否，切换投屏方式，注意此时的投屏帧率大幅降低， | **正常使用时该选项无需进行配置。** |
| 9 | 依赖下载参数 | 配置生成测试服务包下载PyPI依赖包是传递给pip命令的额外参数。例如出现依赖下载慢或失败的情况时，可设置“-i <PyPI Source>”参数，配置可正常访问的PyPI源。 | - |
| 10 | 本地依赖文件存放文件夹 | 设置该文件夹后，在生成测试服务包时，插件将优先使用该目录中已下载的依赖文件，避免重复在线下载，有效应对因网络问题导致的PyPI依赖包安装失败等场景。 | - |

**Ⅴ. 工程创建区域**

在PyCharm顶部点击File -> New Project 进入模板工程创建面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/0JFgbPplTtORSvptN8DIEw/zh-cn_image_0000002524623425.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=C274F4AEAFFA5D30243F7E915EC8BC6851A2C290B1D5BC80F4EBA98F6AA22AC9)

点击左侧的DevEco Testing Hypium，可以创建Hypium用例模板工程。共有两种类型的Hypium模板工程，分别对应单设备和双设备的测试场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/IkpNqpV3QaGCvrfPUufrpA/zh-cn_image_0000002524623429.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=197D3BCB15A5DC2A666A10FA159415302D9D534F68B2B1A568EFE10AF3A975CD "点击放大")

选择对应模板，配置工程路径以及Python环境参数，点击Create即可创建Hypium测试用例工程。工程目录中包含一个模板用例和一个模板配置文件user\_config.xml。

以单设备工程为例，创建完成后的界面如下图所示。连接被测设备后，可右键点击模板用例文件代码编辑区域“执行hypium用例”来运行当前用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/foYYa84MQUW17xf6Jw_qAg/zh-cn_image_0000002492503754.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=F2F3A159CB817560EB441CE3C0C69422E992F7A569A75D48FCDC63FBDFC919B6)

## 测试脚本开发快速入门

本章节将指导用户创建并执行一个简单的测试脚本工程，快速掌握项目目录结构中的关键文件，熟悉基于Hypium的测试脚本开发流程。

* **测试脚本工程创建**

测试脚本工程创建主要有两种方式：

a）直接使用以下附件中的模板工程。

[HypiumProjectTemplate.zip](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260420144409.91208270398374383371124549269383:20260429075751:2800:88B4FA4C5B65AB7C90F8C05DCFA5576F207BEA74D8A4A26A41FB33362211EEDE.zip?needInitFileName=true)

b）通过PyCharm上的DevEcoTesting-Hypium插件进行创建。请参考本文档的**“安装向导 -> DevEco Testing Hypium插件安装及使用方法 -> 插件功能 -> 工程创建区域****”**小节。

**Ⅰ.工程目录文件介绍**

```
1. HypiumProjectTemplate
2. |     |----aw                                     // 工程中自定义模块文件夹
3. |     |     |----Utils.py                           // 示例模块文件
4. |     |----config                                   // 测试工程配置文件夹
5. |     |     |----user_config.xml                    // 测试工程配置文件
6. |     |----resource                              // 测试资源文件夹，测试过程中用到的资源文件默认会优先从当前文件夹进行查找。
7. |     |----testcases                             // 测试用例文件夹，测试过程中的测试用例文件优先会从当前文件夹进行查找。
8. |     |    |----Example.json                        // Example测试用例配置文件，配置用例所需设备等参数。
9. |     |    |----Example.py                          // Example测试用例文件，存储测试逻辑代码。注意该文件无法直接运行，要通过测试框架启动后加载执行，详情参见后文测试用例执行部分。
10. |     |----main.py                               // 测试用例执行入口文件，用户可以通过运行该文件启动测试任务，执行测试用例。
```

**Ⅱ.工程配置文件介绍**

```
1. <?xml version="1.0" encoding="UTF-8"?>
2. <user_config>
3. <environment>
4. <!-- type: 设备连接方式，仅支持设置为usb-hdc，表示使用hdc命令控制设备（默认)。 -->
5. <device type="usb-hdc">
6. <!-- ip: 远端hdc server的ip地址，ip和port为空时使用本地设备，非空时使用远端设备。 -->
7. <!-- port: 远端hdc server的端口号 -->
8. <!-- sn：设备序列号，设为空时，表示所有设备均可用 -->
9. <info ip="" port="" sn="sn"/>
10. <!-- 可添加多个info标签，配置多个设备 -->
11. <info ip="" port="" sn="sn"/>
12. </device>
13. </environment>
14. <testcases>
15. <!-- 测试用例目录，该属性为空时默认使用当前项目下的testcases目录。 -->
16. <dir></dir>
17. </testcases>
18. <resource>
19. <!-- 测试资源文件目录，该属性为空时默认使用当前项目下的resource目录。 -->
20. <dir></dir>
21. </resource>
22. <!-- 用例执行日志级别，当前仅支持设置为INFO或者DEBUG，默认为INFO，如需更详细信息可设置为DEBUG。 -->
23. <loglevel>DEBUG</loglevel>
24. <devicelog>
25. <!-- 指定用例执行完成后自动从设备端拉取的文件目录，多个目录使用分号分隔。 -->
26. <dir>/data/log/tee;/data/log/test</dir>
27. <!-- 设置用例执行时抓取的hilog日志等级，默认值为INFO。 -->
28. <loglevel>DEBUG</loglevel>
29. <!-- 设置单个用例执行完成并抓取设备端hilog日志文件后，是否自动清空设备端的日志文件，默认值为true。-->
30. <clear></clear>
31. <!-- 设置用例执行完成后是否抓取设备端hilog日志文件，默认值为ON。注意设置为OFF时上述devicelog配置下的dir、loglevel以及clear属性不生效。 -->
32. <enable>ON</enable>
33. </devicelog>
34. <taskargs>
35. <!-- pass_through，透传参数给测试用例。如{"task_id":"950191","user_define":{"execType":"3"}} -->
36. <!-- 参数获取方法：from xdevice import Variables; print(Variables.config.pass_through) -->
37. <pass_through></pass_through>
38. <!-- repeat，用例重复运行多少次。大于1的整数才生效 -->
39. <repeat></repeat>
40. <!-- screenshot，操作类接口运行后是否截图。true开启/false不开启，默认值false -->
41. <screenshot>false</screenshot>
42. <!-- screenrecorder，用例Step步骤是否录屏。true开启/false不开启，默认值false -->
43. <screenrecorder>false</screenrecorder>
44. </taskargs>
45. </user_config>
```

**Ⅲ.测试用例介绍**

Hypium 测试用例由两部分组成：测试用例配置文件（JSON 格式）和测试用例脚本文件（Python 格式）。测试用例的组织方式支持两种模式：

* **单个用例模式：**包含一个测试用例脚本（Python）文件和一个测试用例配置（JSON）文件；
* **测试套模式：**包含一个测试套脚本（Python）文件、多个测试用例脚本（Python）文件和一个测试套配置（JSON）文件。

用户可根据实际需求选择合适的组织方式。

**单个测试用例模式**

* **测试用例脚本文件**

该文件包含测试用例的执行逻辑，核心为三个关键的生命周期函数：setup、process、teardown。在用例开发时，用户需要根据业务需求在对应的函数中编写测试逻辑代码。生命周期函数的详细说明见下表：

| 序号 | 生命周期函数 | 说明 |
| --- | --- | --- |
| 1 | setup | 测试用例的前置步骤，主要用于执行测试用例的预置动作。 |
| 2 | process | 测试用例的实际操作步骤，主要描述当前测试用例中的所有测试用例步骤集合。 |
| 3 | teardown | 测试用例的清理步骤，主要用于执行测试用例的环境清理等操作。 |

**示例代码**

```
1. # !/usr/bin/env python
2. # coding: utf-8
3. from devicetest.core.test_case import TestCase, Step
4. from devicetest.utils.file_util import get_resource_path
5. from hypium import *
6. from aw import Utils
7. class Example(TestCase):
8. def __init__(self, controllers):
9. self.TAG = self.__class__.__name__
10. TestCase.__init__(self, self.TAG, controllers)
11. self.driver = UiDriver(self.device1)
12. def setup(self):
13. Step('1.回到桌面')
14. self.driver.swipe_to_home()
15. def process(self):
16. Step('2.检查短信应用版本')
17. mms_version = Utils.get_app_version_code(self.driver, 'com.ohos.mms')
18. host.check_greater(mms_version, 0)
19. Step('3.点击桌面上的短信')
20. self.driver.touch(BY.text("信息"))
21. def teardown(self):
22. Step("4. 停止短信应用")
23. self.driver.stop_app("com.ohos.mms")
```

* **测试用例配置文件**

该文件主要描述测试用例的配置信息，如测试用例所需设备类型和数量、测试用例的测试驱动信息、测试用例的描述信息等。

**注意**：JSON文件不支持注释，请在使用示例时移除其中以 “//”开头的注释部分。

**示例：**

```
1. {
2. // description属性为测试用例的功能描述。
3. "description": "Config for app test suites",
4. // environment属性用于配置测试用例需要的设备类型和数量。
5. "environment": [
6. {
7. "type": "device",   // 设备操作系统类型，device表示HarmonyOS设备。
8. "label": "phone"    // 设备物理形态，phone为手机，tablet为平板，设置为空字符串或者移除该属性表示用例对设备类型无要求。用户可以通过执行hdc shell param get const.product.devicetype查看设备类型。
9. }，
10. {
11. "type": "device",   // 测试用例需要多个设备时，在environment属性中添加多个设备配置项。
12. "label": "phone"
13. }
14. ],
15. // driver字段主要描述测试用例的测试驱动是什么，以及具体要执行的Python脚本文件在哪（填写与当前JSON文件的相对路径即可）
16. // 不填写则在当前JSON文件下寻找同名Python文件
17. "driver": {
18. "type": "DeviceTest",
19. }
20. }
```

**测试套模式**

* **测试套脚本文件**

该文件包含测试套的初始化和清理逻辑，核心为两个关键的生命周期函数：setup、teardown。在用例开发时，用户需要根据业务需求在对应的函数中编写测试逻辑代码。生命周期函数的详细说明见下表：

| 序号 | 生命周期函数 | 说明 |
| --- | --- | --- |
| 1 | setup | 整个测试套的前置步骤，在测试套运行前先执行该函数。 |
| 2 | teardown | 整个测试套的清理步骤，在执行完所有测试用例后执行。 |

**示例代码**

```
1. from devicetest.core.test_case import Step
2. from devicetest.core.suite.test_suite import TestSuite
3. class Testsuite1(TestSuite):
4. # 测试套的前置步骤将在所有测试用例执行前运行。当多个测试用例具有相同的初始化操作时，可将共用的前置逻辑定义在此。
5. def setup(self):
6. Step("TestSuite: setup")
7. # 测试套的清理步骤会在所有测试用例执行完成后运行。
8. def teardown(self):
9. Step("TestSuite: teardown")
```

* **测试套配置文件**

该文件主要描述测试套的配置信息，如测试套所需设备类型和数量、测试套的测试驱动信息、测试套的描述信息等。

**注意**：JSON文件不支持注释，请在使用示例时移除其中以 “//”开头的注释部分。

**示例代码**

```
1. {
2. "description": "Config for app test suites",
3. // environment属性用于配置测试用例需要的设备类型和数量。
4. "environment": [
5. {
6. "type": "device",     // 配置设备操作系统类型，device表示HarmonyOS设备。
7. "label": "phone"      // 设备物理形态，phone为手机，tablet为平板，设置为空字符串或者移除该属性表示用例对设备类型无要求。用户可以通过执行hdc shell param get const.product.devicetype查看设备类型。
8. }
9. ],
10. // driver 属性用于定义测试用例的驱动类型及待执行脚本的路径，脚本路径需为相对于当前 JSON 文件的路径。
11. "driver": {
12. "type": "DeviceTestSuite",
13. // 指定测试套配置（JSON）文件对应的测试套脚本（Python）文件路径（可省略 .py 后缀），支持相对路径或绝对路径。若使用相对路径，需相对于测试工程根目录；若未指定，则默认查找与当前 JSON 文件同目录下同名的 Python文件。
14. "testsuite": "TS_001/TS_001",
15. // 指定测试套中的测试用例脚本(Python)文件列表，指定方式有两种。
16. // 方式一：定义 suitecases 字段，并在其中指定测试用例脚本文件的路径。路径可使用相对路径或绝对路径；若使用相对路径，其根目录为当前测试套目录。
17. "suitecases": [
18. "TestCase1.py",         // 相对路径
19. "/path/to/TestCase2.py" // 绝对路径
20. ]
21. // 方式二：将测试用例脚本（Python）文件保存到测试套目录中，并且设置文件名前缀为"TC_"，框架即可自动扫描当前测试套对应的所有测试用例脚本文件。
22. },
23. // kits字段主要描述测试用例需要的测试公共kit，如pushkit、shellkit等
24. "kits": []
25. }
```

* **测试用例脚本文件**

测试套模式中的测试用例脚本文件和单个测试用例中对应文件完全相同，请参考上文**“单个测试用例模式** -> **测试用例脚本文件**“小节。此处介绍测试用例脚本文件和测试套关联的两种方式：

**方式一：**框架自动扫描的与测试套关联的测试用例脚本，测试用例脚本的保存目录和文件命名需要满足以下规则：

1. 测试用例脚本文件需与测试套脚本文件位于同一目录。
2. 测试用例脚本文件的文件名前缀是“TC\_”（例如：TC\_Login.py）。

**方式二：** 在测试套配置文件中指定所有的测试用例脚本文件路径，详情请参考上文的**“测试套配置文件“**小节。

* **测试用例执行**

本章节主要介绍测试用例的执行方式。测试用例支持两种执行方式：一是通过命令行执行，二是通过 PyCharm IDE 中的DevEco Testing Hypium 插件进行一键执行。

**命令介绍**

Hypium框架命令可以分为三类：help、list和run。其中run为最常用的执行命令。

**命令交互入口**

打开命令行窗口，切换到测试脚本工程的根目录，执行以下命令可以进入Hypium控制台。

```
1. python -m hypium
```

**常用命令介绍**

**help命令**

输入help指令可以查询框架指令帮助信息。

```
1. help:
2. use help to get information.
3. usage:
4. run:  Display a list of supported run command.
5. list: Display a list of supported device and task record.
6. Examples:
7. help run
8. help list
```

说明

help run：展示run指令相关说明；help list：展示 list指令相关说明。

**list命令**

list指令用来展示设备和相关的任务信息。

```
1. list:
2. This command is used to display device list and task record.
3. usage:
4. list
5. list history
6. list <id>
7. Introduction:
8. list:         display device list
9. list history: display history record of a serial of tasks
10. list <id>:    display history record about task what contains specific id
11. Examples:
12. list
13. list history
14. list 6e****90
```

说明

list：展示设备信息；

list history：展示任务历史信息；

list< id >：展示特定id的任务其历史信息。

**run命令**

run指令主要用于执行测试任务。

```
1. run:
2. This command is used to execute the selected testcases.
3. It includes a series of processes such as use case compilation, execution, and result collection.
4. usage: run [-l TESTLIST [TESTLIST ...] | -tf TESTFILE
5. [TESTFILE ...]] [-tc TESTCASE] [-c CONFIG] [-sn DEVICE_SN]
6. [-rp REPORT_PATH [REPORT_PATH ...]]
7. [-respath RESOURCE_PATH [RESOURCE_PATH ...]]
8. [-tcpath TESTCASES_PATH [TESTCASES_PATH ...]]
9. [-ta TESTARGS [TESTARGS ...]]
10. [-env TEST_ENVIRONMENT [TEST_ENVIRONMENT ...]]
11. [--retry RETRY] [--session SESSION]
12. [--repeat REPEAT]
13. action task
14. Specify tests to run.
15. positional arguments:
16. action                Specify action
17. task                    Specify task name,such as "ssts", "acts", "hits"
```

run常用指令基本使用方式如下：

| 序号 | hypium命令 | 功能 | 示例 |
| --- | --- | --- | --- |
| 1 | run -l <testcase> | 运行指定测试用例。如有多个测试用例，测试用例之间以分号分隔。 | run -l Example1;Example2 |
| 2 | run -sn | 指定运行设备SN号，多个SN号之间以分号分隔（英文分号）。 | run -l Example1 -sn sn1  run -l Example1 -sn sn1;sn2 |
| 3 | run -rp | 指定报告生成路径，默认报告生成在项目根目录下的reports文件夹，以时间戳或任务id建立子目录。 | run -l Example1 -rp /path/to/report |
| 4 | run -respath | 指定测试资源路径，默认为项目根目录下的resource文件夹。 | run -l Example1 -respath /path/to/resource |
| 5 | run -tcpath | 指定测试用例路径,默认为项目根目录下的testcases文件夹。 | run -l Example1 -tcpath /path/to/testcases |
| 6 | run - ta | 指定模块运行参数，当前仅支持配置步骤截图开关，配置方式参考示例。 | run -l Example1 -ta screenshot:true |
| 7 | run --retry | 重新运行上次失败的测试用例，通过-session指定report任务报告目录。 | run --retry --session 2022-12-13-12-21-11 |

**PyCharm中用例执行**

PyCharm中执行用例依赖本文档的安装向导部分介绍的PyCharm插件：DevEco Testing Hypium，请参考本文档的**“安装向导 -> DevEco Testing Hypium插件安装及使用方法”**小节。

**测试报告查看**

测试框架执行完用例后，会生成执行结果报告。报告默认存放在测试工程目录的reports目录下。如果用户在启动测试任务时通过-rp参数指定了报告路径，报告会生成在指定的路径下。

测试报告目录结构如下：

```
1. 当前报告目录（默认目录/指定目录）
2. ├── details（用例步骤截图存放目录）
3. ├── result（模块执行结果存放目录）
4. │     ├── <测试用例1结果>.xml
5. │     ├──  ... ...
6. ├── log (设备和任务运行log存放目录)
7. │     ├── <测试用例1设备执行>.log
8. │     ├── ... ...
9. │     ├── <任务执行>.log
10. ├── static (报告展示页面css元素存放目录)
11. ├── summary_report.html（测试任务可视化报告）
12. ├── summary_report.xml（测试任务数据报告）
13. ├── summary.ini（记录测试类型，使用的设备，开始时间和结束时间等信息）
14. ├── task_info.record（记录执行命令，失败用例等清单信息）
```

## API使用说明

Hypium测试框架提供了两大类API来支持用例的编写：设备相关API和设备无关API。

设备相关的API主要包括四个基础API类：**UiDriver，BY，IUiComponent，UiWindow**。

* **UiDriver**类为UI测试的入口，代表了一个被测设备，提供控件查找、控件检查、用户操作模拟、执行shell命令、安装卸载应用等UI测试核心能力。
* **BY**对象用于描述需要操作的控件属性，实现控件定位。
* **IUiComponent**为UiDriver查找返回的控件对象，提供控件属性查询、控件点击、滑动查找等触控/检视能力。
* **UiWindow**为UiDriver查找返回的窗口对象，提供窗口属性查询、窗口拖动、大小调整等触控能力。

**示例代码**

```
1. # -*- coding: utf-8 -*-
2. from devicetest.core.test_case import TestCase, Step, CheckPoint
3. from hypium import *
4. from hypium.model import WindowFilter
5. class DemoCase(TestCase):
6. def __init__(self, configs):
7. self.TAG = self.__class__.__name__
8. TestCase.__init__(self, self.TAG, configs)
9. def setup(self):
10. pass

12. def process(self):
13. # 创建driver对象（self.device1对象在测试用例类中提供）
14. driver = UiDriver(self.device1)
15. # 查找控件
16. component = driver.find_component(BY.text("蓝牙"))
17. # 查找窗口
18. window = driver.find_window(WindowFilter().bundle_name("com.huawei.hmos.settings"))
19. def teardown(self):
20. pass
```

设备无关的API当前主要包括两个基础API类： **host** 和**CV**。

* **host** 提供基础值断言，PC端shell命令执行等PC端基础操作能力。
* **CV** 提供图像查找，图像比较，压缩，清晰度计算等基础图像操作能力。

**示例代码**

```
1. from hypium import host, CV

3. # 执行PC端命令
4. echo = host.shell("a.bat")
5. # 调用图像接口
6. brightness = CV.calculate_brightness("/path/to/image.jpeg")
```

此外Hypium还包含一些常量类型，例如**KeyCode，UiParam，MatchPattern**等，以及数据类型**Point，Rect**等。

**示例代码**

```
1. from hypium.model import KeyCode, UiParam, MatchPattern

3. # 按下电源键（使用常量KeyCode.POWER）
4. driver.press_key(KeyCode.POWER)
5. # 向左滑动屏幕（使用常量UiParam.LEFT）
6. driver.swipe(UiParam.LEFT)
```

下文各小节将详细介绍主要测试场景中Hypium的API的使用方法。

## API使用方法

* **控件查看**

通过 DevEco Testing Hypium插件中的 UiViewer 工具，可以查看界面控件的各项属性，有助于在后续测试用例开发中准确定位控件。具体使用方法请参考本文档的**“安装向导 -> DevEco Testing Hypium插件安装及使用方法**“小节。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/0friJdsKQUmOlm_RK0wVhw/zh-cn_image_0000002524623459.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=84D5732C2B7F0F8658009091A21B750345FB5ED1D245FC13FA75DB14FC34DB87 "点击放大")

* **控件查找**

Hypium 支持三种主要的控件定位方式：控件属性定位、图片匹配定位和比例坐标定位。

从定位的稳定性与可靠性来看，优先级如下：

* **首选：**控件属性定位（基于控件的属性信息精确定位）；
* **次选：**图片匹配定位（适用于属性不可用但界面稳定的场景）；
* **备用：**比例坐标定位（仅在前两种方式不可用时使用，受分辨率影响较大）。

控件属性定位通过BY选择器对象来实现。下文将详细介绍基于控件属性、图片匹配和比例坐标三种方式的控件定位方法。

**单属性定位控件**

从**hypium**包中导入BY选择器对象，从**hypium.model**包中导入匹配模式常量类**MatchPattern**。

```
1. from hypium import BY
2. from hypium.model import MatchPattern
```

通过BY对象描述需要查找或者操作的控件对象的属性，例如查找text属性为“蓝牙”的控件。

```
1. # 查找text属性为"控件文本"的控件。
2. component = driver.find_component(BY.text("蓝牙"))
3. # 读取控件的的边框位置。
4. bounds = component.getBounds()
5. # 直接点击控件。
6. component = driver.touch(BY.text("蓝牙"))
```

注意

默认情况下，find\_component和touch等方法会查找/操作第一个条件匹配的控件，如需操作第n个满足匹配条件的控件，请参考查找所有匹配控件。

当前字符串类型的控件属性支持以下五种**模糊匹配**方式，通过BY选择器方法的第二个可选参数指定，如下表所示：

| 序号 | 匹配方式常量 | 说明 |
| --- | --- | --- |
| 1 | MatchPattern.STARTS\_WITH | 前缀匹配 |
| 2 | MatchPattern.ENDS\_WITH | 后缀匹配 |
| 3 | MatchPattern.CONTAINS | 包含匹配 |
| 4 | MatchPattern.REGEXP | 正则表达式匹配 |
| 5 | MatchPattern.REGEXP\_ICASE | 正则表达式匹配（忽略大小写） |

```
1. # 点击text属性值前缀为“今天星期”的控件。
2. driver.touch(BY.text("今天星期", MatchPattern.STARTS_WITH))
```

BY选择器支持的所有属性如下表所示：

| 序号 | 属性名称 | 属性值类型 | 对应BY选择器 | 是否支持模糊匹配 |
| --- | --- | --- | --- | --- |
| 1 | text | str | BY.text | 是 |
| 2 | key | str | BY.key | 是 |
| 3 | type | str | BY.type | 是 |
| 4 | checkable | bool | BY.checkable | 否 |
| 5 | longClickable | bool | BY.longClickable | 否 |
| 6 | clickable | bool | BY.clickable | 否 |
| 7 | scrollable | bool | BY.scrollable | 否 |
| 8 | enabled | bool | BY.enabled | 否 |
| 9 | focused | bool | BY.focused | 否 |
| 10 | selected | bool | BY.selected | 否 |
| 11 | checked | bool | BY.checked | 否 |
| 12 | hint | str | BY.hint | 是 |

**多属性组合定位控件**

BY选择器支持链式调用，允许用户指定多个控件属性进行联合定位。当界面上存在多个控件的部分属性相同而其他属性不同时，可通过组合条件精确匹配目标控件。

```
1. # 点击文本为"蓝牙", 类型为"Button", 并且key为"bluetooth_switch"的按钮。
2. driver.touch(BY.text("蓝牙").type("Button").key("bluetooth_switch"))

4. # 查找文本为"蓝牙", 类型为"Button", 并且key为"bluetooth_switch"的按钮。
5. component = driver.find_component(BY.text("蓝牙").type("Button").key("bluetooth_switch"))
```

**控件相对位置+属性组合定位控件**

对于某些自身属性不唯一，无法精确定位的控件，BY选择器支持通过**与其他控件的相对位置关系**来定位控件。支持的相对定位方式如下表所示：

| 序号 | 相对位置定位接口 | 功能描述 |
| --- | --- | --- |
| 1 | BY.isBefore | 匹配在指定控件前边的控件。 |
| 2 | BY.isAfter | 匹配在指定控件后边的控件。 |
| 3 | BY.within | 匹配在指定控件内部的控件。 |
| 4 | BY.inWindow | 匹配在指定窗口内部的控件。 |

**注意：**  相对位置中的“前后”关系，对应控件树的前序遍历顺序（即深度优先遍历中根-子节点的访问次序），用户可以在 UiViewer 的可视化控件树中直观查看该顺序：控件在列表中从上到下的排列顺序，即为其在相对定位中的从前到后顺序。

相对位置通常和控件的属性结合使用来定位控件，以下图场景为例，界面上存在多个按钮，用户需要点击显示通知图标之后的按钮，定位方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wF6fZVy-RBGLrbuswokOnw/zh-cn_image_0000002524623441.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=99E6D136CF7E7D0A68EB3B3A5DF08F3C7F53C53B77D663C6729F398E24DA048A "点击放大")

1. 首先选择一个可以通过属性唯一定位的锚点控件。例如**BY.text("显示通知图标")**
2. 然后找到需要操作的目标控件，选择该控件的一个不唯一属性，通常为type属性。例如**BY.type("Button")**
3. 使用相对位置接口来描述锚点控件和目标控件的位置关系，得到完整的控件选择器。例如**BY.type("Button").isAfter(BY.text****("显示通知图标"))**，注意到这里组合使用了type属性和isAfter相对位置接口。

**示例代码**

```
1. # 查找在text属性为"显示通知图标"的控件之后的type属性为"Button"的控件。
2. component = driver.find_component(BY.type("Button").isAfter(BY.text("显示通知图标")))
```

```
1. # 查找在text属性为"账号"的控件之前的type属性为"Image"的控件。
2. component = driver.find_component(BY.type("Image").isBefore(BY.text("账号")))
```

```
1. # 查找在key为"nav_container"内部的类型为"Image"的控件。
2. component = driver.find_component(BY.type("Image").within(BY.key("nav_container")))
```

```
1. # 查找包名为"com.huawei.hmos.settings"的应用内部的text属性为"蓝牙"的控件。
2. component = driver.find_component(BY.text("蓝牙").inWindow("com.huawei.hmos.settings"))
```

注意

相对位置中的锚点控件**不能**再使用相对位置描述，即**BY.isBefore**方法的参数中不能再出现**BY.isBefore**或者**BY.isAfter**等相对定位的方式。

**XPath方式查找匹配的控件**

BY.xpath匹配器支持通过XPath语法来查找控件。部分控件没有唯一定位的属性，同时通过相对定位的方式也无法准确定位，推荐使用XPath语法来进行更精确的控件定位。

注意

XPath不能和其他属性匹配一起使用，通过XPath查找控件相比单属性和多属性查找控件的效率会有所下降。

在如下场景中，用户需要找到红框标识的图标，然而该图标没有唯一定位的属性，推荐使用XPath语法描述该控件相对其他可定位控件的路径关系来定位该控件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/kaPO8lURQDW6tosF680N4A/zh-cn_image_0000002492503760.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=08E5ED1DDEB479E0BC0AC5B7C1EF5D2805BC72AB35A6E35D9E31077F67F9931F "点击放大")

该页面上，“可用 WLAN”是一个固定的可唯一定位的文本，用户可以首先通过XPath定位到该文本**//\*[@text='可用 WLAN']**，然后定位到该文本控件所在的List控件**/ancestor::List**，然后从该List控件开始找到对应的Image控件**/ListItemGroup/ListItem[1]//Text/following::Image**。

**示例代码**

```
1. # 查找上图中红框所示的图标，并点击。
2. comp = driver.find_component(BY.xpath("//*[@text='可用 WLAN']/ancestor::List/ListItemGroup/ListItem[1]//Text/following::Image"))
3. comp.click()
```

在支持传入BY选择器的接口均可以使用XPath来定位控件。

```
1. # 查找text属性为WLAN的控件。
2. driver.find_component(BY.xpath("//*[@text='WLAN']"))
3. driver.find_all_components(BY.xpath("//*[@text='WLAN']"))
4. driver.wait_for_component(BY.xpath("//*[@text='WLAN']"))
5. # 点击text属性为WLAN的控件。
6. driver.touch(BY.xpath("//*[@text='WLAN']"))
```

**查找所有匹配控件**

默认情况下，**driver.find\_component**接口和其他支持传入BY选择器的接口会查找第一个匹配的控件进行操作。对于需要操作特定次序的匹配控件或所有匹配控件的场景，用户可以使用**driver.find\_all\_components**接口。

以如下场景为例，界面上存在多个Button，用户需要点击第2个特定的Button或点击所有Button时，可以使用**driver.find\_all\_components**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ENyC1FTeTSOsMXVJYPDaJQ/zh-cn_image_0000002524503477.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=68BE774C3056955E774E8C6640761EDAA0BCC3135700A9E12D2D6E37A5F8D34C "点击放大")

**示例代码**

```
1. # 查找所有type属性为"Button"的控件, 如果有匹配的结果，components为列表，包含多个满足条件的IUiComponent对象。
2. components = driver.find_all_components(BY.type("Button"))
3. # 点击所有的控件。
4. for component in components:
5. driver.touch(component)
6. # 点击第2个控件。
7. driver.touch(component[1])
```

**图片定位控件**

如果控件没有可用于定位的唯一属性，通过相对位置也无法实现定位，可以通过截取控件的图片，使用**driver.find\_image**查找控件的位置，或使用**driver.touch\_image**直接点击控件。

以如下场景为例，若红框中的控件没有可以唯一定位的属性，也无法通过与附近控件的相对位置定位，用户可以尝试使用图片匹配的方式定位控件，定位方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/AkGRCeKfQC65G8vSBSeFOA/zh-cn_image_0000002524623447.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=2EC2066FD415BB86E396F50686B640858DFF2DEFC322F11FA3F945EC7B4374F4 "点击放大")

1. 截取红框中图片保存到为template.jpeg（文件名根据需要定义）。
2. 调用driver.touch\_image，传入template.jpeg图片的路径。

注意

使用图片定位控件需要安装opencv-python包，使用如下命令安装：

python -m pip install opencv-python

**示例代码**

```
1. # 点击屏幕上和模板图片template.jpeg匹配的位置。
2. driver.touch_image("/path/to/template.jpeg")

4. # 查找屏幕上和模板图片template.jpeg匹配的位置, bounds为Rect类型，记录了控件上下左右边框的位置。
5. bounds = driver.find_image("template.jpeg")
6. print(bounds.top, bounds.left, bounds.bottom, bounds.right)
```

注意

当前仅支持查找匹配度最高的匹配的图片区域，不支持匹配多个目标。

**比例坐标定位控件**

如果图像特征不明显，使用图像匹配的方式也无法准确识别控件位置，用户可以通过比例坐标的方式点击控件。使用坐标的方式操作控件存在以下两个问题：

1. 在屏幕比例或者控件位置发生变化时该方法可能无法操作到预期的控件。

2. 当实际操作界面非预期页面时，点击也会成功，但实际执行效果不符合预期。

因此，在使用该方法时，建议用户在前一步或者后一步操作中通过控件属性定位控件，避免脚本未按照预期方式操作设备，但用例仍然可以执行通过的问题。

以下图场景为例，如果红框中的控件无法通过上述方式定位，用户可以采用比例坐标的方式点击。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/JmKMOevbTEySW7QbQ3ssNw/zh-cn_image_0000002524503469.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=8E48225FBBAB96D87FF43A41DC57095A6489FD91831A944AE4F919C43E7A19A9 "点击放大")

用户可以通过 UiViewer 工具的控件查看模式获取控件的比例坐标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/BYUoN43MQ2SjAHe157sIGg/zh-cn_image_0000002492343782.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=044CF485E3C02EE054F455C0835E0907595AE4FF625903F6243E48F0BA22B877)

```
1. # 点击屏幕上(0.52 * 屏幕宽度, 0.98 * 屏幕高度)的位置。
2. driver.touch((0.52, 0.98))
```

* **窗口查找**

**查找窗口**

```
1. def find_window(filter: WindowFilter) -> UiWindow
```

**接口说明**

根据指定条件查找窗口，返回窗口对象。

**参数说明**

| 参数名称 | 参数描述 |
| --- | --- |
| filter | 使用WindowFilter对象指定的窗口查找条件 |

**返回值**

如果找到window则返回UiWindow对象，否则返回None。

**使用示例**

```
1. # 查找标题为日历的窗口。
2. window = driver.find_window(WindowFilter().title("日历"))
3. # 查找包名为com.huawei.hmos.calendar，并且处于活动状态的窗口。
4. window = driver.find_window(WindowFilter().bundle_name("com.huawei.hmos.calendar").actived(True))
5. # 查找处于活动状态的窗口。
6. window = driver.find_window(WindowFilter().actived(True))
7. # 查找聚焦状态的窗口。
8. window = driver.find_window(WindowFilter().focused(True))
```

* **界面操作**

**Ⅰ.触摸屏**

**点击**

```
1. def touch(target: Union[ISelector, IUiComponent, tuple], mode: str = UiParam.NORMAL, scroll_target: Union[ISelector, IUiComponent] = None, wait_time: float = 0.1)
```

**接口说明**

根据选定的控件或坐标位置执行点击操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | target | 需要点击的目标，支持三种类型：  1. BY控件选择器  2. 控件对象  2. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 2 | mode | 点击模式，支持三种模式：  UiParam.NORMAL 点击  UiParam.LONG 长按（长按后放开）  UiParam.DOUBLE 双击。 |
| 3 | scroll\_target | 指定可滚动的控件，在该控件中滚动搜索指定的目标控件target，仅在target为BY选择器时有效。 |
| 4 | wait\_time | 点击后等待响应的时间，单位为秒，默认0.1秒。 |

**使用示例**

```
1. # 点击文本为"hello"的控件。
2. driver.touch(BY.text("hello"))
3. # 点击(100, 200)的位置。
4. driver.touch((100, 200))
5. # 点击比例坐标为(0.8, 0.9)的位置。
6. driver.touch((0.8, 0.9))
7. # 双击确认按钮(控件文本为"确认", 类型为"Button")。
8. driver.touch(BY.text("确认").type("Button"), mode=UiParam.DOUBLE)
9. # 在类型为Scroll的控件上滑动查找文本为"退出"的控件并点击。
10. driver.touch(BY.text("退出"), scroll_target=BY.type("Scroll"))
11. # 长按比例坐标为(0.8, 0.9)的位置。
12. driver.touch((0.8, 0.9), mode="long")
```

**长按**

```
1. def long_click(self, target: Union[ISelector, IUiComponent, tuple], press_time: float = 2, offset=None):
```

**接口说明**

执行长按操作。

**注意：**该接口仅DevEco Testing Hypium 6.0.5.200以及更新的版本支持。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | target | 需要点击的目标，可以为控件查找条件，控件对象或者屏幕坐标(通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 2 | press\_time | 长按时间，单位为秒。 |
| 3 | offset | 点击坐标在目标控件区域的偏移值。不设置时该参数时默认为(0.5, 0.5), 表示控件中心。支持设置范围是0到1，如(0.1, 0.1)表示点击目标左上角为坐标原点x方向10%，y方向10%的位置。 |

**使用示例**

```
1. # 长按文本为"按钮"的控件5秒
2. driver.long_click(BY.text("按钮"), press_time=5)
3. # 长按(100, 200)的位置5秒
4. driver.long_click((100, 200), press_time=5)
5. # 长按文本为"设置"的控件左上角(偏移0, 0)
6. driver.long_click(BY.text("设置"), offset=(0, 0))
```

**多指点击**

```
1. def multi_finger_touch(points: List[tuple], duration: float = 0.1, area: Rect = None)
```

**接口说明**

执行多指点击操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | points | 需要点击的坐标位置列表，每个坐标对应一个手指，例如[(0.1, 0.2), (0.3, 0.4)]，最多支持4指点击。 |
| 2 | duration | 按下/抬起的时间，可实现多指长按操作，单位秒。 |
| 3 | area | 点击操作的区域，当起始结束坐标为(0.1, 0.2)等相对比例坐标时生效，默认为操作区域为全屏。 |

**使用示例**

```
1. # 执行多指点击操作, 同时点击屏幕(0.1, 0.2), (0.3, 0.4)的位置。
2. driver.multi_finger_touch([(0.1, 0.2), (0.3, 0.4)])
3. # 执行多指点击操作, 设置点击按下时间为1秒。
4. driver.multi_finger_touch([(0.1, 0.2), (0.3, 0.4)], duration=2)
5. # 查找Image类型控件。
6. comp = driver.find_component(BY.type("Image"))
7. # 在指定的控件区域内执行多指点击(点击坐标为控件区域内的比例坐标)。
8. driver.multi_finger_touch([(0.5, 0.5), (0.6, 0.6)], area=comp.getBounds())
```

**滑动**

**执行指定方向的滑动操作**

```
1. def swipe(direction: str, distance: int = 60, area: Union[ISelector, IUiComponent] = None, side: str = None, start_point: tuple = None, swipe_time: float = 0.3)
```

**接口说明**

在屏幕上或者指定区域中执行朝向指定方向的滑动操作。该接口用于无需指定精确起始和结束坐标的滑动操作场景。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | direction | 滑动方向，目前支持：  UiParam.LEFT 左滑  UiParam.RIGHT 右滑  UiParam.UP 上滑  UiParam.DOWN 下滑 |
| 2 | distance | 相对滑动区域总长度的滑动距离，范围为1-100，表示滑动长度为滑动区域总长度的1%到100%， 默认为60。 |
| 3 | area | 通过控件指定的滑动区域，默认为None表示滑动区域为整个屏幕。 |
| 4 | side | 滑动位置， 指定滑动区域内部（屏幕内部）执行操作的大概位置，支持：  UiParam.LEFT 靠左区域  UiParam.RIGHT 靠右区域  UiParam.TOP 靠上区域  UiParam.BOTTOM 靠下区域 |
| 5 | start\_point | 滑动起始点，默认为None，表示在区域中间位置执行滑动操作，可以传入滑动起始点坐标，支持使用比例坐标，例如(0.5, 0.5)。  当同时传入side和start\_point的时候，仅start\_point生效。 |
| 6 | swipe\_time | 滑动时间，单位为秒， 默认0.3秒。 |

**使用示例**

```
1. # 在屏幕上向上滑动, 距离40。
2. driver.swipe(UiParam.UP, distance=40)
3. # 在屏幕上向右滑动, 滑动时间为0.1秒。
4. driver.swipe(UiParam.RIGHT, swipe_time=0.1)
5. # 在屏幕起始点为比例坐标为(0.8, 0.8)的位置向上滑动，距离30。
6. driver.swipe(UiParam.UP, 30, start_point=(0.8, 0.8))
7. # 在屏幕左边区域向下滑动， 距离30。
8. driver.swipe(UiParam.DOWN, 30, side=UiParam.LEFT)
9. # 在屏幕右侧区域向上滑动，距离30。
10. driver.swipe(UiParam.UP, side=UiParam.RIGHT)
11. # 在类型为Scroll的控件中向上滑动。
12. driver.swipe(UiParam.UP, area=BY.type("Scroll"))
```

**执行指定起始结束位置的精确滑动操作**

```
1. def slide(start: Union[ISelector, tuple], end: Union[ISelector, tuple], area: Union[ISelector, IUiComponent] = None, slide_time: float = 0.3)
```

**接口说明**

根据指定的起始和结束位置执行滑动操作，起始和结束的位置可以为控件或屏幕坐标。该接口用于执行精准的滑动操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start | 滑动起始位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 2 | end | 滑动结束位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 3 | area | 滑动操作区域。指定区域后，当start或end参数为坐标类型时，其坐标被视为相对于该指定的区域的相对位置坐标。 |
| 4 | slide\_time | 滑动时间，单位为秒，默认为0.3秒。 |

**使用示例**

```
1. # 从类型为Slider的控件滑动到文本为最大的控件
2. driver.slide(BY.type("Slider"), BY.text("最大"))
3. # 从坐标100, 200滑动到300，400
4. driver.slide((100, 200), (300, 400))
5. # 从坐标100, 200滑动到300，400, 滑动时间为3秒
6. driver.slide((100, 200), (300, 400), slide_time=3)
7. # 在类型为Slider的控件上从(0, 0)滑动到(100, 0)
8. driver.slide((0, 0), (100, 0), area = BY.type("Slider"))
```

**拖拽**

```
1. def drag(start: Union[ISelector, tuple, IUiComponent], end: Union[ISelector, tuple, IUiComponent], area: Union[ISelector, IUiComponent] = None, press_time: float = 1, drag_time: float = 1)
```

**接口说明**

根据指定的起始和结束位置执行拖拽操作，起始和结束的位置可以为控件或者屏幕坐标。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start | 拖拽起始位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定的坐标，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标；或相对于区域长度和宽度的比例坐标，例如(0.1, 0.2)。) |
| 2 | end | 拖拽结束位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定的坐标，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标；或相对于区域长度和宽度的比例坐标，例如(0.1, 0.2)。) |
| 3 | area | 拖拽操作区域，指定区域后，当start或end参数为坐标类型时，其坐标被视为相对于该指定的区域的相对位置坐标。 |
| 4 | press\_time | 拖拽操作开始时，长按的时间，单位为秒，默认为1.5秒。  **注意：** 该参数为可选参数，仅DevEco Testing Hypium 6.0.5.200及更新的版本，且配套测试设备的API level >= 20时支持。 |
| 5 | drag\_time | 拖动的时间，单位秒， 默认为1秒（拖拽操作总时间 = press\_time + drag\_time）。 |

**使用示例**

```
1. # 拖拽文本为"文件.txt"的控件到文本为"上传文件"的控件。
2. driver.drag(BY.text("文件.txt"), BY.text("上传文件"))
3. # 拖拽id为"start_bar"的控件到坐标(100, 200)的位置, 拖拽时间为2秒。
4. driver.drag(BY.key("start_bar"), (100, 200), drag_time=2)
5. # 在id为"Canvas"的控件上执行拖拽操作，从"Canvas"控件中(0.1, 0.5)的位置拖拽到(0.9, 0.5)位置。
6. # 假如"Canvas"控件左上角坐标(100, 100), 宽度为200，高度为50，此操作等价于
7. # driver.drag((100 + 0.1 * 200, 100 + 0.5 * 50), (100 + 0.9 * 200, 100 + 0.5 * 50))。
8. driver.drag((0.1, 0.5), (0.9, 0.5), area=BY.id("Canvas"))
9. # 在滑动条上执行拖拽操作, 以滑动条组件左上角为原点, 从滑动条区域中的(10, 10)拖拽到(10, 200)。
10. # 假设滑动条左上角坐标为(500, 500), 此操作等价于driver.drag((500 + 10, 500 + 10), (500 + 10, 500 + 200))。
11. driver.drag((10, 10), (10, 200), area=BY.type("Slider"))
```

**捏合缩小**

```
1. def pinch_in(area: Union[ISelector, IUiComponent, Rect], scale: float = 0.4, direction: str = "diagonal", **kwargs)
```

**接口说明**

在指定控件上执行双指捏合缩小操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | area | 手势操作执行的区域，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕区域，通过Rect类型指定，例如 Rect(left, right, top, bottom)，其中 left，right，top，bottom 为区域左右上下的坐标值。 |
| 2 | scale | 缩放的比例，范围(0, 1)，值越小表示缩放操作距离越长，缩小的越多。 |
| 3 | direction | 双指缩放时缩放操作方向，当前支持：  "diagonal" 对角线滑动  "horizontal" 水平滑动 |
| 4 | kwargs | 其他可选滑动配置参数：  dead\_zone\_ratio 缩放操作时控件靠近边界不可操作的区域占控件长度/宽度的比例，默认为0.2，调节范围为(0, 0.5)。 |

**使用示例**

```
1. # 在类型为Image的控件上进行双指捏合缩小操作。
2. driver.pinch_in(BY.type("Image"))
3. # 在类型为Image的控件上进行双指捏合缩小操作, 设置水平方向捏合。
4. driver.pinch_in(BY.type("Image"), direction="horizontal")
```

**双指放大**

```
1. def pinch_out(area: Union[ISelector, IUiComponent, Rect], scale: float = 1.6, direction: str = "diagonal", **kwargs)
```

**接口说明**

在指定控件上执行双指放大操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | area | 手势操作执行的区域，支持三种类型：  1. BY控件选择器  2. 控件对象  2. 屏幕区域，通过Rect类型指定，例如 Rect(left, right，top, bottom)，其中 left，right，top，bottom 为区域左右上下的坐标值。 |
| 2 | scale | 缩放的比例，范围 (1, 2)，值越大表示缩放操作滑动的距离越长。 |
| 3 | direction | 双指缩放时缩放操作方向，当前支持：  "diagonal" 对角线滑动  "horizontal" 水平滑动 |
| 4 | kwargs | 其他可选滑动配置参数：  dead\_zone\_ratio 缩放操作时控件靠近边界不可操作的区域占控件长度/宽度的比例，默认为0.2，调节范围为(0, 0.5)。 |

**使用示例**

```
1. # 在类型为Image的控件上进行双指放大操作。
2. driver.pinch_out(BY.type("Image"))
3. # 在类型为Image的控件上进行双指捏合缩小操作, 设置水平方向捏合。
4. driver.pinch_out(BY.type("Image"), direction="horizontal")
```

**双指滑动**

```
1. def two_finger_swipe(start1: tuple, end1: tuple, start2: tuple, end2: tuple, duration: float = 0.5, area: Rect = None)
```

**接口说明**

执行双指滑动操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start1 | 手指1起始坐标 |
| 2 | end1 | 手指1结束坐标 |
| 3 | start2 | 手指2起始坐标 |
| 4 | end2 | 手指2结束坐标 |
| 5 | duration | 滑动操作持续时间，单位为秒，默认0.5秒。 |
| 6 | area | 滑动操作的区域，当起始结束坐标为(0.1, 0.2)等相对比例坐标时生效，默认为操作区域为全屏。 |

**使用示例**

```
1. # 执行双指滑动操作, 手指1从(0.4, 0.4)滑动到(0.2, 0.2), 手指2从(0.6, 0.6)滑动到(0.8, 0.8)。
2. driver.two_finger_swipe((0.4, 0.4), (0.2, 0.2), (0.6, 0.6), (0.8, 0.8))
3. # 执行双指滑动操作, 手指1从(0.4, 0.4)滑动到(0.2, 0.2), 手指2从(0.6, 0.6)滑动到(0.8, 0.8), 持续时间3秒。
4. driver.two_finger_swipe((0.4, 0.4), (0.2, 0.2), (0.6, 0.6), (0.8, 0.8), duration=3)
5. # 查找Image类型控件。
6. comp = driver.find_component(BY.type("Image"))
7. # 在指定的控件区域内执行双指滑动(滑动起始/停止坐标为控件区域内的比例坐标)。
8. driver.two_finger_swipe((0.4, 0.4), (0.1, 0.1), (0.6, 0.6), (0.9, 0.9), area=comp.getBounds())
```

**自定路径滑动手势（单指）**

```
1. def inject_gesture(gesture: Gesture, speed: int = 2000)
```

**接口说明**

执行自定义滑动手势操作。

**参数说明**

| 序列 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | gesture | 描述手势操作的Gesture对象。 |
| 2 | speed | 默认操作速度，单位像素/秒，默认值为2000像素/秒，当生成Gesture对象的步骤中未传入操作时间时默认使用该速度进行操作。 |

**使用示例**

```
1. from hypium.uidriver import Gesture

3. # 创建一个gesture对象。
4. gesture = Gesture()
5. # 获取控件计算器的位置。
6. pos = driver.findComponent(BY.text("计算器")).getBoundsCenter()
7. # 获取屏幕尺寸。
8. size = driver.getDisplaySize()
9. # 起始位置, 长按2秒。
10. gesture.start(pos.to_tuple(), 2)
11. # 移动到屏幕边缘。
12. gesture.move_to(Point(size.X - 20, int(size.Y / 2)).to_tuple())
13. # 停留2秒。
14. gesture.pause(2)
15. # 移动到(360, 500)的位置。
16. gesture.move_to(Point(360, 500).to_tuple())
17. # 停留2秒结束。
18. gesture.pause(2)
19. # 执行gesture对象描述的操作。
20. driver.inject_gesture(gesture)
```

**自定路径滑动手势(多指)**

```
1. def inject_multi_finger_gesture(gestures: List[Gesture], speed: int = 6000)
```

**接口说明**

注入多指手势操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | gestures | 表示单指手势操作的Gesture对象列表，每个Gesture对象描述一个手指的操作轨迹，最多4指。  注意如果各个手势持续时间不同，时间短的手势操作会保持在结束位置，等待所有手势完成后抬起对应手指。 |
| 2 | speed | Gesture对象的步骤未设置时间时，使用该速度计算时间，单位为像素/秒，默认为6000像素/秒。 |

**使用示例**

```
1. from hypium.uidriver import Gesture
2. # 创建手指1的手势, 从(0.4, 0.4)的位置移动到(0.2, 0.2)的位置。
3. gesture1 = Gesture().start((0.4, 0.4)).move_to((0.2, 0.2), interval=1)
4. # 创建手指2的手势, 从(0.6, 0.6)的位置移动到(0.8, 0.8)的位置。
5. gesture2 = Gesture().start((0.6, 0.6)).move_to((0.8, 0.8), interval=1)
6. # 注入多指操作。
7. driver.inject_multi_finger_gesture((gesture1, gesture2))
```

**Ⅱ. 键盘鼠标**

**鼠标点击**

```
1. def mouse_click(pos: Union[tuple, IUiComponent, ISelector], button_id: MouseButton = MouseButton.MOUSE_BUTTON_LEFT, key1: Union[KeyCode, int] = None, key2: Union[KeyCode, int] = None)
```

**接口说明**

执行鼠标点击操作, 支持键鼠组合操作。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | pos | 点击的位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。) |
| 2 | button\_id | 需要点击的鼠标按键。 |
| 3 | key1 | 需要组合按下的第一个键盘按键。 |
| 4 | key2 | 需要组合按下的第二个键盘按键。 |

**使用示例**

```
1. # 使用鼠标左键点击(100, 200)的位置。
2. driver.mouse_click((100, 200), MouseButton.MOUSE_BUTTON_LEFT)
3. # 使用鼠标右键点击文本为"确认"的控件。
4. driver.mouse_click(BY.text("确认"), MouseButton.MOUSE_BUTTON_RIGHT)
5. # 使用鼠标右键点击比例坐标(0.8, 0.5)的位置。
6. driver.mouse_click((0.8, 0.5), MouseButton.MOUSE_BUTTON_RIGHT)
```

**鼠标拖拽**

```
1. def mouse_drag(start: Union[tuple, IUiComponent, ISelector], end: Union[tuple, IUiComponent, ISelector], speed: int = 3000)
```

**接口说明**

执行鼠标拖拽操作（即按住鼠标左键并移动鼠标）。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start | 起始位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。) |
| 2 | end | 结束位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。) |
| 3 | speed | 鼠标移动速度，像素/秒，默认3000像素/秒。 |

**使用示例**

```
1. # 鼠标从控件1拖拽到控件2。
2. driver.mouse_drag(BY.text("控件1"), BY.text("控件2"))
```

**鼠标移动**

```
1. def mouse_move(start: Union[tuple, IUiComponent, ISelector], end: Union[tuple, IUiComponent, ISelector], speed: int = 3000)
```

**接口说明**

将鼠标指针从指定起始位置移动到结束位置，模拟移动轨迹和移动速度。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | start | 起始位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 2 | end | 结束位置，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 3 | speed | 鼠标移动速度，像素/秒，默认3000像素/秒。 |

**使用示例**

```
1. # 鼠标从控件1移动到控件2。
2. driver.mouse_move(BY.text("控件1"), BY.text("控件2"))
```

**按键**

```
1. def press_key(key_code: Union[KeyCode, int], key_code2: Union[KeyCode, int] = None, mode="normal")
```

**接口说明**

执行按键操作（注意不推荐使用该接口实现组合按键模拟，模拟组合按键键请使用press\_combination\_key）。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | key\_code | 需要按下的按键编码。 |
| 2 | key\_code2 | 需要按下的按键编码。 |
| 3 | mode | 按键模式，仅在进行单个按键时支持，当前支持以下模式：  UiParam.NORMAL 单击  UiParam.LONG 长按  UiParam.DOUBLE 双击 |

**使用示例**

```
1. # 按下电源键。
2. driver.press_key(KeyCode.POWER)
3. # 长按电源键。
4. driver.press_key(KeyCode.POWER, mode=UiParam.LONG)
5. # 按下音量下键。
6. driver.press_key(KeyCode.VOLUME_DOWN)
```

**按组合键**

```
1. def press_combination_key(key1: Union[KeyCode, int], key2: Union[KeyCode, int], key3: Union[KeyCode, int] = None)
```

**接口说明**

执行组合键操作，支持2键或3键组合。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | key1 | 组合键第一个按键 |
| 2 | key2 | 组合键第二个按键 |
| 3 | key3 | 组合键第三个按键 |

**使用示例**

```
1. # 按下音量下键和电源键的组合键
2. driver.press_combination_key(KeyCode.VOLUME_DOWN, KeyCode.POWER)
3. # 同时按下ctrl, shift和F键
4. driver.press_combination_key(KeyCode.CTRL_LEFT, KeyCode.SHIFT_LEFT, KeyCode.F)
```

* **hdc/shell命令执行**

**hdc命令执行**

```
1. def hdc(cmd, timeout: float = 60) -> str
```

**接口说明**

执行hdc命令。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | cmd | 需要执行的hdc命令。 |
| 2 | timeout | 超时时间，单位秒，默认60秒。 |

**返回值**

命令执行后的回显内容。

**使用示例**

```
1. # 执行hdc命令list targets。
2. echo = driver.hdc("list targets")
3. # 执行hdc命令hilog, 设置30秒超时。
4. echo = driver.hdc("hilog", timeout = 30)
```

**设备侧shell命令执行**

```
1. def shell(cmd: str, timeout: float = 60) -> str
```

**接口说明**

在设备端shell中执行命令。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | cmd | 需要执行的shell命令。 |
| 2 | timeout | 超时时间，单位秒，默认60秒。 |

**返回值**

命令执行后的回显内容。

**使用示例**

```
1. # 在设备shell中执行命令ls -l。
2. echo = driver.shell("ls -l")
3. # 在设备shell中执行命令top, 设置10秒超时时间。
4. echo = driver.shell("top", timeout=10)
```

**PC侧shell命令执行**

```
1. def shell(cmd: Union[str, list], timeout: float = 300) -> str
```

**接口说明**

在PC端执行shell命令。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | cmd | 需要执行的命令内容。 |
| 2 | timeout | 超时时间，单位秒，默认300秒。 |

**使用示例**

```
1. # 在PC端执行dir命令。
2. echo = host.shell("dir")
3. # 在PC端执行netstat命令读取回显结果, 设置超时时间为10秒。
4. echo = host.shell("netstat", timeout=10)
```

* **应用预置操作**

**安装应用**

```
1. def install_app(package_path: str, options: str = "", **kwargs)
```

**接口说明**

安装指定应用安装包。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | package\_path | PC端保存的安装包路径。 |
| 2 | options | 传递给bm install命令的额外参数。 |

**使用示例**

```
1. # 安装路径为test.hap的安装包到手机。
2. driver.install_app(r"test.hap")
3. # 替换安装路径为test.hap的安装包到手机(增加-r参数指定替换安装)。
4. driver.install_app(r"test.hap", "-r")
```

**卸载应用**

```
1. def uninstall_app(package_name: str, **kwargs)
```

**接口说明**

卸载指定包名应用。

**参数说明**

| 参数名称 | 参数描述 |
| --- | --- |
| package\_name | 需要卸载的应用包名 |

**使用示例**

```
1. # 卸载包名为com.test.myapp的应用。
2. driver.uninstall_app("com.test.myapp")
```

**清除应用缓存数据**

```
1. def clear_app_data(package_name: str)
```

**接口说明**

清除应用的缓存数据。

**参数说明**

| 参数名称 | 参数描述 |
| --- | --- |
| package\_name | 需要清除缓存的应用包名（bundle name） |

**使用示例**

```
1. # 清除包名为com.test.myapp的应用的缓存数据。
2. driver.clear_app_data("com.test.myapp")
```

**启动应用**

```
1. def start_app(package_name: str, page_name: str = None, params: str = "", wait_time: float = 1)
```

**接口说明**

根据包名启动指定的应用。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | package\_name | 应用程序包名(bundle name)。 |
| 2 | page\_name | 应用内页面名称(ability name)。 |
| 3 | params | 其他传递给aa命令的参数。 |
| 4 | wait\_time | 发送启动指令后，等待应用启动的时间，单位为秒，默认为1秒。 |

**使用示例**

```
1. # 启动浏览器。
2. driver.start_app("com.huawei.hmos.browser", "MainAbility")
```

**停止应用**

```
1. def stop_app(package_name: str, wait_time: float = 0.5)
```

**接口说明**

停止指定包名的应用。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | package\_name | 应用程序包名。 |
| 2 | wait\_time | 停止应用后等待的时间，单位为秒，默认为0.5秒。 |

**使用示例**

```
1. # 停止包名为com.huawei.hmos.settings的应用。
2. driver.stop_app("com.huawei.hmos.settings")
```

* **文件拉取/推送**

**拉取文件**

```
1. def pull_file(device_path: str, local_path: str = None, timeout: int = 60)
```

**接口说明**

从设备端的传输文件到PC端。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | device\_path | 设备侧保存文件的路径。 |
| 2 | local\_path | PC侧保存文件的路径。 |
| 3 | timeout | 拉取文件超时时间，单位秒，默认60秒。 |

**使用示例**

```
1. # 从设备中拉取文件"/data/local/tmp/test.log"保存到PC端的test.log。
2. driver.pull_file("/data/local/tmp/test.log", "test.log")
```

**推送文件**

```
1. def push_file(local_path: str, device_path: str, timeout: int = 60)
```

**接口说明**

从PC端传输文件到设备端。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | local\_path | PC侧文件的路径。 |
| 2 | device\_path | 设备侧文件的路径。 |
| 3 | timeout | 推送文件超时时间，单位秒，默认60秒。 |

**使用示例**

```
1. # 从PC端推送文件test.hap保存到设备端的"/data/local/tmp/test.hap"。
2. driver.push_file("test.hap", "/data/local/tmp/test.hap")
```

**查询文件是否存在**

```
1. def has_file(file_path: str) -> bool
```

**接口说明**

查询设备中是否有存在路径为file\_path的文件。

**参数说明**

| 参数名称 | 参数描述 |
| --- | --- |
| file\_path | 需要检查的设备端文件路径。 |

**使用示例**

```
1. # 查询设备端是否存在文件/data/local/tmp/test_file.txt。
2. driver.has_file("/data/local/tmp/test_file.txt")
```

* **文本输入/清除**

**输入文本**

```
1. def input_text(component: Union[ISelector, IUiComponent, tuple], text: str, mode: InputTextMode = None):
```

**接口说明**

向指定控件中输入文本内容。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | component | 需要输入文本的控件，支持三种类型：  1. BY控件选择器  2. 控件对象  3. 屏幕坐标（通过tuple类型指定，例如(100, 200)， 其中100为x轴坐标，200为y轴坐标。） |
| 2 | text | 需要输入的文本。 |
| 3. | mode | 输入模式配置，默认模式操作如下：  1. 默认清空指定的控件中的文本后再执行输入。  2. 英文字符长度<200时，逐个输入，超过200时，通过剪切板粘贴一次输入。  3. 中文文本通过剪切板粘贴一次输入。  通过该参数可以配置：  1. 追加输入：InputTextMode().addition(True)。  2. 输入英文时，不考虑文本长度直接使用剪切板快速输入：InputTextMode().paste(True)。  **注意**：该参数为可选参数，仅DevEco Testing Hypium 6.0.5.200以及更新的版本，且配套测试设备的API level >= 20支持。 |

使用示例

```
1. from hypium import BY
2. from hypium.model import InputTextMode
3. # 在类型为"TextInput"的控件中输入文本"hello world"。
4. driver.input_text(BY.type("TextInput"), "hello world")
5. # 在类型为"TextInput"的控件中使用剪切板一次性输入文本"hello world"。
6. driver.input_text(BY.type("TextInput"), "hello world", mode=InputTextMode().paste(True))
7. # 在类型为"TextInput"的控件中使用剪切板一次性并追加输入文本"hello world"。
8. driver.input_text(BY.type("TextInput"), "hello world", mode=InputTextMode().paste(True).addition(True))
```

**清除文本**

```
1. def clear_text(component: [ISelector, IUiComponent])
```

**接口说明**

清空指定控件中的文本内容。

**参数说明**

| 参数名称 | 参数描述 |
| --- | --- |
| component | 需要清除文本的控件 |

使用示例

```
1. # 清除类型为"InputText"的控件中的内容。
2. driver.clear_text(BY.type("InputText"))
```

* **断言**

**Ⅰ. 常规断言**

**检查是否相等**

```
1. def check_equal(value: Any, expect: Any = True, fail_msg: str = None, expect_equal=True)
```

**接口说明**

检查实际值和期望值相等，在不一致时抛出异常，并打印fail\_msg。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | value | 实际值，如果为list或者tuple，将取其中每个值同expect中的每个值进行比较。 |
| 2 | expect | 期望值， 如果为list或者tuple，将取其中每个值同value中的每个值进行比较。 |
| 3 | fail\_msg | 断言失败时打印的提示信息。 |

**使用示例**

```
1. # 检查a等于b。
2. host.check_equal(a, b, "a != b")
```

**检查是否超过预期值**

```
1. def check_greater(value: Any, expect: Any, fail_msg: str = None)
```

**接口说明**

检查value是否大于expect，不满足时抛出异常，并在日志中打印fail\_msg。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | value | 实际值 |
| 2 | expect | 期望值 |
| 3 | fail\_msg | 断言失败时打印的提示信息 |

**使用示例**

```
1. # 检查a大于b
2. host.check_greater(a, b)
```

**Ⅱ. 控件断言**

**检查控件是否存在**

```
1. def check_component_exist(component: ISelector, expect_exist: bool = True, wait_time: int = 0, scroll_target: Union[ISelector, IUiComponent] = None)
```

**接口说明**

检查指定控件在当前界面是否存在。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | component | 待检查的UI控件，使用BY选择器指定。 |
| 2 | expect\_exist | 是否期望控件存在，True表示期望控件存在，False表示期望控件不存在。 |
| 3 | wait\_time | 检查过程中等待控件出现的时间，单位秒，默认为0。 |
| 4 | scroll\_target | 需要上下滚动检查目标控件时滑动的控件，默认为None，表示不进行滑动查找。 |

**使用示例**

```
1. # 检查类型为Button的控件存在。
2. driver.check_component_exist(BY.type("Button"))
3. # 检查类型为Button的控件存在，如果不存在等待最多5秒。
4. driver.check_component_exist(BY.type("Button"), wait_time=5)
5. # 在类型为Scroll的控件上滚动检查文本为"hello"的控件存在。
6. driver.check_component_exist(BY.text("hello"), scroll_target=BY.type("Scroll"))
7. # 检查文本为确认的控件不存在。
8. driver.check_component_exist(BY.text("确认"), expect_exist=False)
```

**检查控件属性**

```
1. def check_component(component: Union[ISelector, IUiComponent], expected_equal: bool = True, **kwargs)
```

**接口说明**

检查当前界面上指定控件的属性是否符合预期。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | component | 需要检查的控件，支持BY选择器或控件对象。 |
| 2 | expected\_equal | 预期值和实际值是否相等，True表示预期相等，False表示预期不相等。 |
| 3 | kwargs | 指定预期的控件属性值，目前支持：  "id"，"text"，"key"，"type"，"enabled"，"focused"，"clickable"，"scrollable"  "checked"，"checkable"。 |

**使用示例**

```
1. # 检查id为xxx的控件的checked属性为True。
2. driver.check_component(BY.key("xxx"), checked=True)
3. # 检查id为check_button的按钮enabled属性为True。
4. driver.check_component(BY.key("checked_button"), enabled=True)
5. # 检查id为container的控件文本内容为“正在检查”。
6. driver.check_component(BY.key("container"), text="正在检查")
7. # 检查id为container的控件文本内容不为空。
8. driver.check_component(BY.key("container"), text="", expect_equal=False)
```

**检查图片是否存在**

```
1. def check_image_exist(image_path_pc: str, expect_exist: bool = True, similarity: float = 0.95, timeout: int = 3, mode="template", **kwargs)
```

**接口说明**

使用图片模板匹配算法检测当前屏幕截图中是否有指定图片，需要保证模板图片的分辨率和屏幕截图中目标图像的分辨率一致。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | image\_path\_pc | 待检查的图片路径（图片保存在PC端）。 |
| 2 | expect\_exist | 是否期望图片在设备屏幕上存在，True表示期望控件存在，False表示期望控件不存在。 |
| 3 | similarity | 图像匹配算法比较图片时使用的相似度，范围[0, 1]。 |
| 4 | timeout | 检查的总时间，每秒会进行获取一次屏幕截图检查指定图片是否存在，通过timeout可指定检查的次数。 |
| 5 | mode | 图片匹配模式，支持"template"和"sift"，图片分辨率/旋转变化对sift模式影响相对较小，但sift模式难以处理缺少较复杂图案的纯色，无线条图片。 |
| 6 | kwargs | 其他配置参数：  min\_match\_point： 最少匹配特征点数，值越大匹配越严格，默认为16，仅sift模式有效。 |

**使用示例**

```
1. # 检查图片存在。
2. driver.check_image_exist("test.jpeg")
3. # 检查图片不存在。
4. driver.check_image_exist("test.jpeg", expect_exist=False)
5. # 检查图片存在, 图片相似度要求95%, 重复检查时间5秒。
6. driver.check_image_exist("test.jpeg", timeout=5, similarity=0.95)
7. # 检查图片不存在, 重复检查时间5秒。
8. driver.check_image_exist("test.jpeg", timeout=5, expect_exist=False)
9. # 使用sift算法检查图片存在, 设置最少匹配特征点数量为16。
10. driver.check_image_exist("test.jpeg", mode="sift", min_match_point=16)
```

**Ⅲ. 窗口断言**

**检查窗口**

```
1. def check_window(window: WindowFilter, title: str = None, bundle_name: str = None)
```

**接口说明**

检查指定的window的属性是否符合预期。

**参数说明**

| 序号 | 参数名称 | 参数描述 |
| --- | --- | --- |
| 1 | title | 预期的窗口标题，None表示不检查。 |
| 2 | bundle\_name | 预期窗口所属的应用包名，None表示不检查。 |

**使用示例**

```
1. # 检查当前焦点窗口的包名为com.huawei.hmos.settings。
2. driver.check_window(WindowFilter().focused(True), bundle_name="com.huawei.hmos.settings")
```

* **日志打印**

用户使用以下方法可以在测试用例脚本中打印日志，日志会记录到测试报告中。

```
1. from devicetest.core.test_case import Step, CheckPoint, MESSAGE

3. Step("点击按钮")
4. CheckPoint("检查联系人存在")
5. MESSAGE("打印一条提示消息")
```

在自定义实现的接口中，可以调用driver对象中的log模块打印日志消息，对应日志也会记录到测试报告中。

```
1. driver.log.debug("debug级别的日志")
2. driver.log.info("info级别的日志")
3. driver.log.warning("warning级别的日志")
4. driver.log.error("error级别的日志")
```

* **读取测试项目中资源文件路径**

用户可通过以下接口读取测试工程资源目录中的文件路径。接口接收文件名或相对路径作为参数，搜索测试工程资源文件目录并返回文件的完整路径。若未找到对应文件，则抛出异常。

```
1. from devicetest.utils import file_util
2. file_path = file_util.get_resource_path("filename")
```

该接口默认搜索文件，开发者可以设置isdir=True来搜索目录路径。

```
1. dir_path = file_util.get_resource_path("dirname", isdir=True)
```

## 隐私协议

**概述**

DevEco Testing Hypium(以下简称Hypium)是由华为终端有限公司（以下简称“我们”或“华为”）提供的UI自动化测试框架。华为非常重视您的个人信息和隐私保护，我们将会按照法律要求和业界成熟的安全标准，为您的个人信息提供相应的安全保护措施。

**1** **我们如何收集和使用您的个人信息**

我们将通过Hypium为您提供下述业务功能，在您使用相关业务功能的过程中，我们会处理下列提供功能所必需的信息，以便履行我们的合同义务。若您不提供相关信息，会影响到您使用本应用的相关功能。

**运行Hypium**

在您使用Hypium的过程中，我们会收集执行设备的操作系统平台和版本号，用于更好的提供和执行平台适配的测试服务。

**测试鸿蒙设备**

当您使用Hypium测试鸿蒙设备上的应用时，我们会收集被测设备的型号以及鸿蒙系统版本、被测应用的名称或者包名、Hypium特性功能的触发时间和使用次数，用于分析Hypium各功能在不同平台上的使用情况，从而针对性的优化我们的产品，更好的为客户提供服务。

**2** **对未成年人的保护**

我们非常重视对未成年人个人信息的保护，华为将严格按照国家法律法规要求在未成年人使用服务时提供相应的保护。如果您是未成年人，需要您的父母或其他监护人同意您使用本应用并同意相关应用的服务条款。父母或其他监护人也应采取适当的预防措施来保护未成年人，包括监督其对本应用的使用。如您是儿童，请务必退出使用本应用。

**3** **管理您的个人信息**

华为非常尊重您对个人信息的关注，并为您提供了数据主体权利及选择。

**3.1** **信息访问**

如您希望收集和存储的您的个人信息及其副本，可通过本声明中“如何联系我们”章节中所述方式与我们取得联系，并获取您的个人信息及其副本。

**3.2** **信息更正**

当您需要更新您的个人信息，或发现我们处理您的个人信息有误时，您有权作出更正或更新。您可以通过本声明中“如何联系我们”章节中所述方式与我们取得联系，并修改您的个人信息。

**3.3** **信息删除**

您随时可以通过本声明中“如何联系我们”章节中所述方式与我们取得联系，并要求我们删除您的个人信息。

**3.4** **停用服务**

对于hypium-driver-js安装包，您可以在项目根目录运行 `npx hypium-driver telemetry disable` 来停止Hypium处理您的个人信息。

对于hypium安装包，您可以在项目根目录运行 `python -m hypium telemetry disable` 来停止Hypium处理您的个人信息。

对于hypium-pycharm-plugin的插件，您可以在pycharm顶部导航栏中的DevEco Testing Hypium > 隐私协议页面，点击“拒绝并关闭”按钮来停止Hypium处理您的个人信息。

对于hypium-driver-js安装包，您可以在项目根目录运行 `npx hypium-driver telemetry enable ` 来恢复Hypium对您个人信息的处理。

对于hypium安装包，您可以在项目根目录运行 ` python -m hypium telemetry enable` 来恢复Hypium对您个人信息的处理。

对于hypium-pycharm-plugin的插件，您可以在pycharm顶部导航栏中的DevEco Testing Hypium > 隐私协议页面，点击“同意并开启”按钮来恢复Hypium对您个人信息的处理。

对于hypium-driver-js安装包，您可以在项目根目录运行 `npx hypium-driver telemetry status` 来查看Hypium个人信息处理状态。

对于hypium安装包，您可以在项目根目录运行 `python -m hypium telemetry status` 来查看Hypium个人信息处理状态。

对于hypium-pycharm-plugin的插件，您可以在pycharm顶部导航栏中的DevEco Testing Hypium > 隐私协议页面来查看Hypium个人信息处理状态。

**4** **数据存储地点及期限**

**4.1** **存储地点**

上述信息将会传输并保存至中华人民共和国境内的服务器。

**4.2** **存储期限**

我们仅在实现本声明所述目的所必需的时间内保留您的个人信息，并在超出下述保留时间后删除或匿名化处理您的个人信息，除非法律法规另有要求。

工具自身的测试数据及其备份数据将保存5年，目的是为了确保您的数据安全。

此外，当我们的产品或服务发生停止运营的情形时，我们将以推送通知、公告等形式通知您，并在合理的期限内删除您的个人信息或进行匿名化处理。

**5** **如何联系我们**

我们指定了个人信息保护负责人，您可以通过此[链接](https://consumer.huawei.com/cn/legal/privacy-questions/)联系个人信息保护负责人。您也可以通过访问[隐私问题页面](https://consumer.huawei.com/cn/legal/privacy-questions/)与我们其取得联系，我们会尽快回复。

如果您对我们的回复不满意，特别是当我们的个人信息处理行为损害了您的合法权益时，您还可以通过向有管辖权的人民法院提起诉讼、向行业自律协会或政府相关管理机构投诉等外部途径进行解决。您也可以向我们了解可能适用的相关投诉途径的信息。

华为将始终遵照我们的隐私政策来收集和使用您的信息。有关我们的隐私政策，可参阅[华为消费者业务隐私声明](https://consumer.huawei.com/minisite/legal/privacy/statement.htm?code=CN&language=zh-CN)。
