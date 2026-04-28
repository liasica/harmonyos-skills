---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-88
title: 构建流水线报错：Failed to request the remote SDK
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建流水线报错：Failed to request the remote SDK
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ad39c29ea42912b94bc27a4969ed0cca10f06f309c34e6f3d229e956ea56210d
---

**问题描述**

执行SDK安装时出现错误，请协助检查问题原因。

./sdkmgr install xxx --sdk-directory="/opt/HarmonyOS/SDK" Failed to request url https://devecostudio-dre.op.hicloud.com/sdkmanager/v7/hos/getSdkList [ ]0% Failed to request the remote SDK. This may be caused by a network error. If your environment needs a proxy to access the Internet, check whether the --proxy and --no-proxy parameters are correctly set. If they are not set, check whether the http\_proxy/HTTP\_PROXY and no\_proxy/NO\_PROXY environment variables are correctly set. root@luckyclientbuild01-test3-ucscompute16-cloudvsp:~/command-line-tools/sdkmanager/bin#

**解决方案**

编译时建议先执行clean操作，以避免上次编译的产物影响新的编译。
