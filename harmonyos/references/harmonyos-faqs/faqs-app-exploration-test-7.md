---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-exploration-test-7
title: 应用为什么无法进行应用探索测试
breadcrumb: FAQ > DevEco Testing > 探索测试 > 应用探索测试 > 应用为什么无法进行应用探索测试
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5a36f50520dab8aa02bc67df6a6fad2b61181bddd820834f0d6258815dac164f
---

若发现应用界面控件无法点击，请使用 DevEco Testing 实用工具中的 UIViewer 打开该应用界面，逐层检查控件树以排查问题。

1. 查看页面控件树，如果仅存在一个节点且最底层组件为XComponent，则不支持进一步遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/nlHOD3OWSrGqtIdaAVGEgw/zh-cn_image_0000002429905500.png?HW-CC-KV=V1&HW-CC-Date=20260428T003037Z&HW-CC-Expire=86400&HW-CC-Sign=014136E3BFCCDEB4C2BB5ECD7031BFD46501E225BC95631F369A7B3D4F18FD64 "点击放大")
2. 查看该页面的控件树。如果页面中大部分控件的clickable属性为false，则表示这些控件不支持点击或点击无效。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Iprm5OjNRx20bRIrm7hRWg/zh-cn_image_0000002430065352.png?HW-CC-KV=V1&HW-CC-Date=20260428T003037Z&HW-CC-Expire=86400&HW-CC-Sign=F6C97170167D13B9AEE5377C02725D824999E13464729B758B4EF1B6CB284BAC "点击放大")
3. 当前页面的遍历层级限制为8层。如果测试场景的页面层级超过8层，将无法继续遍历。
