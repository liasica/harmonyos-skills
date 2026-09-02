---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-emulator
title: 使用模拟器调试
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 使用模拟器调试
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b3e443a184d346ab8a8a12da2180da94f2fb6eddbc0b62fea3bd8d481b33cfb2
---

使用模拟器调试时，需在AGC云侧注册调试凭据，以保护应用/元服务对Cloud Foundation Kit的访问。在模拟器中启动应用/元服务时，开发者触发一次云函数、云数据库或云存储业务接口，该模拟器下会生成调试凭据并输出到日志；将生成的调试凭据注册到AGC云侧，即可在模拟器中调试应用/元服务。

具体可按如下步骤操作：

1. 获取调试凭据。

   1. 创建并启动模拟器，具体请参见[管理模拟器](ide-emulator-management.md)。
   2. 在模拟器中启动应用，并触发任意一次云函数、云数据库或云存储业务接口（建议使用云函数接口）。此时，由于未注册调试凭据，接口调用会失败，请忽略，继续执行下一步。
   3. 通过设置“No filters”模式、过滤“clouddevelopproxy.debugToken”关键字，查找日志中打印的调试凭据，并复制该调试凭据。

      格式示例：[clouddevelopproxy.debugToken=xxx]，其中“xxx”为调试凭据。

      **说明** 

      如日志中查找不到调试凭据，请排查：

      * 模拟器网络连接是否正常。
      * 应用是否使用了错误的签名方式。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing-auto.md#section6333421192714)和[手动签名](ide-signing-manual.md)两种方式，请修改后再重试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/wCmXurwZQbmG2fPeAO83hA/zh-cn_image_0000002736314001.png)
2. 将获取的调试凭据注册到AGC云侧，具体可参见[注册模拟器调试凭据](../app/agc-help-add-credential-0000002415343501.md)。
3. 调试凭据注册成功后，您即可使用模拟器调试应用/元服务。关于模拟器使用指导，请参见[使用模拟器运行应用](ide-run-emulator.md)。

   如调用接口时返回的错误信息提示401签名校验失败、403鉴权失败、或者“create http task error”，可能原因如下：

   * 调试凭据未注册。请先[注册模拟器调试凭据](../app/agc-help-add-credential-0000002415343501.md)。
   * 注册调试凭据时绑定了错误的应用/元服务。请先删除该调试凭据，重新绑定正确的应用/元服务，等待30分钟后再进行调试。
