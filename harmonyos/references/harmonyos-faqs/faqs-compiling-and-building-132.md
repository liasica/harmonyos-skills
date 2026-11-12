---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-132
title: 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:849ad5e616d77ca6e064aa754d517b4666f394c2270f6f820e892b3057513ba6
---

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程时，可能会遇到以下错误：resource busy or locked, open 'xxx\outputs\build-logs\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/7LwtDM5XQ6Sb1iMFw1cOfA/zh-cn_image_0000002654837925.png?HW-CC-KV=V1&HW-CC-Date=20261112T233207Z&HW-CC-Expire=31536000000&HW-CC-Sign=8EBF20AB76CFB6A20218A8F3C60C12C80B6B74A22C4A3849969FAD98716B2003)

**问题原因**

初始化时，日志写入存在冲突，.hvigor目录中的build-log文件被占用，导致报错。

**解决方案**

* 方法一：点击编辑器窗口上方的Sync Now。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kZusECeFQQqIuYGEO7PoRw/zh-cn_image_0000002624478616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233207Z&HW-CC-Expire=31536000000&HW-CC-Sign=248BC45D590CE88A7EB800BD2ADEF05E5003EEF5C05726EA0206047B0D758BCC)
* 方法二：点击工具栏**File > Sync and Refresh Project**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/HiXUemH7T3OCxOz1v_usuQ/zh-cn_image_0000002654797973.png?HW-CC-KV=V1&HW-CC-Date=20261112T233207Z&HW-CC-Expire=31536000000&HW-CC-Sign=D26DC80FC623A6583027D080B736FC34F9852A126FDD4818B0D17F83A80F4CD2)
* 方法三：如果方法一和方法二无法解决问题，可以手动删除工程目录下的 .hvigor目录，然后重启并执行 Sync。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/N2OubVfnQC20wvEwLGxRMg/zh-cn_image_0000002624638522.png?HW-CC-KV=V1&HW-CC-Date=20261112T233207Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB1E65A6A94FDB6F5861714D777C83A601B18B3440DB1D6C57E879C94E712522)
