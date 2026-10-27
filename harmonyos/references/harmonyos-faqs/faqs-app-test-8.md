---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-8
title: ohosTest测试文件引用了entry模块的方法，测试时报cppcrash
breadcrumb: FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了entry模块的方法，测试时报cppcrash
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:01+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:faa174681ec1f02493fa79eacc5783d7f4c6b395094f5dee135cd4536f74d3f4
---

**问题现象**

如果ohosTest测试文件引用了entry的方法，并且entry中存在以普通形式（例如"entry/ets/workers/Worker.ets"）加载worker时，测试执行期间会报cppcrash。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/pQE3iOy1QJaJ974ujUbFIA/zh-cn_image_0000002654798189.png)

**解决措施**

修改entry中实例化worker的路径形式为带@标识的路径加载形式或相对路径加载形式，再次执行测试以确保可以正常通过。

* @标识路径加载形式("@entry/ets/workers/Worker.ets")：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/UKLBSEGZTj6J6qktszcMiQ/zh-cn_image_0000002624638728.png)
* 相对路径加载形式("../workers/Worker.ets")：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/4CbAPdgUQ2-qzJQKLxha4Q/zh-cn_image_0000002654838145.png)
