---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-cloudobj-coding
title: 开发云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 开发云对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:93071203d3ddcf8cacd5b9baf33b187af423c4de8dbf75f9fc7fbfdcd6c378b7
---

云对象创建完成后，您便可以直接在云对象中编写需要实现的方法。例如，通过云对象实现add与subtract两个方法。

1. 打开云对象入口文件（此处以“myCloudObject.ts”为例），添加add与subtract方法。

   ```
   1. export class MyCloudObject {
   2. add(num1: number, num2: number) {
   3. return { result: num1 + num2 };
   4. }
   5. subtract(num1: number, num2: number) {
   6. return { result: num1 - num2 };
   7. }
   8. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/kf0nqf4KRU6cd58UgvxQCg/zh-cn_image_0000002179338600.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=1D4F9CE5DFCA0680712B1CD2EFCE2BC0B86C2178D4A7883D919596905E0AC02D)

   注意

   * 云对象是无状态性的。云对象部署至云侧后，每一次调用都可能是不同的后台节点，因此在云对象上定义类成员变量是无意义的。从一个Method中对一个类成员属性赋值，然后期望从另一个Method去获取类成员属性，这样的做法是错误的。
   * 云对象无需编写构造函数。云侧在收到对云对象的某一个函数的请求时，会调用云对象的默认的无参构造函数。
   * 云对象方法的输入是从JSON反序列化而来，只能是string、number或者Object，不支持Date、Uint8Array等类型。如果在编写云对象代码的过程中需要传递Date或Uint8Array，建议通过定义成number或者数组，在Method内通过显式地调用Date或Uint8Array的构造函数来达到目的。
   * 云对象的方法的输出当前不支持单个number返回。
   * 云对象的方法的输入、输出可以使用自定义对象，不能使用第三方依赖定义的对象或类型。注意，并不是云对象不能有第三方依赖，而是云对象的输入和输出不能有第三方依赖，否则在"Generator Invoke Interface"阶段，将会因为找不到依赖而失败，根本原因是，端侧代码运行在HarmonyOS支持方舟运行时，而云侧运行在Node.js中，二者的依赖管理不同。

2. （可选）如云对象存在依赖关系，可在“package.json”文件的“dependencies”下添加需要的依赖，然后点击右上角“Sync Now”。

   下文以添加“@hw-agconnect/cloud-server”依赖为例进行说明，请添加实际业务所需的依赖。

   说明

   右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/JuuTufRpSvW-2sw_iBxTaw/zh-cn_image_0000002425894173.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=47E5FA8A458AC82C9F142F862A056CA9992385D14B0660394506CCCE099A6AE0)

   所有安装的依赖包都会存储在当前云对象的“node\_modules”目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/FEYu542vRpGV9zQt_06o0w/zh-cn_image_0000002425974957.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=9631B39C7F49387CF9792C6A2BF4D608722E1AF479D4BAD2090D94E6EACFA5ED)
