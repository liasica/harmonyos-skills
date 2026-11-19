---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-4
title: 运行应用时报“XXX Read timed out”异常
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时报“XXX Read timed out”异常
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6a677248aa8f2bd67f348ad26f299ecba2dddb1ec7d49e30938fccfaac7a189d
---

**问题现象**

运行应用时报“XXX Read timed out”异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/i_6Ww4VxRZinmAvEouwmSg/zh-cn_image_0000002791566336.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=90D3FEAB49FDF0904DCC6CB07AC93E8DBB5D016B9FE29701CBB5B8BC9D1B2DB2)

**解决措施**

出现此错误，是因为云侧没有启动云函数实例，卸载应用重新安装即可。
