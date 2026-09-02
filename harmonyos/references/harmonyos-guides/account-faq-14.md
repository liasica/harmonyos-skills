---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-14
title: 订阅到系统未成年人模式开启了，这个时候应用要怎么处理
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 订阅到系统未成年人模式开启了，这个时候应用要怎么处理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c41d3aae13bc372ef12ae09ef75b6a21524db7823983d8d40ca3c4721d4f5c67
---

如果应用处于后台，可以在应用切换至前台时进行页面内容的刷新。开发者可自行关注应用后台行为是否需要中断，例如是否需要中断后台播放的音视频内容等，避免未成年人绕过限制，继续访问非适龄内容。

如果应用处于前台（用户正在浏览内容或播放音视频等场景），可以在监听到状态变化后回到应用的主页，并将主页内容刷新为当前模式下的适龄内容。如果未及时刷新，可能存在未成年用户浏览到非适龄内容绕过管控，或成年用户仍浏览未成年人模式下的内容，无法关闭未成年人模式的情况。刷新后的未成年人模式主页可参考如下设计：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/k-D344MiR-Gw_Yap6JvzIw/zh-cn_image_0000002706674836.png "点击放大")
