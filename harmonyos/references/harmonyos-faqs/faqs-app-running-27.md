---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-27
title: 使用模拟器发起HTTPS请求时如何安装数字证书
breadcrumb: FAQ > DevEco Studio > 应用运行 > 使用模拟器发起HTTPS请求时如何安装数字证书
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4a4179f28e56e56be7055c8e2266a15f7ef3c2d0c7deaa7f0d07c8d751a67a17
---

**问题现象**

在使用网络代理发送HTTPS请求时，需要安装网站服务器的数字证书。

**解决措施**

1. 将证书拖拽上传至模拟器，可在文件管理的“我的手机”>“下载”目录下查看上传的文件。
2. 安装证书的方式如下：
   * 点击**设置 > WLAN >**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/0o5GnL3qQEaFpPWz7y30AA/zh-cn_image_0000002654798123.png)**> 安装证书 > CA证书**，选择pem格式证书进行安装。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/nyQq1WG_R6-0CtpmGbNbfw/zh-cn_image_0000002624638670.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/YRJ_zFNUS1a-UCmizyvPUw/zh-cn_image_0000002654838077.png)
   * 在本机命令行窗口中使用以下命令打开证书管理。

     ```powershell
     hdc shell aa start -a MainAbility -b com.ohos.certmanager
     ```

     选择从存储设备安装，安装pem格式的证书。
