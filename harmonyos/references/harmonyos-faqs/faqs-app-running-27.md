---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-27
title: 使用模拟器发起HTTPS请求时如何安装数字证书
breadcrumb: FAQ > DevEco Studio > 应用运行 > 使用模拟器发起HTTPS请求时如何安装数字证书
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9094f6f42cf2c89419b174f3623216ceabb9c9686d0b33ed3201f80e06cc2000
---

**问题现象**

在使用网络代理发送HTTPS请求时，需要安装网站服务器的数字证书。

**解决措施**

1. 将证书拖拽上传至模拟器，可在文件管理的“我的手机”>“下载”目录下查看上传的文件。
2. 安装证书的方式如下：
   * 点击**设置 > WLAN >**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Ru88R87vTXqcxFu34HGl4A/zh-cn_image_0000002395407910.png?HW-CC-KV=V1&HW-CC-Date=20260428T002959Z&HW-CC-Expire=86400&HW-CC-Sign=D174E347164593FC8C532F4F8D1607DFF1DC63467780DD8497BCD036F82D49B1)**> 安装证书 > CA证书**，选择pem格式证书进行安装。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Nj9_1QWWR0OPbKmKf7BQQg/zh-cn_image_0000002229758177.png?HW-CC-KV=V1&HW-CC-Date=20260428T002959Z&HW-CC-Expire=86400&HW-CC-Sign=2697EAB026C32757F3EDEDAD02D7BD31B834E05ACA75A42657D4566A299D2B22) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/0AkcSOgDR06NNomSWmlq1A/zh-cn_image_0000002194317924.png?HW-CC-KV=V1&HW-CC-Date=20260428T002959Z&HW-CC-Expire=86400&HW-CC-Sign=CA68286B2BCF3EEB307F5D535E00C9E4A682099D657D7B488DEBDC76CAEC03D9)
   * 在本机命令行窗口中使用以下命令打开证书管理。

     ```
     1. hdc shell aa start -a MainAbility -b com.ohos.certmanager
     ```

     选择从存储设备安装，安装pem格式的证书。
