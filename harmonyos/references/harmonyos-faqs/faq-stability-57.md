---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-57
title: 使用hdc file recv命令接收文件失败
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 使用hdc file recv命令接收文件失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8115631b866a9d1a1d89b6b2f055ef9b039bc7e7ea9b17ecf5be825c7ebffd43
---

## 问题现象

使用hdc file recv命令接收文件失败。

```shell
hdc file recv XXXX YYYY
# XXXX是远程待发送的文件路径（手机设备中文件的地址）
# YYYY是本地待接收的文件路径（本地存放文件的地址）
```

* **场景一**：报错hdc is sending or deleting file now，please wait...

* **场景二**：报错no such file or directory...

  ```shell
  D:\soft\img>hdc file recv file://media/Photo/147/IMG_1751371660_141/IMG_141.png
  [Fail]Error opening file: no such file or directory, path:file://media/Photo/147/IMG_1751371660_141/IMG_141.png
  ```
* **场景三**：使用open函数在沙箱中创建文件，接收文件时报错Error opening file: permission denied...

  ```cpp
    int fd = open(filePath, O_CREAT | O_APPEND, S_IRUSR | S_IWUSR);
    write(fd, buf, len);
  ```

  ```shell
    D:\>hdc file recv /data/app/el2/100/base/com.example.myapplication/files/test.txt
    [Fail]Error opening file: permission denied, path:/data/app/el2/100/base/com.example.myapplication/files/test.txt
  ```
* **场景四**：接收data/log/hilog/时报错Error opening file: no such file or directory。

  ```shell
    D:\>hdc file recv data/log/hilog/ ./
    [Fail]Error opening file: no such file or directory, path:data/log/hilog/hilog.xxx.xxxxxx.gz
  ```

## 背景知识

* hdc file recv是从远端设备接收文件至本地的命令。
* 更多hdc知识可以参考：[hdc](../harmonyos-guides/hdc.md)。

## 问题定位

* **场景一**：报错hdc is sending or deleting file now，please wait...

  说明当前hdc正在执行其他文件操作任务。
* **场景二**：media目录为媒体库目录，当前已禁止通过hdc file recv命令从媒体库目录获取文件。
* **场景三**：在使用open创建文件时，设置的mode参数是否包含S\_IRGRP。
* **场景四**：参考[hdc版本配套表](../harmonyos-guides/hdc.md#hdc版本配套表)，排查hdc版本是否与设备API版本匹配。

## 分析结论

* **场景一**：报错hdc is sending or deleting file now，please wait...

  hdc正在执行其他文件操作任务，当前命令被阻塞。
* **场景二**：hdc file recv命令不支持获取媒体库目录下的文件。
* **场景三**：使用open函数创建文件时，设置的mode参数未包含S\_IRGRP，导致无法使用hdc file recv接收文件。
* **场景四**：hdc版本过低。

## 修改建议

* **场景一**：报错hdc is sending or deleting file now，please wait...

  等待当前任务完成。如一直不完成，可以使用hdc kill命令结束当前hdc任务并再次尝试操作。
* **场景二**：使用[mediatool工具](../harmonyos-guides/mediatool.md#mediatool工具)来进行文件导出。mediatool工具可以根据媒体文件在图库中的名字，对媒体文件进行导出。方法步骤如下：
  1. 查询目标文件。

     ```shell
     $ mediatool query IMG_141.jpg -u
     find 1 result
     uri
     "file://media/Photo/147/IMG_1751371660_141/IMG_141.jpg"
     ```
  2. 将目标文件导出到临时文件目录。

     ```shell
     $ mediatool recv file://media/Photo/147/IMG_1751371660_141/IMG_141.jpg /data/local/tmp/out.jpg
     Table Name: Photos
     /data/local/tmp/out.jpg
     ```
  3. 使用file recv命令将目标文件传输到本地。

     ```shell
     D:\soft\img>hdc file recv /data/local/tmp/out.jpg
     FileTransfer finish, Size:2159874, File count = 1, time:102ms rate:21175.24kB/s
     ```
* **场景三**：在使用open函数创建文件时，设置的mode参数加上S\_IRGRP即可。
* **场景四**：参考[hdc版本配套表](../harmonyos-guides/hdc.md#hdc版本配套表)，升级hdc到最新版本。
