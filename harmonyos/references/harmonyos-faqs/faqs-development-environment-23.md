---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-23
title: 创建新工程Create Project为空白如何解决
breadcrumb: FAQ > DevEco Studio > 环境准备 > 创建新工程Create Project为空白如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:be976c7e7ed571c43334f260ab64f057947fcdb1e8d3686d5f3a1ba41d742a46
---

## 问题现象

1. 创建新工程时，Create Project为空白。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/v4knCHoQSSu7KQIFv005nA/zh-cn_image_0000002628405062.png "点击放大")
2. 环境变量JAVA\_HOME没有指向有效的jvm。

   ```shell
   The environment variable JAVA_HOME with the value of does not point to a valid JVM installation。
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Q90qiVJ_RY6mKu4r9dmllg/zh-cn_image_0000002658924283.png "点击放大")

## 背景知识

[DevEco Studio](../harmonyos-guides/ide-tools-overview.md)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。

## 问题定位

解决问题的核心思路就是jcef有没有打开，按照如下步骤进行排查：

1. 检查DevEco Studio是否存在报错：Too many restarts of GPU-process (jcef)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/7K2H1yeiTJmzIOg8ecHGkQ/zh-cn_image_0000002658804333.png "点击放大")
2. 查看DevEco Studio依赖的jbr路径下，jvm.dll与chrome\_elf.dll是否存在，如果不存在很可能是被杀毒软件误删除了。

   jvm.dll路径：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/hefRYuveRmmt1ZAP3OFVJg/zh-cn_image_0000002628564972.png)

   chrome\_elf.dll路径：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/anfkXI7WSvWrbaevRSqerg/zh-cn_image_0000002628405072.png)
3. 开发者的环境可能和沙箱环境是否冲突，检查ide.browser.jcef.sandbox.enable=false是否勾选。

## 分析结论

* IntelliJ IDEA底层架构的jcef窗口组件的GPU兼容性问题。需要勾选jcef.gpu.disable选项。
* DevEco Studio依赖的jbr路径下没有jvm.dll与chrome\_elf.dll文件。DevEco Studio的界面主要是两种swing和jcef，jcef就相当于在开发浏览器的预览，浏览器的预览功能需要依赖chrome的动态链接库，没有这个文件，所有的jcef都起不了。
* 开发者的环境可能和沙箱环境冲突。需要把沙箱屏蔽关掉，就可以正常的打开jcef：ide.browser.jcef.sandbox.enable=false。

## 修改建议

根据如下建议修改，查看是否能解决问题（不是所有选项都要改掉）：

* 按照图示开启jcef.gpu.disable：help->find action，输入registry，点击生成registry界面；registry界面中勾选jcef.gpu.disable选项。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/LBZIX0sCQSO9fDmFVlT4UA/zh-cn_image_0000002658924287.png "点击放大")
* 找杀毒软件，将文件添加到白名单并恢复文件。或者重新安装应用，在杀毒软件提示拦截的时候放行。
* 直接添加ide.browser.jcef.sandbox.enable=false，通过Help -> Edit Custom Properties...打开对应的配置页面，在后面添加ide.browser.jcef.sandbox.enable=false即可。

## 总结

DevEco Studio在运行过程中会遇到页面打开空白的情况，这个问题与GPU兼容性有关，特别是在使用Native调试堆栈可视化功能时，通常发生在电脑GPU不兼容或在云桌面环境下使用DevEco Studio的情况下。如果发现多数页面都空白，例如Create Project、Project Structure等页面，大概率是IDE的jcef配置有问题，着重从这方面开始排查问题即可。
