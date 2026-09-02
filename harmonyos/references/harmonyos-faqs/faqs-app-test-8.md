---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-8
title: ohosTest测试文件引用了entry模块的方法，测试时报cppcrash
breadcrumb: FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了entry模块的方法，测试时报cppcrash
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b5c084c8073303f1c44c346f8920ffd69a456179f05e59fbe1f641b686a125e1
---

**问题现象**

如果ohosTest测试文件引用了entry的方法，并且entry中存在以普通形式（例如"entry/ets/workers/Worker.ets"）加载worker时，测试执行期间会报cppcrash。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/6zpoBfaKQAmc9vP_dN5P9g/zh-cn_image_0000002194318400.png)

**解决措施**

修改entry中实例化worker的路径形式为带@标识的路径加载形式或相对路径加载形式，再次执行测试以确保可以正常通过。

* @标识路径加载形式("@entry/ets/workers/Worker.ets")：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/rB8XTOSsRE6VUbaFXRgqCQ/zh-cn_image_0000002194158792.png)
* 相对路径加载形式("../workers/Worker.ets")：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/M0gLXJIpQJ259lfQZESTIQ/zh-cn_image_0000002229758665.png)
