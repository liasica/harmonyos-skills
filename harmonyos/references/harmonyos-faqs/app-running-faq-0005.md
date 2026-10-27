---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-running-faq-0005
title: DevEco Studio设备管理获取模板数据、下载模拟器镜像提示网络异常
breadcrumb: FAQ > DevEco Studio > 应用运行 > 常见问题 > DevEco Studio设备管理获取模板数据、下载模拟器镜像提示网络异常
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:aa471ae76b76e9efd484928f0b2bc4c2ec7358c09097f7125d74fcd5364a21c7
---

**Q：设备管理获取模板数据失败，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/1RztnPfUQQyVMwEbsv-StA/zh-cn_image_0000002802354179.png)

**A**：解决措施如下：

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：
   * Windows：C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches
   * Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../harmonyos-guides/ide-emulator-devicetype.md)内。

**Q：模拟器镜像下载失败，提示“The network or server is abnormal.”**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/C22eumubScONMZZThQMJWw/zh-cn_image_0000002773154414.png "点击放大")

**A**：解决措施如下：

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：
   * Windows：C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches
   * Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../harmonyos-guides/ide-emulator-devicetype.md)内。

**Q：打开设备管理，界面显示为空，错误提示：“Network request failed. Verify your network connection and Emulator is available in your country/region.”**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/NSIGTUo9SIq87zg6HJO9Cg/zh-cn_image_0000002772994448.png "点击放大")

**A**：解决措施如下：

1. 尝试清除本机DevEco Studio缓存文件后重启，缓存目录：
   * Windows：C:\Users\xxx\AppData\Local\Huawei\DevEcoStudioX.X\caches
   * Mac：~/Library/Caches/Huawei/DevEcoStudioX.X/caches
2. 尝试修改本机网络环境后进行重试，例如：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)、连接手机热点、关闭VPN。
3. 请检测您的网络并确认您当前电脑环境或华为账号是否在[模拟器支持的国家/地区](../harmonyos-guides/ide-emulator-devicetype.md)内。
