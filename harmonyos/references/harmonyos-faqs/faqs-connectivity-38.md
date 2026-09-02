---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-38
title: BLE蓝牙连接类问题定位定界指导
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE蓝牙连接类问题定位定界指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:fd9024f615c3972e36fdd5c00c3586d1d7dcee006dc2f67deb3db91b08cd3777
---

## 问题现象

本文就BLE蓝牙连接类问题进行定位定界指导，连接类问题可以具体表现为：

1. 蓝牙无法连接设备。
2. 蓝牙连接后异常断开。
3. 蓝牙连接设备耗时较长，或二次连接失败。

## 背景知识

**蓝牙全场景流程图：**

首先需要了解BLE蓝牙的业务流程，确定上述故障场景可能发生的阶段：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/jUMbl_ZTQiqnuC-W_CCt4w/zh-cn_image_0000002686068917.png "点击放大")

1. 由上图可知，蓝牙无法连接设备主要发生在广播/扫描阶段和连接阶段，连接后断开问题主要发生在业务交互和蓝牙断开阶段。
2. 针对无法连接设备的场景，对于广播/扫描阶段的排查步骤，请参考[蓝牙BLE扫描无法获取设备](faqs-connectivity-23.md)进行交叉验证，本文主要介绍针对连接阶段、业务交互阶段、断开阶段的排查步骤。

**蓝牙连接阶段流程图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/jqsQeMU5REqqUWrk2VTvbA/zh-cn_image_0000002655829628.png "点击放大")

**业务交互与连接维护阶段流程图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/f0Svj6n2QoCrRwi8fVoyLg/zh-cn_image_0000002655989612.png "点击放大")

**业务交互与连接维护阶段时序逻辑：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/gi6R_ZMwQYyU3N4NrOQkiw/zh-cn_image_0000002655829704.png "点击放大")

**蓝牙断连流程图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/QWPBhSD0SqWjQmjEpiU2Vg/zh-cn_image_0000002655989944.png "点击放大")

**蓝牙无法连接设备问题分析流程（连接阶段）：**

基于蓝牙连接阶段流程图，给出蓝牙连接阶段排查流程：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/WyCvtCChTwiqSphxkq4DRg/zh-cn_image_0000002655990158.png "点击放大")

1. 首先根据Hilog日志和HCI日志排查是否正常连接（若连接失败，后续的服务发现和鉴权环节将无法正常进行），此时建连失败主要由未接收到广播包、信道强干扰导致。
2. 此处的连接属于底层的物理链路连接，并不是应用层面的连接，还需要经过鉴权、服务发现等流程，应用层才会正常连接（通常表现为UI显示已连接、可进行业务交互）。
3. 若连接正常，优先根据Hilog和HCI日志排查发现服务流程（大多数无法连接问题都集中在发现服务阶段）。
4. 对于涉及配对的蓝牙设备（如蓝牙车钥匙等），若连接和发现服务正常，需要查看HCI日志排查身份验证（鉴权）是否通过（该过程在Hilog日志中体现较少，从HCI日志可更直观的排查）。
5. 由于鉴权失败会直接导致蓝牙断连（可根据下方的断连reason code反向验证是由于鉴权失败导致的断连），若鉴权成功，则仅凭Hilog和HCI日志无法继续排查，需要抓取空口日志和蓝牙芯片日志进一步分析。

**蓝牙连接后断开问题分析流程：**

由蓝牙断连流程图可知，蓝牙断开时必然会输出对应的断连Hilog日志，且该日志中会写明连接错误码reason code，因此定界流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/_52r85-IRAap-_mlXBivBw/zh-cn_image_0000002655990246.png "点击放大")

1. 根据断连日志中打印的reason code，结合下方的reason code对照表，预分析结论。
2. 部分场景中，发生断连的时间点附近会打印应用调用的蓝牙接口报错日志，可以参考[蓝牙服务子系统错误码](../harmonyos-references/errorcode-bluetoothmanager.md)辅助定界。此外，还可能打印应用主动调用断连方法的Hilog日志（该方法由应用自己实现和封装），也可以作为定界依据。
3. 若Hilog日志中的上述日志不足以确定根因，需要进一步查看HCI日志，结合上述业务交互流程图和时序逻辑，确定根因。
4. “BLE蓝牙连接后断开”故障场景下，HCI日志主要排查业务交互阶段，即MTU协商、GATT服务发现、特征获取等。下方提供了常用的HCI日志排查关键字。

**reason code对照表如下所示：**

| 编号 | 宏 | 连接错误码 | 注释 |
| --- | --- | --- | --- |
| 0 | HCI\_SUCCESS 0x00 |  | HCI连接成功 |
| 1 | HCI\_ERR\_ILLEGAL\_COMMAND | 0x01 | 对端命令非法，对端问题 |
| 2 | HCI\_ERR\_NO\_CONNECTION | 0x02 | Host发送了一个应该识别连接的命令，但该连接不存在 |
| 3 | HCI\_ERR\_HW\_FAILURE | 0x03 | Controller硬件故障错误代码 |
| 4 | HCI\_ERR\_PAGE\_TIMEOUT | 0x04 | page timeout 设备不在配对状态，请检查设备状态 |
| 5 | HCI\_ERR\_AUTH\_FAILURE | 0x05 | 鉴权失败，请底层确认 |
| 6 | HCI\_ERR\_KEY\_MISSING | 0x06 | linkkey丢失，对端问题 |
| 7 | HCI\_ERR\_MEMORY\_FULL | 0x07 | 内存满 |
| 8 | HCI\_ERR\_CONNECTION\_TOUT | 0x08 | 连接超时断开,主设备或从设备在监督超时内未收到对方的有效数据包或链路层应答 |
| 9 | HCI\_ERR\_MAX\_NUM\_OF\_CONNECTIONS | 0x09 | 连接个数超限 |
| 10 | HCI\_ERR\_MAX\_NUM\_OF\_SCOS | 0x0A | SCO连接个数超限 |
| 11 | HCI\_ERR\_CONNECTION\_EXISTS | 0x0B | 连接已存在 |
| 12 | HCI\_ERR\_COMMAND\_DISALLOWED | 0x0C | Controller无法处理该命令 |
| 13 | HCI\_ERR\_HOST\_REJECT\_RESOURCES | 0x0D | 对端由于资源有限而拒绝连接 |
| 14 | HCI\_ERR\_HOST\_REJECT\_SECURITY | 0x0E | 对端由于安全原因而拒绝连接 |
| 15 | HCI\_ERR\_HOST\_REJECT\_DEVICE | 0x0F | 对端因BD\_ADDR错误而拒绝连接 |
| 16 | HCI\_ERR\_HOST\_TIMEOUT | 0x10 | 此次连接尝试的连接接受超时已被超过 |
| 17 | HCI\_ERR\_UNSUPPORTED\_VALUE | 0x11 | HCI 命令中的某个功能或参数值不被支持 |
| 18 | HCI\_ERR\_ILLEGAL\_PARAMETER\_FMT | 0x12 | 无效的 HCI 命令参数错误：参数总长度无效、命令参数类型无效、连接标识符与相应事件不匹配、参数应为偶数但为奇数、参数超出指定范围、两个或多个参数值不一致 |
| 19 | #define HCI\_ERR\_PEER\_USER | 0x13 | 对端断开连接，对端问题 |
| 20 | HCI\_ERR\_PEER\_LOW\_RESOURCES | 0x14 | 对端设备因资源不足而终止了连接 |
| 21 | HCI\_ERR\_PEER\_POWER\_OFF | 0x15 | 对端设备即将断电 |
| 22 | HCI\_ERR\_CONN\_CAUSE\_LOCAL\_HOST | 0x16 | 本地设备（手机、PC等）断开连接，需要结合问题背景分析 |
| 23 | HCI\_ERR\_REPEATED\_ATTEMPTS | 0x17 | 自上次身份验证或配对尝试失败以来经过的时间太短，重复尝试 |
| 24 | HCI\_ERR\_PAIRING\_NOT\_ALLOWED | 0x18 | 对端不允许配对 |
| 25 | HCI\_ERR\_UNKNOWN\_LMP\_PDU | 0x19 | Controller收到了未知的LMP操作码，对端问题 |
| 26 | HCI\_ERR\_UNSUPPORTED\_REM\_FEATURE | 0x1A | 对端设备不支持的远程功能，对端问题 |
| 27 | HCI\_ERR\_SCO\_OFFSET\_REJECTED | 0x1B | LMP\_SCO\_link\_req PDU中请求的偏移量已被拒绝，对端问题 |
| 28 | HCI\_ERR\_SCO\_INTERVAL\_REJECTED | 0x1C | LMP\_SCO\_link\_req PDU中请求的间隔已被拒绝，对端问题 |
| 29 | HCI\_ERR\_SCO\_AIR\_MODE | 0x1D | LMP\_SCO\_link\_req PDU中请求的空中模式已被拒绝，对端问题 |
| 30 | HCI\_ERR\_INVALID\_LMP\_PARAM | 0x1E | 无效的LMP参数/无效的LL参数，对端问题 |
| 31 | HCI\_ERR\_UNSPECIFIED | 0x1F | 未指定错误 |
| 32 | HCI\_ERR\_UNSUPPORTED\_LMP\_FEATURE | 0x20 | 不支持的LMP参数值/不支持的LL参数 |
| 33 | HCI\_ERR\_ROLE\_CHANGE\_NOT\_ALLOWED | 0x21 | Controller此时不允许更改角色 |
| 34 | HCI\_ERR\_LMP\_RESPONSE\_TIMEOUT | 0x22 | Host发出的命令未收到回复，30s超时断开，蓝牙芯片或者对端问题，请开发人员确认 |
| 35 | HCI\_ERR\_LMP\_ERR\_TRANS\_COLLISION | 0x23 | LMP错误业务冲突/LL过程冲突错，对端问题 |
| 36 | HCI\_ERR\_LMP\_PDU\_NOT\_ALLOWED | 0x24 | Controller发送了一个操作码不被允许的，对端问题LMP PDU |
| 37 | HCI\_ERR\_ENCRY\_MODE\_NOT\_ACCEPTABLE | 0x25 | 当前请求的加密模式不可接受 |
| 38 | HCI\_ERR\_UNIT\_KEY\_USED | 0x26 | 无法更改链接密钥，因为正在使用固定的设备密钥 |
| 39 | HCI\_ERR\_QOS\_NOT\_SUPPORTED | 0x27 | 所请求的QoS服务质量不被支持 |
| 40 | HCI\_ERR\_INSTANT\_PASSED | 0x28 | 设备移动超出通信范围、射频干扰、或连接参数配置不合理（如监管超时），与0x08在逻辑上等效 |
| 41 | HCI\_ERR\_PAIRING\_WITH\_UNIT\_KEY\_NOT\_SUPPORTED | 0x29 | 请求使用单元密钥，而该功能不被支持 |
| 42 | HCI\_ERR\_DIFF\_TRANSACTION\_COLLISION | 0x2A | 不同事务冲突，启动了与正在进行的事务冲突的LMP事务或LL过程 |
| 43 | HCI\_ERR\_UNDEFINED\_0x2B | 0x2B | 未定义错误 |
| 44 | HCI\_ERR\_QOS\_UNACCEPTABLE\_PARAM | 0x2C | QoS存在不可接受参数，但其他参数可能是可以接受的 |
| 45 | HCI\_ERR\_QOS\_REJECTED | 0x2D | QoS拒绝，应终止QoS协商 |
| 46 | HCI\_ERR\_CHAN\_CLASSIF\_NOT\_SUPPORTED | 0x2E | Controller无法执行通道评估，因为该功能不被支持 |
| 47 | HCI\_ERR\_INSUFFCIENT\_SECURITY | 0x2F | 安全性不足，发送的HCI命令或LMP PDU仅在加密连接上才可能执行 |
| 48 | HCI\_ERR\_PARAM\_OUT\_OF\_RANGE | 0x30 | 参数超出强制范围，并且接收方不接受该值 |
| 49 | HCI\_ERR\_UNDEFINED\_0x31 | 0x31 | 未定义错误 |
| 50 | HCI\_ERR\_ROLE\_SWITCH\_PENDING | 0x32 | HCI命令或LMP PDU因角色切换待处理而无法被接受时 |
| 51 | HCI\_ERR\_UNDEFINED\_0x33 | 0x33 | 未定义错误 |
| 52 | HCI\_ERR\_RESERVED\_SLOT\_VIOLATION | 0x34 | 保留时隙违规，表示当前的同步协商被终止 |
| 53 | HCI\_ERR\_ROLE\_SWITCH\_FAILED | 0x35 | 尝试进行角色切换但失败 |
| 54 | HCI\_ERR\_INQ\_RSP\_DATA\_TOO\_LARGE | 0x36 | 有所请求FEC要求的扩展查询响应太大，无法适应Controller支持的任何数据包类型 |
| 55 | HCI\_ERR\_SIMPLE\_PAIRING\_NOT\_SUPPORTED | 0x37 | Host不支持安全简单配对 |
| 56 | HCI\_ERR\_HOST\_BUSY\_PAIRING | 0x38 | Host正在进行其他配对操作 |
| 57 | HCI\_ERR\_REJ\_NO\_SUITABLE\_CHANNEL | 0x39 | 未找到合适的通道而拒绝连接 |
| 58 | HCI\_ERR\_CONTROLLER\_BUSY | 0x3A | Controller忙，无法处理请求 |
| 59 | HCI\_ERR\_UNACCEPT\_CONN\_INTERVAL | 0x3B | 远程设备由于一个或多个不可接受的连接参数而终止了连接或拒绝了一个请求 |
| 60 | HCI\_ERR\_ADVERTISING\_TIMEOUT | 0x3C | 定向广告完成，但超时未建立连接 |
| 61 | HCI\_ERR\_CONN\_TOUT\_DUE\_TO\_MIC\_FAILURE | 0x3D | 消息完整性检查（MIC）失败而导致连接中断，对端问题 |
| 62 | HCI\_ERR\_CONN\_FAILED\_ESTABLISHMENT | 0x3E | 同步包接收失败，主设备提议的连接参数超出从设备的允许范围，与0x3B逻辑上等效 |
| 63 | HCI\_ERR\_MAC\_CONNECTION\_FAILED | 0x3F | 请求802.11 AMP的MAC连接，但连接失败，对端问题 |
| 64 | COARSE CLOCK ADJUSTMENT REJECTED BUT WILL TRY TO ADJUST USING CLOCK DRAGGING | 0x40 | 主设备此时无法使用提供的参数对微网时钟进行调整 |
| 65 | TYPE0 SUBMAP NOT DEFINED | 0x41 | 当前未定义Type0子映射，LMP PDU被拒绝 |
| 66 | UNKNOWN ADVERTISING IDENTIFIER | 0x42 | 未知广播标识符，广播异常 |
| 67 | HCI\_ERR\_LIMIT\_REACHED | 0x43 | 请求的操作次数已达上限，对端问题 |

**Hilog连接类问题关键字：**

| 编号 | 关键字 | 注释 |
| --- | --- | --- |
| 1 | onConnectionStateChange, connectCallback, CreateGattClientDevice, isRegisterSucceeded, ConnUpdatedCallback | client连接 |
| 2 | gatt\_client.\*Disconnect, HwBleHciDisconnectionCompEvt, connectionState:3, gatt\_client.\*close | client断连 |
| 3 | getService, Request not supported, GATTC\_Discover, Start service discovery, DiscoverStart, DiscoverServices | client发现服务 |
| 4 | SetBLEMtuSize, OnMtuChanged, MtuChangedCallback | client MTU设置 |

**HCI蓝牙连接阶段关键字：**

| 编号 | 关键字 | 注释 |
| --- | --- | --- |
| 1 | "HCI LE Extended Create Connection Command" | 创建连接 |
| 2 | "HCI LE Enhanced Connection Complete " | 创建连接完成 |
| 3 | "ATT Exchange MTU Transaction" | 协商MTU（最大传输单元） |
| 4 | "HCI Disconnect" | 蓝牙断连 |
| 5 | "HCI Disconnection Complete" | 蓝牙断连完成 |
| 6 | "SMP\*" | 安全管理协议（鉴权相关） |
| 7 | "HCI LE Start Encryption" | 开始密钥认证鉴权 |
| 8 | "HCI LE Read Remote Used Features" | 获取对端设备特征 |
| 9 | "ATT\_READ\_BY\_GROUP\_TYPE" | GATT发现服务（第一步发现Primary Service） |
| 10 | "ATT\_READ\_BY\_TYPE" | GATT发现服务（发现service下属的include） |
| 11 | "ATT\_FIND\_INFORMATION" | GATT发现服务（发现service下属的characteristic） |

## 问题定位

* **案例一（蓝牙连接后断开）：** 使用蓝牙车钥匙连接车辆后断开。
  1. 查看Hilog日志，搜索断连关键词“gatt\_client.\*Disconnect|HwBleHciDisconnectionCompEvt|connectionState:3|ATT protocol channel|gatt\_client.\*close”：

     ```txt
     01-06 07:05:23.248 I C00104/bluetooth_service/bt_btm: [17]HwBleHciDisconnectionCompEvt
     01-06 07:05:23.248 I C00104/bluetooth_service/bt_btm: [17]HwBleHciDisconnectionCompEvt status 0x0, handle 0x42, reason 0x13
     01-06 07:05:23.248 I C00104/bluetooth_service/bt_btm: [17]HwBleHciDisconnectionCompEvt no handle 0x42
     01-06 07:05:23.249 I C00104/bluetooth_service/Bluetooth: [17]GATT   ATT protocol channel with BDA: [对端设备MAC地址] is disconnected
     01-06 07:05:23.311 I C00101/[应用包名]/bt_napi_gatt_client_callback: (OnConnectionStateChangedWithReason:62)connectionState:3, disconnectReason:2, ret:0
     ```
  2. 日志中显示断连原因编码reason 0x13，查看连接错误码得知，该问题由对端设备断开导致，确认为对端问题，具体断连原因通过Hilog日志无法定位，需要进一步分析HCI日志中的交互信息，发现断连HCI日志显示，当前全信道干扰达-110dBm，属于严重干扰：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/0KGEy5asQfOPR-Tz2MYWzQ/zh-cn_image_0000002685912693.png "点击放大")
  3. 过高的干扰强度使BLE物理层解调成功率急剧下降，导致HCI指令和数据帧大量丢失，这也是断连HCI日志前5秒没有任何其他HCI日志的原因，对端不断重传未被确认的数据包，超过重传次数后，协议栈会判定链路异常并断开。
* **案例二（蓝牙无法连接设备）：** 车机APP一直显示蓝牙车钥匙连接中。
  1. 查看Hilog日志和HCI日志，蓝牙正常连接。

     ```txt
     01-19 13:47:40.928 I C00102/bluetooth_service/bt_server_device_manager: [19](SetDeviceRetentionFlag)realMacAddr: [对端MAC地址], randomMacAddr: [生成的随机地址], isRetention: 1
     01-19 13:47:40.928 I C00102/bluetooth_service/bt_service_common_state: [19](AddServerDeviceList)add devices, addr: [对端MAC地址]
     01-19 13:47:40.928 I C00102/bluetooth_service/bt_service_gatt_client: [19](operator())clientIf 8 state changed to 1
     01-19 13:47:40.928  I C00101/com.huawei.hmos.walletservice/bt_napi_gatt_client_callback: (OnConnectionStateChangedWithReason:62)connectionState:1, disconnectReason:-1, ret:0
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/pt1fyrP0T6iPRME5L0z9FA/zh-cn_image_0000002655835094.png "点击放大")
  2. Hilog日志中搜索发现服务关键字，发现服务启动10秒后显示超时，查看HCI日志，发现服务流程持续近20秒，耗时过长且远超应用层10秒的阈值，进一步分析本端发包迅速，接收对端数据包越耗时1秒，时间较长：

     ```txt
     01-19 13:47:42.971  I C00101/com.huawei.hmos.walletservice/bt_napi_gatt_client: (GetServices:436)enter
     ...
     01-19 13:47:52.978  E C00101/com.huawei.hmos.walletservice/bt_fwk_gatt_client: (GetServices:521)timeout
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/66uAs-5-Spum7Oo-3IqLNg/zh-cn_image_0000002655995040.png "点击放大")
* **案例三（蓝牙无法连接设备）**：

  Hilog查看连接状态，发现连接状态connectionState由0（未连接）转至1（已连接）期间，就调用了发现服务，且有蓝牙服务子系统错误码2900099（操作失败）：

  ```txt
  [napi_bluetooth_gatt_client_callback.cpp (OnConnectionStateChanged:55)]connectionState:0, ret:0
  [napi_bluetooth_utils.cpp (GetCallbackErrorValue:37) ]errCode: 2900099
  errCodegetServices: 2900099, errMessage: BussinessError 2900099: Operation failed
  [napi_bluetooth_gatt_client _callback.cpp(OnConnectionStateChanged:55) ]connectionState:1, ret:0
  198l:~WorkerThread:65 WorkerThread enter destruction
  ```
* **案例四（蓝牙连接耗时长及二次连接失败）：** 连接纯蓝牙设备时，第一次连接耗时约8秒，断开后第二次连接失败。
  1. 查看连接日志，第一次发起连接后，对端设备约7秒才回复连接请求，导致连接耗时较长。手机和设备交互过程未发现异常。
  2. 断开后第二次发起连接，对端设备未回复连接请求，10秒后超时断开。

## 分析结论

**案例一：** 对端设备主动断开，具体表现为信道严重干扰的情况下，HCI指令数据包丢失严重，对端多次重传未响应，断开连接。

**案例二：** BLE发现服务过程耗时20s，远超应用层设置的10s，导致报错发现服务timeout。

**案例三：** 未连接成功就调用getServices进行服务发现。

**案例四：** 第一次连接耗时长是由于对端设备回复连接请求较慢（约7秒），手机和设备交互过程未发现异常；第二次连接失败是由于对端设备未回复连接请求。

## 修改建议

**案例一：** 应用适当延长强干扰网络下的重传次数和超时阈值，实时监控信道环境，若信道忙，则应增加提示弹窗。

**案例二：** 需要排查车端日志，分析发包速度慢原因，同时适当延长超时判断时间阈值。

**案例三：** gatt\_client的connect函数只是发起连接指令，需要在on('BLEConnectionStateChange')中监听到蓝牙连接成功后才可以调用getServices。

**案例四：** 连接耗时长和二次连接失败均为对端设备问题，建议排查对端设备的连接响应逻辑，确保对端设备在收到连接请求后能及时回复。
