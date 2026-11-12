---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/confidentialspace-calling
title: 运行数据应用处理数据
breadcrumb: 指南 > 系统 > 安全 > Confidential Space Kit（机密空间服务） > 运行数据应用处理数据
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:36508b8a7ade7e05f8361c9754788397de6c46d61ecc148eac553a5268a2b600
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/ZJbQxm2WQpK0MwpnZ0wqDA/zh-cn_image_0000002815559069.png)

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

## 开通机密空间服务

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)，进入“开发者管理 -> ID、证书和Profile -> APP ID -> 开放能力管理”。
2. 在“选择应用”列表中选择您需要开通机密空间服务的应用。
3. 找到机密空间服务，点击右侧“申请”链接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/SN4hG_aJSAG0xbCnk-GGvg/zh-cn_image_0000002815399153.png)
4. 参照申请页面中的说明，检测应用是否满足申请条件。

   **说明** 

   1. 申请主体仅限完成实名认证的企业开发者账号，请完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。
   2. 应用类型仅限银行、商城、移动支付行业的应用，请参考[配置应用分类、标签](../doccenter-submission/agc-help-release-app-class-tag-0000002271695234.md)。
   3. 机密空间服务仅面向注册地在中国大陆地区的开发者开放，请参考[配置发布国家或地区](../doccenter-submission/agc-help-release-app-area-0000002313510997.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/OgRiKGKASEmvMT7g2mGbgQ/zh-cn_image_0000002786519578.png)
5. 选择机密空间的使用场景，参考模板填写“申请原因”，在“举证材料”附件中提交安全报告说明和场景流程说明。填写完成后，点击“提交”按钮。

   **说明** 

   提交申请后，HarmonyOS 开发者中心运营将审核相关材料，审核周期为1-3个工作日，请耐心等待。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/AItN4cTgRpmTN2eBilS3OA/zh-cn_image_0000002786359650.png)
6. 审核通过后，在“开放能力管理”标签页中勾选机密空间服务并点击“保存”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/mvC-6Pe_Tu-pMHr8yR9O4w/zh-cn_image_0000002815559071.png)

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
