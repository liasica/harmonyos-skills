---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/customize-bytecode-during-compilation
title: 编译期自定义修改方舟字节码
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS编译工具链 > 方舟字节码 > 编译期自定义修改方舟字节码
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1107bb52b8e133d46ef5a132345ad821d50db89ebfc4c0b8279412c1feeb6ccc
---

如果开发者希望自定义修改方舟字节码文件的内容，可以使用ArkTS编译工具链提供的方法自定义修改方舟字节码文件。

## 能力配置说明

准备一个操作方舟字节码文件的动态库文件，在工程的配置文件build-profile.json5中[配置编译选项transformLib](arkoptions-guide.md#transformlib)，选项值为这个动态库的路径，编译器会在指定时机加载该动态库，并执行其中指定的Transform方法。

## 能力执行机制

如果配置了transformLib且对应的动态库文件能正确加载，编译器将先生成方舟字节码文件到默认目标位置，然后调用动态库中的Transform方法，并将方舟字节码文件的路径作为参数传入。Transform方法包含开发者自定义的修改逻辑，用于重新生成方舟字节码文件，同时更新字节码文件的落盘操作是由用户执行。

以下提供动态库模板，开发者可根据需求实现Transform逻辑。

## 开发示例

1. 创建自定义修改动态库的源码。

   example.cpp：

   ```
   1. /**
   2. * @brief 方舟字节码文件修改的入口方法
   3. * @param abc_path 待处理的方舟字节码文件的存储路径
   4. */
   5. extern "C" int Transform(const char *abc_path)
   6. {
   7. // 开发者可以在这里读取abc_path对应的方舟字节码文件，然后根据方舟字节码格式修改相关数据，然后再重新生成方舟字节码文件
   8. return 0;
   9. }
   ```
2. 使用C语言编译工具（这里使用g++）编译动态库。

   Windows平台：

   ```
   1. g++ --shared -o example.dll example.cpp
   ```

   Linux平台：

   ```
   1. g++ --shared -o example.so example.cpp
   ```

   Mac平台：

   ```
   1. g++ --shared -o example.so example.cpp
   ```
3. 在DevEco Studio中配置build-profile.json5的transformLib选项（以Windows环境为例）。

   选项中配置的路径为步骤2生成的链接库文件在项目中的路径（这里是dll目录下）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/byzBJ8WTTUOIPtxUBbmwZg/zh-cn_image_0000002589243843.png?HW-CC-KV=V1&HW-CC-Date=20260429T052653Z&HW-CC-Expire=86400&HW-CC-Sign=D16298AF22EDA902B523DBF1B998703328A3979114C14D58AD409D5980BC1152)
4. 重新编译项目，即可完成自定义修改方舟字节码。
