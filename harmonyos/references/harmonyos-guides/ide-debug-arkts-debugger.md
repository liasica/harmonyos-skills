---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e6bec4b0d189921ca7193f8ea48e9dc694d7dcd086001067645b06c0238635b4
---

Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/j24Rt-3kQF2pOdJYr8xkLQ/zh-cn_image_0000002530913488.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=979B27B71C71BBF6A0394019B965274B8B70AE3B90DB7BAEEFA55ADB2AA5EE2B)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/N1IGNWZRQs6gIlSFy8YrxA/zh-cn_image_0000002530753478.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=DE776D9FED42B30334F65E5B62C0F9FDA2A561074756C19F4EA0D7D7A470457D)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/1M8kUAkPQnGEbNrBmADI2Q/zh-cn_image_0000002561833399.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=D35FADFF77D431E3853DE12B39F6CD2EF0E7A00F1FF897D363D0B12A6DAD3E09)

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

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/JuG9wobKTB6iJIm--uomCQ/zh-cn_image_0000002530913484.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=70A745EB980BF29D74A3BA96A7680ED61DB33444FF4AA223119132BB628FF45E)，如果存在断点时，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/vQGSx5ZVTQqFo9KC8Ph_tw/zh-cn_image_0000002530913478.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=50F80F7E146D0438E56491172A4D0456EE86929FA61C76A68B33E435A74620E0)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/e9j7kSXCRoOgABJ-8Eg7PA/zh-cn_image_0000002561833433.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=1FF26D487DD5126A598456207C32D2639525015810BCE50C0D0434451804FF11)，当有对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/b2xRVNArQ5Cwxw0-aa5Q8g/zh-cn_image_0000002561833431.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=278A8055AE31A6DB28F8D8D887C9025F3DE7E01C44CE771539BD2BD06920CDFA)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/fs-07LonQi6GugUrmqhY9A/zh-cn_image_0000002530913480.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=76423AE998FCA62F08D6BFAF1D41FC5B7E593BCCA2D5E904F0E4B852369F3E35)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/l-jPHhT5RY2YJmIB13oIGw/zh-cn_image_0000002561833435.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=603129A2B3DA4B0FEC8F3C9EF2B2A2843F911B873197A146CE586B0A9FF976E0)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/d8FkAxGPQwK-WTW6Dbyd9A/zh-cn_image_0000002530913482.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=0AF8A5B390F27534D43082E805A3BA134E6ACAFF770BED2526B5717A2FF2C465)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Ey48Y7TXRrupd9Iw9nuLFA/zh-cn_image_0000002561753443.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=F21C3A82FFA851DF214F77DD1C06E1D51D56CC6FB883EDC8764F76030E835AEA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/M8h6j_I9Qy-idLQ5ESqTLg/zh-cn_image_0000002561753413.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=4FDBF68090B9ED8525FD664AACD4AB1F73B872E05C345E297FA52FFDEF44AA5F)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/M3LA63VYQGKOL4fhXIIE_Q/zh-cn_image_0000002530913494.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=E6EA738E26AEA6D6A240EAD6A9E841EA70D53D7F44B11B3A61F6D9C197529E8E)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/V1ywIXRJQdil4LRqVwBBLQ/zh-cn_image_0000002561833449.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=66330849DEF0E82645624B7E368C599F318261012B5829E7E8404E67D9B9987E)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/GMEnKN5eSiykk_NvsfJWUg/zh-cn_image_0000002530913460.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=FA63E0A7BAFA179803E475012C43CFA2F3498B3AB29128D1ED4B528C61425255)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/LJhvf2XHRoWexk_o6ps_Sg/zh-cn_image_0000002561833445.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=41AAC8802F97A6AF88E92BFB04766ADCC3663F34ABB2B9644AAEB92C5F02BDF6)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/p31Ti_sGRzOpIHYl_Z0l6g/zh-cn_image_0000002561833439.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=7B56523A40FF4AB5DF26A1C5227A4CEF1E2F24FCA1D47470197A4984093CCDF2)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，打开对应的URL即可对JS代码进行调试。关于如何调试C++拉起的JS代码，请查阅[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/6ODK_yAXSZmIIviukUNXJQ/zh-cn_image_0000002561833389.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=BF90BA25F3212208F9F8686E68D417D394B0D0C815F991BDCF0DD54FB5A892EE) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/_TZiT1UMRgmDuPSGnIMsww/zh-cn_image_0000002561833443.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=DFED9AADED074482A120C802E6C5E6255AABE9D872E1A5CE4BD22070E9966E11)

## Console窗格

Console窗格用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/8G90rhotShWhfrsy_14vvQ/zh-cn_image_0000002561833441.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=1F90ECE6B543C73C7F576C28C8E790CA53AB9C9446C14EE53EC016BF16F06E28)
