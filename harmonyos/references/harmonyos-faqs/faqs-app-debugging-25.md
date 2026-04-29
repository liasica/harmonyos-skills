---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-25
title: 启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:25+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:ce6a6c4b71d10e8c3902224760efb414bded0c18ac9a29880bcda6fa6e30c8ec
---

**问题现象**

启动C++调试时出现错误，提示“Failed to connect to unix-abstract-connect://\\*\\*\\*\\*\\*\\*\\*\\*\\*.sock: Connection shut down by remote side while waiting for reply to initial handshake packet”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/AWqbN6vORpWEflhi09yERQ/zh-cn_image_0000002194158920.png?HW-CC-KV=V1&HW-CC-Date=20260429T062124Z&HW-CC-Expire=86400&HW-CC-Sign=CA3930BBF1E1B35B4B76016B9763FB213EF3E5A1D8DA366374F9100CE803686C)

**解决措施**

1. 如果设备镜像与DevEco Studio版本不匹配，请尝试更换设备镜像版本以解决问题。
2. 签名使用了release证书，请更换为debug证书。
3. 到设备路径 /data/local/tmp/debugserver/ 下，删除与应用包名相同的文件夹。
