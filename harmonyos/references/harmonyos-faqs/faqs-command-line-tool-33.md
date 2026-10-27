---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-33
title: 动态共享包是否可以发布
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 动态共享包是否可以发布
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:777e16e117f7ca3903999a675a402c5a18259c6703b0f879f3df6a2a941725c9
---

## 问题现象

动态共享包是否支持发布？是否支持源码发布？如何引用发布后的动态共享包？

## 背景知识

[HSP](../harmonyos-guides/in-app-hsp.md)（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。HSP不支持独立发布上架，而是跟随宿主应用的APP包一起发布，与宿主应用同进程，具有相同的包名和生命周期。

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* 集成态HSP：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于宿主应用HAP的应用内HSP。

## 解决方案

* OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布，如需在应用内共享HSP，从ohpm命令行工具1.3.0版本和ohpm-repo私仓1.1.0版本开始，可将HSP共享包以.tgz文件形式发布到ohpm-repo。
* HSP不支持源码发布，仅支持以.tgz文件形式发布到ohpm-repo。无法直接从私仓的HSP中拿到源码，HAR有源码模式，可以使用源码模式进行调试开发，参考[源码HAR](../harmonyos-guides/ide-hvigor-build-har.md#section1031922925716)。
* 动态共享包HSP包不能直接发布在ohpm-repo内，需要以.tgz文件形式发布共享，以发布集成态HSP为例参考如下步骤：
  + 创建编译集成态HSP：
    1. 创建方-按如下步骤新建HSP模块publish\_hsp：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/_QY21BfcQO6utaQRFLrdng/zh-cn_image_0000002658928951.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/O-WTz2hIRaeE3xloTd3aAw/zh-cn_image_0000002658808995.png "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/1gAJvZVuTI68Nkz7aNkXcw/zh-cn_image_0000002628409730.png "点击放大")
    2. 创建方-[工程级build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)中useNormalizedOHMUrl配置项设置为true。
    3. 创建方-[模块级build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile.md)中integratedHsp配置项设置为true。
    4. 点击工具栏右上角Product图标切换编译模式为release：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/O_WxBKHnQu6Xq9MEDWKpvg/zh-cn_image_0000002628569632.png "点击放大")
    5. 选中publish\_hsp模块的根目录，点击Build图标，选择Make Module 'publish\_hsp'启动构建可得到.tgz产物：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/YiVsztp9Rqaag4IifstT_w/zh-cn_image_0000002658928953.png)

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/1HkLhTKNQjON5o0TY-WsMg/zh-cn_image_0000002658808997.png "点击放大")
  + 发布HSP：

    使用[ohpm publish](../harmonyos-guides/ide-ohpm-publish.md)命令即可将publish\_hsp-default.tgz上传至ohpm-repo私仓，私仓搭建参考[ohpm-repo私仓搭建工具](../harmonyos-guides/ide-ohpm-repo.md)：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/0JtR08jEQfifyo1-U2EbXw/zh-cn_image_0000002628409732.png "点击放大")
  + 引用已使用的集成态HSP：
    1. 使用方-工程级build-profile.json5中useNormalizedOHMUrl配置项设置为true。
    2. 使用方-在主模块的oh-package.json5配置文件dependencies配置依赖私有库：publish\_hsp: "1.0.0"。
