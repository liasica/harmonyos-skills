---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-40
title: 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
breadcrumb: FAQ > DevEco Studio > 应用运行 > 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:07ac9e30d98ed724bc24b4ea7ad5089046b86da8b3347ecc9c9023ca03815d3d
---

**问题现象**

* **场景一**：设备管理获取模板数据失败，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/3SwY8KXEQtG2f3a8NaNGqw/zh-cn_image_0000002624478770.png)
* **场景二**：模拟器镜像下载失败，提示“The network or server is abnormal.”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/obchl9RKSbadPVdgf7TSaA/zh-cn_image_0000002654798137.png)
* **场景三**：打开设备管理，界面显示为空，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/2DoDXvSjTM6sIatfw7WgYQ/zh-cn_image_0000002624638680.png)

**解决措施**

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：

   Windows:C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches

   Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../harmonyos-guides/ide-emulator-devicetype.md)内。
