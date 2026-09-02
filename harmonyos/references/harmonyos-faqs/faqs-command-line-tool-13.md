---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-13
title: 如何使用ohpm引入三四方库
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何使用ohpm引入三四方库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ac4125174b12c457c422d9c5e34646cda77dd1a136ad7abf4db5e17fd8f4d8d7
---

* 方式一：
  1. 打开Terminal窗口，通过如下指令进入到entry目录。

     cd entry
  2. 引入“dayjs”，执行以下指令进行安装。

     ohpm install dayjs
  3. 在对应的JS文件中直接引用。

     import dayjs from 'dayjs';
* 方式二：
  1. 打开工程目录下的entry目录，找到该目录下的oh-package.json5文件。
  2. 在oh-package.json5文件中写入要安装的三方库，以dayjs为例，示例如下：

     ```json
     "dependencies": {
       "dayjs": "^1.10.4",
     } ,
     ```
  3. 打开Terminal窗口，通过如下指令进入到entry目录。

     cd entry
  4. 执行指令进行安装。

     ohpm install
  5. 在对应的ArkTS文件中引用。

     import dayjs from 'dayjs';
