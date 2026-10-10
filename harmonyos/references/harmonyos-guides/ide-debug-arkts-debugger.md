---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:04+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e79ec82a1b358094d885eb557635cdb0cbbc051fb56926c36245446f1d38d711
---

Debug界面有三个tab页，分别是“entry”、“entry(PandaDebugger)”和“entry(Native)”。

通常第一个tab页“entry”用于展示推包安装过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/2qiKE9kyT3a--g2U8ew9yg/zh-cn_image_0000002731543079.png)

第二个tab页“entry(PandaDebugger)”和第三个tab页“entry(Native)”是调试器，用于调试Debugger功能，其中“entry(Native)”仅在涉及Native调试时才会拉起。调试器包含两个窗格，**[Debugger](ide-debug-arkts-debugger.md#section1437520119316)**和**[Console](ide-debug-arkts-debugger.md#section327153017314)**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/CM8uiZVXQu6_9-Hct4XQmg/zh-cn_image_0000002731383113.png)

## Debugger窗格

Debugger显示两个独立的窗格：

* 左侧区域是Frames，当应用调试到某个断点时，Frames区会显示当前代码所引用的代码位置。
* 右侧区域是Variables，用于展示当前变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/qhq4_XJySf--BU1ggZUUJw/zh-cn_image_0000002731543025.png)

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

点击Resume Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/91SHUMmgTq-5kZlubObGew/zh-cn_image_0000002731383101.png)，如果存在断点时，命中下一个断点，并展示对应的Frames和Variables信息；如果不存在断点，设备上的应用正常运行，Frames和Variables信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/9dPMY743TumC25trXJak2g/zh-cn_image_0000002731383051.png)

### Pause Program

点击Pause Program图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/pB526t2AT4yxJRrqkymT0Q/zh-cn_image_0000002731383089.png)，当有对应源代码时，应用会暂停。

### Step Over

点击Step Over![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/5jw7EnyyRP2J7zqJAhXNFw/zh-cn_image_0000002731543067.png)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/WRYFIQxjQV-LgGF4NoFbRw/zh-cn_image_0000002731543073.png)

### Step Into

点击Step Into![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2kMyo1k-TsOfPzTHPI0xUQ/zh-cn_image_0000002731383119.png)，当前代码进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Wc-Pq-gBSWaaPvs1YT6o6w/zh-cn_image_0000002731383065.png)

例如代码进入add方法的定义处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/QxkkFOfLTnOWjYuD2j-Jgg/zh-cn_image_0000002731383083.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/YRiSDIzySXOzenbc9U0IEg/zh-cn_image_0000002701663838.png)

### Step Out

点击Step Out![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/j-daw8x6ROWhigx-dcln_A/zh-cn_image_0000002701823766.png)，代码会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/_i0MAWbdQqmf3xPGgsFj-A/zh-cn_image_0000002731543059.png)

### Run to Cursor

点击Run to Cursor![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ZjddumAhQhqHm3BCxyXyrQ/zh-cn_image_0000002701823778.png)，代码停留在鼠标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/4VA-6-ckRR20i9Ypbp6raw/zh-cn_image_0000002701663846.png)

### JSVM Debug Port

点击JSVM Debug Port![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/s_2eC0IcS-yaLYqgghgxBQ/zh-cn_image_0000002731543089.png)，弹出输入转发端口的面板，输入端口并点击**OK**后会开始转发，转发成功后会有弹窗提示，根据提示对JS代码进行调试。具体的调试方法请参考[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/MYyhuUzNTPmuBvhyBFF5Ew/zh-cn_image_0000002731543085.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/1qHihCtSRGGXbbeffuzrfA/zh-cn_image_0000002701823792.png)

## Console窗格

Console窗格用于展示已加载的ets、js或so。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/odmAYD_6TXa8iMSrmSrXYg/zh-cn_image_0000002701663852.png)
