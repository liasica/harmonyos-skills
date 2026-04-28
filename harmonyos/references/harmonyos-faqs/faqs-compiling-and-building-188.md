---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-188
title: DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:48+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:54e53717a329da2ebb70b9d09396c34d143b2af198c8cc70223729b8b894e2f4
---

**问题现象**

构建app报错：“Could not open settings generic class cache for settings file”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/GvHrkadLTJa1PnjhFf6oEA/zh-cn_image_0000002381980508.png?HW-CC-KV=V1&HW-CC-Date=20260428T002947Z&HW-CC-Expire=86400&HW-CC-Sign=27FA2F05A34816D36DADB20D5373FCC47D3A0A744D8D913726DC39A60F01D099)

**常见错误场景**

当前工程使用的是低于DevEco Studio 6.0.0 Beta1 版本的DevEco Studio创建的。

**问题原因**

DevEco Studio 6.0.0 Beta1版本DevEco Studio内置的Java版本为21，当前Gradle的版本低于Java21配套的版本。

**解决措施**：

* **方式一：升级gradle版本**

  修改Gradle-wrapper.properties中的distributionUrl，升级为8.4版本。

  ```
  1. distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-8.4-bin.zip
  ```

* **方式二：指定使用Java17**

  如果本地有JDK17，可以在Gradle.properties中通过org.gradle.java.home变量指定使用Java17。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/cBX7bWR7QoSH2Pb2DAyreg/zh-cn_image_0000002415859685.png?HW-CC-KV=V1&HW-CC-Date=20260428T002947Z&HW-CC-Expire=86400&HW-CC-Sign=D85AA462C19CED7DAF61B088680EDAD3271A92829412B041C238885059173D16)
