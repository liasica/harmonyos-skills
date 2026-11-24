---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:f7f70d806dffd0e51811bda9ad9c26fa14c92d5c2f70c736d1547383c0a71e3e
---

调试界面有两个窗格，分别是“调试器”和“调试器控制台”。第一个窗格“调试器”，用于调试功能；第二个窗格“调试器控制台”用于展示已加载的ets/js。

## 调试器窗格

调试器面板显示三个独立的窗格：

* 左侧区域是堆栈：当应用暂停时，堆栈区会显示当前代码所引用的代码位置。
* 右侧区域是变量：显示当前运行位置上下文变量，开发者可以在此窗口添加需要监控的变量或表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/gE4E3iyDQyGrmkdbbKBy6g/zh-cn_image_0000002820681207.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=14685723EEA6E2A074B69227AA105730F28FD0C0A08F9B3B635105B17A2EB0F0)

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

点击继续图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/_ZGQ8u3-TCyE5uiBL4Rl2A/zh-cn_image_0000002820681219.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=197F3C758F43E2B801E241A8509DBD1E66A7F87EF673D047A09F8EEE675ACB17)，如果命中下一个断点，展示对应的堆栈和变量信息；如果未命中断点，设备上的应用正常运行，变量信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/1BtwO6CRSuivuKaA4eQxnQ/zh-cn_image_0000002791841274.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E3139528BC5FFF78FF87A175A86CB926EB54F3869B04E5E1E185D965D721989)

### 单步跳过

点击单步跳过![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/hA7ABLfJTzuEueH52Fm9Vg/zh-cn_image_0000002792001258.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=C99220ABB57D5EFC02015B9372002E72ABA20CF1EED094687F0EDFFFEABE24B4)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/C7k3Ncm4QXy5fjwjbFMjmA/zh-cn_image_0000002820721213.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=943BF662A9FF372AEBE6FE122F7170C45B0178F8CDFB4A309ACE68683A97E2D6)

### 单步执行

点击单步执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/HecdhHGWSzqp4KVoIG0N_A/zh-cn_image_0000002791841266.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E8BAEF8ACAFB5CCCA26574802E228D4564C06E3B8B92CC25B15AEE183612EB1)，当前调试断点进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eE7nJEgvR-6pqHGwojwwmw/zh-cn_image_0000002820721223.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C02C9FF8619A08B8034FC5FBC930D6AD6DD64788C7757A1D38C34ABB16CB07D)

### 单步停止

点击单步停止![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/9lfghxX4To6p2Ss2Z3CZ4w/zh-cn_image_0000002791841278.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB2FF78DF8166446F52176932E3DCBE82CDDECBB8DD75396B066DF74200AF9BA)，调试节点会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/PwpzZhi7QtiywCrtMCuCdQ/zh-cn_image_0000002792001244.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2012C0DC7A4DCD4F3BAEE292253EFE53C2CFD3DA28C505771833B29FA48E368)

### 运行到光标处

点击运行到光标处![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/D1GarRhQQEylqlFl1kfQGg/zh-cn_image_0000002820681205.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7F83292DAE50E6E8177C9965E50E14DA941C51DEBB9206EAAA6C4162712C1A2)，代码停留在光标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/AjlHhDL_SEmQzFdEg257yw/zh-cn_image_0000002791841272.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7BDEC4258104A84DE2785D2C053559069DFA781AD70602404E40A88436C6B51)

### 重启调试

点击重启调试![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/T2j97bU7R5SQkzBsw_k9Ig/zh-cn_image_0000002792001252.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=31F6039976DC527B3729785D1FD7A32A47AC6289E17305508F2DB54CE734C4C2)，重新启动代码调试。

## 调试控制台窗格

用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/bBJLp_iuT929CF5xTMHj4w/zh-cn_image_0000002791841270.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=82B6BBF070F07C9158DB321C2E0A6D7AD070585E584E753138CD32B6A0784EC8)
