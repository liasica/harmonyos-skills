---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-25
title: 启动C++调试时出现错误
breadcrumb: FAQ > DevEco Studio > 应用调试 > 启动C++调试时出现错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:dec29027c779de2ee1539f70b1f5e50544c47525c769c4ce076c3a55ee76248f
---

**问题现象**

启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\\*\\*\\*\\*\\*\\*\\*\\*\\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/4dhoOHz2ROOMji8z2406LQ/zh-cn_image_0000002654798163.png)

**解决措施**

1. 如果设备镜像与DevEco Studio版本不匹配，请尝试更换设备镜像版本以解决问题。
2. 签名使用了release证书，请更换为debug证书。
3. 到设备路径 /data/local/tmp/ 下，删除debugserver文件夹，并重启设备。
4. MacOS下 /etc/hosts文件被修改，在/etc/hosts文件后添加如下内容：

   ```screen
   127.0.0.1 localhost
   255.255.255.255 broadcasthost
   ::1 localhost
   ```

   重启电脑使修改生效。

**问题现象**

启动C++调试时出现错误，提示“com.huawei.bitfun.utils.DapRuntimeException: server already exited”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/EGNsabvWRGiayJO93WUS8w/zh-cn_image_0000002624638704.png "点击放大")

**解决措施**

使用的sdk与DevEco Studio内置的sdk版本差异过大，请更新sdk或使用DevEco Studio内置的sdk进行调试。
