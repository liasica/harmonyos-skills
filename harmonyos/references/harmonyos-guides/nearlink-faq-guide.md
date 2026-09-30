---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-faq-guide
title: 星闪常见问题
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 星闪 > 星闪常见问题
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:9cda9d6fdc9dabdacc67976ee0d7d82b939db19df4d4e7bc108aaeb99f2c802f
---

## 标准UUID与自定义UUID有什么区别

通用唯一标识（UUID）用于标识星闪服务及其成员（属性、方法、事件等）。根据标识的分配方式，星闪中的UUID分为两类：

* **标准UUID（Standard UUID）**：长度为16比特，由星闪联盟统一分配，具有全局唯一性，用于标识标准服务或标准服务成员（例如标准服务、标准属性）。完整UUID形式为128比特，由基础标识（Base UUID，固定值37BEA880-FC70-11EA-B720-000000000000）的前112比特与16比特标准标识拼接而成，例如37BEA880-FC70-11EA-B720-00000000FDEE。通过标识，客户端可以明确条目承载的是某一个服务、属性、方法或事件等，详情可查阅[星闪标准服务标识](https://www.isla.org.cn/trial/identCid/identListSsid)。
* **自定义UUID（Custom UUID）**：长度为128比特，由开发者自行定义，用于标识自定义服务或自定义服务成员。开发者可在128比特范围内自行规划，例如FFFFFFFF-1234-5678-ABCD-000000001234。自定义UUID不能以基础标识的前112比特为前缀（即不能以37BEA880-FC70-11EA-B720-00000000开头），否则将被识别为标准UUID。

**说明** 

自定义服务必须使用自定义UUID，禁止使用标准UUID。

自定义服务的[ssap.Service.serviceUuid](../harmonyos-references/js-apis-nearlink-ssap.md#service)、[ssap.Property.serviceUuid](../harmonyos-references/js-apis-nearlink-ssap.md#property)等用于标识服务及服务成员的UUID字段，取值必须为128比特的自定义UUID；使用标准UUID时，接口将返回[36100044 禁止使用星闪标准服务UUID](../harmonyos-references/errorcode-nearlink-service.md#section36100044-禁止使用星闪标准服务uuid)错误。

## 事件订阅类接口的权限要求问题

星闪的事件订阅类接口采用onXXX / offXXX成对形式：

* onXXX(callback) 订阅某类事件，当事件发生时回调callback；
* offXXX(callback?) 取消订阅；不传callback时取消该类型全部回调。

星闪的事件订阅类接口一般没有强制权限要求，在订阅时不会因缺失权限而报错，但未获得相应权限的应用无法收到事件回调。事件订阅所需的权限参见API参考中对应接口说明，权限申请方式参见[开发准备](nearlink-preparations-guide.md)。

**说明** 

订阅类接口调用成功不代表一定能收到事件，还需确认已获得相应权限。

## SSAP属性描述符的作用

属性描述符是属性（ssap.Property）中的可选组成部分，由描述符类型（descriptorType）和描述符值（value）组成，用于对属性数据值进行解释说明、格式解析或操作方式的控制。

描述符类型包括：

* PROPERTY：属性说明描述符，存放属性数据值的文字性说明；
* CLIENT\_PROPERTY\_CONFIG：客户端属性值配置描述符（CPCD，[Client Property Configuration Descriptor](nearlink-glossary-guide.md#client-property-configuration-descriptor-cpcd客户端属性值配置描述符)），定义了客户端如何配置属性值；
* SERVER\_PROPERTY\_CONFIG：服务端属性值配置描述符，定义了服务端上的属性值如何配置，一经写入对所有客户端生效；
* PROPERTY\_FORMAT：属性格式描述符，说明了属性值的格式；
* TYPE\_VENDOR：厂商自定义描述符，用于厂商自定义功能。

其中，客户端属性值配置描述符和服务端属性值配置描述符在一个属性中最多只能有一个。

当属性支持通知（NOTIFY）操作时，需要为其声明客户端属性值配置描述符：客户端通过[setPropertyNotification()](../harmonyos-references/js-apis-nearlink-ssap.md#setpropertynotification)开启或关闭该属性的通知，服务端通过[notifyPropertyChanged()](../harmonyos-references/js-apis-nearlink-ssap.md#notifypropertychanged)向已开启通知的客户端推送属性变化。

## 客户端如何接收属性变化通知

客户端接收属性变化通知（即收到[onPropertyChange()](../harmonyos-references/js-apis-nearlink-ssap.md#onpropertychange)回调）需同时满足以下条件：

1. 服务端在创建该属性时声明了通知（NOTIFY）操作和客户端属性值配置描述符（CLIENT\_PROPERTY\_CONFIG）；
2. 客户端已与服务端成功建立SSAP连接；
3. 客户端已通过[getServices()](../harmonyos-references/js-apis-nearlink-ssap.md#getservices)获取到该属性；
4. 客户端已调用[setPropertyNotification()](../harmonyos-references/js-apis-nearlink-ssap.md#setpropertynotification)启用该属性的通知；
5. 客户端已调用[onPropertyChange()](../harmonyos-references/js-apis-nearlink-ssap.md#onpropertychange)注册属性变化回调。

满足上述条件后，服务端调用[notifyPropertyChanged()](../harmonyos-references/js-apis-nearlink-ssap.md#notifypropertychanged)更新属性值时，会向客户端发送属性变化通知。若上述任一条件不满足，客户端将收不到通知。

**说明** 

连接断开后，已启用的通知会失效，重新连接后需重新调用[setPropertyNotification()](../harmonyos-references/js-apis-nearlink-ssap.md#setpropertynotification)启用。

## 什么是星闪设备随机地址

星闪设备地址为6字节的媒体接入层标识（MAC地址），字符串由12位十六进制字符与冒号分隔符组成（共17个字符），例如：11:22:33:AA:BB:FF。

扫描结果（scan.ScanResults.address）中返回的设备地址是随机地址：系统为保护设备隐私，不直接暴露设备的真实地址，而是将其转换为随机地址后上报，并维护真实地址与随机地址的映射关系。同一设备的随机地址在映射保留周期内保持不变（已配对设备的映射长期保留），映射被清理后重新扫描会生成新的随机地址。

应用不宜将扫描到的地址作为长期标识持久化使用。需要长期识别设备时，应结合设备名称、配对关系等信息综合判断，已配对设备的地址可通过manager.[getPairedDevices()](../harmonyos-references/js-apis-nearlink-manager.md#managergetpaireddevices)获取。随机地址不影响设备连接：可通过扫描获取的当前地址发起连接（如[SSAP连接](nearlink-ssap-connection-guide.md)、[端口数据传输](nearlink-data-transfer-guide.md)）。

## 星闪数据传输方式如何选择

星闪提供基于SSAP和基于端口两种数据传输方式：

* [基于SSAP的数据传输](nearlink-ssap-connection-guide.md)：采用服务端-客户端交互模型，服务端提供服务能力，客户端访问服务端的服务。交互由客户端主动发起，适合设备控制数据交互、状态更新上报等小数据量场景。
* [基于端口的数据传输](nearlink-data-transfer-guide.md)：两端不分服务端和客户端角色，均需先注册端口，任一方均可发起连接，通道建立后两端直接收发数据。适合大文件传输、设备升级等高速率、大流量场景。

低功耗、小数据量的业务用SSAP交互即可；需要持续大流量传输时，选择端口传输。

## 手机、平板和PC/2in1之间为什么无法通过设置界面建立星闪连接

手机、平板和PC/2in1之间可以完成星闪配对，但无法通过设置界面建立连接。设置界面发起的连接为系统连接流程，与应用通过星闪接口发起的连接（如[SSAP连接](nearlink-ssap-connection-guide.md)、[端口数据传输](nearlink-data-transfer-guide.md)）不同：链路建立后，系统会检查对端设备是否提供本端可用的服务，若没有可用的服务，连接会立即断开。

手机、平板和PC/2in1一般作为中心设备使用外围设备提供的服务（如键盘、鼠标、手写笔等HID设备提供的服务），是服务的使用者而非提供者，这些设备之间没有可用的服务，因此无法从设置界面建立连接。需要建立设备间的业务连接时，应通过[ssap.Client.connect()](../harmonyos-references/js-apis-nearlink-ssap.md#connect)（SSAP连接）或[dataTransfer.connect()](../harmonyos-references/js-apis-nearlink-data-transfer-api.md#datatransferconnect)（端口数据传输）等接口发起连接，由应用明确业务。

## 连续调用writeData为什么会发送失败

连续多次调用[writeData()](../harmonyos-references/js-apis-nearlink-data-transfer-api.md#datatransferwritedata)可能会导致发送队列拥塞，从而发送失败。

您可以通过设置数据发送间隔来解决连续传输数据时失败的问题。使用[setInterval()](../harmonyos-references/js-apis-timer.md#setinterval)设置函数调用的时间间隔，建议的数据发送时间间隔为10ms。
