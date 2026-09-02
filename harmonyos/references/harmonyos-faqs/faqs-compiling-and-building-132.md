---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-132
title: 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6998c1ec2782ebb4feb8c11c50b3f057a4731c761485b7ea804b6d1ce0578fd9
---

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程时，可能会遇到以下错误：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/xN8VuurpSa-e-a9mprs6Jg/zh-cn_image_0000002194158364.png)

**问题原因**

初始化时，日志写入存在冲突，.hvigor目录中的build-log文件被占用，导致报错。

**解决方案**

* 方法一：点击编辑器窗口上方的Sync Now。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/LoToklKWQOuWj0v2eqZzjw/zh-cn_image_0000002194317984.png)
* 方法二：点击工具栏**File > Sync and Refresh Project**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/f_vApYQ7QYabQoKBG1EssA/zh-cn_image_0000002229758229.png)
* 方法三：如果方法一和方法二无法解决问题，可以手动删除工程目录下的 .hvigor目录，然后重启并执行 Sync。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/TZuOFWmoQROvVFr1Sc9N_g/zh-cn_image_0000002229758233.png)
