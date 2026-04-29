---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-3
title: 输入华为账号后，未出现“允许”按钮，浏览器界面无跳转
breadcrumb: FAQ > DevEco Studio > 签名服务 > 输入华为账号后，未出现“允许”按钮，浏览器界面无跳转
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e78d871cb1d2143503d660d1f9e22912aa1a9e7181155037bfc8b79cb0e3ac10
---

**问题现象**

使用浏览器登录华为账号后，如果账号已实名认证但未出现授权的“允许”按钮，界面也未跳转或提示。

**解决措施**

该问题由浏览器兼容性问题导致。模拟器登录授权已在Chrome、IE11和Safari浏览器中进行了充分验证，建议将默认浏览器设置为其中一种。

1. 设置或更改默认浏览器。
   * **Windows****平台**：以Windows 10为例，打开“**控制面板 > 程序 > 默认程序 > 设置默认程序**”，更改或设置默认浏览器。
   * **macOS平台**：以macOS 15为例，打开**系统设置，选择“桌面与程序坞”，再选择“默认网页浏览器****”**，更改或设置默认浏览器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/5u7YPD-2SNGSkzLqrzSG0w/zh-cn_image_0000002523427811.png?HW-CC-KV=V1&HW-CC-Date=20260429T062106Z&HW-CC-Expire=86400&HW-CC-Sign=547DD657D488511EC16C7A1B84AE9D09488C56095D23BC781E1FCDDE30F7E87C "点击放大")

     使用Safari浏览器时，点击**Safari 浏览器 > 偏好设置>****隐私/高级**，取消“防止跨站跟踪”和“阻止所有Cookie”设置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/L2Tri00bS7Ossx32kPBgVA/zh-cn_image_0000002491108268.png?HW-CC-KV=V1&HW-CC-Date=20260429T062106Z&HW-CC-Expire=86400&HW-CC-Sign=22192BE34AA78E60426ED068DFAEBF8AFB50CD01F793719B8504A7D3BD5F3BD3 "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/6dd9dNc6T3SNXWGuq4n38Q/zh-cn_image_0000002523268149.png?HW-CC-KV=V1&HW-CC-Date=20260429T062106Z&HW-CC-Expire=86400&HW-CC-Sign=DCDB89A5CA334E1978A6B426CBF4B81BE9DDA1DE3ECD855F921D4EE8F08259AC "点击放大")
2. 在DevEco Studio界面，点击**Cancel**按钮，然后重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/hM8z6o1zTm6_AOiwEmFmUw/zh-cn_image_0000002229603917.png?HW-CC-KV=V1&HW-CC-Date=20260429T062106Z&HW-CC-Expire=86400&HW-CC-Sign=C3F175A72DD0F4AA875937A645CB31AFD4C2B68142F59A52B85C1D614E770036)
