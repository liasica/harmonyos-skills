---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/signature-service-faq-0002
title: 配置调试签名异常
breadcrumb: FAQ > DevEco Studio > 签名服务 > 常见问题 > 配置调试签名异常
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b2a317ca1728c7cc7043515e9746364626f64d51b7ed24fa96ce943694f121b9
---

**Q：提示"Bundle name \*\*\* does not exist."的原因和解决措施是什么？**

**A**：报错原因：上传的应用/元服务在HarmonyOS 开发者中心中不存在，导致校验失败。

解决措施：

方式一：

1. 点击报错信息弹窗中"AddApp ID"，在DevEco Studio界面添加应用/元服务的基本信息，点击OK。
   * Project：项目名称。可以输入一个新项目名称，或在下拉框中选择已有项目。
   * App type：应用类型为HarmonyOS应用/元服务。
   * App name：华为应用市场详情页展示的名称。
   * App package name：应用包名。App type为HarmonyOS应用时，才需要填写该字段。字段内容跟工程的Bundle name一致，不支持修改。
   * App category：应用分类。关于应用/元服务名称、包名的要求请参考[操作步骤](../app/agc-help-create-app-0000002247955506.md#section1772711713288)、[创建元服务](../app/agc-help-create-atomic-service-0000002247795706.md)。
2. 应用/元服务添加完成后，再进行签名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/iF8n6V6NQL2VKqoTrDzo7A/zh-cn_image_0000002801599759.png "点击放大")

方式二：

1. 进入HarmonyOS 开发者中心创建应用/元服务，创建时包名和DevEco Studio创建应用时的Bundle name一致。创建过程具体可参考[操作步骤](../app/agc-help-create-app-0000002247955506.md#section1772711713288)、[创建元服务](../app/agc-help-create-atomic-service-0000002247795706.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/7rZy4KFdRh2mjL4E45UE9w/zh-cn_image_0000002772519876.png "点击放大")
2. 创建完成后，返回DevEco Studio界面重新签名。

**Q：提示"Bundle name \*\*\* is already in use. Choose a different name, or use the team account that owns it."的原因和解决措施是什么？**

**A**：报错原因：

场景一：在应用市场中应用名称具有唯一性，应用名称（包名）不可重复。包名被其它应用使用。

场景二：应用名称被其它团队使用，开发者不在该团队。

解决措施：

方式一：修改包名。根据提示信息添加应用，再进行签名。

方式二：

1. 加入目标团队，具体可参考[添加成员账号](../app/agc-help-manageaccount-0000002306610129.md#section151241455193313)。
2. 加入团队成功后，将Team修改为目标团队。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/APjhS-SBR5qqX3-oGhU5jg/zh-cn_image_0000002772519878.png "点击放大")

**Q：提示"Failed to find the capabilities.Check the following configurations: Networkconnection,HTTP Proxy,etc."的原因和解决措施是什么？**

**A**：报错原因和解决措施：

场景一：网络连通问题，请先检查和配置网络，再进行签名。配置网络具体请参考[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。

场景二：应用没有开放能力管理和ACL权限设置项，需要重新创建应用，再进行签名。查看设置项和创建应用的操作如下：

1. 进入[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击开发与服务，选择应用所在的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Jf6JdhAfQEWALo01e7YVuw/zh-cn_image_0000002801759665.png "点击放大")
2. 选择应用，查看应用的开放能力管理和ACL权限设置项。若两个设置项不存在，需重新创建HarmonyOS应用和添加APP ID，具体请参考为HarmonyOS应用创建APP ID。

参考链接：[操作步骤](../app/agc-help-create-app-0000002247955506.md#section1772711713288)。

**Q：提示"Failed to verify the bundle name. Check your network connection or try again after configuring a proxy."的原因和解决措施是什么？**

**A**：报错原因和解决措施：

场景一：网络连通问题，请先检查和配置网络，再进行签名。配置网络具体请参考[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。

场景二：在DevEco Studio退出登录，重新登录，再进行签名。
