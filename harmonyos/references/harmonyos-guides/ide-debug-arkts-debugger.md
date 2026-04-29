---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e50b8e887ed24b7cf0f5e34d2b5319a325e8cee244e34f5b87258a3f3757f3c2
---

Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Zh3HzwfGQxSMTppcDQXCgA/zh-cn_image_0000002530913488.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=B0E7976FECFE6CBCF8E8460DBA30A6F08BD386A3318A2C946CF03BDF123EA111)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/jyfigosjRqyN-2MJROLR5Q/zh-cn_image_0000002530753478.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=30F4A93452C347285A2E552D3FF2D801D679C99F5A6C1419E0679CE7D1430129)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/P2HT6xbJRFqzKEJ6Q-vdWw/zh-cn_image_0000002561833399.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=03DBAB0F050FA4399BD5C8F70D1F7216D544BDFCC6EC39CC969354DFD5AFE2EF)

Debugger窗格有多个按钮：

**表1** 调试器按钮

| 按钮 | 名称 | 快捷键 | 功能 |
| --- | --- | --- | --- |
|  | Resume Program | **F9**（macOS为**Option+Command+R**） | 当程序执行到断点时停止执行，单击此按钮程序继续执行。 |
|  | Step Over | **F8**（macOS为**F8**） | 在单步调试时，直接前进到下一行（如果在函数中存在子函数时，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。 |
|  | Step Into | **F7**（macOS为**F7**） | 在单步调试时，遇到子函数后，进入子函数并继续单步执行。 |
|  | Force Step Into | **Alt+Shift+F7**（macOS为**Option+Shift+F7**） | 在单步调试时，强制进入方法。 |
|  | Step Out | **Shift+F8**（macOS为**Shift+F8**） | 在单步调试执行到子函数内时，单击Step Out会执行完子函数剩余部分，并跳出返回到上一层函数。 |
|  | Stop | **Ctrl+F2**（macOS为**Command+F2**） | 停止调试任务。 |
|  | Run To Cursor | **Alt+F9**（macOS为**Option+F9**） | 断点执行到鼠标停留处。 |
|  | JSVM Debug Port | 无 | 转发JSVM调试的端口，转发后可以在浏览器的DevTools工具上进行[JSVM-API调试](jsvm-debugger-cpuprofiler-heapsnapshot.md)。  说明  仅Native调试器中支持该按钮。 |

### Resume Program

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/LeQWtOOASeeGnqmRi6W1wg/zh-cn_image_0000002530913484.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=F6D4505003EFF852F965359E6953EAE2728310392EA9C3C3C229644FD882683E)，如果存在断点时，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/r7SoKz5wR4yTYr7CiDZxQg/zh-cn_image_0000002530913478.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=A78F740F7129B1DDF203BE9386599854F6AB365736666FA17336566F28C7D44F)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/laoIxOxpSsOl_FKVkmpgEw/zh-cn_image_0000002561833433.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=E606869AAA72A34EAE8DE418F0AD0DBBC3A0679927900F4B63DDAEC13150549D)，当有对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xnVjV-bKSk2dIQUl_VhkHg/zh-cn_image_0000002561833431.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=E708A92C7DF61A45FE3699DF082A50E4BAF73EC42725FB7CF25702FF58630DC5)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/OTgdJaMcS2Ki5Y-8aYysUA/zh-cn_image_0000002530913480.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=BF462C75ECBBB3183402F617EF7CB1E785E710E2C325B8FA3AD2CE6D7D82474F)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/5nwCM2CvS7G_CUB74Ooz6Q/zh-cn_image_0000002561833435.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=71313F6D93447C5090C334A8F5CC2AF74986B937FEF071CCA9A8AE6788769E95)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/ACwRxCE2QuuSSGmDG15aVg/zh-cn_image_0000002530913482.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=BC39A46B5EA6CB123BED4DC5F6E8EE71C10A0732B000B7DAA5291352E59B902A)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/AoFMbt2HRF-93S8cza575w/zh-cn_image_0000002561753443.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=C4C97EBB62AB707D767667EF43689A5D9919C60AA0DEBCCECB1595D8784A5AED)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/kvgPYRGKQpSxMn-_cu_PKA/zh-cn_image_0000002561753413.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=A5ED5F711EA39DCC2DCA6424681FC87D69CA57C305E73CD118972D97EBC6F132)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ZIJ6INinT5GG-PkpD7-SuQ/zh-cn_image_0000002530913494.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=DD5D88A562ECB317B0CC3C830EF384A5656533E0904A966FE4975A84D284A62D)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/inTJ518BQHy0w-T5WxOhKg/zh-cn_image_0000002561833449.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=BA71C9B5F2EA53EF9E767C06DEFA5512A3CE7EE2A408B9D94B9B033AF0C06BB4)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/PxA6cA59R1mxIhkIDuVkTg/zh-cn_image_0000002530913460.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=BD2EB3E64E7DBF8A37EAB81A32DDAEC7D2F3952632EA2E341F1F70B28DFEF6D8)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JF5xV1lKQTiirZjdbMy2lw/zh-cn_image_0000002561833445.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=0FC247D7573E1D883EFE3F8A2CD1FCECCD4238C56598F2752193811099791917)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/td7omKkpTbaCRsW4TIR0Zg/zh-cn_image_0000002561833439.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=B97F1D4BCAF2EAEE4D8E64A23E50A9242BB661608F9DE9B6C7C73F844A017373)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，打开对应的URL即可对JS代码进行调试。关于如何调试C++拉起的JS代码，请查阅[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/QwWM4vkcTwKSl_3sJl96Og/zh-cn_image_0000002561833389.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=22552D4FA7E4F4C7CE916BF2892FB81AB66F4CD5EDE7C6E8DAAF2275E329EA3A) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/1YUOuGbHReSnSuQY2wy7Dg/zh-cn_image_0000002561833443.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=2C79389E6DCD5271301550146B3BBA1818D1C0BD7C700E2458062734BCBDE7BB)

## Console窗格

Console窗格用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/3HGzfJFCT5yaCf0hvxWGnA/zh-cn_image_0000002561833441.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=D4FECD7B33F4F99BEFFDE52D3050EC41FCACA95CB44992A1DE45BD2D44108997)
