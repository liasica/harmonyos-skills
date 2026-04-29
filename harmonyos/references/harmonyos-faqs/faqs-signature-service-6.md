---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-6
title: 登录时浏览器提示不安全，“你的连接不是私密连接”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 登录时浏览器提示不安全，“你的连接不是私密连接”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1ab1a338ec54b7ad66ac3b5f7bca8bc5bcc91968d81b3a6567ec2ff1206a32f6
---

**问题现象**

使用模拟器时，需通过浏览器登录授权。如果浏览器提示网站“不安全”或“连接不是私密连接”，请检查网络连接或联系技术支持。

**解决措施**

DevEco Studio云端服务平台使用的是ACTALIS颁发的商业证书。主流浏览器通常预置了ACTALIS公司的根证书。如果遇到上述问题，可以通过以下措施解决：

1. 检查是否已安装ACTALIS公司的根证书（不同浏览器的查看方法请自行查阅）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/jYYFuhM_T-S4dP4clTbGEA/zh-cn_image_0000002194158872.png?HW-CC-KV=V1&HW-CC-Date=20260429T062107Z&HW-CC-Expire=86400&HW-CC-Sign=E09A28085CD67621D5CAFAC44B7CDEE5F5F84E05B226D78B940A516A1EB4327F "点击放大")

   * 已安装：检查Actalis证书是否被禁用。
   * 未安装：请前往[https://www.actalis.it/area-download#](https://www.actalis.it/area-download)下载和安装“Actalis Authentication Root CA”，安装完成后重启浏览器即可。
2. 打开命令行工具，执行**certmgr.msc**命令，打开证书管理界面。
3. 在**受信任的根证书颁发机构 > 证书**中，找到 Actalis Authentication Root CA，右键点击并选择“属性”。
4. 选择“启用此证书的所有目的(E)”，点击**确定**，然后重启浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/KMqoSYF8Se-JFpzv767pBQ/zh-cn_image_0000002229758745.png?HW-CC-KV=V1&HW-CC-Date=20260429T062107Z&HW-CC-Expire=86400&HW-CC-Sign=6ED46260669A18E0EB0DD7659DB013ED9C9A245A06B12E4FF5A68D246C9C8E7B)
