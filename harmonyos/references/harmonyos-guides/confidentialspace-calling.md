---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/confidentialspace-calling
title: 运行数据应用处理数据
breadcrumb: 指南 > 系统 > 安全 > Confidential Space Kit（机密空间服务） > 运行数据应用处理数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:529bd572d8e1f4fc773a107adb43c34293c0181884e745eff2b337d50b9b5596
---

## 概述

本节介绍如何在机密空间内运行数据应用，并完成相应的数据处理任务。

机密空间是一个对外隔离的计算环境，专注于用户隐私数据的计算，仅支持通过机密空间接口加载、运行数据应用。

数据应用（Data application，简称DA）是运行于机密空间内部的独立程序，可使用外部应用提供的数据、机密空间内数据管理服务提供的用户数据，完成特定计算任务，再将最终计算结果发送回外部应用。数据应用以动态库（.so文件）形式通过机密空间API加载到空间中运行。

## 约束与限制

1. 同一应用一天内最多调用20次[runApp](../harmonyos-references/confidentialspace-confidentialspace.md#confidentialspacerunapp)接口。
2. 数据应用在单次运行期间最多发送总计4比特的数据，即长度为1的数组，并且此元素范围为[0, 15]。
3. 数据应用单次运行时长不得超过5秒，超时的实例将被强制结束。

## 业务流程

为了方便开发者理解机密空间的运行完整流程，本节描述机密空间内部运行原理。

机密空间相关的系统服务进程有：机密空间管理服务、数据管理服务。

* 机密空间管理服务是负责机密空间生命周期管理、提供机密空间API的系统服务。机密空间不常驻，由机密空间管理服务在被调用时动态创建，在所有数据应用结束后择机销毁。
* 数据管理服务是机密空间内部的系统服务进程，负责配置各数据应用的运行环境，转发外部应用和数据应用之间的通信内容，对由空间内到空间外发送的数据进行管控和签名，并提供空间内部消息转发、数据库等服务。

应用在机密空间中运行数据应用（以下简称DA）的业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/cBY5Mr5uQMO1vqF_880D8w/zh-cn_image_0000002736313379.png)

1. 应用调用[runApp](../harmonyos-references/confidentialspace-confidentialspace.md#confidentialspacerunapp)，异步发起运行DA请求：

   1. 应用连接系统中的机密空间管理服务，后者按需启动机密空间。
   2. 通过空间内服务拉起空间内部新进程，加载待启动的DA动态库文件。
   3. 调用DA的初始化函数。
   4. 完成DA启动后，应用与数据管理服务间建立socket，数据管理服务与DA间建立socket；应用与数据管理服务间的socket被包装成[DataAppHandle](../harmonyos-references/confidentialspace-confidentialspace.md#dataapphandle)对象。
2. 应用调用[onReceiveData](../harmonyos-references/confidentialspace-confidentialspace.md#onreceivedata)，注册消息接收回调。
3. 应用调用[sendData](../harmonyos-references/confidentialspace-confidentialspace.md#senddata)，异步发送数据：

   1. 应用向数据管理服务发送报文，传递要发送的数据，数据管理服务读取报文，将要发送的数据转发给DA。
   2. DA接收到消息，进入消息处理逻辑。
   3. DA完成消息处理后，向应用发送数据。
   4. 数据管理服务对DA发送的数据进行校验，校验成功时，生成数据签名，发送回调用方应用。
   5. 调用方应用接收到数据，触发消息接收回调。
4. 应用调用[stop](../harmonyos-references/confidentialspace-confidentialspace.md#stop)停止DA，由机密空间服务结束DA进程。

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/confidentialspace-confidentialspace.md)。

| 接口名 | 描述 |
| --- | --- |
| [runApp](../harmonyos-references/confidentialspace-confidentialspace.md#confidentialspacerunapp)(appPath: string, argv: string[]): Promise<[DataAppHandle](../harmonyos-references/confidentialspace-confidentialspace.md#dataapphandle)> | 以给定路径启动数据应用。 |
| [sendData](../harmonyos-references/confidentialspace-confidentialspace.md#senddata)(data: Uint8Array): Promise<void> | 向数据应用发送数据。 |
| [onReceiveData](../harmonyos-references/confidentialspace-confidentialspace.md#onreceivedata)(callback: Callback<Uint8Array>): void | 注册从数据应用接收数据的回调函数。 |
| [offReceiveData](../harmonyos-references/confidentialspace-confidentialspace.md#offreceivedata)(callback?: Callback<Uint8Array>): void | 取消注册从数据应用接收数据的回调函数。 |
| [onReceiveDataError](../harmonyos-references/confidentialspace-confidentialspace.md#onreceivedataerror)(callback: ErrorCallback<BusinessError<[DataAppErrorInfo](../harmonyos-references/confidentialspace-confidentialspace.md#dataapperrorinfo)>>): void | 注册处理接收数据时发生错误的回调函数。 |
| [offReceiveDataError](../harmonyos-references/confidentialspace-confidentialspace.md#offreceivedataerror)(callback?: ErrorCallback<BusinessError<[DataAppErrorInfo](../harmonyos-references/confidentialspace-confidentialspace.md#dataapperrorinfo)>>): void | 取消注册处理接收数据时发生错误的回调函数。 |
| [stop](../harmonyos-references/confidentialspace-confidentialspace.md#stop)(): void | 结束数据应用。 |

## 开发步骤

1. 导入机密空间模块。

   ```typescript
   import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
   // 导入示例代码所需的日志模块和文本转二进制能力
   import { buffer } from '@kit.ArkTS';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[runApp](../harmonyos-references/confidentialspace-confidentialspace.md#confidentialspacerunapp)方法在机密空间中启动数据应用。

   ```typescript
   const TAG = 'ConfidentialSpace';

   let handle: confidentialSpace.DataAppHandle;
   try {
     // 在机密空间中运行数据应用
     handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
   } catch (e) {
     hilog.error(0x0000, TAG, `Failed to run app. code=${e.code} message=${e.message}`);
     // ...
   }
   ```
3. 调用[onReceiveData](../harmonyos-references/confidentialspace-confidentialspace.md#onreceivedata)和[onReceiveDataError](../harmonyos-references/confidentialspace-confidentialspace.md#onreceivedataerror)方法注册接收到数据（或接收出错）时的回调。

   ```typescript
   // 注册消息接收回调和错误回调
   handle.onReceiveData((data: Uint8Array) => {
     hilog.info(0x0000, TAG, `Received data, length=${data.length}`);
     handle.stop();
     handle.offReceiveData();
     handle.offReceiveDataError();
     // ...
   });
   handle.onReceiveDataError((e: BusinessError<confidentialSpace.DataAppErrorInfo>) => {
     hilog.error(0x0000, TAG, `Failed to receive data. code=${e.code} message=${e.message}`);
     if (e.code === 1028700014) { // 数据应用产生的错误
       hilog.error(0x0000, TAG, `Error is from DA; raw code=${e.data?.dataAppErrorCode}`);
     }
     handle.stop();
     handle.offReceiveData();
     handle.offReceiveDataError();
     // ...
   });
   ```
4. 调用[sendData](../harmonyos-references/confidentialspace-confidentialspace.md#senddata)发送数据到数据应用中。

   ```typescript
   // 定义消息格式为 "ECHO:${msg}"，并将其转换为字符数组
   let payload = new Uint8Array(buffer.from(`ECHO:${msg}`, 'utf-8').buffer);
   // 发送数据
   try {
     await handle.sendData(payload);
   } catch (e) {
     hilog.error(0x0000, TAG, `Failed to send data. code=${e.code} message=${e.message}`);
     handle.stop();
     // ...
   }
   ```
