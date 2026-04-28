---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-2
title: 升级DevEco Studio后执行测试任务失败
breadcrumb: FAQ > DevEco Studio > 应用测试 > 升级DevEco Studio后执行测试任务失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:195e3f0e33959e46069bd430e6de818900037ed5114ecbbbcf0871cf743e3dfc
---

**问题现象**

升级DevEco Studio后，打开先前创建的工程并执行测试框架任务时遇到失败。

**解决措施**

出现该问题的原因是升级DevEco Studio后，测试框架hypium的版本及框架内的模板OpenHarmonyTestRunner与原工程不匹配。建议的解决措施如下：

* 措施一：使用升级后的DevEco Studio创建新工程，迁移原有测试任务。
* 措施二：升级原工程，具体包括以下步骤：
  + 升级hypium插件版本：在工程级oh-package.json5中，将hypium升级至最新版本。具体版本信息请参考[DevEco Studio](../harmonyos-releases/deveco-studio-new-features.md)。
  + 替换OpenHarmonyTestRunner入口文件模板：新建工程，将src/ohosTest/ets/testrunner/OpenHarmonyTestRunner.ets文件拷贝到原工程的相同目录中。
  + 修正错误：替换完上述文件后，仍需根据编辑器的错误提示逐一修正错误。
