---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:ce1f91ec4ade5d08c733cd91b9c96ed1f23d0e04c0ccfa38d08dc898f877a122
---

调试界面有两个窗格，分别是“调试器”和“调试器控制台”。第一个窗格“调试器”，用于调试功能；第二个窗格“调试器控制台”用于展示已加载的ets/js。

## 调试器窗格

调试器面板显示三个独立的窗格：

* 左侧区域是堆栈：当应用暂停时，堆栈区会显示当前代码所引用的代码位置。
* 右侧区域是变量：显示当前运行位置上下文变量，开发者可以在此窗口添加需要监控的变量或表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/kPhuAcS1RkKMY2JlLqSiug/zh-cn_image_0000002781471098.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=72C30D7E1B074DDFEBBD3677B7D82F632D1FE53E27ADCC1D6BD003802AED5A8D)

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

点击继续图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/tpiq_UXcRouGYY1DWrf0fw/zh-cn_image_0000002810750761.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A2CF586EE8CF50FF5F35D0C533686F315C0CAE8C63589C5BA805E800D5472D8)，如果命中下一个断点，展示对应的堆栈和变量信息；如果未命中断点，设备上的应用正常运行，变量信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/yLaFPw6wS7Sg3lo99zE_WA/zh-cn_image_0000002810630651.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9721637DF921B20FEC1C67C4DC55F414C424DFF9B6B524CC388E479487EDB3D0)

### 单步跳过

点击单步跳过![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Cg7IE_jjSmuGBO5nA51I1w/zh-cn_image_0000002810750751.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=364541B468894414379D49AA1AE5CC2D9EF419A2B9AC9C7C31ED58654351CC2E)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Vx0UjNbTRQGR-irF4hrdzg/zh-cn_image_0000002810630657.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC7D16A88DA950C9E1193BEE25FD4CF02B23F9B3312A94D7866059D2986FDAAF)

### 单步执行

点击单步执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/OibcxSmfQ6GrsO-oWEmBmg/zh-cn_image_0000002810750755.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1539EDFD0D1B97FF51F33F172112B87B83D2A494087F667EBA579970C4FE4807)，当前调试断点进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/tGqn-RThSQm1bgvXTYWjqg/zh-cn_image_0000002781471094.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=71EEFF6C801D77D77E502B402C3952F4E293BF182F89CD6DC66157614B6CB155)

### 单步停止

点击单步停止![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ypdu_MdLTeKs6tXxgkLZKg/zh-cn_image_0000002781471092.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B6E646DE4A96E5F8B0534C3A9B7AE97050C6E6B856E461A0175AE9F3DBE3339)，调试节点会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/_MB2QdGgRBeMmXAf2i1PDQ/zh-cn_image_0000002810630649.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FBBAA719185C2446F2970E503ED98F60FBA22DF43E34537D3F75F18CF121EF1)

### 运行到光标处

点击运行到光标处![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/lj19zJcOTAWM9P0h9bVQtQ/zh-cn_image_0000002810630647.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A159FBF192F514A2EC9D058B4A3585FED4DC778D076209E8E58352626758D6AE)，代码停留在光标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/zEu_NRbRSoG4cKqffE7gzg/zh-cn_image_0000002781311160.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=85C52B622D2DCCDC47C74D99D788A0ABFC669061B154F05265D4D2C86F29079E)

### 重启调试

点击重启调试![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/-TXbqi1aQFusMy2q19Qqkw/zh-cn_image_0000002781471090.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B606E933F879D995ACBCDC716060E7FDFE0FA83B5987FD0506946A2BCB23BC6F)，重新启动代码调试。

## 调试控制台窗格

用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/4Yu4hRFAQgCdp-rz85uKzQ/zh-cn_image_0000002810630645.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=186AD3D0B610A05983DE717515872D32FB91DA54EC39B1C71C5A2B21A20F90AC)
