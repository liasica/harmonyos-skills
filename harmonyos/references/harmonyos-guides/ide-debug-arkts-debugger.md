---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e755670e263e98dddb53b8a4b20e936affdc9eb3d24d2c06cda1f8268c5b0d57
---

Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/lgSjKGxKRAqw-tnSPxt20w/zh-cn_image_0000002808766907.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3F1F92F0C4F05DCDA20D727F3531C422EAC3122C19A22B69EFE42C49DFBEEAF)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/PVGup54KQFa5Jez6AQQQNA/zh-cn_image_0000002808766901.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A5AA79497A7DDCE11C12D3D08F09342D00F262A62FB815193BE12D91A290ADA)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Ty17HlLCTsWN7vGAdZKgDg/zh-cn_image_0000002808766903.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEC4CF0EFFD4D0B78DEF185FDA574D9B3D78CDEC7A2891EC865D3DE057A5C31C)

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

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/CpKdG4G5RlazCh93ECfRXQ/zh-cn_image_0000002779567326.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=830CEC2B39DB6E947BA08F92D9BB2E8013110CBBECBE37936806F93B9246A225)，如果存在断点，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/57sS91o1Ru-g2-XYBzBAug/zh-cn_image_0000002808886985.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3453E48E125A08A8DC4D867C7C15CE8103AD0578D0C5696926B0555B69842279)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/q-CU4rhQShi9KezAjhracA/zh-cn_image_0000002779567334.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=694C94C204213E7DA2D6B6C1329CD185A588F8A05116F75DB982EA6FE34DC489)，存在对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Yw2nrzFlQLOvn43BB6cBMw/zh-cn_image_0000002779407354.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D07A6E7C54A79A25D09CB11C85F4E040EFB6B5D2DB9778B0B859CB9D3861DE2A)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/1FdU7D-nTyuUQWV4yyDcEA/zh-cn_image_0000002779567324.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA6A5D3EE06F64C24C3974B2C734F220F90F49A5F6D0DDAC0690307FC1EF6E63)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Ws7PIjZ8QSGOoHzRYyKyPg/zh-cn_image_0000002808886997.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A14CEE7772B42745B2267A3A3A04D80FE320D5D5A31F8FA2F683A3A34961288E)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ILaptgdZSaKhdyk9aTa8vA/zh-cn_image_0000002808886987.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=998B2169E303404CAE35AE873CCD67834A17F740166D37254D6B3C28999B925D)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/1lLifv0BR-K2oRTDaaV9aA/zh-cn_image_0000002779567330.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCD92EB8C230D207BD491B4D19CCFC7CB9145389499402FBEC75DEF0AC5351EC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/GGUlXptcROyEoAIl47xNnw/zh-cn_image_0000002808766899.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BCF04645C16AFF8124CED56A8E7DCABC33DF5338D17EFB4E59ED9CFF9A5007A)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/3g577qczSryAYa4JPmohrw/zh-cn_image_0000002779567328.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C9616DDC2C53AFF1947E79B1965F6F6B5CC498606A8A52CF993AF8490EF4B60)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/i64IMzIARCSA4cAG5FWUSw/zh-cn_image_0000002808887003.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3B884AE7107C2A8FBEFC9B80FC6617C6856B4EC16A5A9E4B23532E3D1F582EA)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/F_gR7PuGSleyo4Iis4o7sw/zh-cn_image_0000002779567316.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C4B565355AE5CF26B51ABF8B6436044C0FDA77F2BB0D2381FFE272B80B57FA1)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Gju16_q9TauFr2amrOzTnQ/zh-cn_image_0000002808766919.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E28C623D6B91509BB4DA1E454D5F692B809A1839819ABE79B92D1D92E3220239)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/mA9FKCjMT7u0N1ArP14yUA/zh-cn_image_0000002808766917.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFABEEDC61918E99D6F29B625EC9E5846968AF6FC993CE6D2070C1253F3FEAAB)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，根据提示对JS代码进行调试。具体的调试方法请参考[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/83y-90NSSAW9E5rtNnni7A/zh-cn_image_0000002808886979.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F8AA381BC5B62D556F807128A5433621A3B9B7E75E47CB44093E0532CDF747E) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/VTF0AYnnScaJIL4gA8dV_A/zh-cn_image_0000002779567340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C61D9384BE6FDAE28AABCAF845F229F206966956196A892E56768293CCEF773)

## Console窗格

Console窗格用于展示已加载的ets、js或so。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/JaUr-oG1TxOYxLftx8v-hQ/zh-cn_image_0000002808886999.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A2DA5457CB66F1583A7C00B2A18DFBE6D2E9182CE907C6837B3B966E1E7D170)
