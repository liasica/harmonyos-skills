---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-12
title: 如何更换回执服务器证书的问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 如何更换回执服务器证书的问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:279baea0fec6ac717b8c52ebcae8e6a69e8da23a9c5de820b674685f9154c027
---

* 场景1：新旧证书均为商用CA签发证书或自签证书但CA未改变。

  您只需更换回执服务器上的证书，不需要登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站做其他修改。
* 场景2：新证书为商用CA签发证书，旧证书为自签证书。

  您需要更换回执服务器上的证书，并登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站同步修改回执配置。此操作过程中回执服务不会中断。

  修改回执配置操作：

  1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，点击“开发与服务”，在项目列表中找到您的项目，通过“增长 > 推送服务 > 配置”导航到“配置”页签。
  2. 选择需要修改回执的应用，点击“修改”应用回执状态。
  3. 在“选择回执”页面，选择需要更换证书的回执，点击“修改”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/g4w5kr1oQj--iS1REvjaEA/zh-cn_image_0000002558765642.png?HW-CC-KV=V1&HW-CC-Date=20260429T053959Z&HW-CC-Expire=86400&HW-CC-Sign=082D2247FB1D9D52A2BAA0A74DA48EBEA8BE0419DDF2E55CD22B1889FCA3F8A4)
  4. 在“回执配置”页面，回执服务会检测最新的证书信息，您无需做任何修改。
  5. 点击“提交”，保存回执信息。
  6. 点击“确定”，返回“配置”页面。
* 场景3：新旧证书均为自签证书且CA有变化。

  为确保新旧证书替换过程中回执服务不中断，在更换回执服务器上的证书前，您需要先登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，将新证书设置为“备用证书”。

  在30天内现有证书和备用证书均被回执服务信任，30天后若回执服务器已完成证书更换，回执服务将使用备用证书替换现有证书。

  设置备用证书操作：

  1. 参考场景2的步骤1到步骤3进入“回执配置”页面。
  2. 在“回执配置”页面，点击“设置备用证书”，填入新证书信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/uLAMtaDKT3mLwpwOJrPTcQ/zh-cn_image_0000002558605986.png?HW-CC-KV=V1&HW-CC-Date=20260429T053959Z&HW-CC-Expire=86400&HW-CC-Sign=D6641CA85C627A07310AE34AAD3482D833876B381F678F661B5F45E4C122D88C)
  3. 点击“提交”，保存回执信息。
  4. 点击“确定”，返回“配置”页面。

说明

如何获取回执服务器证书的CA信息？

* 若证书已安装到回执服务器且回执服务器可访问，您可以新建一个回执配置，输入回调地址后会显示当前证书的CA信息。
* 若证书未安装到回执服务器，您可以从证书中获取CA信息。

回执服务会保留证书的CA信息，通过校验证书的CA信息来确保回执消息正确发送到您配置的回执地址。
