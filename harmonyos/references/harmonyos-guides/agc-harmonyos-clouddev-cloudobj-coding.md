---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-cloudobj-coding
title: 开发云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 开发云对象
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6d1270a176b388b0c3a8a5c69ded52924e2151b1e014faab221caed1a719e0f6
---

云对象创建完成后，您便可以直接在云对象中编写需要实现的方法。例如，通过云对象实现add与subtract两个方法。

1. 打开云对象入口文件（此处以“myCloudObject.ts”为例），添加add与subtract方法。

   ```screen
   export class MyCloudObject {
       add(num1: number, num2: number) {
           return { result: num1 + num2 };
       }
       subtract(num1: number, num2: number) {
           return { result: num1 - num2 };
       }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Tl1Qf4XASg2x_gCBmNXmqw/zh-cn_image_0000002179338600.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=E87F2316FB509CFA20973CEACD8EFC37CF4A92D4C03910350056153203641DDA)

   **注意** 

   * 云对象是无状态性的。云对象部署至云侧后，每一次调用都可能是不同的后台节点，因此在云对象上定义类成员变量是无意义的。从一个Method中对一个类成员属性赋值，然后期望从另一个Method去获取类成员属性，这样的做法是错误的。
   * 云对象无需编写构造函数。云侧在收到对云对象的某一个函数的请求时，会调用云对象的默认的无参构造函数。
   * 云对象方法的输入是从JSON反序列化而来，只能是string、number或者Object，不支持Date、Uint8Array等类型。如果在编写云对象代码的过程中需要传递Date或Uint8Array，建议通过定义成number或者数组，在Method内通过显式地调用Date或Uint8Array的构造函数来达到目的。
   * 云对象的方法的输出当前不支持单个number返回。
   * 云对象的方法的输入、输出可以使用自定义对象，不能使用第三方依赖定义的对象或类型。注意，并不是云对象不能有第三方依赖，而是云对象的输入和输出不能有第三方依赖，否则在"Generator Invoke Interface"阶段，将会因为找不到依赖而失败，根本原因是，端侧代码运行在HarmonyOS支持方舟运行时，而云侧运行在Node.js中，二者的依赖管理不同。

2. （可选）如云对象存在依赖关系，可在“package.json”文件的“dependencies”下添加需要的依赖，然后点击右上角“Sync Now”。

   下文以添加“@hw-agconnect/cloud-server”依赖为例进行说明，请添加实际业务所需的依赖。

   **说明** 

   右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/9CKXQ8x0SsOGpxjoM_F7rg/zh-cn_image_0000002425894173.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=279C06AC993AE135A9E56043815763B1C116F3D31E9151ADC2174CC01AFA8123)

   所有安装的依赖包都会存储在当前云对象的“node\_modules”目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/op6r7HiNQ1er-EtKBew9iw/zh-cn_image_0000002425974957.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5CF4AAA9CFF3E1CC8393D443E81649A9F2E48274050FC51A7CDECD9945B4BCC)
