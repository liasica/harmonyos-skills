---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0007
title: 应用安装到设备方式常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 应用安装到设备方式常见问题
category: harmonyos-faqs
scraped_at: 2026-11-12T09:58:18+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6c1dac8a57c9433d0ea4960074ba97f94625b2c0934c224e76f90dc1a62f5127
---

**Q：应用安装到设备的方式有哪些？**

**A**：支持以下方式安装HAP包到设备：

方式一：通过[hdc](../harmonyos-guides/hdc.md)命令安装，安装包在电脑上，支持同时指定多个HAP。

```bash
# 安装（多HAP可指定多个文件路径）
hdc install entry-default-signed.hap
# 覆盖安装
hdc install -r entry-default-signed.hap
# 卸载
hdc uninstall com.example.myapplication
```

方式二：先将HAP包推送到设备，再用[bm工具](../harmonyos-guides/bm-tool.md)安装。

```bash
# 将签名HAP推送至设备
hdc file send "entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
# 在设备上安装
hdc shell bm install -p "data/local/tmp/entry-default-signed.hap"
# 安装完成后删除临时包
hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
```

方式三：使用[DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/)进行安装。

方式四：将.app文件上架到应用市场后，通过应用市场将HAP分发部署到设备中。参考[发布应用（APP）](../app/agc-help-releaseharmony-0000001933963166.md)。

**Q：如何实现应用侧载？**

**A**：目前不支持侧载（直接安装包体）的方式，需通过应用市场上架流程进行安装。具体流程参考[发布应用](../guidebook/develop-once-deploy-everwhere-7-1-0000002625192371.md)。
