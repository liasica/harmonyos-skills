---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-40
title: 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
breadcrumb: FAQ > DevEco Studio > 应用运行 > 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:02+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:2aadbe77bea27bb82939ae3677770a71db10a9b388397c780d634f82b77a74eb
---

**问题现象**

* **场景一**：设备管理获取模板数据失败，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/SZd8jBAcTdGgDU04yJgb3Q/zh-cn_image_0000002194318324.png?HW-CC-KV=V1&HW-CC-Date=20260428T003001Z&HW-CC-Expire=86400&HW-CC-Sign=5444F286A6549B0786E18ACADBAE1B7397E4CEA626C0E3FF39F12CE7039B394F)
* **场景二**：模拟器镜像下载失败，提示“The network or server is abnormal.”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/28Q0Ql1STXyWHdyRKCnlPg/zh-cn_image_0000002229758585.png?HW-CC-KV=V1&HW-CC-Date=20260428T003001Z&HW-CC-Expire=86400&HW-CC-Sign=1E486316E98ECB94E37BF87BB33043DBFED84DF1ED36AA01B990379145DF431E)
* **场景三**：打开设备管理，界面显示为空，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/zE03FeFyS9qVKDtzAmWUog/zh-cn_image_0000002313594524.png?HW-CC-KV=V1&HW-CC-Date=20260428T003001Z&HW-CC-Expire=86400&HW-CC-Sign=B9DC815985A558C5C817904FA25A6EDD7FFDF89AD4EA6BC9A2AF6CDFE438F2B9)

**解决措施**

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：

   Windows:C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches

   Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../harmonyos-guides/ide-emulator-devicetype.md)内。
