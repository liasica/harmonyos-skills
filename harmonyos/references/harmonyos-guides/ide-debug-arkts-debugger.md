---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d02c771a9407a38415588c60854a5fe659f426260c995349628edee101edfd77
---

Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Rkd5qjWLT4G0eTDoJ7KgkA/zh-cn_image_0000002808766907.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=72B2250C3FB3A999A454609ADDE61F0613A676A80BD8E4AD3951021B9354D4B6)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/26BEAGBnQAC5m5dIYfkDWw/zh-cn_image_0000002808766901.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=C563CF05412D1485149193ED97AE5FA348245ECFA81BC7DBEC5E69F11363345C)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Qquz8lgKTPebBk-mJfb6vg/zh-cn_image_0000002808766903.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=56E533CA0AFE36B5984574460300C1F4972280F57B314F5C930F6614591DD27F)

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

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/0xL6Ez9DQYGMDL2BlriHNg/zh-cn_image_0000002779567326.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=D78493421E5AFD12E3B5B6E44EC239B41942A1D3455C1482326CB0CD9BFB8D23)，如果存在断点，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/m7K5wOLhRtKX3PjG0H0icg/zh-cn_image_0000002808886985.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FA06F932751D6FB390CE1E77D23A0807669A93743A3DA1D6A24FB57AF345E3A)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/tvuoNpv9THyX2KW5gC-78A/zh-cn_image_0000002779567334.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=982126B33492B61F99DF55BE6B34933BB52EE72D78B85E49F0FAE6FC5EF13520)，存在对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/SqHy-IB9TrC429-8f8t_1w/zh-cn_image_0000002779407354.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6E13B259BC369ADD904B704EE9D2A68C29F8D9F20D84EE70687371032A25B02)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/TLxzYjx8SaKX1AtHxim2ZQ/zh-cn_image_0000002779567324.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7E1E054B127035C9DD06672612F603A7E554A1CEFE556B86A9EDDDB29B95B0B)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/q97NSyUARNKGdvFQnjvkJg/zh-cn_image_0000002808886997.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=136BE20C3A7BC59130045C905C4861342F36C753C014F6A8152F90253EEAB0C0)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Ey9EwdFuTt6FZarqPzcQug/zh-cn_image_0000002808886987.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E75097838C9B1224ED84314CA76CB60E875936743F1AB46E163406A3A1D9032)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Qy0Uk74ARN-IJQ9iCycPbg/zh-cn_image_0000002779567330.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CFF3D45541B473D366595685D766197FF4719DEF9989CD854D29D61A115ED7B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/amHDv8WpR_aojmtd8LNSeA/zh-cn_image_0000002808766899.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=61B1DFC2EF9B62140148B8189B1282C1F0D850EA7F320182A42E54B809134856)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/M-ARd_LHRd2i7yINY37crA/zh-cn_image_0000002779567328.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=948884D17189E5F381B7DCD8711D264840002A143FBA8F095ED8745B0465E38F)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/jgHpNuSbSAO90rh-d-2evQ/zh-cn_image_0000002808887003.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDAA542FA09385E1B28C996151E7BCE1CD85AB9DF794DD31BA271ADC9DD1712A)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/LvC-SNshTpqrUAAPLZBRjw/zh-cn_image_0000002779567316.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2E447E7DFE779D0085CA2BA8A7EA1E5CD2E5ACF5B7920B8280D0ECDA7D02948)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/MNyLLvTMSyCmOmAIlR7GsQ/zh-cn_image_0000002808766919.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=92BD745272ADDBB5DCD3009711A78A9540D42A3CC5EBA2D1BE0856F69F122AD6)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/14QrBb3YSWiC-f1Zct1OuA/zh-cn_image_0000002808766917.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=84BCF74D9DE26909F8B3E1F5719723FCBCBE4802B134D665EBE30FB1B109E3F7)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，根据提示对JS代码进行调试。具体的调试方法请参考[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ROnnq0KdQumNd-vU_2opfg/zh-cn_image_0000002808886979.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA48F94BEDA17ECF5232A9B5028A3448B365EF5BBAD5770467D079DC88412EF8) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/AAGE6VVWQEixdH1ot23L3g/zh-cn_image_0000002779567340.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B54581674E300410C1059E1B2EFB98773738AB4ED27D995F1AA982FE16F015B9)

## Console窗格

Console窗格用于展示已加载的ets、js或so。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/fVrke-GwRk6H7H2F2bqNlg/zh-cn_image_0000002808886999.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FF3FC019A69DFDE02A2DE6460FB6AEF722ECFF5EED7B5B0B8F878193CC967CD)
