---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-1
title: "应用UI生成插件解压缩APK文件时，提示“tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes”"
breadcrumb: "FAQ > DevEco Studio > AI辅助编程 > 应用UI生成插件解压缩APK文件时，提示“tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes”"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d52811e345af8cc88b0c9facdcfd224e8db3617d6b246724f3d2cfe6293234b3
---

**问题现象**

在Windows环境下使用应用UI生成插件时，选择完配置项信息（Install Package Path、SDK Path、Git Bash Path），点击Next按钮后，在应用UI生成插件的执行终端中提示“tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/S584L4kkS6SwfBziq-vhTw/zh-cn_image_0000002624638732.png)

**可能原因**

Windows内置的C:/Windows/System32/tar.exe不支持解压apk文件。

**解决措施**

1. 确保系统中安装了支持解压APK文件的工具（APK文件默认压缩格式为ZIP格式，即系统中安装了支持解压ZIP格式的工具即可）。

2. 打开“C:/Users/<用户名>/AppData/Local/Huawei/<DevEco Studio缓存目录>/ui-generation/sim-sdk”目录。将路径中的<用户名>替换为电脑使用的用户名，<DevEco Studio缓存目录>替换为正在使用的DevEco Studio版本下的缓存目录，例如如果当前DevEco Studio版本命名格式是以DevEco Studio6.1.xx开头，则将<DevEco Studio缓存目录>替换为DevEcoStudio6.1。

3. 修改“C:/Users/<用户名>/AppData/Local/Huawei/<DevEco Studio缓存目录>/ui-generation/sim-sdk/apk\_unzip\_all.sh”文件，将解压工具 /c/Windows/System32/tar替换为我们安装的解压工具。替换内容如下：

```screen
if [ "${uu_names: 0: 5}" == "MINGW" ] || [ "${uu_names: 0: 6}" == "CYGWIN" ];then
    mkdir -p $unzipfile
    #/c/Windows/System32/tar -xf $dir_or_file -C $unzipfile
    # 使用安装的解压工具代替原本使用的 tar 命令
    unzip -q $dir_or_file -d $unzipfile
else
    unzip -q $dir_or_file -d $unzipfile
fi
```

4. 替换完成后清理历史转换缓存“C:/Users/<用户名>/AppData/Local/Huawei/<DevEco Studio缓存目录>/ui-generation/build”，重新执行转换逻辑验证是否能够成功执行。
