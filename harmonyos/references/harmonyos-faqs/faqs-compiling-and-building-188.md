---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-188
title: DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:adbb209f57765ddf5526cb2eda6240049cd28990c8e06757a634f8c5ec73c6c5
---

**问题现象**

构建app报错：“Could not open settings generic class cache for settings file”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Yl4mCngTRdWWpFLAgzqQdA/zh-cn_image_0000002654798059.png)

**常见错误场景**

当前工程使用的是低于DevEco Studio 6.0.0 Beta1 版本的DevEco Studio创建的。

**问题原因**

DevEco Studio 6.0.0 Beta1版本DevEco Studio内置的Java版本为21，当前Gradle的版本低于Java21配套的版本。

**解决措施**：

* **方式一：升级gradle版本**

  修改Gradle-wrapper.properties中的distributionUrl，升级为8.4版本。

  ```screen
  distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-8.4-bin.zip
  ```

* **方式二：指定使用Java17**

  如果本地有JDK17，可以在Gradle.properties中通过org.gradle.java.home变量指定使用Java17。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/TsLvxnY-SEm6dOeUb-pWnQ/zh-cn_image_0000002624638612.png)
