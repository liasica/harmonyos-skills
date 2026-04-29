---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-40
title: 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
breadcrumb: FAQ > DevEco Studio > 应用运行 > 设备管理获取模板数据提示网络异常，下载模拟器镜像提示网络异常
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:21+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:82aebc7d932e3a845fe1638c6a3eb690276ac8508e067fc587b9af280dd807ef
---

**问题现象**

* **场景一**：设备管理获取模板数据失败，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/SZd8jBAcTdGgDU04yJgb3Q/zh-cn_image_0000002194318324.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=2E7E6F16C5810226C4848ED6B6A78BC4DC743B26CF489E602E817B1840F2B6DB)
* **场景二**：模拟器镜像下载失败，提示“The network or server is abnormal.”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/28Q0Ql1STXyWHdyRKCnlPg/zh-cn_image_0000002229758585.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=4FDA0BC13538421AB9D52E431EF7A959884D1C68C19BB4A95E5DF5292F2620F5)
* **场景三**：打开设备管理，界面显示为空，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/zE03FeFyS9qVKDtzAmWUog/zh-cn_image_0000002313594524.png?HW-CC-KV=V1&HW-CC-Date=20260429T062120Z&HW-CC-Expire=86400&HW-CC-Sign=80ADF7F986AC4B74B7EB651F09E76DED75010DB6A2DAA4336ED569EE96545FE6)

**解决措施**

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：

   Windows:C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches

   Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../harmonyos-guides/ide-emulator-devicetype.md)内。
