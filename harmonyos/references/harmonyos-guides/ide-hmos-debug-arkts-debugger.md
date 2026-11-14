---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:64aa3b7e99c8c817c80f24d50e596ae4736d427051fbe571d630a94c7302d059
---

调试界面有两个窗格，分别是“调试器”和“调试器控制台”。第一个窗格“调试器”，用于调试功能；第二个窗格“调试器控制台”用于展示已加载的ets/js。

## 调试器窗格

调试器面板显示三个独立的窗格：

* 左侧区域是堆栈：当应用暂停时，堆栈区会显示当前代码所引用的代码位置。
* 右侧区域是变量：显示当前运行位置上下文变量，开发者可以在此窗口添加需要监控的变量或表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/g4nzt0-lQlq2PkEYlv5Z3A/zh-cn_image_0000002781471098.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=082D6E698E9E9F0941CA7C8B5F2B902863A8FE1A07FFB07AD8A79B3AFD8BA35D)

调试器窗格有多个按钮：

**表1** 调试器按钮

| 按钮 | 名称 | 快捷键 | 功能 |
| --- | --- | --- | --- |
|  | 继续 | **F9** | 当程序执行到断点时停止执行，单击此按钮程序继续执行。 |
|  | 单步跳过 | **F8** | 在单步调试时，直接前进到下一行（如果函数中存在子函数，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。 |
|  | 单步执行 | **F7** | 在单步调试时，遇到子函数后，进入子函数并继续单步执行。 |
|  | 单步停止 | **Shift+F8** | 在单步调试执行到子函数内时，单击单步停止会执行完子函数剩余部分，并跳出返回到上一层函数。 |
|  | 停止 | **Ctrl+F2** | 停止调试任务。 |
|  | 运行到光标处 | **Alt+F6** | 断点执行到鼠标停留处。 |
|  | 重启调试 | **Ctrl+F5** | 重新启动调试。 |

### 继续

点击继续图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/nifqwj3lS7avjcVScPAJHQ/zh-cn_image_0000002810750761.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=63F1BDDA56ECDA1116972D3E52D62AED7B09B6CD5D34958721C8FD15929B9A3B)，如果命中下一个断点，展示对应的堆栈和变量信息；如果未命中断点，设备上的应用正常运行，变量信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/sNADm1CjRxW4DPC0rSYXRQ/zh-cn_image_0000002810630651.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=87DD3BA4E37172644385D252962BA5A1F1F2270F2F30B026CA410402834C172E)

### 单步跳过

点击单步跳过![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/3uigPY5vRliNnf-bnWBBow/zh-cn_image_0000002810750751.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3EB0ADC8863241512FABFFB21D8617AE57D20C8C6705FF66F7013BCB74A39C3)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Pirc32nwS52U3oLZIGiJOg/zh-cn_image_0000002810630657.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DF80C992617D47545368F729020A9697C5C5047C3FCD8A51E746FCA57221966)

### 单步执行

点击单步执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/c2Ffpb3oQGi968zO2NQNRQ/zh-cn_image_0000002810750755.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=7122809ACC9A225425007B1D8DF53AB8A4212E40FEF967E13B27DE7B26B05E32)，当前调试断点进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/-fZeOYDORWKAzCYeNmMfCQ/zh-cn_image_0000002781471094.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C700A11C6269F2A4801273C07D07A4C4D850BE1FBC664624306240E2B8B1644)

### 单步停止

点击单步停止![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/1IIPzNU0TJKFNe-3T3o9VQ/zh-cn_image_0000002781471092.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF56298123CE81F37CD180B65519FA79BAA46A1F486703B29A90CA6C87A0066E)，调试节点会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/dSh9y0vnSeurF8Y2OsJmgg/zh-cn_image_0000002810630649.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E66993B58EF0F40A1F12A91419B2551F5AB11F8A53695F844974FAC67D7A6B4)

### 运行到光标处

点击运行到光标处![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/h9P8Jt5aQPWdxavkXEdqFQ/zh-cn_image_0000002810630647.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=89717E35A059BE12AC0B56D6329A1336B467CC1D29ADD1E71E46010451309E9B)，代码停留在光标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/LnBrs2QpQkapHP2SkPi4rA/zh-cn_image_0000002781311160.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=89B6135BB5ABD1D183F6DD679C52D8C7D0AC9671E931806B7650A65208E8F4CE)

### 重启调试

点击重启调试![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/N0Iqwf4IQT6hMBdtHKZfRw/zh-cn_image_0000002781471090.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF8681183A714EC23BDC18541C5F69FA33A3A0B39D30082C03458F61D3560D98)，重新启动代码调试。

## 调试控制台窗格

用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/iNph2-ThTPW_9A6w9-UIRA/zh-cn_image_0000002810630645.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F5948B1B9D983EAAA3229F3155FAAA584F985D784DB84D8B6CA351BE6D08434)
