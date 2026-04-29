---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudobj
title: 在端侧调用云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发端侧工程 > 在端侧调用云侧代码 > 在端侧调用云对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:04+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:87b38ef17eb892a8ead2cba0176e4742f8dbe91bc5c6af30f44388284e4092ed
---

云对象开发完成后，您可以为其生成端侧调用接口类，供后续端侧工程调用云对象使用。

## 前提条件

请确保[云对象已正确开发并部署](agc-harmonyos-clouddev-deploycloudobj.md)。

## 操作步骤

1. 右击云对象（以“my-cloud-object”为例），选择“Generate Invoke Interface”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/RhqeNfH5RlS9cPWdDZkZQg/zh-cn_image_0000002179498324.png?HW-CC-KV=V1&HW-CC-Date=20260429T054503Z&HW-CC-Expire=86400&HW-CC-Sign=EA57C32214F146EE2944718E82733D1C2A1DD82EB6B7B942CE8CA520694F627D)
2. 在弹出的“Generate Invoke Interface”窗口，可以看到生成的端侧调用接口类将默认存储在“Application/cloud\_objects”模块目录下，点击“OK”确认。您也可以点击“...”按钮自定义存储目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ZhD4oMV5RDuVsf7Xwj5Qtw/zh-cn_image_0000002214704581.png?HW-CC-KV=V1&HW-CC-Date=20260429T054503Z&HW-CC-Expire=86400&HW-CC-Sign=3BE529304A08A1E12ADB52DCDC427D131BAE0DDAC6F225563EF386490BC5D725)
3. DevEco Studio自动打开指定的端侧调用接口类存储目录，该目录包含“ImportObject.ts”文件和“my-cloud-object”文件夹。
   * “ImportObject.ts”文件：定义了importObject方法，可以通过该方法来实例化一个云对象的代理。
   * “my-cloud-object”文件夹：包含了该云对象在端侧可能用到的所有模型。示例中只有一个“MyCloudObject.ts”文件，如果有其它的模型也将生成在该文件夹下。
   * “MyCloudObject.ts”文件：定义了MyCloudObject class，并且定义了add和subtract两个方法。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/L3xbTj2kQ7WXokfbkxRxPw/zh-cn_image_0000002214704573.png?HW-CC-KV=V1&HW-CC-Date=20260429T054503Z&HW-CC-Expire=86400&HW-CC-Sign=77CD31D44EFA9F63C7689D68A20EB855BD14815B7674D3831BBA0C288D475689)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ZlrRorbAQ9iSBGAjrRX03A/zh-cn_image_0000002179498328.png?HW-CC-KV=V1&HW-CC-Date=20260429T054503Z&HW-CC-Expire=86400&HW-CC-Sign=2B50FF18EACE5307589528D5447B9128162641ADBEE18DB69387EC066832E327)
