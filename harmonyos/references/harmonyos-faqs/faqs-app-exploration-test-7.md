---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-exploration-test-7
title: 应用为什么无法进行应用探索测试
breadcrumb: FAQ > DevEco Testing > 探索测试 > 应用探索测试 > 应用为什么无法进行应用探索测试
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e8d7282a428a233efb297c77c0e128d9edb93b685d81d0d0608eea696aa6dbdc
---

若发现应用界面控件无法点击，请使用 DevEco Testing 实用工具中的 UIViewer 打开该应用界面，逐层检查控件树以排查问题。

1. 查看页面控件树，如果仅存在一个节点且最底层组件为XComponent，则不支持进一步遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/iH_lKhVTQzuDpLtg6nvLBA/zh-cn_image_0000002624478984.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=69CB64F79DD167EE5D98AD1705641C7D2C457DA8A1A50A8AA34EC39867749F7E "点击放大")
2. 查看该页面的控件树。如果页面中大部分控件的clickable属性为false，则表示这些控件不支持点击或点击无效。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/gGUzPT0AQl-Jc7yLSRfC9Q/zh-cn_image_0000002654798347.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=897529BF7C0A909696B37808276FE6B520B66989A3B5A140FA4044F0D382B23E "点击放大")
3. 当前页面的遍历层级限制为8层。如果测试场景的页面层级超过8层，将无法继续遍历。
