---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-49
title: 一个HSP模块如何快速切换成HAR模块
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 一个HSP模块如何快速切换成HAR模块
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:35+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d76aec44f2a64ef43071f72545e61d157984b12831d695106f0571a79c62ca95
---

**解决方案**

1.在HSP下的module.json5中，把"type": "shared"修改为"type": "har"，删除"deliveryWithInstall"、"pages"字段。

2.删除HSP下的oh-package.json5中"packageType"字段。

3.删除HSP中的页面，如果要以页面的形式使用的话，就需要改为命名路由的写法。

4.然后再找到HSP下的hvigorfile.ts文件，将里面的hspTasks改为harTasks。

5.最后编译该模块即可。

编译过程中遇到其他错误时，根据提示找到对应位置并进行修改。
