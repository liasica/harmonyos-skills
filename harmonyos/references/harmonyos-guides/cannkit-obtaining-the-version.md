---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-obtaining-the-version
title: 版本获取方法
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 版本获取方法
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5cde2a69a40aaba1949e2ae5ff531cb5363b86beacd3ed34a5ee3205bc1a91c5
---

开发者可以使用以下两种方法获取CANN Kit Version版本号。

* 方法1：通过hdc命令。

  如果开发者的手机终端直接连接在2in1上，可以使用以下命令，获取const.hiai.vendor.hiaiversion属性。

  ```shell
  hdc shell param get const.hiai.vendor.hiaiversion
  ```
* 方法2：通过CANN Kit开放接口，具体请参见[HMS\_HiAI\_GetVersion](../harmonyos-references/cannkit.md#hms_hiai_getversion)。
