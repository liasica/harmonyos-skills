---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudobj
title: 在端侧调用云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发端侧工程 > 在端侧调用云侧代码 > 在端侧调用云对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5afb86558e388891599c9ab96c3a14b876474bd967e05752850e1fd109f2530d
---

云对象开发完成后，您可以为其生成端侧调用接口类，供后续端侧工程调用云对象使用。

## 前提条件

请确保[云对象已正确开发并部署](agc-harmonyos-clouddev-deploycloudobj.md)。

## 操作步骤

1. 右击云对象（以“my-cloud-object”为例），选择“Generate Invoke Interface”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Mfi4DQhnQx28XdfeMECLuA/zh-cn_image_0000002179498324.png?HW-CC-KV=V1&HW-CC-Date=20260427T235507Z&HW-CC-Expire=86400&HW-CC-Sign=2B33B38BA2B630D6BB94815725C5383099582609561AD0E85BDFDFAEB7FD7476)
2. 在弹出的“Generate Invoke Interface”窗口，可以看到生成的端侧调用接口类将默认存储在“Application/cloud\_objects”模块目录下，点击“OK”确认。您也可以点击“...”按钮自定义存储目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/bGjyq2cRS6CwidvR_KVdpg/zh-cn_image_0000002214704581.png?HW-CC-KV=V1&HW-CC-Date=20260427T235507Z&HW-CC-Expire=86400&HW-CC-Sign=D62B07003BA2953CBA8776D62AD377CB629993B2F63A417D5A89162C32503441)
3. DevEco Studio自动打开指定的端侧调用接口类存储目录，该目录包含“ImportObject.ts”文件和“my-cloud-object”文件夹。
   * “ImportObject.ts”文件：定义了importObject方法，可以通过该方法来实例化一个云对象的代理。
   * “my-cloud-object”文件夹：包含了该云对象在端侧可能用到的所有模型。示例中只有一个“MyCloudObject.ts”文件，如果有其它的模型也将生成在该文件夹下。
   * “MyCloudObject.ts”文件：定义了MyCloudObject class，并且定义了add和subtract两个方法。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/2bg6iJqMTxCregP1F-enMQ/zh-cn_image_0000002214704573.png?HW-CC-KV=V1&HW-CC-Date=20260427T235507Z&HW-CC-Expire=86400&HW-CC-Sign=77CC63AF955559AED1A91D53D1DE33975FE92403D9063106A2ACA2CCA05456CE)
4. 在代码文件中引入云对象。

   ```
   1. import { MyCloudObject, importObject } from 'cloud_objects';
   ```
5. 调用云对象中的方法。

   ```
   1. let myCloudObject = importObject(MyCloudObject); // 使用importObject实例化MyCloudObject的代理
   2. myCloudObject.add(1, 2).then(addResult => {
   3. console.log(`1 + 2 = ${addResult.result}`);
   4. }); // 忽略异常处理
   5. myCloudObject.subtract(6, 3).then(subtractResult => {
   6. console.log(`6 - 3 = ${subtractResult.result}`);
   7. });
   ```

   由于“Generate Invoke Interface”时已经生成所需要的模型以及importObject方法，因此在编码时可以很方便地使用联想、自动引入等DevEco Studio提供的高阶能力，如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/yrMtvw-iSB6XgZY2ONZB6w/zh-cn_image_0000002179498328.png?HW-CC-KV=V1&HW-CC-Date=20260427T235507Z&HW-CC-Expire=86400&HW-CC-Sign=5C480F26BD125E97D3D57097A809C2948892512A78A77899834C04B36B6BADBE)
