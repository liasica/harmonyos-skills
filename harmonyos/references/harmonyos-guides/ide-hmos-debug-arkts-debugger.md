---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:56+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:8a34ec100ca6fc75442e72125c7640417711d0cdb9c79f153bde122d03d22354
---

调试界面有两个窗格，分别是“调试器”和“调试器控制台”。第一个窗格“调试器”，用于调试功能；第二个窗格“调试器控制台”用于展示已加载的ets/js。

## 调试器窗格

调试器面板显示三个独立的窗格：

* 左侧区域是堆栈：当应用暂停时，堆栈区会显示当前代码所引用的代码位置。
* 右侧区域是变量：显示当前运行位置上下文变量，开发者可以在此窗口添加需要监控的变量或表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Xf2k-R99QJGKSnA4N2-yGQ/zh-cn_image_0000002820681207.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A585D666D332CBF87D7BFE21415FF3C85B8111569DDAEC37D9DBECE2FF964BB)

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

点击继续图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/_vk6excATM23xEHUzEIk0A/zh-cn_image_0000002820681219.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=224D6EBE48237AB8D2B0032638E2B3EC34FC3F270E909006D2F92FA894BE3053)，如果命中下一个断点，展示对应的堆栈和变量信息；如果未命中断点，设备上的应用正常运行，变量信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/GoJ7Zm4qRbG2k0fCX34SLg/zh-cn_image_0000002791841274.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B25860908CE98A59620011F387F9D856D510BC8E268774A761DDBAB80183600C)

### 单步跳过

点击单步跳过![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/CbhgyANRR2iQ45S4OqgKOw/zh-cn_image_0000002792001258.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=24EE567AA90DD6ABDF3DC260298519E62DA82F396D950E3ED51E5446D934174C)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/QAnboIiZQtSExfNUsOOKfw/zh-cn_image_0000002820721213.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=09BF3668855C292C79A51ABCF9CDF958827F47C6A0E7E8BE923DABFD04195396)

### 单步执行

点击单步执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/5yjOuG8XSoadWLsUU7Syiw/zh-cn_image_0000002791841266.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFD187D194565980B087788DFE76014DBE3A6D9345C23C03D8BAE5E6CEEBD154)，当前调试断点进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/mQhf_mRWQiyThmYBI1liuQ/zh-cn_image_0000002820721223.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FCBF37EDBC7FA18165EE39566EC490D67C3FE344942B243094D836E3AF6C04A)

### 单步停止

点击单步停止![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/O6C7DIEhRJKoM33ash2n4Q/zh-cn_image_0000002791841278.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=398F8B664A074F9913D706E48614CDFD295AFA82A6F8FAF78F53B2B8B7B089FD)，调试节点会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/9rN7SoUBSxeDuoYsh7_SGA/zh-cn_image_0000002792001244.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F61E4F3C94BF5C8269B94986DBE3070C52B2824A709CE988A86B09FDAC44D661)

### 运行到光标处

点击运行到光标处![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/SIgw3MWsSK6zldKXv2Su2w/zh-cn_image_0000002820681205.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AAEFE79C958DC7FD3EA86F0A59A3AC3C8F26BF2A6AF803DE5EA87CA1D573D79)，代码停留在光标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ypRysIyLRpq-qogeyttjzA/zh-cn_image_0000002791841272.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=05C2E10F4339F1A07787CF21F8528014853601D6FDED092FC8C7EF78D63D2799)

### 重启调试

点击重启调试![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/RlU6hdu2Qs-6Mu8IDk4IJg/zh-cn_image_0000002792001252.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EB90D5FF1BC0E6A6DD5C9F611A3511834D17C8D370F07655B35D30A63C3943C)，重新启动代码调试。

## 调试控制台窗格

用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/X3-dWr1GRke-7JV9Hm4yVg/zh-cn_image_0000002791841270.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=49BF2617A903498FDBD83F0F076A6CD0E563DCC30D75C626ECD75902EB9AD413)
