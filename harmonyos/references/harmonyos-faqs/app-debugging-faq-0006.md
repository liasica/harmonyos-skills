---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0006
title: C++调试启动报错问题排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > C++调试启动报错问题排查
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:652da703265c58deb2350b23ce28cc6a59b246ab16e4785d90392e92ac91f22a
---

**Q：启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\*\*\*\*\*\*\*\*\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/bm17iQ-ERzSJ5DUg6e2Wfg/zh-cn_image_0000002766071482.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FDBE37AEF24ED57F4E46A0B92520A72980825860802155859796DB8CEACAA50)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/pxJZtdAZSmaRqjS7BZuFkQ/zh-cn_image_0000002795310523.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF2363E6160AB6295C363974E00169366316DA4C45379B2F4D629CFA67C16E4C)

**A**：使用的sdk与DevEco Studio内置的sdk版本差异过大，请更新sdk或使用DevEco Studio内置的sdk进行调试。
