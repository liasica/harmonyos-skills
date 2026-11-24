---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudobj
title: 在端侧调用云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发端侧工程 > 在端侧调用云侧代码 > 在端侧调用云对象
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7db98adb6215aecec8bffe31a28253e42abf5c6128ce8688ce4523f01246d449
---

云对象开发完成后，您可以为其生成端侧调用接口类，供后续端侧工程调用云对象使用。

## 前提条件

请确保[云对象已正确开发并部署](agc-harmonyos-clouddev-deploycloudobj.md)。

## 操作步骤

1. 右击云对象（以“my-cloud-object”为例），选择“Generate Invoke Interface”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/dBKjnHYuRlymsimpEBpUEQ/zh-cn_image_0000002179498324.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=660626667870E1E5EF25CBAF942FE2A78CA6335CDCC40AD87E8CFB0B0E461A17)
2. 在弹出的“Generate Invoke Interface”窗口，可以看到生成的端侧调用接口类将默认存储在“Application/cloud\_objects”模块目录下，点击“OK”确认。您也可以点击“...”按钮自定义存储目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/NdpXRqEtSZur2zuCJp3CcQ/zh-cn_image_0000002214704581.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD51BCFEF35DF05B55E5CF4A5E4A93B4E0512D0FA335058F116E07E5F17E08DA)
3. DevEco Studio自动打开指定的端侧调用接口类存储目录，该目录包含“ImportObject.ts”文件和“my-cloud-object”文件夹。
   * “ImportObject.ts”文件：定义了importObject方法，可以通过该方法来实例化一个云对象的代理。
   * “my-cloud-object”文件夹：包含了该云对象在端侧可能用到的所有模型。示例中只有一个“MyCloudObject.ts”文件，如果有其它的模型也将生成在该文件夹下。
   * “MyCloudObject.ts”文件：定义了MyCloudObject class，并且定义了add和subtract两个方法。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/XHKEuh_VTZiA00OtfadChg/zh-cn_image_0000002214704573.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D95DC828817C9B186D753E79A5076D5C322C35A50F5EE86A24FC0C5CBF20DEB)
4. 在代码文件中引入云对象。

   ```screen
   import { MyCloudObject, importObject } from 'cloud_objects';
   ```
5. 调用云对象中的方法。

   ```screen
   let myCloudObject = importObject(MyCloudObject); // 使用importObject实例化MyCloudObject的代理
   myCloudObject.add(1, 2).then(addResult => {
     console.log(`1 + 2 = ${addResult.result}`);
   }); // 忽略异常处理
   myCloudObject.subtract(6, 3).then(subtractResult => {
     console.log(`6 - 3 = ${subtractResult.result}`);
   });
   ```

   由于“Generate Invoke Interface”时已经生成所需要的模型以及importObject方法，因此在编码时可以很方便地使用联想、自动引入等DevEco Studio提供的高阶能力，如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/aaBfj1CvSiSQvVDLPyl3JQ/zh-cn_image_0000002179498328.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=37D38F1A6CF7BB6EEC4A747881C1C11E58DEB8CF5DE54A440362311DBE07C5ED)
