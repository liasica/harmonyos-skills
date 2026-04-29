---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-27
title: 使用模拟器发起HTTPS请求时如何安装数字证书
breadcrumb: FAQ > DevEco Studio > 应用运行 > 使用模拟器发起HTTPS请求时如何安装数字证书
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c17ff762c4cb15ce508c02ba3c6b4e1c04073b8ebd51baa1004a5dd1c814c3f6
---

**问题现象**

在使用网络代理发送HTTPS请求时，需要安装网站服务器的数字证书。

**解决措施**

1. 将证书拖拽上传至模拟器，可在文件管理的“我的手机”>“下载”目录下查看上传的文件。
2. 安装证书的方式如下：
   * 点击**设置 > WLAN >**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Ru88R87vTXqcxFu34HGl4A/zh-cn_image_0000002395407910.png?HW-CC-KV=V1&HW-CC-Date=20260429T062115Z&HW-CC-Expire=86400&HW-CC-Sign=51872651038D00B43AEDBCE0DBD837C266960CB96686492ECE1FECB39815044C)**> 安装证书 > CA证书**，选择pem格式证书进行安装。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Nj9_1QWWR0OPbKmKf7BQQg/zh-cn_image_0000002229758177.png?HW-CC-KV=V1&HW-CC-Date=20260429T062115Z&HW-CC-Expire=86400&HW-CC-Sign=7B8B20B04094A5E81F13C6D18BA4F60CC8733D12A862FE73ECAD4FE429C69048) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/0AkcSOgDR06NNomSWmlq1A/zh-cn_image_0000002194317924.png?HW-CC-KV=V1&HW-CC-Date=20260429T062115Z&HW-CC-Expire=86400&HW-CC-Sign=13D3D51085EFA22CDDCC23FCF298127508425AC8CC5896C4D89570ECA6F63630)
   * 在本机命令行窗口中使用以下命令打开证书管理。

     ```
     1. hdc shell aa start -a MainAbility -b com.ohos.certmanager
     ```

     选择从存储设备安装，安装pem格式的证书。
