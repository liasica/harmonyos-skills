---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-132
title: 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b620dec9a42ebc06ddfcdd824574cc05f7e5ad17938b6144f74cabbec6265859
---

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程时，可能会遇到以下错误：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/xN8VuurpSa-e-a9mprs6Jg/zh-cn_image_0000002194158364.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=137EF564522B9387F63EDF7EC7CB743A19DA54ED1FBF3F0202B1B6CAC02DE37B)

**问题原因**

初始化时，日志写入存在冲突，.hvigor目录中的build-log文件被占用，导致报错。

**解决方案**

* 方法一：点击编辑器窗口上方的Sync Now。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/LoToklKWQOuWj0v2eqZzjw/zh-cn_image_0000002194317984.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=475994D63DFE908BE8EDBB03A33E103431BAEAF9FB65CFD8487F2DDF66F10F11)
* 方法二：点击工具栏**File > Sync and Refresh Project**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/f_vApYQ7QYabQoKBG1EssA/zh-cn_image_0000002229758229.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=BB660DA24087964240ADDD6A94DCEEE1F3810DB884D4300BFFBB1A94C14C5D1C)
* 方法三：如果方法一和方法二无法解决问题，可以手动删除工程目录下的 .hvigor目录，然后重启并执行 Sync。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/TZuOFWmoQROvVFr1Sc9N_g/zh-cn_image_0000002229758233.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=8326298EE9D825E849F08654229A82602E5F70A3ABF7AD6067DE2B264A3D5688)
