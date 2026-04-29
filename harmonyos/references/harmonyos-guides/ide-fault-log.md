---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log
title: FaultLog
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:54+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:c19132b6a167761d4e6dd0446e4cd6ef2bde939e60fc5f1f38aef95a0a9695ec
---

当应用运行发生错误导致应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

FaultLog由系统自动从设备进行收集，包括如下几类故障信息：

* App Freeze
* CPP Crash
* JS Crash
* System Freeze
* [ASan](ide-asan.md)
* [HWASan](ide-hwasan.md)
* [TSan](ide-tsan.md)
* [UBSan](ide-ubsan.md)

说明

调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的App Freeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。

当前支持屏蔽的App Freeze故障类型：

* THREAD\_BLOCK\_3S/THREAD\_BLOCK\_6S：应用主线程卡死检测，卡住3秒/6秒。
* APP\_INPUT\_BLOCK：输入响应超时。

当前支持屏蔽的System Freeze故障类型：

* LIFECYCLE\_TIMEOUT：app、ability生命周期切换超时。

## 查看FaultLog日志

### 查看设备历史抛出的FaultLog日志

打开FaultLog窗口，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/LP5GHiI2ScKer6Hx-glhSA/zh-cn_image_0000002530913384.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=99BC81C5C9C153E713877DF5B471B897CDB7FCE2819AB3DEC868CECD86FA2AC9)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，开发者点击**Jump to Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/BikMQ1AHS_yVII5OrpjdRQ/zh-cn_image_0000002561833305.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=DB5B1F289BCA2598759A3DD17D1C4730BF5A729DA726E1DA8928082B3B1AD983)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Iapf2tuGTx-E2gO5cVpskw/zh-cn_image_0000002561833313.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=F4060BB5B24049B934D493F2E4F7FA8752843D4295C03223526197E98A6FDF99)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便后续的进一步分析。开发者可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**Export FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ZVsgRtFoSyO3TjABeyf8sg/zh-cn_image_0000002561833285.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=004266328FB05C4A04A80E747EB45F6053E8B9637F07DF6A7030CD852A5F4828)
  + 点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/wjcgCng-SpmGdWFMyErwhA/zh-cn_image_0000002561753315.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=FD1656CC7D7692290A9159E9E392E22E7DD9028FD4C5E9016E8077F67B44EC87)，弹出子选项后进一步点击**Export Selected FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/rRW9SL9RSQWinh8v3AO3Lw/zh-cn_image_0000002561753299.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=67337A5408CC5A03457DFBEA825C3BAB76E9464867920FC4BACC5DD6CAAB70B5)
* 保存所有日志：点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/cCVlUn9PQ7S0jrMmKxHoeQ/zh-cn_image_0000002530753376.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=0B8C65EDEC26C2E9CEC8D741E6310D9F18AA2585747F42324AB8A8CB0C27962E)，弹出子选项后进一步点击**Export All FaultLog**。

## 查看cppcrash结构化日志

从DevEco Studio 6.0.0 Beta1版本开始，支持对Cpp Crash类型的FaultLog，进行结构化展示和日志过滤。

1. 双击cppcrash日志，**Fault Info**右侧会出现**Fault Analysis**页签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/K1dQL6mkT2OiIdB_CWJmxw/zh-cn_image_0000002530913356.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=90AF2FE3C1AD6427A0F6A136F0C8DDFD852F85B3CCB8F549E13F741F64193377)
2. 点击**Fault Analysis**页签，会展示结构化的日志信息。
   * 页面上方的字段对应了FaultLog中的字段，具体对应关系请查看[字段说明](ide-fault-log.md#section1983219211210)。
   * 页面下方包含Stacks和Logs两个页签。
     + **Stacks**：展示线程的堆栈信息，具体请参考[查看堆栈信息](ide-fault-log.md#section459581010138)。
     + **Logs**：展示FaultLog中的HiLog日志，具体请查看[查看HiLog日志](ide-fault-log.md#section13361239195113)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/rvLMlpoxSG-lo_JQJG9ARw/zh-cn_image_0000002530753372.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=33F5B0A35F2C8ED0FB768E100DB63C3ED0BC0A3EE8AF222C0857E351147F25A9 "点击放大")

### 字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

**表1**

| **Fault Analysis**的字段 | 说明 |
| --- | --- |
| Occurrence time | FaultLog发生的时间，对应FaultLog中的Timestamp字段 |
| Analysis time | 触发日志结构化展示的时间，即双击日志文件的时间 |
| Frontend | 是否是前台应用，对应FaultLog中的Foreground字段 |
| Bundle name | 包名，对应FaultLog中的Module name字段 |
| Device type | 设备类型 |
| App build number | 应用构建号，对应FaultLog中的VersionCode字段 |
| App version | 应用版本，对应FaultLog中的Version字段 |
| Device model | 设备信息，对应FaultLog中的Device info字段 |
| System version | 系统镜像版本，对应FaultLog中的Build info字段 |
| Abnormal signal | 异常信号，对应FaultLog中的Reason字段 |

### 查看堆栈信息

Stacks页面包含了FaultLog中的堆栈信息，并以线程为单元进行折叠，点击展开按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/l11z99t7Th-Zkp0gzWZeaQ/zh-cn_image_0000002530753398.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=41EB29921B16D94C2F81F53053184397AA39BD5EDB2D556911E485E8B93AA75B)，可以展开对应线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/KViFJ9jJSUKQna5FtZlhNw/zh-cn_image_0000002561833275.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=892C79E859E6567BB11E95FB39CA94E41C17917EFA612EBED1DB6F8385F8C09A "点击放大")

图中标注1的勾选框是展开应用堆栈，标注2的勾选框是展开系统堆栈，两个勾选框一共组成了四种状态，具体如下表。

**表2**

| 勾选框勾选状态 | 说明 |
| --- | --- |
| 1、2都不勾选 | 展示所有线程，线程处于折叠状态。 |
| 1、2都勾选 | 展示所有线程，线程处于展开状态。 |
| 只勾选1 | 只展示应用线程，线程处于展开状态。 |
| 只勾选2 | 只展示系统线程，线程处于展开状态。 |

### 查看HiLog日志

Logs页面展示了FaultLog中的HiLog日志，支持日志级别的过滤和搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/wL_NG9V1T6m0wcaPVofkKQ/zh-cn_image_0000002561753301.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=7D4C1D188A6420548F2F8331F85CE9E8B9F8F884FE3377D27AD60FEDCFB5EA85 "点击放大")

## 查看appfreeze结构化日志

从DevEco Studio 6.0.0 Beta2版本开始，支持对AppFreeze类型的FaultLog，进行结构化展示和日志过滤。

1. 双击appfreeze日志，**Fault Info**右侧会出现**Fault Analysis**页签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/NhgHLLoCTb6-gdP3RbzqOw/zh-cn_image_0000002561753321.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=659D9A159C769EFF17121987C0629875DAB7E5BABC34A4D22B8C4AB491795E89)
2. 点击**Fault Analysis**页签，会展示结构化的日志信息。
   * 页面上方的字段对应了FaultLog中的字段，具体对应关系请查看[字段说明](ide-fault-log.md#section15864144624712)。
   * 页面下方包含Stacks、Logs、System、3s/6s Compare四个页签。
     + **Stacks**：展示线程的堆栈信息，使用方式和cppcrash日志相同，具体请参考[查看堆栈信息](ide-fault-log.md#section459581010138)。
     + **Logs**：展示FaultLog中的HiLog日志，使用方式和cppcrash日志相同，具体请参考[查看HiLog日志](ide-fault-log.md#section13361239195113)。
     + **System**：从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，具体请参考[查看高负载CPU/内存日志信息](ide-fault-log.md#section179717814915)。
     + **3s/6s Compare**：从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD\_BLOCK\_6S](appfreeze-guidelines.md#thread_block_6s-应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，具体请参考[查看3s/6s堆栈日志](ide-fault-log.md#section76467955514)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/CW1RthS9S3Gmo0gxV-aThw/zh-cn_image_0000002561753323.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=0521DA1A45C4BB4384227F13401EC0EC064470022A5B3B0AC7D7113551C2BFD1)

### 字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

**表3**

| **Fault Analysis**的字段 | 说明 |
| --- | --- |
| Occurrence time | FaultLog发生的时间，对应FaultLog中的Timestamp字段 |
| Analysis time | 触发日志结构化展示的时间，即双击日志文件的时间 |
| Frontend | 是否是前台应用，对应FaultLog中的Foreground字段 |
| Bundle name | 包名，对应FaultLog中的Module name字段 |
| Device type | 设备类型 |
| App build number | 应用构建号，对应FaultLog中的VersionCode字段 |
| App version | 应用版本，对应FaultLog中的Version字段 |
| Device model | 设备信息，对应FaultLog中的Device info字段 |
| System version | 系统镜像版本，对应FaultLog中的Build info字段 |
| Freeze type | 冻结类型，对应FaultLog中的Reason字段 |

### 查看堆栈信息

Stacks页签用于查看appfreeze中的堆栈信息，使用方式和cppcrash日志相同，具体请参考[查看堆栈信息](ide-fault-log.md#section459581010138)。

### 查看HiLog日志

Logs页签用于查看appfreeze中的HiLog，使用方式和cppcrash日志相同，具体请参考[查看HiLog日志](ide-fault-log.md#section13361239195113)。

### 查看高负载CPU/内存日志信息

从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，有助于分析高负载和appfreeze之间的关联关系。

如下是CPU的相关日志。

①：柱状图表示对应时间点的CPU使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示CPU总使用率、CPU使用率top5的进程号（Pid）和对应的CPU使用率。

③：选中柱状图后，显示相关的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/ictD64MeS26tjX7AvRnrzQ/zh-cn_image_0000002561833271.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=7B79EE04054DB8C5D887FD86FCE5697034CEF06CB184A038E780FC296420D790 "点击放大")

如下是内存的相关日志。

①：柱状图表示对应时间点的内存使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示内存使用率、内存占用top5的进程和对应的内存大小。

③：选中柱状图后，显示相关的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/t1pL46McQhusMqVhcaMtUQ/zh-cn_image_0000002530913348.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=08F4F71B2999B0734FAAE41BB9813798837D75D0064AAA395729FC1EF039D492 "点击放大")

### 查看3s/6s堆栈日志

从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD\_BLOCK\_6S](appfreeze-guidelines.md#thread_block_6s-应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，并标识栈帧中可能的故障处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Ej5QJxSMRYady9j5xGIKsg/zh-cn_image_0000002561753295.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=80DA01596D86C3720C5DDE1FD19C34E6DCBC613C2BD915ED988FDA6C7DFAFF31)

如果不是THREAD\_BLOCK\_6S类型的AppFreeze问题，不会展示3s/6s Compare页签。

## 查看应用终止日志

从DevEco Studio 6.0.2 Beta1版本开始，提供**AppKilled**窗口，用于查看设备上应用终止的相关信息，包括应用异常退出的时间、进程名、是否前台应用、异常退出原因，点击**recordId**可以查看详细的FaultLog信息。支持按设备、应用和异常原因对信息进行过滤。

AppKilled窗口中支持查看的异常退出原因请参考[reason字段说明](hidumper.md#reason字段说明)，如需对问题进行排查处理，请参考[App Killed（应用终止）检测](appkilled-guidelines.md)。

说明

2in1、Tablet设备不支持查看APP\_INPUT\_BLOCK和THREAD\_BLOCK\_6S类型的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/s3Xw07gdSyuXMCiSRLRN5Q/zh-cn_image_0000002561753307.png?HW-CC-KV=V1&HW-CC-Date=20260429T054653Z&HW-CC-Expire=86400&HW-CC-Sign=F93400DCF11A55C5368DC79BB0E5EB65EB895BC74663A5325FBCCF75E373B359)
