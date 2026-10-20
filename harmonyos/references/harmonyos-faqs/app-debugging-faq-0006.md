---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0006
title: C++调试启动报错问题排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > C++调试启动报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:46+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:61e71f6607f8fe386a5d16fa46858846b9b132542c6ea2cf48e3a58a2ba8b762
---

**Q：启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\*\*\*\*\*\*\*\*\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/1DD0Tq67RjmQvkMo9cLhOg/zh-cn_image_0000002766071482.png)

**A**：解决措施如下：

1. 如果设备镜像与DevEco Studio版本不匹配，请尝试更换设备镜像版本以解决问题。
2. 签名使用了release证书，请更换为debug证书。
3. 到设备路径 /data/local/tmp/ 下，删除debugserver文件夹，并重启设备。
4. MacOS下 /etc/hosts文件被修改，在/etc/hosts文件后添加如下内容：

   ```text
   127.0.0.1 localhost
   255.255.255.255 broadcasthost
   ::1 localhost
   ```

   重启电脑使修改生效。

**Q：启动C++调试时出现错误，提示“com.huawei.bitfun.utils.DapRuntimeException: server already exited”。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/WeIleRsQRNS2lNDDhZ31Cw/zh-cn_image_0000002795310523.png)

**A**：使用的sdk与DevEco Studio内置的sdk版本差异过大，请更新sdk或使用DevEco Studio内置的sdk进行调试。
