---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5bd6038752347f4d30492f70faceca3954fdeed3e4fff4a4f8723582cddd65a6
---

Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vEAgWOhCSZSpNH1KeELGMw/zh-cn_image_0000002808766907.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=266780F758E57BCF7993D667A9FF11DBC5C1BB0773009DD4CC589EF67D8EB3C6)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/4y7SBJsmQzGlazn5sNVeXQ/zh-cn_image_0000002808766901.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC922EECAB70F9C4FC524794407505C81CA771426B6612B60D8A14DFD73055B1)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/PjfBFW0gTEiJrvzDMnRAYQ/zh-cn_image_0000002808766903.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2F4841D4205B4FB7FB1943423A84C52E7A9A3608882C08E4507F8D1E3279896)

Debugger窗格有多个按钮：

**表1** 调试器按钮

| 按钮 | 名称 | 快捷键 | 功能 |
| --- | --- | --- | --- |
|  | Resume Program | **F9**（macOS为**Option+Command+R**） | 当程序执行到断点时停止执行，单击此按钮程序继续执行。 |
|  | Step Over | **F8**（macOS为**F8**） | 在单步调试时，直接前进到下一行（如果在函数中存在子函数时，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。 |
|  | Step Into | **F7**（macOS为**F7**） | 在单步调试时，遇到子函数后，进入子函数并继续单步执行。 |
|  | Smart Step Into | **Shift+F7**（macOS为**Shift+F7**） | 代码行存在多个函数嵌套或调用时，可以智能步入选择想进入的方法。 |
|  | Step Out | **Shift+F8**（macOS为**Shift+F8**） | 在单步调试执行到子函数内时，单击Step Out会执行完子函数剩余部分，并跳出返回到上一层函数。 |
|  | Stop | **Ctrl+F2**（macOS为**Command+F2**） | 停止调试任务。 |
|  | Run To Cursor | **Alt+F9**（macOS为**Option+F9**） | 断点执行到鼠标停留处。 |
|  | JSVM Debug Port | 无 | 转发JSVM调试的端口，转发后可以在浏览器的DevTools工具上进行[JSVM-API调试](jsvm-debugger-cpuprofiler-heapsnapshot.md)。  说明：  仅Native调试器中支持该按钮。 |

### Resume Program

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/SLDpUnyNSge9_mxxYCV1dg/zh-cn_image_0000002779567326.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=41F3F03DA2F233A84F23681CD41B4302DBB818A70FA438FA8B0F8139E7D75456)，如果存在断点，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/rQwywAPBRNOLu2EtbMBVuw/zh-cn_image_0000002808886985.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9D34876621F1961A2951B11F760342BC661F72427A81B432F92D46790DED234)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/bQ2GrFSCTOSOPFdjTlyFlw/zh-cn_image_0000002779567334.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=E22D9F6E1BCE50F3D4B699F3BCF82C6C49F3D2D442CABD1AFEF90A0A0E6A3C30)，存在对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/bizC6MDcRPuo1aiRnfeZ4w/zh-cn_image_0000002779407354.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=1364B75971CE6B3AF41C930FB2EC364B908BDA3A1BDE667FA579F0C6B8B6020B)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/heJlU0zBRMudH1kSp15mIA/zh-cn_image_0000002779567324.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=61534FC90B5156526020E69937BE8263435BF73AD6D9B6F3D0638CF679EB5F0E)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/kJQqIzcbSfSROyLOmcShFg/zh-cn_image_0000002808886997.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=41003E02A9F517A08A7B09B6BC640048F669DF43D1478A5FE977E3D469D6F902)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/OoLzcJOQT-KAdvjex4tC-Q/zh-cn_image_0000002808886987.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB5D56217AC0C1CF298D8D99DB39D690509C23008AF30088CCAF1CD423C276D7)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5zuPXXE1TuaJBPHvZDD6vw/zh-cn_image_0000002779567330.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=C844010717770302E52BE4C4134B57825679D2BCF4D4B8FF166038631C13EB43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/KdkKuZloQoe6v__OJq4EmQ/zh-cn_image_0000002808766899.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=D394412EEE1F48CA3C14FA4D03190206BFDE3384C758CA30983310B33513AEBF)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/FhiGTuNWQOG2_hbZi6aBVw/zh-cn_image_0000002779567328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=80F7CD6F3467BC8A83D9C1023E87D41859AF4557A72C40EB0EDB0008806F9B26)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/jZHT3O-YTV2KlcQnUxiBHA/zh-cn_image_0000002808887003.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C79C44C5607E58267709E93DC8C8DEB2198E890FCBE4912129AD0ECDA442EC4)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/v-Mmjyo0T9-o3PDfsxppqA/zh-cn_image_0000002779567316.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D41699F4661404C45837678A6E97FC956DAD4E8B6B9E2884AAB32576299032C)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/LGobZQ5sSlWCqopD94cipw/zh-cn_image_0000002808766919.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=898DF07B7C44CFAC4B78B195FDE40C9E7EE2876EA1DBBA8B5DFDB71579919C03)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/-u7gCM9ETY-mb9tVi6n4Xg/zh-cn_image_0000002808766917.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=9074098094FBE10D8B33CD8E45E25D60BA19C6E4AE6198B03D29835BEA940CA9)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，根据提示对JS代码进行调试。具体的调试方法请参考[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-9AGCVYiQNm3OpE90xeprw/zh-cn_image_0000002808886979.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=91AD841A424E05862B4EDE8DBEAA22F5017ADDBD9789C920E63DE61D2DE7F7B0) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/eYCHoFVmS7OvJUBwtS1Lhw/zh-cn_image_0000002779567340.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=B668A4EBC50A9755CBD801CE627FBD8539B519D3B621F14AF0FB7C693939C075)

## Console窗格

Console窗格用于展示已加载的ets、js或so。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/d9fZ_aCoTxapEG9lRXTJ3A/zh-cn_image_0000002808886999.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBE22C83C73969F3EB154FC8C2ECBD38F201558A8280E57593AD7921BB33FF31)
